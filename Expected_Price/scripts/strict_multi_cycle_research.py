#!/usr/bin/env python3
r"""Strict Separation + Multi-Cycle 연구 러너.

핵심 규칙:
1) 한 사이클 내부에서는 튜닝하지 않고 기본 공식 후보만 생성한다.
2) 사이클 i 후보는 사이클 i+1에서 "검증만" 한다.
3) 모든 사이클 후 메타 통합(유사 공식 그룹 요약)한다.
4) 마지막 unseen 구간에서 최종 후보만 재검증한다.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
for _p in (ROOT / "code", ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import gap_forward_return_research as gfr  # noqa: E402
import system_price_validation_matrix as spm  # noqa: E402
import validation_trade_metrics as vtm  # noqa: E402
import vbt_gap_research as vg  # noqa: E402
from temporal_validation import run_holdout_validation  # noqa: E402

SYMBOL_FILES: dict[str, tuple[str, str]] = {
    "BTC": ("data/btcusdt_1h_30d.csv", "data/derived/btcusdt_factors_4p.csv"),
    "ETH": ("data/ethusdt_1h_30d.csv", "data/derived/ethusdt_factors_4p.csv"),
    "SOL": ("data/solusdt_1h_30d.csv", "data/derived/solusdt_factors_4p.csv"),
    "BNB": ("data/bnbusdt_1h_30d.csv", "data/derived/bnbusdt_factors_4p.csv"),
    "XRP": ("data/xrpusdt_1h_30d.csv", "data/derived/xrpusdt_factors_4p.csv"),
    "ADA": ("data/adausdt_1h_30d.csv", "data/derived/adausdt_factors_4p.csv"),
    "DOGE": ("data/dogeusdt_1h_30d.csv", "data/derived/dogeusdt_factors_4p.csv"),
    "AVAX": ("data/avaxusdt_1h_30d.csv", "data/derived/avaxusdt_factors_4p.csv"),
    "LINK": ("data/linkusdt_1h_30d.csv", "data/derived/linkusdt_factors_4p.csv"),
    "TRX": ("data/trxusdt_1h_30d.csv", "data/derived/trxusdt_factors_4p.csv"),
}


@dataclass(frozen=True)
class CycleWindow:
    cycle_id: int
    start: int
    stop: int


def _parse_floats(raw: str) -> list[float]:
    return [float(x.strip()) for x in raw.split(",") if x.strip()]


def _parse_ints(raw: str) -> list[int]:
    return [int(x.strip()) for x in raw.split(",") if x.strip()]


def _fmt(x: Any, nd: int = 4) -> str:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return "n/a"
    if math.isnan(v):
        return "n/a"
    return f"{v:.{nd}f}"


# argparse 기본 가중치 = schemas/strict_multi_cycle_composite.example.json 의 balanced 프리셋
_RECOMMENDED_WEIGHT_PRESETS: dict[str, tuple[float, float, float, float, float]] = {
    "balanced": (0.4, 0.2, 0.15, 0.15, 0.1),
    "direction_focused": (0.28, 0.38, 0.22, 0.08, 0.04),
    "risk_adjusted_focused": (0.32, 0.12, 0.1, 0.28, 0.18),
}


def _detect_weight_preset(args: Any) -> str | None:
    t = (
        float(args.w_mae),
        float(args.w_hit),
        float(args.w_rr),
        float(args.w_sharpe),
        float(args.w_calmar),
    )
    for name, ref in _RECOMMENDED_WEIGHT_PRESETS.items():
        if all(abs(a - b) < 1e-6 for a, b in zip(t, ref)):
            return name
    return None


def _improvement_vs_all_cell(top_bucket: dict[str, Any], baseline: dict[str, Any]) -> str:
    """top 코호트 vs 전체 validations: hit 은 퍼센트포인트 차, mae_ratio 는 낮을수록 좋음을 상대%로 표시."""
    h_t = _safe_float((top_bucket.get("directional_hit_rate") or {}).get("mean"))
    h_a = _safe_float((baseline.get("directional_hit_rate") or {}).get("mean"))
    m_t = _safe_float((top_bucket.get("mae_ratio_sys_over_naive") or {}).get("mean"))
    m_a = _safe_float((baseline.get("mae_ratio_sys_over_naive") or {}).get("mean"))
    parts: list[str] = []
    if math.isfinite(h_t) and math.isfinite(h_a):
        parts.append(f"hit {(h_t - h_a) * 100.0:+.2f}pp")
    if math.isfinite(m_t) and math.isfinite(m_a) and abs(m_a) > 1e-12:
        rel = (m_a - m_t) / abs(m_a) * 100.0
        parts.append(f"mae {rel:+.1f}%rel")
    return ", ".join(parts) if parts else "n/a"


def _safe_float(x: Any) -> float:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return float("nan")
    if math.isnan(v):
        return float("nan")
    return v


def _composite_score(
    metrics: dict[str, Any],
    *,
    w_mae: float,
    w_mae_tail: float,
    w_hit: float,
    w_rr: float,
    w_sharpe: float,
    w_calmar: float,
) -> float:
    mae = _safe_float(metrics.get("mae_ratio_sys_over_naive"))
    mae_p90 = _safe_float(metrics.get("mae_ratio_sys_over_naive_p90"))
    hit = _safe_float(metrics.get("directional_hit_rate"))
    rr = _safe_float(metrics.get("mean_rr"))
    shp = _safe_float(metrics.get("sharpe_annualized"))
    cal = _safe_float(metrics.get("calmar_proxy"))
    if not math.isfinite(mae):
        return float("nan")
    # bounded transforms for robust linear blend
    mae_term = 1.0 / max(mae, 1e-9)  # lower mae_ratio is better
    if math.isfinite(mae_p90) and float(w_mae_tail) > 0.0:
        tail_term = 1.0 / max(mae_p90, 1e-9)
    else:
        tail_term = mae_term
    hit_term = hit if math.isfinite(hit) else 0.0
    rr_term = math.tanh(rr / 3.0) if math.isfinite(rr) else 0.0
    shp_term = math.tanh(shp / 3.0) if math.isfinite(shp) else 0.0
    cal_term = math.tanh(cal / 3.0) if math.isfinite(cal) else 0.0
    return float(
        w_mae * mae_term
        + float(w_mae_tail) * tail_term
        + w_hit * hit_term
        + w_rr * rr_term
        + w_sharpe * shp_term
        + w_calmar * cal_term
    )


def _zscore_vector(xs: list[float]) -> list[float]:
    """유한값만으로 mean/pstdev 계산; 비유한은 z 기여 0(중립)."""
    vals = [_safe_float(v) for v in xs]
    finite = [v for v in vals if math.isfinite(v)]
    if len(finite) < 2:
        # 표본이 너무 적거나 전부 NaN이면 차원 전체를 중립(0) 처리
        return [0.0 for _ in vals]
    mu = statistics.mean(finite)
    sd = statistics.pstdev(finite)
    if sd < 1e-12:
        return [0.0 for _ in vals]
    out: list[float] = []
    for v in vals:
        if not math.isfinite(v):
            out.append(0.0)
        else:
            out.append((v - mu) / sd)
    return out


def _blend_weighted_z(
    zs: list[float],
    *,
    w_mae: float,
    w_hit: float,
    w_rr: float,
    w_sharpe: float,
    w_calmar: float,
) -> float:
    w = (w_mae, w_hit, w_rr, w_sharpe, w_calmar)
    return float(
        sum((0.0 if (not math.isfinite(z)) else z) * ww for z, ww in zip(zs, w))
    )


def _attach_composite_rank_meta(
    meta_rows: list[dict[str, Any]],
    *,
    composite_norm: str,
    w_mae: float,
    w_hit: float,
    w_rr: float,
    w_sharpe: float,
    w_calmar: float,
) -> None:
    if composite_norm != "zscore_within_run" or len(meta_rows) < 2:
        for r in meta_rows:
            r["composite_rank_score"] = float(_safe_float(r.get("composite_mean", float("nan"))))
        return
    mae_better = [-_safe_float(r.get("mae_ratio_mean")) for r in meta_rows]
    hit_v = [_safe_float(r.get("hit_mean")) for r in meta_rows]
    rr_v = [_safe_float(r.get("mean_rr_mean")) for r in meta_rows]
    sh_v = [_safe_float(r.get("sharpe_annualized_mean")) for r in meta_rows]
    ca_v = [_safe_float(r.get("calmar_mean")) for r in meta_rows]
    z_m = _zscore_vector(mae_better)
    z_h = _zscore_vector(hit_v)
    z_r = _zscore_vector(rr_v)
    z_s = _zscore_vector(sh_v)
    z_c = _zscore_vector(ca_v)
    for i, r in enumerate(meta_rows):
        r["composite_rank_score"] = _blend_weighted_z(
            [z_m[i], z_h[i], z_r[i], z_s[i], z_c[i]],
            w_mae=w_mae,
            w_hit=w_hit,
            w_rr=w_rr,
            w_sharpe=w_sharpe,
            w_calmar=w_calmar,
        )


def _attach_composite_rank_final(
    final_rows: list[dict[str, Any]],
    *,
    composite_norm: str,
    w_mae: float,
    w_hit: float,
    w_rr: float,
    w_sharpe: float,
    w_calmar: float,
) -> None:
    if composite_norm != "zscore_within_run" or len(final_rows) < 2:
        for fr in final_rows:
            m = fr["metrics"]
            m["composite_rank_score"] = float(_safe_float(m.get("composite_score", float("nan"))))
        return
    ms = [fr["metrics"] for fr in final_rows]
    mae_better = [-_safe_float(m.get("mae_ratio_sys_over_naive")) for m in ms]
    hit_v = [_safe_float(m.get("directional_hit_rate")) for m in ms]
    rr_v = [_safe_float(m.get("mean_rr")) for m in ms]
    sh_v = [_safe_float(m.get("sharpe_annualized")) for m in ms]
    ca_v = [_safe_float(m.get("calmar_proxy")) for m in ms]
    z_m = _zscore_vector(mae_better)
    z_h = _zscore_vector(hit_v)
    z_r = _zscore_vector(rr_v)
    z_s = _zscore_vector(sh_v)
    z_c = _zscore_vector(ca_v)
    for i, fr in enumerate(final_rows):
        fr["metrics"]["composite_rank_score"] = _blend_weighted_z(
            [z_m[i], z_h[i], z_r[i], z_s[i], z_c[i]],
            w_mae=w_mae,
            w_hit=w_hit,
            w_rr=w_rr,
            w_sharpe=w_sharpe,
            w_calmar=w_calmar,
        )


def _extract_composite_config_path(argv: list[str] | None) -> Path | None:
    av = argv if argv is not None else sys.argv[1:]
    i = 0
    while i < len(av):
        if av[i] == "--composite-config":
            if i + 1 < len(av):
                return Path(av[i + 1])
            return None
        if av[i].startswith("--composite-config="):
            return Path(av[i].split("=", 1)[1].strip().strip('"').strip("'"))
        i += 1
    return None


def _load_composite_defaults(path: Path) -> dict[str, Any]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        return {}
    out: dict[str, Any] = {}
    cw = raw.get("composite_weights")
    if isinstance(cw, dict):
        for k in ("w_mae", "w_mae_tail", "w_hit", "w_rr", "w_sharpe", "w_calmar"):
            if k in cw and cw[k] is not None:
                out[k] = float(cw[k])
    for k in ("w_mae", "w_mae_tail", "w_hit", "w_rr", "w_sharpe", "w_calmar"):
        if k in raw and raw[k] is not None and k not in out:
            out[k] = float(raw[k])
    if raw.get("composite_norm") is not None:
        out["composite_norm"] = str(raw["composite_norm"])
    if raw.get("composite_norm_final") is not None:
        out["composite_norm_final"] = str(raw["composite_norm_final"])
    if raw.get("rank_by") is not None:
        out["rank_by"] = str(raw["rank_by"])
    if raw.get("cohort_top_fraction") is not None:
        out["cohort_top_fraction"] = float(raw["cohort_top_fraction"])
    if raw.get("cohort_sensitivity") is not None:
        out["cohort_sensitivity"] = bool(raw["cohort_sensitivity"])
    csf = raw.get("cohort_sensitivity_fractions")
    if csf is not None:
        if isinstance(csf, list):
            out["cohort_sensitivity_fractions"] = ",".join(str(x).strip() for x in csf if str(x).strip())
        else:
            out["cohort_sensitivity_fractions"] = str(csf).strip()
    return out


def _stats_numeric(xs: list[float]) -> dict[str, float | int]:
    ys = [float(x) for x in xs if math.isfinite(float(x))]
    if not ys:
        return {"n": 0, "mean": float("nan"), "pstdev": float("nan"), "min": float("nan"), "max": float("nan")}
    pst = statistics.pstdev(ys) if len(ys) > 1 else 0.0
    return {
        "n": int(len(ys)),
        "mean": float(statistics.mean(ys)),
        "pstdev": float(pst),
        "min": float(min(ys)),
        "max": float(max(ys)),
    }


def _percentile_sorted(sorted_vals: list[float], p: float) -> float:
    if not sorted_vals:
        return float("nan")
    p = float(max(0.0, min(1.0, p)))
    idx = int(round((len(sorted_vals) - 1) * p))
    return float(sorted_vals[max(0, min(len(sorted_vals) - 1, idx))])


def _dev_top_fraction_cohort_report(
    validations: list[dict[str, Any]],
    *,
    fraction: float,
    rank_key: str = "composite_score",
) -> dict[str, Any]:
    """dev cycle(i)->(i+1) 검증 행들 중 rank_key 기준 상위 fraction 코호트의 성능 분포(연구용)."""
    frac = float(max(0.0, min(0.5, fraction)))
    scored: list[tuple[float, dict[str, Any]]] = []
    for v in validations:
        m = v.get("metrics") or {}
        s = _safe_float(m.get(rank_key))
        if math.isfinite(s):
            scored.append((s, m))
    n_eligible = len(scored)
    if n_eligible == 0:
        return {
            "n_eligible": 0,
            "fraction_requested": frac,
            "top_n": 0,
            "rank_key": rank_key,
            "cutoff_rank_score": float("nan"),
        }
    scored.sort(key=lambda t: -t[0])
    top_n = max(1, int(math.ceil(n_eligible * frac)))
    top_mets = [t[1] for t in scored[:top_n]]
    cutoff = float(scored[top_n - 1][0])

    def pull(key: str) -> list[float]:
        return [_safe_float(mm.get(key)) for mm in top_mets]

    pool_scores = sorted(float(t[0]) for t in scored)
    all_hit = [_safe_float((v.get("metrics") or {}).get("directional_hit_rate")) for v in validations]
    all_mae = [_safe_float((v.get("metrics") or {}).get("mae_ratio_sys_over_naive")) for v in validations]
    return {
        "n_eligible": int(n_eligible),
        "fraction_used": frac,
        "top_n": int(top_n),
        "rank_key": rank_key,
        "cutoff_rank_score": cutoff,
        "full_pool_rank_score_percentiles": {
            "p10": _percentile_sorted(pool_scores, 0.10),
            "p50": _percentile_sorted(pool_scores, 0.50),
            "p90": _percentile_sorted(pool_scores, 0.90),
        },
        "top_bucket": {
            "directional_hit_rate": _stats_numeric(pull("directional_hit_rate")),
            "mae_ratio_sys_over_naive": _stats_numeric(pull("mae_ratio_sys_over_naive")),
            "mean_rr": _stats_numeric(pull("mean_rr")),
            "sharpe_annualized": _stats_numeric(pull("sharpe_annualized")),
            "calmar_proxy": _stats_numeric(pull("calmar_proxy")),
            "composite_score": _stats_numeric(pull("composite_score")),
        },
        "all_validations_baseline": {
            "directional_hit_rate": _stats_numeric(all_hit),
            "mae_ratio_sys_over_naive": _stats_numeric(all_mae),
        },
    }


def _build_cycles(n_rows: int, *, n_window: int, step: int) -> list[CycleWindow]:
    out: list[CycleWindow] = []
    cid = 0
    s = 0
    while s + n_window <= n_rows:
        out.append(CycleWindow(cycle_id=cid, start=s, stop=s + n_window))
        s += step
        cid += 1
    return out


def _discover_candidates(
    cycle_id: int,
    shrinks: list[float],
    embargos: list[int],
    *,
    feature: str,
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    idx = 0
    for emb in embargos:
        for sh in shrinks:
            out.append(
                {
                    "formula_id": f"C{cycle_id:04d}-F{idx:04d}",
                    "family": "base",
                    "system_col": "p_system_shrunk_custom",
                    "shrink_weight": float(sh),
                    "embargo_bars": int(emb),
                    "trust_feature": None,
                    "trust_q_low": None,
                    "trust_q_high": None,
                }
            )
            idx += 1
            # 조건부 신뢰 규칙 후보(사이클 내부 튜닝 없이 고정 분위 대역)
            for ql, qh, fam in ((0.0, 0.4, "trust_low40"), (0.6, 1.0, "trust_high40")):
                out.append(
                    {
                        "formula_id": f"C{cycle_id:04d}-F{idx:04d}",
                        "family": fam,
                        "system_col": "p_system_shrunk_custom",
                        "shrink_weight": float(sh),
                        "embargo_bars": int(emb),
                        "trust_feature": feature,
                        "trust_q_low": float(ql),
                        "trust_q_high": float(qh),
                    }
                )
                idx += 1
    return out


def _subset_validation_by_gap_intensity(
    val_df_eval: pd.DataFrame,
    *,
    column: str | None,
    vmin: float | None,
    vmax: float | None,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Trust(또는 전체 val) 적용 뒤 검증 행에 Gap/Tension 등 스칼라 임계 필터.

    ``column`` 이 비어 있거나 ``vmin``·``vmax`` 가 모두 None 이면 필터 비활성.
    컬럼이 없으면 행은 유지하고 ``eval_gap_filter_error`` 만 기록한다.
    """
    meta: dict[str, Any] = {"eval_gap_filter_active": False}
    col = (column or "").strip()
    if not col or (vmin is None and vmax is None):
        return val_df_eval, meta
    meta["eval_gap_filter_active"] = True
    meta["eval_gap_filter_column"] = col
    meta["eval_gap_filter_min"] = vmin
    meta["eval_gap_filter_max"] = vmax
    n_before = int(len(val_df_eval))
    meta["n_rows_before_eval_gap_filter"] = n_before
    if n_before == 0:
        meta["eval_gap_filter_note"] = "empty_input"
        meta["eval_gap_filter_active"] = False
        return val_df_eval, meta
    if col not in val_df_eval.columns:
        meta["eval_gap_filter_error"] = f"missing_column:{col}"
        meta["eval_gap_filter_active"] = False
        return val_df_eval, meta
    ser = pd.to_numeric(val_df_eval[col], errors="coerce")
    mask = pd.Series(True, index=val_df_eval.index)
    if vmin is not None:
        mask &= ser >= float(vmin)
    if vmax is not None:
        mask &= ser <= float(vmax)
    sub = val_df_eval.loc[mask.fillna(False)].copy()
    n_after = int(len(sub))
    meta["n_rows_after_eval_gap_filter"] = n_after
    meta["eval_gap_filter_coverage"] = (n_after / n_before) if n_before else float("nan")
    if n_after < 5:
        meta["eval_gap_filter_too_few_rows"] = True
        return val_df_eval.iloc[:0].copy(), meta
    meta["eval_gap_filter_too_few_rows"] = False
    return sub, meta


