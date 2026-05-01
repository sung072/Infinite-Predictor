#!/usr/bin/env python3
r"""OOS/WF 중심 시스템가 수축( shrink ) 파라미터 튜닝.

기존 gap CSV의 `p_system`, `P_now`, `mean_pairwise_rel`을 사용해
후처리 방식으로 시스템가를 재정의하고(재백테스트 없이), 다음 봉 종가 기준
MAE 비율/방향 적중률을 비교한다.
"""
from __future__ import annotations

import argparse
import importlib.util
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import system_price_skill as sps  # noqa: E402


@dataclass(frozen=True)
class CaseSpec:
    name: str
    gap_csv: Path
    ohlcv_csv: Path


def parse_case(raw: str) -> CaseSpec:
    parts = [x.strip() for x in raw.split("|")]
    if len(parts) != 3 or any(not x for x in parts):
        raise ValueError("case format must be NAME|gap_csv_path|ohlcv_csv_path")
    name, gap_raw, ohlcv_raw = parts
    gap = Path(gap_raw)
    ohlcv = Path(ohlcv_raw)
    if not gap.is_absolute():
        gap = (ROOT / gap).resolve()
    else:
        gap = gap.resolve()
    if not ohlcv.is_absolute():
        ohlcv = (ROOT / ohlcv).resolve()
    else:
        ohlcv = ohlcv.resolve()
    return CaseSpec(name=name, gap_csv=gap, ohlcv_csv=ohlcv)


