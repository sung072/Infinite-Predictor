#!/usr/bin/env python3
r"""시스템가 예측력 퍼뮤테이션(셔플 라벨) 유의성 점검.

질문: 관측 `hit_rate`, `mae_ratio` 개선이 우연인가?
방법: 다음 봉 종가(`close_{t+1}`)를 시계열 내에서 섞어(라벨 퍼뮤테이션)
동일 지표 분포를 만들고 경험적 p-value를 계산한다.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
_SCRIPTS = ROOT / "scripts"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import system_price_skill as sps  # noqa: E402
import system_price_validation_matrix as spm  # noqa: E402


@dataclass(frozen=True)
class CaseSpec:
    name: str
    gap_csv: Path
    ohlcv_csv: Path


def _load_gfr():
    p = ROOT / "scripts" / "gap_forward_return_research.py"
    spec = importlib.util.spec_from_file_location("gap_forward_return_research", p)
    if spec is None or spec.loader is None:
        raise ImportError(p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _perm_test_one(
    m: pd.DataFrame,
    *,
    system_col: str,
    shrink_weight: float,
    n_perm: int,
    seed: int,
) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    # observed
    gfr = _load_gfr()
    sk, _sp, _ps = spm._skill_from_system_col(
        m,
        gfr,
        system_col=system_col,
        shrink_weight=shrink_weight,
    )
    obs_hit = float(sk["directional_hit_rate"])
    obs_ratio = float(sk["mae_ratio_sys_over_naive"])

    ps = pd.to_numeric(m.get("p_system"), errors="coerce")
    pw = pd.to_numeric(m.get("P_now"), errors="coerce")
    if system_col == "p_system_shrunk_custom":
        w = float(max(0.0, min(1.0, shrink_weight)))
        ps = (1.0 - w) * ps + w * pw
    elif system_col in m.columns:
        ps = pd.to_numeric(m.get(system_col), errors="coerce")

    ct = pd.to_numeric(m.get("close_ohlc"), errors="coerce")
    fwd = pd.to_numeric(m.get("fwd_1"), errors="coerce")
    cn = ct * (1.0 + fwd)
    ok = ps.notna() & pw.notna() & cn.notna()
    psb = ps[ok].to_numpy(dtype=float)
    pwb = pw[ok].to_numpy(dtype=float)
    cnb = cn[ok].to_numpy(dtype=float)
    n = len(cnb)
    if n < 20:
        return {
            "n_used": float(n),
            "obs_hit": obs_hit,
            "obs_ratio": obs_ratio,
            "p_hit_perm_ge": float("nan"),
            "p_ratio_perm_le": float("nan"),
            "p_joint": float("nan"),
        }

    near_zero = (np.abs(psb - pwb) < 1e-9)
    hit_perm_ge = 0
    ratio_perm_le = 0
    joint = 0
    valid_perm = 0
    for _ in range(int(n_perm)):
        sh = rng.permutation(cnb)
        dir_hit = np.sign(psb - pwb) == np.sign(sh - pwb)
        dir_valid = ~(near_zero | (np.abs(sh - pwb) < 1e-9))
        if not np.any(dir_valid):
            continue
        hit = float(np.mean(dir_hit[dir_valid]))
        mae_sys = float(np.mean(np.abs(psb - sh)))
        mae_naive = float(np.mean(np.abs(pwb - sh)))
        ratio = mae_sys / mae_naive if mae_naive > 1e-12 else np.nan
        if not np.isfinite(ratio):
            continue
        valid_perm += 1
        if np.isfinite(obs_hit) and hit >= obs_hit:
            hit_perm_ge += 1
        if np.isfinite(obs_ratio) and ratio <= obs_ratio:
            ratio_perm_le += 1
        if np.isfinite(obs_hit) and np.isfinite(obs_ratio) and hit >= obs_hit and ratio <= obs_ratio:
            joint += 1

    den = valid_perm + 1
    return {
        "n_used": float(n),
        "obs_hit": obs_hit,
        "obs_ratio": obs_ratio,
        "p_hit_perm_ge": (hit_perm_ge + 1) / den,
        "p_ratio_perm_le": (ratio_perm_le + 1) / den,
        "p_joint": (joint + 1) / den,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--case", action="append", default=[], help="NAME|gap_csv|ohlcv")
    p.add_argument("--n-perm", type=int, default=300)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument(
        "--system-col",
        default="p_system_shrunk_custom",
        choices=("p_system", "p_system_shrunk", "p_system_tension", "p_system_shrunk_custom"),
    )
    p.add_argument("--shrink-weight", type=float, default=0.96)
    p.add_argument(
        "--symbol-shrink-weights",
        default="",
        help="케이스 이름 접두어(BTC-oos 등)별 shrink: 예 BTC=0.96,ETH=0.99 (미지정 시 --shrink-weight)",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_permutation_significance.md",
    )
    p.add_argument(
        "--out-json",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_permutation_significance.json",
    )
    args = p.parse_args(argv)

    try:
        by_sym = spm.parse_symbol_weights(args.symbol_shrink_weights)
    except ValueError as e:
        print(f"bad --symbol-shrink-weights: {e}", file=sys.stderr)
        return 1

    cases_raw = args.case or [
        "BTC-oos|data/runs/btcusdt_4p_gap_oos.csv|data/btcusdt_1h_30d.csv",
        "BTC-wf|data/runs/btcusdt_4p_gap_wf.csv|data/btcusdt_1h_30d.csv",
        "ETH-oos|data/runs/ethusdt_4p_gap_oos.csv|data/ethusdt_1h_30d.csv",
        "ETH-wf|data/runs/ethusdt_4p_gap_wf.csv|data/ethusdt_1h_30d.csv",
        "SOL-oos|data/runs/solusdt_4p_gap_oos.csv|data/solusdt_1h_30d.csv",
        "SOL-wf|data/runs/solusdt_4p_gap_wf.csv|data/solusdt_1h_30d.csv",
    ]

    gfr = _load_gfr()
    out_rows: list[dict[str, Any]] = []
    for raw in cases_raw:
        c = spm.parse_case(raw)
        if not c.gap_csv.is_file() or not c.ohlcv_csv.is_file():
            continue
        gap = gfr._read_gap_csv(c.gap_csv)
        ohl = gfr._read_ohlcv(c.ohlcv_csv)
        m = gfr.add_features_and_forwards(gfr._align(ohl, gap), anchor_id=None)
        w = spm.resolve_shrink_weight(c.name, args.shrink_weight, by_sym)
        r = _perm_test_one(
            m,
            system_col=args.system_col,
            shrink_weight=w,
            n_perm=args.n_perm,
            seed=args.seed,
        )
        r["case"] = c.name
        out_rows.append(r)

    if not out_rows:
        print("no valid cases", file=sys.stderr)
        return 1

    df = pd.DataFrame(out_rows).sort_values("p_joint")
    sw_note = (
        f"symbol_shrink={args.symbol_shrink_weights!r}, default={args.shrink_weight:.3f}"
        if args.symbol_shrink_weights.strip()
        else f"shrink_weight={args.shrink_weight:.3f}"
    )
    lines = [
        "# 시스템가 퍼뮤테이션 유의성 리포트",
        "",
        f"- n_perm={args.n_perm}, seed={args.seed}",
        f"- system_col={args.system_col}, {sw_note}",
        "",
        "| case | obs_hit | obs_ratio | p(hit_perm>=obs) | p(ratio_perm<=obs) | p_joint |",
        "|------|---------|-----------|------------------|--------------------|---------|",
    ]
    for _, r in df.iterrows():
        lines.append(
            f"| `{r['case']}` | {r['obs_hit']:.4f} | {r['obs_ratio']:.4f} | "
            f"{r['p_hit_perm_ge']:.4f} | {r['p_ratio_perm_le']:.4f} | {r['p_joint']:.4f} |"
        )
    lines += [
        "",
        "해석: p_joint가 낮을수록(예: <0.05) 관측 성능이 셔플 우연 대비 드물다는 근거가 강함.",
        "",
    ]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines), encoding="utf-8")
    args.out_json.write_text(json.dumps(out_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print("== wrote:", args.out.resolve(), flush=True)
    print("== wrote:", args.out_json.resolve(), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