def _evaluate_formula_on_cycle(
    formula: dict[str, Any],
    *,
    ohl_segment: Any,
    registry: Path,
    factors_csv: Path,
    train_bars: int,
    val_bars: int,
    seed: int,
    bars_per_year: float,
    include_regime_quintiles: bool = False,
    eval_gap_filter_column: str | None = None,
    eval_gap_filter_min: float | None = None,
    eval_gap_filter_max: float | None = None,
) -> dict[str, Any]:
    ho = run_holdout_validation(
        registry,
        ohl_segment,
        n_train_bars=train_bars,
        n_embargo_bars=int(formula["embargo_bars"]),
        n_val_bars=val_bars,
        seed=seed,
        factors_path=factors_csv,
        include_pairwise_columns=True,
        include_system_variants=True,
        system_col=str(formula["system_col"]),
        shrink_weight=float(formula["shrink_weight"]),
    )
    # base metrics (all validation rows)
    metrics = dict(ho["metrics_validation"])
    coverage = 1.0
    n_sel = int(metrics.get("n_rows_validation", 0))
    val_df = ho["merged_validation_df"]
    val_df_eval = val_df
    trust_feature = formula.get("trust_feature")
    if trust_feature:
        full = ho["merged_full_df"]
        split = ho["holdout_split"]
        train_df = full.iloc[split.train_slice]
        sf_train = train_df.get(trust_feature)
        sf_val = val_df.get(trust_feature)
        if sf_train is not None and sf_val is not None:
            tser = pd.to_numeric(sf_train, errors="coerce").dropna()
            if len(tser) >= 10:
                ql = float(formula["trust_q_low"])
                qh = float(formula["trust_q_high"])
                lo = float(tser.quantile(ql))
                hi = float(tser.quantile(qh))
                sv = pd.to_numeric(sf_val, errors="coerce")
                mask = sv.between(lo, hi, inclusive="both")
                sub = val_df.loc[mask.fillna(False)]
                n_sel = int(len(sub))
                n_tot = int(len(val_df))
                coverage = (n_sel / n_tot) if n_tot > 0 else float("nan")
                if n_sel >= 5:
                    val_df_eval = sub
                    sk, rho, _ = spm._skill_from_system_col(
                        sub,
                        gfr,
                        system_col=str(formula["system_col"]),
                        shrink_weight=float(formula["shrink_weight"]),
                    )
                    metrics.update(sk)
                    metrics["spearman_signed_sys_vs_fwd1"] = float(rho)
                else:
                    val_df_eval = val_df.iloc[:0]
                    metrics["directional_hit_rate"] = float("nan")
                    metrics["mae_ratio_sys_over_naive"] = float("nan")
                    metrics["spearman_signed_sys_vs_fwd1"] = float("nan")
    val_df_eval, gap_meta = _subset_validation_by_gap_intensity(
        val_df_eval,
        column=eval_gap_filter_column,
        vmin=eval_gap_filter_min,
        vmax=eval_gap_filter_max,
    )
    metrics.update(gap_meta)
    if gap_meta.get("eval_gap_filter_active") and not gap_meta.get("eval_gap_filter_error"):
        if gap_meta.get("eval_gap_filter_too_few_rows"):
            metrics["directional_hit_rate"] = float("nan")
            metrics["mae_ratio_sys_over_naive"] = float("nan")
            metrics["spearman_signed_sys_vs_fwd1"] = float("nan")
        else:
            skg, rhog, _ = spm._skill_from_system_col(
                val_df_eval,
                gfr,
                system_col=str(formula["system_col"]),
                shrink_weight=float(formula["shrink_weight"]),
            )
            metrics.update(skg)
            metrics["spearman_signed_sys_vs_fwd1"] = float(rhog)
    metrics["trust_coverage"] = coverage
    metrics["n_selected"] = n_sel
    tm = vtm.compute_trade_metrics(
        val_df_eval,
        system_col=str(formula["system_col"]),
        shrink_weight=float(formula["shrink_weight"]),
        bars_per_year=bars_per_year,
    )
    metrics.update(tm)
    if include_regime_quintiles and len(val_df_eval) >= 20:
        tables: dict[str, Any] = {}
        for col in ("mean_pairwise_per_atr", "p_system_tension"):
            t5 = vtm.regime_quintile_table(
                val_df_eval,
                col,
                system_col=str(formula["system_col"]),
                shrink_weight=float(formula["shrink_weight"]),
                gfr=gfr,
                q=5,
                bars_per_year=bars_per_year,
            )
            t10 = vtm.regime_quintile_table(
                val_df_eval,
                col,
                system_col=str(formula["system_col"]),
                shrink_weight=float(formula["shrink_weight"]),
                gfr=gfr,
                q=10,
                bars_per_year=bars_per_year,
            )
            tt = vtm.regime_tail_band_table(
                val_df_eval,
                col,
                system_col=str(formula["system_col"]),
                shrink_weight=float(formula["shrink_weight"]),
                gfr=gfr,
                bands=(0.1, 0.2),
                bars_per_year=bars_per_year,
            )
            if t5 or t10 or tt:
                tables[col] = {
                    "q5": t5,
                    "q10": t10,
                    "tails_10_20": tt,
                }
        if tables:
            metrics["regime_quintile_tables"] = tables
    return metrics