def _load_gfr():
    p = ROOT / "scripts" / "gap_forward_return_research.py"
    spec = importlib.util.spec_from_file_location("gap_forward_return_research", p)
    if spec is None or spec.loader is None:
        raise ImportError(p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _default_cases() -> list[CaseSpec]:
    raw = [
        "BTC-oos|data/runs/btc_4p_gap_oos.csv|data/btcusdt_1h_30d.csv",
        "BTC-wf|data/runs/btc_4p_gap_wf.csv|data/btcusdt_1h_30d.csv",
        "ETH-oos|data/runs/eth_4p_gap_oos.csv|data/ethusdt_1h_30d.csv",
        "ETH-wf|data/runs/eth_4p_gap_wf.csv|data/ethusdt_1h_30d.csv",
    ]
    out: list[CaseSpec] = []
    for r in raw:
        c = parse_case(r)
        if c.gap_csv.is_file() and c.ohlcv_csv.is_file():
            out.append(c)
    return out


def _parse_float_list(s: str) -> list[float]:
    vals: list[float] = []
    for t in s.split(","):
        x = t.strip()
        if not x:
            continue
        vals.append(float(x))
    return vals


def tuned_shrunk(ps: pd.Series, pw: pd.Series, w: float) -> pd.Series:
    wc = float(max(0.0, min(1.0, w)))
    return (1.0 - wc) * ps + wc * pw


def tuned_tension(ps: pd.Series, pw: pd.Series, mpr: pd.Series, cap: float, max_pull: float) -> pd.Series:
    capv = max(float(cap), 1e-12)
    m = pd.to_numeric(mpr, errors="coerce").clip(lower=0.0)
    t = (m / capv).clip(upper=1.0) * float(max(0.0, min(1.0, max_pull)))
    return (1.0 - t) * ps + t * pw


def tuned_regime_shrunk(
    ps: pd.Series,
    pw: pd.Series,
    mpr: pd.Series,
    *,
    q: float,
    w_calm: float,
    w_stress: float,
) -> pd.Series:
    m = pd.to_numeric(mpr, errors="coerce")
    thr = float(m.quantile(max(0.0, min(1.0, q))))
    wc = float(max(0.0, min(1.0, w_calm)))
    ws = float(max(0.0, min(1.0, w_stress)))
    w = pd.Series(np.where(m > thr, ws, wc), index=m.index, dtype="float64")
    return (1.0 - w) * ps + w * pw


def _eval_case(m: pd.DataFrame, ps_tuned: pd.Series) -> dict[str, float]:
    m2 = m.copy()
    pw = pd.to_numeric(m2.get("P_now"), errors="coerce")
    sc = pd.to_numeric(m2.get("scale_used"), errors="coerce").replace(0, np.nan)
    m2["p_system"] = pd.to_numeric(ps_tuned, errors="coerce")
    m2["signed_sys_vs_now_rel"] = (m2["p_system"] - pw) / sc
    sk = sps.compute_system_price_skill(m2)
    return {
        "n_used": float(sk["n_used"]),
        "hit_rate": float(sk["directional_hit_rate"]),
        "mae_ratio": float(sk["mae_ratio_sys_over_naive"]),
    }


def _load_case_df(c: CaseSpec, gfr: Any) -> pd.DataFrame:
    gap = gfr._read_gap_csv(c.gap_csv)
    raw = gfr._read_ohlcv(c.ohlcv_csv)
    m = gfr._align(raw, gap)
    return gfr.add_features_and_forwards(m, anchor_id=None)


def _agg_score(rows: list[dict[str, float]]) -> tuple[float, float]:
    ratios = [r["mae_ratio"] for r in rows if math.isfinite(r["mae_ratio"])]
    hits = [r["hit_rate"] for r in rows if math.isfinite(r["hit_rate"])]
    mean_ratio = float(np.mean(ratios)) if ratios else float("nan")
    mean_hit = float(np.mean(hits)) if hits else float("nan")
    return mean_ratio, mean_hit


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--case", action="append", default=[], help="NAME|gap_csv|ohlcv 반복")
    p.add_argument(
        "--weights",
        default="0,0.05,0.10,0.15,0.20,0.25,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.95",
        help="shrink 고정 가중치 목록(csv)",
    )
    p.add_argument(
        "--caps",
        default="0.10,0.20,0.30,0.50,0.80,1.00",
        help="tension cap 목록(csv)",
    )
    p.add_argument(
        "--max-pulls",
        default="0.25,0.50,0.75",
        help="tension 최대 pull 목록(csv)",
    )
    p.add_argument(
        "--regime-quantiles",
        default="0.5,0.7,0.8",
        help="regime split quantile 목록(csv, mean_pairwise_rel 기준)",
    )
    p.add_argument(
        "--regime-calm-weights",
        default="0.90,0.93,0.95",
        help="calm 구간 weight 목록(csv)",
    )
    p.add_argument(
        "--regime-stress-weights",
        default="0.95,0.97,0.99",
        help="stress 구간 weight 목록(csv)",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_shrink_tuning.md",
    )
    p.add_argument(
        "--out-csv",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_shrink_tuning.csv",
    )
    args = p.parse_args(argv)

    cases = [parse_case(x) for x in args.case] if args.case else _default_cases()
    if not cases:
        print("no valid OOS/WF cases", file=sys.stderr)
        return 1

    gfr = _load_gfr()
    loaded: dict[str, pd.DataFrame] = {}
    for c in cases:
        if not c.gap_csv.is_file() or not c.ohlcv_csv.is_file():
            print(f"skip case missing files: {c.name}", file=sys.stderr)
            continue
        loaded[c.name] = _load_case_df(c, gfr)
    if not loaded:
        print("all cases skipped", file=sys.stderr)
        return 1

    rows: list[dict[str, Any]] = []
    # baseline
    b_case_rows = []
    for name, m in loaded.items():
        r = _eval_case(m, pd.to_numeric(m.get("p_system"), errors="coerce"))
        b_case_rows.append(r)
    b_ratio, b_hit = _agg_score(b_case_rows)
    rows.append(
        {
            "family": "baseline",
            "param": "p_system",
            "mean_mae_ratio": b_ratio,
            "mean_hit_rate": b_hit,
            "n_cases": len(b_case_rows),
        }
    )

    # shrink sweep
    for w in _parse_float_list(args.weights):
        case_rows = []
        for m in loaded.values():
            ps = pd.to_numeric(m.get("p_system"), errors="coerce")
            pw = pd.to_numeric(m.get("P_now"), errors="coerce")
            case_rows.append(_eval_case(m, tuned_shrunk(ps, pw, w)))
        mean_ratio, mean_hit = _agg_score(case_rows)
        rows.append(
            {
                "family": "shrink",
                "param": f"w={w:.3f}",
                "mean_mae_ratio": mean_ratio,
                "mean_hit_rate": mean_hit,
                "n_cases": len(case_rows),
            }
        )

    # tension sweep
    for cap in _parse_float_list(args.caps):
        for mp in _parse_float_list(args.max_pulls):
            case_rows = []
            for m in loaded.values():
                ps = pd.to_numeric(m.get("p_system"), errors="coerce")
                pw = pd.to_numeric(m.get("P_now"), errors="coerce")
                mpr = pd.to_numeric(m.get("mean_pairwise_rel"), errors="coerce")
                case_rows.append(_eval_case(m, tuned_tension(ps, pw, mpr, cap=cap, max_pull=mp)))
            mean_ratio, mean_hit = _agg_score(case_rows)
            rows.append(
                {
                    "family": "tension",
                    "param": f"cap={cap:.3f},max_pull={mp:.3f}",
                    "mean_mae_ratio": mean_ratio,
                    "mean_hit_rate": mean_hit,
                    "n_cases": len(case_rows),
                }
            )

    # regime-shrink sweep
    for q in _parse_float_list(args.regime_quantiles):
        for wc in _parse_float_list(args.regime_calm_weights):
            for ws in _parse_float_list(args.regime_stress_weights):
                if ws < wc:
                    continue
                case_rows = []
                for m in loaded.values():
                    ps = pd.to_numeric(m.get("p_system"), errors="coerce")
                    pw = pd.to_numeric(m.get("P_now"), errors="coerce")
                    mpr = pd.to_numeric(m.get("mean_pairwise_rel"), errors="coerce")
                    tuned = tuned_regime_shrunk(
                        ps,
                        pw,
                        mpr,
                        q=q,
                        w_calm=wc,
                        w_stress=ws,
                    )
                    case_rows.append(_eval_case(m, tuned))
                mean_ratio, mean_hit = _agg_score(case_rows)
                rows.append(
                    {
                        "family": "regime_shrink",
                        "param": f"q={q:.2f},w_calm={wc:.3f},w_stress={ws:.3f}",
                        "mean_mae_ratio": mean_ratio,
                        "mean_hit_rate": mean_hit,
                        "n_cases": len(case_rows),
                    }
                )

    df = pd.DataFrame(rows)
    df = df.sort_values(["mean_mae_ratio", "mean_hit_rate"], ascending=[True, False]).reset_index(drop=True)
    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out_csv, index=False)

    best = df.iloc[0].to_dict()
    best_shrink = df[df["family"] == "shrink"].head(1)
    best_tension = df[df["family"] == "tension"].head(1)
    b = df[df["family"] == "baseline"].iloc[0]

    lines = [
        "# 시스템가 수축 튜닝 리포트 (OOS/WF 중심)",
        "",
        f"- 케이스 수: **{len(loaded)}** (기본: BTC/ETH OOS/WF)",
        f"- baseline mean_mae_ratio: **{b['mean_mae_ratio']:.4f}** / mean_hit_rate: **{b['mean_hit_rate']:.4f}**",
        f"- best overall: **{best['family']} {best['param']}** (ratio={best['mean_mae_ratio']:.4f}, hit={best['mean_hit_rate']:.4f})",
        "",
        "## Top 10 (ratio 낮은 순)",
        "",
        "| rank | family | param | mean_mae_ratio | mean_hit_rate |",
        "|------|--------|-------|----------------|---------------|",
    ]
    for i, (_, r) in enumerate(df.head(10).iterrows(), start=1):
        lines.append(
            f"| {i} | `{r['family']}` | `{r['param']}` | {r['mean_mae_ratio']:.4f} | {r['mean_hit_rate']:.4f} |"
        )
    lines += ["", "## 후보 비교", ""]
    if not best_shrink.empty:
        rs = best_shrink.iloc[0]
        lines.append(
            f"- best shrink: `{rs['param']}` -> ratio={rs['mean_mae_ratio']:.4f}, hit={rs['mean_hit_rate']:.4f}"
        )
    if not best_tension.empty:
        rt = best_tension.iloc[0]
        lines.append(
            f"- best tension: `{rt['param']}` -> ratio={rt['mean_mae_ratio']:.4f}, hit={rt['mean_hit_rate']:.4f}"
        )
    lines += [
        "",
        "## 해석",
        "",
        "- 목표는 ratio<1 이며, 여전히 1을 크게 넘으면 구조/앵커 자체 개선이 우선.",
        "- 본 결과는 OOS/WF 연구용이며, 매매 권고가 아님.",
        "",
    ]
    args.out.write_text("\n".join(lines), encoding="utf-8")
    print("== wrote:", args.out.resolve(), flush=True)
    print("== wrote:", args.out_csv.resolve(), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
