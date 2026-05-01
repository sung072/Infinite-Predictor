#!/usr/bin/env python3
r"""다중 케이스(종목/분할) 시스템가 검증 매트릭스 리포트 (연구용).

단일 리포트(`system_price_validation_report.py`)를 확장해, 여러 종목·구간(full/OOS/WF)을
한 번에 비교한다.

예시:
  python scripts/system_price_validation_matrix.py
  python scripts/system_price_validation_matrix.py ^
    --case "ETH-full|data/runs/eth_4p_gap_backtest.csv|data/ethusdt_1h_30d.csv" ^
    --case "ETH-oos|data/runs/eth_4p_gap_oos.csv|data/ethusdt_1h_30d.csv"
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from statistics import NormalDist
from typing import Any

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import system_price_skill as sps  # noqa: E402
import llm_report_from_snapshot as lrs  # noqa: E402


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


def parse_case(raw: str) -> CaseSpec:
    parts = [x.strip() for x in raw.split("|")]
    if len(parts) != 3 or any(not x for x in parts):
        raise ValueError(
            "case format must be: NAME|gap_csv_path|ohlcv_csv_path"
        )
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


def parse_symbol_weights(raw: str) -> dict[str, float]:
    out: dict[str, float] = {}
    txt = raw.strip()
    if not txt:
        return out
    for part in txt.split(","):
        p = part.strip()
        if not p:
            continue
        if "=" not in p:
            raise ValueError("symbol weights must be like BTC=0.96,ETH=0.99")
        k, v = [x.strip() for x in p.split("=", 1)]
        if not k:
            raise ValueError("empty symbol in symbol weights")
        out[k.upper()] = float(v)
    return out


def wilson_interval(k: int, n: int, *, z: float = 1.96) -> tuple[float, float]:
    if n <= 0:
        return (float("nan"), float("nan"))
    phat = k / n
    den = 1.0 + (z * z) / n
    center = (phat + (z * z) / (2.0 * n)) / den
    margin = z * math.sqrt((phat * (1.0 - phat) + (z * z) / (4.0 * n)) / n) / den
    return (max(0.0, center - margin), min(1.0, center + margin))


def one_sided_p_hit_rate_gt_half(k: int, n: int) -> float:
    if n <= 0:
        return float("nan")
    p0 = 0.5
    mean = n * p0
    sd = math.sqrt(n * p0 * (1.0 - p0))
    if sd <= 0:
        return float("nan")
    z = (k - mean) / sd
    return 1.0 - NormalDist().cdf(z)


def _default_cases() -> list[CaseSpec]:
    # 저장소 데모 명명 규칙 기본 세트(BTC + ETH, 존재 파일만 자동 채택)
    raw = [
        "BTC-full|data/runs/btc_4p_gap_backtest.csv|data/btcusdt_1h_30d.csv",
        "BTC-oos|data/runs/btc_4p_gap_oos.csv|data/btcusdt_1h_30d.csv",
        "BTC-wf|data/runs/btc_4p_gap_wf.csv|data/btcusdt_1h_30d.csv",
        "ETH-full|data/runs/eth_4p_gap_backtest.csv|data/ethusdt_1h_30d.csv",
        "ETH-oos|data/runs/eth_4p_gap_oos.csv|data/ethusdt_1h_30d.csv",
        "ETH-wf|data/runs/eth_4p_gap_wf.csv|data/ethusdt_1h_30d.csv",
    ]
    out: list[CaseSpec] = []
    for r in raw:
        c = parse_case(r)
        if c.gap_csv.is_file() and c.ohlcv_csv.is_file():
            out.append(c)
    return out


def _run_one_case(c: CaseSpec, gfr: Any) -> dict[str, Any]:
    if not c.gap_csv.is_file():
        raise FileNotFoundError(f"missing gap csv: {c.gap_csv}")
    if not c.ohlcv_csv.is_file():
        raise FileNotFoundError(f"missing ohlcv csv: {c.ohlcv_csv}")
    gap = gfr._read_gap_csv(c.gap_csv)
    raw = gfr._read_ohlcv(c.ohlcv_csv)
    m = gfr._align(raw, gap)
    m = gfr.add_features_and_forwards(m, anchor_id=None)

    sk, p_sys, ps = _skill_from_system_col(m, gfr, system_col="p_system")
    pw = pd.to_numeric(m.get("P_now"), errors="coerce")
    ct = pd.to_numeric(m.get("close_ohlc"), errors="coerce")
    fwd = pd.to_numeric(m.get("fwd_1"), errors="coerce")
    cn = ct * (1.0 + fwd)
    n_dir, k_dir, ci_lo, ci_hi, p_hit = _directional_stats(ps, pw, cn)

    out = {
        "name": c.name,
        "gap_csv": str(c.gap_csv.relative_to(ROOT)),
        "ohlcv": str(c.ohlcv_csv.relative_to(ROOT)),
        "n_used": int(sk["n_used"]),
        "n_dir": n_dir,
        "k_dir": k_dir,
        "hit_rate": float(sk["directional_hit_rate"]),
        "hit_ci_lo": ci_lo,
        "hit_ci_hi": ci_hi,
        "p_hit_gt_half": p_hit,
        "mae_sys": float(sk["mae_sys_next_close"]),
        "mae_naive": float(sk["mae_naive_now_next_close"]),
        "mae_ratio": float(sk["mae_ratio_sys_over_naive"]),
        "mae_gain_pct": (1.0 - float(sk["mae_ratio_sys_over_naive"])) * 100.0,
        "spearman_signed_sys_vs_fwd1": float(p_sys),
    }
    return out


def _directional_stats(
    ps: pd.Series,
    pw: pd.Series,
    cn: pd.Series,
) -> tuple[int, int, float, float, float]:
    ok = ps.notna() & pw.notna() & cn.notna()
    psb, pwb, cnb = ps[ok], pw[ok], cn[ok]
    near_zero = (np.abs(psb - pwb) < 1e-9) | (np.abs(cnb - pwb) < 1e-9)
    dir_valid = ~near_zero
    dir_sign = np.sign(psb - pwb) == np.sign(cnb - pwb)
    n_dir = int(dir_valid.sum())
    k_dir = int(dir_sign[dir_valid].sum()) if n_dir > 0 else 0
    ci_lo, ci_hi = wilson_interval(k_dir, n_dir)
    p_hit = one_sided_p_hit_rate_gt_half(k_dir, n_dir)
    return n_dir, k_dir, ci_lo, ci_hi, p_hit


def _skill_from_system_col(
    m: pd.DataFrame,
    gfr: Any,
    *,
    system_col: str,
    shrink_weight: float = 0.96,
) -> tuple[dict[str, Any], float, pd.Series]:
    m2 = m.copy()
    pw = pd.to_numeric(m2.get("P_now"), errors="coerce")
    if system_col == "p_system_shrunk_custom":
        base = pd.to_numeric(m2.get("p_system"), errors="coerce")
        w = float(max(0.0, min(1.0, shrink_weight)))
        ps = (1.0 - w) * base + w * pw
    else:
        if system_col not in m2.columns:
            raise KeyError(f"missing system column: {system_col}")
        ps = pd.to_numeric(m2.get(system_col), errors="coerce")
    sc = pd.to_numeric(m2.get("scale_used"), errors="coerce").replace(0, np.nan)
    m2["p_system"] = ps
    m2["signed_sys_vs_now_rel"] = (ps - pw) / sc
    sk = sps.compute_system_price_skill(m2)
    p_sys = gfr._spearman(m2["signed_sys_vs_now_rel"], m2["fwd_1"])
    return sk, p_sys, ps


def resolve_shrink_weight(
    case_name: str,
    default_weight: float,
    by_symbol: dict[str, float],
) -> float:
    sym = str(case_name).split("-")[0].strip().upper()
    return float(by_symbol.get(sym, default_weight))


def _fmt(x: float, nd: int = 4) -> str:
    return f"{x:.{nd}f}" if np.isfinite(x) else "nan"


def build_markdown(
    rows: list[dict[str, Any]],
    *,
    min_hit_rate: float,
    max_mae_ratio: float,
    system_col: str,
    strict_oos_wf_only: bool,
    shrink_weight: float,
    ai_block: str = "",
) -> str:
    strict_rows = [r for r in rows if ("-oos" in r["name"].lower() or "-wf" in r["name"].lower())]
    scope_rows = strict_rows if strict_oos_wf_only and strict_rows else rows
    lines: list[str] = [
        "# 시스템가 검증 매트릭스 리포트 (연구용)",
        "",
        "- 목적: 종목·구간(full/OOS/WF)별로 시스템가가 단순 기준(`P_now`)보다 일관되게 나은지 점검",
        f"- 시스템가 열: `{system_col}`",
        f"- custom shrink weight: `{shrink_weight:.3f}` (system_col=`p_system_shrunk_custom` 일 때 사용)",
        "- 판정 규칙(연구용): `hit_rate >= min_hit_rate` AND `mae_ratio <= max_mae_ratio`",
        f"- 현재 임계값: `min_hit_rate={min_hit_rate:.3f}`, `max_mae_ratio={max_mae_ratio:.3f}`",
        f"- PASS 집계 범위: `{'OOS/WF only' if strict_oos_wf_only else 'all cases'}`",
        "",
        "## 케이스별 결과",
        "",
        "| case | n_used | hit_rate | 95% CI | p(hit>0.5) | mae_ratio | mae_gain% | spearman(signed_sys,fwd_1) | pass |",
        "|------|--------|----------|--------|------------|-----------|-----------|----------------------------|------|",
    ]
    for r in sorted(rows, key=lambda x: (np.nan_to_num(x["mae_ratio"], nan=999.0), -x["n_used"])):
        is_pass = (
            np.isfinite(r["hit_rate"])
            and np.isfinite(r["mae_ratio"])
            and r["hit_rate"] >= min_hit_rate
            and r["mae_ratio"] <= max_mae_ratio
        )
        lines.append(
            f"| `{r['name']}` | {r['n_used']} | {_fmt(r['hit_rate'])} | "
            f"[{_fmt(r['hit_ci_lo'])}, {_fmt(r['hit_ci_hi'])}] | {_fmt(r['p_hit_gt_half'])} | "
            f"{_fmt(r['mae_ratio'])} | {_fmt(r['mae_gain_pct'], 2)} | {_fmt(r['spearman_signed_sys_vs_fwd1'])} | "
            f"{'PASS' if is_pass else 'FAIL'} |"
        )

    if rows:
        hit_ok = [
            r for r in scope_rows if np.isfinite(r["hit_rate"]) and r["hit_rate"] >= min_hit_rate
        ]
        mae_ok = [
            r for r in scope_rows if np.isfinite(r["mae_ratio"]) and r["mae_ratio"] <= max_mae_ratio
        ]
        both_ok = [
            r
            for r in scope_rows
            if np.isfinite(r["hit_rate"])
            and np.isfinite(r["mae_ratio"])
            and r["hit_rate"] >= min_hit_rate
            and r["mae_ratio"] <= max_mae_ratio
        ]
        lines += [
            "",
            "## 요약",
            "",
            f"- hit_rate 기준 통과: **{len(hit_ok)}/{len(scope_rows)}**",
            f"- mae_ratio 기준 통과: **{len(mae_ok)}/{len(scope_rows)}**",
            f"- 동시 통과(PASS): **{len(both_ok)}/{len(scope_rows)}**",
            "",
            "## 실패 원인 분해(간단)",
            "",
        ]
        by_symbol: dict[str, list[dict[str, Any]]] = {}
        for r in rows:
            sym = str(r["name"]).split("-")[0].upper()
            by_symbol.setdefault(sym, []).append(r)
        for sym, rs in sorted(by_symbol.items()):
            r_best = min(
                rs,
                key=lambda x: (
                    np.nan_to_num(x["mae_ratio"], nan=999.0),
                    -np.nan_to_num(x["hit_rate"], nan=0.0),
                ),
            )
            lines.append(
                f"- `{sym}` best-case=`{r_best['name']}`: mae_ratio={_fmt(r_best['mae_ratio'])}, hit_rate={_fmt(r_best['hit_rate'])}"
            )
        lines += [
            "",
            "## 해석 주의",
            "",
            "- 본 리포트는 연구용 검증 요약이며, 매매 권고/수익 보장을 의미하지 않음.",
            "- WF/OOS를 우선 신뢰하고, full은 참고치로만 사용 권장.",
            "- p(hit>0.5)는 정규근사 기반 단순값(독립성 가정)으로 참고용임.",
            "",
        ]
    if ai_block:
        lines += ["## AI 추천(보조)", "", ai_block.strip(), ""]
    return "\n".join(lines)


def build_ai_advice_block(
    rows: list[dict[str, Any]],
    *,
    min_hit_rate: float,
    max_mae_ratio: float,
    try_llm: bool,
) -> str:
    by_case = [
        {
            "case": r["name"],
            "hit_rate": r["hit_rate"],
            "mae_ratio": r["mae_ratio"],
            "pass_rule": bool(
                np.isfinite(r["hit_rate"])
                and np.isfinite(r["mae_ratio"])
                and r["hit_rate"] >= min_hit_rate
                and r["mae_ratio"] <= max_mae_ratio
            ),
        }
        for r in rows
    ]
    payload = {
        "thresholds": {"min_hit_rate": min_hit_rate, "max_mae_ratio": max_mae_ratio},
        "cases": by_case,
    }
    rule_text = (
        "- 기본 원칙: `mae_ratio <= 1`을 우선, `hit_rate`는 보조 지표로 유지\n"
        "- OOS/WF PASS가 유지되면 임계값 고정, 깨지면 `symbol_shrink_weights`만 소폭 재튜닝\n"
        "- full 구간 FAIL은 경보 참고치로만 사용(운영 판정은 OOS/WF 우선)"
    )
    if not try_llm:
        return rule_text + "\n- (LLM 미사용: 규칙 추천만 출력)"

    sys_prompt = (
        "당신은 리스크-보수적 검증 보조자다. 매수/매도/수익 예측 금지. "
        "threshold와 재튜닝 우선순위만 한국어 bullet 3~5개로 답하라."
    )
    user_prompt = (
        "아래 검증 요약을 보고 임계값 운영 제안만 하라.\n"
        f"```json\n{json.dumps(payload, ensure_ascii=False)}\n```"
    )
    out = lrs.llm_openai_chat_completion(
        [{"role": "system", "content": sys_prompt}, {"role": "user", "content": user_prompt}]
    )
    if out:
        return out.strip()
    return rule_text + "\n- (LLM 호출 실패 또는 키 미설정: 규칙 추천으로 대체)"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--case",
        action="append",
        default=[],
        help="NAME|gap_csv_path|ohlcv_csv_path (반복 사용 가능)",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_validation_matrix.md",
    )
    p.add_argument(
        "--min-hit-rate",
        type=float,
        default=0.505,
        help="PASS 판정용 최소 방향 적중률",
    )
    p.add_argument(
        "--max-mae-ratio",
        type=float,
        default=1.00,
        help="PASS 판정용 최대 MAE 비율(시스템/단순, 1 이하면 단순 대비 우위)",
    )
    p.add_argument(
        "--system-col",
        default="p_system_shrunk_custom",
        choices=("p_system", "p_system_shrunk", "p_system_tension", "p_system_shrunk_custom"),
        help="검증에 사용할 시스템가 열",
    )
    p.add_argument(
        "--shrink-weight",
        type=float,
        default=0.96,
        help="system_col=p_system_shrunk_custom 일 때 P_now 쪽 가중치",
    )
    p.add_argument(
        "--symbol-shrink-weights",
        default="BTC=0.96,ETH=0.99",
        help="종목별 shrink 가중치(예: BTC=0.96,ETH=0.99). 심볼 미지정은 --shrink-weight 사용",
    )
    p.add_argument(
        "--strict-oos-wf-only",
        action="store_true",
        help="PASS 집계를 OOS/WF 케이스로만 계산(full 제외)",
    )
    p.add_argument(
        "--ai-judge",
        action="store_true",
        help="리포트 하단에 AI 추천(LLM 우선, 실패 시 규칙 대체) 추가",
    )
    p.add_argument(
        "--ai-no-llm",
        action="store_true",
        help="--ai-judge 사용 시 LLM 호출 없이 규칙 추천만 추가",
    )
    args = p.parse_args(argv)
    try:
        symbol_weights = parse_symbol_weights(args.symbol_shrink_weights)
    except ValueError as e:
        print(f"bad --symbol-shrink-weights: {e}", file=sys.stderr)
        return 2

    cases: list[CaseSpec] = []
    for raw in args.case:
        try:
            cases.append(parse_case(raw))
        except ValueError as e:
            print(f"bad --case `{raw}`: {e}", file=sys.stderr)
            return 2
    if not cases:
        cases = _default_cases()
    if not cases:
        print("no valid cases. pass --case NAME|gap_csv|ohlcv", file=sys.stderr)
        return 1

    gfr = _load_gfr()
    rows: list[dict[str, Any]] = []
    for c in cases:
        try:
            r = _run_one_case(c, gfr)
            # 재계산: 선택한 시스템가 열로 검증
            gap = gfr._read_gap_csv(c.gap_csv)
            raw = gfr._read_ohlcv(c.ohlcv_csv)
            m = gfr._align(raw, gap)
            m = gfr.add_features_and_forwards(m, anchor_id=None)
            sk, p_sys, ps_sel = _skill_from_system_col(
                m,
                gfr,
                system_col=args.system_col,
                shrink_weight=resolve_shrink_weight(
                    c.name,
                    args.shrink_weight,
                    symbol_weights,
                ),
            )
            pw = pd.to_numeric(m.get("P_now"), errors="coerce")
            ct = pd.to_numeric(m.get("close_ohlc"), errors="coerce")
            fwd = pd.to_numeric(m.get("fwd_1"), errors="coerce")
            cn = ct * (1.0 + fwd)
            n_dir, k_dir, ci_lo, ci_hi, p_hit = _directional_stats(ps_sel, pw, cn)
            r.update(
                {
                    "n_used": int(sk["n_used"]),
                    "n_dir": n_dir,
                    "k_dir": k_dir,
                    "hit_rate": float(sk["directional_hit_rate"]),
                    "hit_ci_lo": ci_lo,
                    "hit_ci_hi": ci_hi,
                    "p_hit_gt_half": p_hit,
                    "mae_sys": float(sk["mae_sys_next_close"]),
                    "mae_naive": float(sk["mae_naive_now_next_close"]),
                    "mae_ratio": float(sk["mae_ratio_sys_over_naive"]),
                    "mae_gain_pct": (1.0 - float(sk["mae_ratio_sys_over_naive"])) * 100.0,
                    "spearman_signed_sys_vs_fwd1": float(p_sys),
                }
            )
            rows.append(r)
        except (FileNotFoundError, ValueError, KeyError) as e:
            print(f"skip `{c.name}`: {e}", file=sys.stderr)

    if not rows:
        print("all cases failed/skipped", file=sys.stderr)
        return 1

    ai_block = ""
    if args.ai_judge:
        ai_block = build_ai_advice_block(
            rows,
            min_hit_rate=args.min_hit_rate,
            max_mae_ratio=args.max_mae_ratio,
            try_llm=not args.ai_no_llm,
        )

    md = build_markdown(
        rows,
        min_hit_rate=args.min_hit_rate,
        max_mae_ratio=args.max_mae_ratio,
        system_col=args.system_col,
        strict_oos_wf_only=args.strict_oos_wf_only,
        shrink_weight=args.shrink_weight,
        ai_block=ai_block,
    )
    out = args.out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print("== wrote:", out, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