def _cluster_key(f: dict[str, Any]) -> str:
    if f.get("trust_feature"):
        return (
            f"{f['family']}|emb={f['embargo_bars']}|sh={float(f['shrink_weight']):.2f}|"
            f"feat={f['trust_feature']}|q={f['trust_q_low']:.1f}-{f['trust_q_high']:.1f}"
        )
    return f"{f['family']}|emb={f['embargo_bars']}|sh={float(f['shrink_weight']):.2f}"


def main(argv: list[str] | None = None) -> int:
    av = list(sys.argv[1:] if argv is None else argv)
    peek_cfg = _extract_composite_config_path(av)
    file_defaults: dict[str, Any] = {}
    if peek_cfg is not None:
        if not peek_cfg.is_file():
            print("warning: --composite-config file not found:", peek_cfg.resolve(), file=sys.stderr)
        else:
            try:
                file_defaults = _load_composite_defaults(peek_cfg)
            except (OSError, json.JSONDecodeError, TypeError, ValueError) as e:
                print("warning: failed to load composite config:", peek_cfg, e, file=sys.stderr)
                file_defaults = {}
    _cfg_allow = {
        "w_mae",
        "w_mae_tail",
        "w_hit",
        "w_rr",
        "w_sharpe",
        "w_calmar",
        "composite_norm",
        "composite_norm_final",
        "rank_by",
        "cohort_top_fraction",
        "cohort_sensitivity",
        "cohort_sensitivity_fractions",
    }
    p = argparse.ArgumentParser(description=__doc__)
    p.set_defaults(**{k: v for k, v in file_defaults.items() if k in _cfg_allow})
    p.add_argument("--symbol", default="BTC", help="BTC/ETH/SOL")
    p.add_argument(
        "--ohlcv",
        type=Path,
        default=None,
        help="OHLCV CSV 경로(지정 시 symbol 기본 경로보다 우선)",
    )
    p.add_argument(
        "--factors-csv",
        type=Path,
        default=None,
        help="factor CSV 경로(지정 시 symbol 기본 경로보다 우선)",
    )
    p.add_argument(
        "--registry",
        type=Path,
        default=ROOT / "schemas" / "predictor_registry.btc_4p.json",
    )
    p.add_argument("--train-bars", type=int, default=120)
    p.add_argument("--val-bars", type=int, default=36)
    p.add_argument("--cycle-step", type=int, default=20)
    p.add_argument("--embargos", default="12,24")
    p.add_argument("--shrinks", default="0.94,0.95,0.96,0.97")
    p.add_argument("--trust-feature", default="mean_pairwise_per_atr")
    p.add_argument(
        "--eval-gap-filter-column",
        default="",
        help=(
            "Trust(또는 전체 val) 적용 후 검증 행을 한 번 더 줄일 컬럼 "
            "(예: mean_pairwise_per_atr, mean_pairwise_rel, p_system_tension). "
            "비우면 비활성. min/max 중 하나 이상과 함께 사용."
        ),
    )
    p.add_argument(
        "--eval-gap-filter-min",
        type=float,
        default=None,
        help="eval-gap-filter-column 값이 이 값 이상인 봉만 hit/mae/trade 집계.",
    )
    p.add_argument(
        "--eval-gap-filter-max",
        type=float,
        default=None,
        help="eval-gap-filter-column 값이 이 값 이하인 봉만 집계(상한·밴드용).",
    )
    p.add_argument("--unseen-ratio", type=float, default=0.25)
    p.add_argument("--min-evals", type=int, default=3)
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--bars-per-year", type=float, default=24.0 * 365.0)
    p.add_argument(
        "--rank-by",
        choices=["composite", "mae_hit"],
        default="composite",
    )
    p.add_argument(
        "--w-mae",
        type=float,
        default=0.40,
        help="composite 가중치 (기본값은 balanced 프리셋과 동일; 예시는 schemas/strict_multi_cycle_composite.example.json)",
    )
    p.add_argument("--w-hit", type=float, default=0.20, help="composite 가중치 (balanced 기본)")
    p.add_argument("--w-rr", type=float, default=0.15, help="composite 가중치 (balanced 기본)")
    p.add_argument("--w-sharpe", type=float, default=0.15, help="composite 가중치 (balanced 기본)")
    p.add_argument("--w-calmar", type=float, default=0.10, help="composite 가중치 (balanced 기본)")
    p.add_argument(
        "--w-mae-tail",
        type=float,
        default=0.0,
        help=(
            "봉별 mae_ratio(시스템오차/naive오차)의 90%분위에 대한 가중(꼬리 리스크). "
            "0이면 비활성. metrics 에 mae_ratio_sys_over_naive_p90 필요(system_price_skill)."
        ),
    )
    p.add_argument(
        "--composite-norm",
        choices=["raw", "zscore_within_run"],
        default="raw",
        help=(
            "메타 클러스터 정렬용: raw=composite_mean, zscore_within_run=클러스터 간 z 가중합. "
            "최종 unseen 정책은 --composite-norm-final 참고."
        ),
    )
    p.add_argument(
        "--composite-norm-final",
        choices=["raw", "zscore_within_run"],
        default="raw",
        help=(
            "최종 unseen 후보 정렬. 기본 raw: 각 후보의 comp_raw는 unseen 구간 지표만으로 계산되며 "
            "후보 간 z-score로 재정렬하지 않아 '같은 unseen 창 안에서 동료 후보 분포로 보정'하는 "
            "peer coupling(해석/보고 편향)을 피한다. zscore_within_run은 finalists K명 안에서만 "
            "상대 비교가 필요할 때 명시적으로 사용."
        ),
    )
    p.add_argument(
        "--composite-config",
        type=Path,
        default=None,
        help=(
            "JSON 가중치/정규화 설정. parse 전에 로드되어 set_defaults로 반영되며, "
            "같은 항목을 CLI에도 주면 일반적으로 CLI 값이 우선한다. "
            "예: schemas/strict_multi_cycle_composite.example.json"
        ),
    )
    p.add_argument(
        "--cohort-top-fraction",
        type=float,
        default=0.10,
        help="dev validations 풀에서 composite_score 상위 fraction 코호트 리포트 (0~0.5)",
    )
    p.add_argument(
        "--cohort-sensitivity",
        action="store_true",
        help=(
            "여러 fraction에 대해 코호트 리포트를 추가(JSON dev_cohort_sensitivity, MD 표). "
            "각 fraction마다 전체 리포트 dict가 복제되므로 항목이 많으면 JSON이 빠르게 커진다. "
            "기본 목록은 3개(0.05,0.1,0.2); 더 필요할 때만 --cohort-sensitivity-fractions 를 짧게 유지하는 것을 권장."
        ),
    )
    p.add_argument(
        "--cohort-sensitivity-fractions",
        type=str,
        default="0.05,0.1,0.2",
        help="--cohort-sensitivity 시 사용할 fraction 목록(쉼표 구분, 각각 (0,0.5])",
    )
    p.add_argument(
        "--out-json",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_result.json",
    )
    p.add_argument(
        "--out-md",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_result.md",
    )
    args = p.parse_args(av)
    if args.composite_config is None and peek_cfg is not None and peek_cfg.is_file():
        args.composite_config = peek_cfg
    if args.composite_config is not None and not args.composite_config.is_file():
        print("composite-config not found:", args.composite_config.resolve(), file=sys.stderr)
        return 2
    ctf = float(args.cohort_top_fraction)
    if not (0.0 < ctf <= 0.5):
        print("cohort-top-fraction must be in (0, 0.5], got", ctf, file=sys.stderr)
        return 2

    eg_col = (args.eval_gap_filter_column or "").strip() or None
    eg_min = args.eval_gap_filter_min
    eg_max = args.eval_gap_filter_max
    if eg_col is None and (eg_min is not None or eg_max is not None):
        print(
            "warning: --eval-gap-filter-min/max without --eval-gap-filter-column; gap filter ignored",
            file=sys.stderr,
        )
        eg_min, eg_max = None, None
    if eg_col is not None and eg_min is None and eg_max is None:
        print(
            "warning: --eval-gap-filter-column without min/max; gap filter ignored",
            file=sys.stderr,
        )
        eg_col = None

    sym = args.symbol.strip().upper()
    if args.ohlcv is not None:
        ohl_path = args.ohlcv
    elif sym in SYMBOL_FILES:
        ohl_rel, _fac_rel = SYMBOL_FILES[sym]
        ohl_path = ROOT / ohl_rel
    else:
        print(
            "unknown --symbol and no --ohlcv provided:",
            sym,
            "known:",
            list(SYMBOL_FILES),
            file=sys.stderr,
        )
        return 2
    if args.factors_csv is not None:
        fac_path = args.factors_csv
    elif sym in SYMBOL_FILES:
        _ohl_rel, fac_rel = SYMBOL_FILES[sym]
        fac_path = ROOT / fac_rel
    else:
        print("unknown --symbol and no --factors-csv provided:", sym, file=sys.stderr)
        return 2
    if not ohl_path.is_file() or not fac_path.is_file():
        print("missing data/factors for symbol", sym, file=sys.stderr)
        return 2

    embargos = _parse_ints(args.embargos)
    shrinks = _parse_floats(args.shrinks)
    if not embargos or not shrinks:
        print("embargos/shrinks empty", file=sys.stderr)
        return 2

    ohl = vg.load_ohlcv_csv(ohl_path)
    n = len(ohl)
    n_unseen = int(round(n * args.unseen_ratio))
    n_dev = n - n_unseen
    n_window = args.train_bars + max(embargos) + args.val_bars
    if n_dev < n_window + args.cycle_step:
        print(
            f"development rows too short: dev={n_dev}, need at least {n_window + args.cycle_step}",
            file=sys.stderr,
        )
        return 2
    dev = ohl.iloc[:n_dev]
    unseen = ohl.iloc[n_dev:]
    cycles = _build_cycles(len(dev), n_window=n_window, step=args.cycle_step)
    if len(cycles) < 2:
        print("need >=2 cycles for strict cycle(i)->validate(i+1)", file=sys.stderr)
        return 2

    discovered_by_cycle: dict[int, list[dict[str, Any]]] = {}
    validations: list[dict[str, Any]] = []
    for c in cycles:
        discovered_by_cycle[c.cycle_id] = _discover_candidates(
            c.cycle_id, shrinks, embargos, feature=args.trust_feature
        )
    for c in cycles[1:]:
        prev = discovered_by_cycle[c.cycle_id - 1]
        seg = dev.iloc[c.start : c.stop]
        for f in prev:
            m = _evaluate_formula_on_cycle(
                f,
                ohl_segment=seg,
                registry=args.registry,
                factors_csv=fac_path,
                train_bars=args.train_bars,
                val_bars=args.val_bars,
                seed=args.seed,
                bars_per_year=args.bars_per_year,
                eval_gap_filter_column=eg_col,
                eval_gap_filter_min=eg_min,
                eval_gap_filter_max=eg_max,
            )
            m["composite_score"] = _composite_score(
                m,
                w_mae=args.w_mae,
                w_mae_tail=args.w_mae_tail,
                w_hit=args.w_hit,
                w_rr=args.w_rr,
                w_sharpe=args.w_sharpe,
                w_calmar=args.w_calmar,
            )
            row = {
                "validated_cycle": c.cycle_id,
                "from_cycle": c.cycle_id - 1,
                "formula_id": f["formula_id"],
                "cluster_key": _cluster_key(f),
                "formula": dict(f),
                "metrics": m,
            }
            validations.append(row)

    cohort_report = _dev_top_fraction_cohort_report(
        validations,
        fraction=ctf,
        rank_key="composite_score",
    )
    cohort_sensitivity: dict[str, Any] | None = None
    if args.cohort_sensitivity:
        sens_fracs = _parse_floats(args.cohort_sensitivity_fractions)
        if not sens_fracs:
            print("cohort-sensitivity-fractions empty", file=sys.stderr)
            return 2
        for sf in sens_fracs:
            if not (0.0 < float(sf) <= 0.5):
                print("cohort sensitivity fraction must be in (0, 0.5], got", sf, file=sys.stderr)
                return 2
        n_sens = len(sorted(set(float(x) for x in sens_fracs)))
        print(
            "note: dev_cohort_sensitivity stores one full cohort report per fraction; "
            "JSON size scales with the number of fractions (and validations).",
            file=sys.stderr,
        )
        if n_sens > 5:
            print(
                "warning: cohort-sensitivity has",
                n_sens,
                "distinct fractions (>5); consider fewer to keep outputs small.",
                file=sys.stderr,
            )
        cohort_sensitivity = {
            str(float(f)): _dev_top_fraction_cohort_report(
                validations,
                fraction=float(f),
                rank_key="composite_score",
            )
            for f in sorted(set(float(x) for x in sens_fracs))
        }

    # Meta synthesis
    clusters: dict[str, list[dict[str, Any]]] = {}
    for r in validations:
        clusters.setdefault(r["cluster_key"], []).append(r)
    meta_rows: list[dict[str, Any]] = []
    for k, rs in clusters.items():
        hr = [x["metrics"].get("directional_hit_rate") for x in rs]
        mr = [x["metrics"].get("mae_ratio_sys_over_naive") for x in rs]
        cov = [x["metrics"].get("trust_coverage", float("nan")) for x in rs]
        rr = [x["metrics"].get("mean_rr") for x in rs]
        sh = [x["metrics"].get("sharpe_per_bar") for x in rs]
        sha = [x["metrics"].get("sharpe_annualized") for x in rs]
        cm = [x["metrics"].get("calmar_proxy") for x in rs]
        cs = [x["metrics"].get("composite_score") for x in rs]
        hr2 = [float(x) for x in hr if isinstance(x, (int, float)) and not math.isnan(float(x))]
        mr2 = [float(x) for x in mr if isinstance(x, (int, float)) and not math.isnan(float(x))]
        cov2 = [float(x) for x in cov if isinstance(x, (int, float)) and not math.isnan(float(x))]
        rr2 = [float(x) for x in rr if isinstance(x, (int, float)) and not math.isnan(float(x))]
        sh2 = [float(x) for x in sh if isinstance(x, (int, float)) and not math.isnan(float(x))]
        sha2 = [float(x) for x in sha if isinstance(x, (int, float)) and not math.isnan(float(x))]
        cm2 = [float(x) for x in cm if isinstance(x, (int, float)) and not math.isnan(float(x))]
        cs2 = [float(x) for x in cs if isinstance(x, (int, float)) and not math.isnan(float(x))]
        n_eval = len(rs)
        meta_rows.append(
            {
                "cluster_key": k,
                "n_eval": n_eval,
                "hit_mean": statistics.mean(hr2) if hr2 else float("nan"),
                "mae_ratio_mean": statistics.mean(mr2) if mr2 else float("nan"),
                "coverage_mean": statistics.mean(cov2) if cov2 else float("nan"),
                "mean_rr_mean": statistics.mean(rr2) if rr2 else float("nan"),
                "sharpe_mean": statistics.mean(sh2) if sh2 else float("nan"),
                "sharpe_annualized_mean": statistics.mean(sha2) if sha2 else float("nan"),
                "calmar_mean": statistics.mean(cm2) if cm2 else float("nan"),
                "composite_mean": statistics.mean(cs2) if cs2 else float("nan"),
                "sample_formula": rs[0]["formula"],
            }
        )
    _attach_composite_rank_meta(
        meta_rows,
        composite_norm=str(args.composite_norm),
        w_mae=args.w_mae,
        w_hit=args.w_hit,
        w_rr=args.w_rr,
        w_sharpe=args.w_sharpe,
        w_calmar=args.w_calmar,
    )
    if args.rank_by == "composite":
        meta_rows.sort(
            key=lambda x: (
                -1.0
                if math.isnan(float(x.get("composite_rank_score", float("nan"))))
                else -float(x["composite_rank_score"]),
                999.0 if math.isnan(float(x["mae_ratio_mean"])) else float(x["mae_ratio_mean"]),
            )
        )
    else:
        meta_rows.sort(
            key=lambda x: (
                999.0 if math.isnan(float(x["mae_ratio_mean"])) else float(x["mae_ratio_mean"]),
                -1.0 if math.isnan(float(x["hit_mean"])) else -float(x["hit_mean"]),
            )
        )
    selected = [r for r in meta_rows if r["n_eval"] >= args.min_evals][: args.top_k]
    base_row = next(
        (r for r in meta_rows if r["n_eval"] >= args.min_evals and str(r["cluster_key"]).startswith("base|")),
        None,
    )
    if base_row is not None and all(r["cluster_key"] != base_row["cluster_key"] for r in selected):
        if len(selected) < max(args.top_k, 1):
            selected.append(base_row)
        elif selected:
            selected[-1] = base_row

    # Strict final unseen validation (never used above)
    final_rows: list[dict[str, Any]] = []
    n_need_final = args.train_bars + max(embargos) + args.val_bars
    if len(unseen) < n_need_final:
        print(
            f"warning: unseen too short for strict final eval, unseen={len(unseen)}, need={n_need_final}",
            file=sys.stderr,
        )
    else:
        seg_u = unseen.iloc[:n_need_final]
        for s in selected:
            f = dict(s["sample_formula"])
            m = _evaluate_formula_on_cycle(
                f,
                ohl_segment=seg_u,
                registry=args.registry,
                factors_csv=fac_path,
                train_bars=args.train_bars,
                val_bars=args.val_bars,
                seed=args.seed,
                bars_per_year=args.bars_per_year,
                include_regime_quintiles=True,
                eval_gap_filter_column=eg_col,
                eval_gap_filter_min=eg_min,
                eval_gap_filter_max=eg_max,
            )
            m["composite_score"] = _composite_score(
                m,
                w_mae=args.w_mae,
                w_mae_tail=args.w_mae_tail,
                w_hit=args.w_hit,
                w_rr=args.w_rr,
                w_sharpe=args.w_sharpe,
                w_calmar=args.w_calmar,
            )
            final_rows.append(
                {
                    "cluster_key": s["cluster_key"],
                    "formula": f,
                    "metrics": m,
                }
            )
        _attach_composite_rank_final(
            final_rows,
            composite_norm=str(args.composite_norm_final),
            w_mae=args.w_mae,
            w_hit=args.w_hit,
            w_rr=args.w_rr,
            w_sharpe=args.w_sharpe,
            w_calmar=args.w_calmar,
        )
        if args.rank_by == "composite":
            final_rows.sort(
                key=lambda x: (
                    -1.0
                    if math.isnan(float(x["metrics"].get("composite_rank_score", float("nan"))))
                    else -float(x["metrics"]["composite_rank_score"]),
                    999.0
                    if math.isnan(float(x["metrics"].get("mae_ratio_sys_over_naive", float("nan"))))
                    else float(x["metrics"]["mae_ratio_sys_over_naive"]),
                )
            )
        else:
            final_rows.sort(
                key=lambda x: (
                    999.0
                    if math.isnan(float(x["metrics"].get("mae_ratio_sys_over_naive", float("nan"))))
                    else float(x["metrics"]["mae_ratio_sys_over_naive"]),
                    -1.0
                    if math.isnan(float(x["metrics"].get("directional_hit_rate", float("nan"))))
                    else -float(x["metrics"]["directional_hit_rate"]),
                )
            )

    out = {
        "symbol": sym,
        "risk_metrics_legend": (
            "mean_rr = mean(win)/|mean(loss)| on per-bar signed returns "
            "(sign(p_system-P_now)*fwd_1, flat when tie); "
            "sharpe_per_bar = mean/sd of per-bar signed returns; "
            "sharpe_sample_window = sharpe_per_bar * sqrt(n_trade_rows); "
            "sharpe_annualized = sharpe_per_bar * sqrt(bars_per_year); "
            "calmar_proxy = compound total return / max drawdown on the same series; "
            "short val_bars => high variance / unstable interpretability. "
            "composite_norm (meta) zscore_within_run: cluster-level relative score only. "
            "composite_norm_final (default raw): final unseen rank_score equals comp_raw unless "
            "explicitly set to zscore_within_run (peer coupling on finalists). "
            "Why raw by default: few finalists share one unseen slice, so z-scoring peers mostly re-ranks noise "
            "and is easy to misread as skill; raw keeps an absolute leaderboard per formula. "
            "Neither leaks dev labels into unseen metrics; selection still uses dev-only meta."
        ),
        "config": {
            "train_bars": args.train_bars,
            "val_bars": args.val_bars,
            "cycle_step": args.cycle_step,
            "embargos": embargos,
            "shrinks": shrinks,
            "trust_feature": args.trust_feature,
            "eval_gap_filter_column": eg_col,
            "eval_gap_filter_min": eg_min,
            "eval_gap_filter_max": eg_max,
            "unseen_ratio": args.unseen_ratio,
            "min_evals": args.min_evals,
            "top_k": args.top_k,
            "bars_per_year": args.bars_per_year,
            "rank_by": args.rank_by,
            "composite_norm": args.composite_norm,
            "composite_norm_final": args.composite_norm_final,
            "cohort_top_fraction": float(args.cohort_top_fraction),
            "cohort_sensitivity": bool(args.cohort_sensitivity),
            "cohort_sensitivity_fractions": str(args.cohort_sensitivity_fractions)
            if args.cohort_sensitivity
            else None,
            "composite_config": str(args.composite_config.resolve())
            if args.composite_config is not None
            else None,
            "composite_weights": {
                "w_mae": args.w_mae,
                "w_mae_tail": args.w_mae_tail,
                "w_hit": args.w_hit,
                "w_rr": args.w_rr,
                "w_sharpe": args.w_sharpe,
                "w_calmar": args.w_calmar,
            },
            "reference_default_weight_preset": "balanced",
            "weights_equal_to_preset": _detect_weight_preset(args),
        },
        "strict_unseen_guard": {
            "unseen_starts_at_index": int(n_dev),
            "final_eval_uses_unseen_slice_only": [0, int(n_need_final)],
            "unseen_used_in_discovery_or_meta_validation": False,
            "ranking_policy": {
                "meta_composite_norm": str(args.composite_norm),
                "final_composite_norm": str(args.composite_norm_final),
                "why_final_raw_default_ko": (
                    "최종 구간은 후보 수가 적고 동일 unseen 창을 공유하므로, 후보 간 z-score 랭킹은 "
                    "'같은 잡음 창에서의 상대 순위'로 읽히기 쉬워 보고 편향이 생길 수 있다. "
                    "raw는 각 공식의 절대 comp_raw만으로 순위를 매겨 해석이 직관적이고 peer coupling이 없다."
                ),
                "note_ko": (
                    "메타는 dev 사이클 검증만 사용. 최종 unseen 지표는 동일 공식을 unseen 구간에만 적용해 산출. "
                    "composite_norm_final=raw이면 최종 rank_score는 unseen에서만 계산한 comp_raw와 동일해 "
                    "후보 간 z-score 정렬로 인한 수평 누설이 없음(명시적으로 zscore_within_run 선택 시만 해당)."
                ),
            },
        },
        "dev_cohort_top_fraction": cohort_report,
        "counts": {
            "n_total_rows": len(ohl),
            "n_dev_rows": len(dev),
            "n_unseen_rows": len(unseen),
            "n_cycles": len(cycles),
            "n_validations": len(validations),
            "n_clusters": len(meta_rows),
            "n_selected_for_final": len(selected),
            "n_final_evals": len(final_rows),
        },
        "meta_clusters": meta_rows,
        "final_unseen": final_rows,
    }
    if cohort_sensitivity is not None:
        out["dev_cohort_sensitivity"] = cohort_sensitivity

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    gap_md = ""
    if eg_col is not None and (eg_min is not None or eg_max is not None):
        gap_md = (
            f"- eval gap filter: `{eg_col}` "
            f"min={eg_min if eg_min is not None else '—'} max={eg_max if eg_max is not None else '—'} "
            "(trust 분위 이후 검증 행 추가 필터)"
        )
    lines = [
        "# Strict Multi-Cycle Research Result",
        "",
        f"- symbol: `{sym}`",
        f"- cycles: {len(cycles)} (dev rows={len(dev)}, unseen rows={len(unseen)})",
        f"- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)",
        *([gap_md] if gap_md else []),
        "",
        "## Meta Synthesis (cluster summary)",
        "",
        "| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in meta_rows[:20]:
        lines.append(
            f"| `{r['cluster_key']}` | {r['n_eval']} | {_fmt(r['hit_mean'])} | "
            f"{_fmt(r['mae_ratio_mean'])} | {_fmt(r['coverage_mean'])} | "
            f"{_fmt(r.get('mean_rr_mean'))} | {_fmt(r.get('sharpe_annualized_mean'))} | "
            f"{_fmt(r.get('calmar_mean'))} | {_fmt(r.get('composite_mean'))} | "
            f"{_fmt(r.get('composite_rank_score'))} |"
        )
    lines += [
        "",
        "## Dev cohort (top fraction by composite_score)",
        "",
        f"- fraction={cohort_report.get('fraction_used')}, n_eligible={cohort_report.get('n_eligible')}, "
        f"top_n={cohort_report.get('top_n')}, cutoff={_fmt(cohort_report.get('cutoff_rank_score'))}",
        "",
        "| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |",
        "|---|---:|---:|---:|---:|",
    ]
    tb = cohort_report.get("top_bucket") or {}
    ab = cohort_report.get("all_validations_baseline") or {}
    h_top = tb.get("directional_hit_rate") or {}
    m_top = tb.get("mae_ratio_sys_over_naive") or {}
    h_all = ab.get("directional_hit_rate") or {}
    m_all = ab.get("mae_ratio_sys_over_naive") or {}
    lines.append(
        f"| top bucket | {_fmt(h_top.get('mean'))} | {_fmt(h_top.get('pstdev'))} | "
        f"{_fmt(m_top.get('mean'))} | {_fmt(m_top.get('pstdev'))} |"
    )
    lines.append(
        f"| all validations | {_fmt(h_all.get('mean'))} | {_fmt(h_all.get('pstdev'))} | "
        f"{_fmt(m_all.get('mean'))} | {_fmt(m_all.get('pstdev'))} |"
    )
    lines += [
        "",
        f"- improvement vs all (primary fraction): `{_improvement_vs_all_cell(tb, ab)}` "
        "(hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)",
    ]
    if cohort_sensitivity:
        lines += [
            "",
            "## Dev cohort sensitivity (multiple top fractions)",
            "",
            "각 fraction마다 `dev_cohort_sensitivity` 에 전체 코호트 dict가 들어가므로 fraction 개수는 적게 유지하는 것이 좋다.",
            "",
            "Improvement vs all: hit 은 (top−all)을 퍼센트포인트로, mae_ratio 는 (all−top)/|all|×100 상대% (양수면 top 이 더 우수).",
            "",
            "| fraction | n_top | cutoff | hit_top | mae_top | rr_top | sharpe_ann_top | calmar_top | vs all |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
        for fk in sorted(cohort_sensitivity.keys(), key=lambda x: float(x)):
            rep = cohort_sensitivity[fk] or {}
            tb2 = rep.get("top_bucket") or {}
            ab2 = rep.get("all_validations_baseline") or {}
            ht = (tb2.get("directional_hit_rate") or {}).get("mean")
            mt = (tb2.get("mae_ratio_sys_over_naive") or {}).get("mean")
            rt = (tb2.get("mean_rr") or {}).get("mean")
            st = (tb2.get("sharpe_annualized") or {}).get("mean")
            ct = (tb2.get("calmar_proxy") or {}).get("mean")
            vs = _improvement_vs_all_cell(tb2, ab2)
            lines.append(
                f"| {fk} | {rep.get('top_n')} | {_fmt(rep.get('cutoff_rank_score'))} | "
                f"{_fmt(ht)} | {_fmt(mt)} | {_fmt(rt)} | {_fmt(st)} | {_fmt(ct)} | `{vs}` |"
            )
    lines += [
        "",
        "## Final Unseen Validation",
        "",
        "| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for i, r in enumerate(final_rows, start=1):
        m = r["metrics"]
        lines.append(
            f"| {i} | `{r['cluster_key']}` | {_fmt(m.get('directional_hit_rate'))} | "
            f"{_fmt(m.get('mae_ratio_sys_over_naive'))} | {_fmt(m.get('trust_coverage'))} | "
            f"{_fmt(m.get('mean_rr'))} | {_fmt(m.get('sharpe_per_bar'))} | "
            f"{_fmt(m.get('sharpe_annualized'))} | {_fmt(m.get('calmar_proxy'))} | "
            f"{_fmt(m.get('composite_score'))} | {_fmt(m.get('composite_rank_score'))} |"
        )
    if final_rows:
        m0 = final_rows[0].get("metrics") or {}
        tables = m0.get("regime_quintile_tables") or {}
        if isinstance(tables, dict) and tables:
            lines += ["", "## Final rank-1 regime bins (gap / tension)", ""]
            for feat, tbl in tables.items():
                if not isinstance(tbl, dict):
                    continue
                lines.append(f"### `{feat}`")
                lines.append("")
                for bucket_name in ("q5", "q10", "tails_10_20"):
                    bt = tbl.get(bucket_name)
                    if not isinstance(bt, list) or not bt:
                        continue
                    lines.append(f"- {bucket_name}")
                    lines.append("")
                    lines.append(
                        "| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |"
                    )
                    lines.append("|---|---:|---:|---:|---:|---:|---:|")
                    for row in bt:
                        lines.append(
                            f"| {row.get('bucket')} | {row.get('n')} | "
                            f"{_fmt(row.get('directional_hit_rate'))} | "
                            f"{_fmt(row.get('mae_ratio_sys_over_naive'))} | "
                            f"{_fmt(row.get('mean_rr'))} | {_fmt(row.get('sharpe_annualized'))} | "
                            f"{_fmt(row.get('calmar_proxy'))} |"
                        )
                    lines.append("")
    args.out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("wrote", args.out_json.resolve())
    print("wrote", args.out_md.resolve())
    if final_rows:
        best_row = None
        for r in final_rows:
            h = r["metrics"].get("directional_hit_rate")
            m = r["metrics"].get("mae_ratio_sys_over_naive")
            if isinstance(h, (int, float)) and isinstance(m, (int, float)):
                if not math.isnan(float(h)) and not math.isnan(float(m)):
                    best_row = r
                    break
        if best_row is None:
            best_row = final_rows[0]
        best = best_row["metrics"]
        print(
            "best_final",
            "hit_rate",
            _fmt(best.get("directional_hit_rate")),
            "mae_ratio",
            _fmt(best.get("mae_ratio_sys_over_naive")),
            "coverage",
            _fmt(best.get("trust_coverage")),
            "mean_rr",
            _fmt(best.get("mean_rr")),
            "sharpe_bar",
            _fmt(best.get("sharpe_per_bar")),
            "sharpe_ann",
            _fmt(best.get("sharpe_annualized")),
            "calmar",
            _fmt(best.get("calmar_proxy")),
            "comp_raw",
            _fmt(best.get("composite_score")),
            "rank_score",
            _fmt(best.get("composite_rank_score")),
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

