"""검증 구간 행만으로 단순 방향 전략의 보조 지표(연구용, 운용 신호 아님).

가정: 각 행에서 `fwd_1` 은 다음 봉 수익률, 포지션은 sign(p_system - P_now).
"""
from __future__ import annotations

import math
from typing import Any

import numpy as np
import pandas as pd

import system_price_validation_matrix as spm

__all__ = [
    "system_price_series",
    "compute_trade_metrics",
    "regime_quintile_table",
    "regime_tail_band_table",
]


def system_price_series(
    m: pd.DataFrame,
    *,
    system_col: str,
    shrink_weight: float,
) -> pd.Series:
    pw = pd.to_numeric(m.get("P_now"), errors="coerce")
    if system_col == "p_system_shrunk_custom":
        base = pd.to_numeric(m.get("p_system"), errors="coerce")
        w = float(max(0.0, min(1.0, shrink_weight)))
        return (1.0 - w) * base + w * pw
    if system_col not in m.columns:
        raise KeyError(f"missing system column: {system_col}")
    return pd.to_numeric(m.get(system_col), errors="coerce")


def compute_trade_metrics(
    m_val: pd.DataFrame,
    *,
    system_col: str,
    shrink_weight: float,
    bars_per_year: float = 24.0 * 365.0,
) -> dict[str, Any]:
    ps = system_price_series(m_val, system_col=system_col, shrink_weight=shrink_weight)
    pw = pd.to_numeric(m_val.get("P_now"), errors="coerce")
    fwd = pd.to_numeric(m_val.get("fwd_1"), errors="coerce")
    ok = ps.notna() & pw.notna() & fwd.notna()
    if ok.sum() < 5:
        return {
            "n_trade_rows": int(ok.sum()),
            "mean_rr": float("nan"),
            "sharpe_per_bar": float("nan"),
            "sharpe_sample_window": float("nan"),
            "sharpe_annualized": float("nan"),
            "calmar_proxy": float("nan"),
            "strategy_mean_fwd": float("nan"),
            "naive_mean_fwd": float("nan"),
        }

    psb = ps[ok].to_numpy(dtype=float)
    pwb = pw[ok].to_numpy(dtype=float)
    fwdb = fwd[ok].to_numpy(dtype=float)

    near = (np.abs(psb - pwb) < 1e-9) | (np.abs(fwdb) < 1e-15)
    pos = np.sign(psb - pwb)
    strat = np.where(near, np.nan, pos * fwdb)
    mask = np.isfinite(strat)
    r = strat[mask]
    n = int(len(r))
    if n < 3:
        return {
            "n_trade_rows": n,
            "mean_rr": float("nan"),
            "sharpe_per_bar": float("nan"),
            "sharpe_sample_window": float("nan"),
            "sharpe_annualized": float("nan"),
            "calmar_proxy": float("nan"),
            "strategy_mean_fwd": float("nan"),
            "naive_mean_fwd": float(np.nanmean(fwdb)),
        }

    wins = r[r > 0]
    losses = r[r < 0]
    win_m = float(np.mean(wins)) if len(wins) else float("nan")
    loss_m = float(np.mean(losses)) if len(losses) else float("nan")
    if math.isfinite(win_m) and math.isfinite(loss_m) and loss_m < 0:
        mean_rr = win_m / abs(loss_m)
    else:
        mean_rr = float("nan")

    mu = float(np.mean(r))
    sd = float(np.std(r, ddof=1)) if n > 1 else float("nan")
    sharpe_bar = (mu / sd) if sd and sd > 1e-18 and math.isfinite(sd) else float("nan")
    sharpe_sample = (
        sharpe_bar * math.sqrt(n) if math.isfinite(sharpe_bar) else float("nan")
    )
    sharpe_ann = (
        sharpe_bar * math.sqrt(max(float(bars_per_year), 0.0))
        if math.isfinite(sharpe_bar)
        else float("nan")
    )

    eq = np.cumprod(1.0 + r)
    peak = np.maximum.accumulate(eq)
    dd = (eq - peak) / np.maximum(peak, 1e-12)
    max_dd = float(-np.min(dd)) if len(dd) else float("nan")
    tot_ret = float(eq[-1] - 1.0) if len(eq) else float("nan")
    calmar = (tot_ret / max_dd) if max_dd > 1e-12 and math.isfinite(max_dd) else float("nan")

    return {
        "n_trade_rows": n,
        "mean_rr": float(mean_rr),
        "sharpe_per_bar": float(sharpe_bar),
        "sharpe_sample_window": float(sharpe_sample),
        "sharpe_annualized": float(sharpe_ann),
        "calmar_proxy": float(calmar),
        "strategy_mean_fwd": float(mu),
        "naive_mean_fwd": float(np.nanmean(fwdb)),
    }


def regime_quintile_table(
    m_val: pd.DataFrame,
    feature_col: str,
    *,
    system_col: str,
    shrink_weight: float,
    gfr: Any,
    q: int = 5,
    bars_per_year: float = 24.0 * 365.0,
) -> list[dict[str, Any]]:
    if feature_col not in m_val.columns:
        return []
    s = pd.to_numeric(m_val[feature_col], errors="coerce")
    ok = s.notna()
    m2 = m_val.loc[ok].copy()
    if len(m2) < max(20, q * 4):
        return []
    try:
        m2["_q"] = pd.qcut(s[ok], q=q, labels=False, duplicates="drop")
    except (ValueError, TypeError):
        return []
    out: list[dict[str, Any]] = []
    for qi in sorted(int(x) for x in m2["_q"].dropna().unique()):
        sub = m2[m2["_q"] == qi].drop(columns=["_q"], errors="ignore")
        if len(sub) < 5:
            continue
        sk, rho_sp, _ps = spm._skill_from_system_col(
            sub,
            gfr,
            system_col=system_col,
            shrink_weight=shrink_weight,
        )
        tm = compute_trade_metrics(
            sub,
            system_col=system_col,
            shrink_weight=shrink_weight,
            bars_per_year=bars_per_year,
        )
        out.append(
            {
                "bucket": qi,
                "n": int(len(sub)),
                "directional_hit_rate": sk.get("directional_hit_rate"),
                "mae_ratio_sys_over_naive": sk.get("mae_ratio_sys_over_naive"),
                "spearman_signed_sys_vs_fwd1": float(rho_sp),
                **tm,
            }
        )
    return out


def regime_tail_band_table(
    m_val: pd.DataFrame,
    feature_col: str,
    *,
    system_col: str,
    shrink_weight: float,
    gfr: Any,
    bands: tuple[float, ...] = (0.1, 0.2),
    bars_per_year: float = 24.0 * 365.0,
) -> list[dict[str, Any]]:
    if feature_col not in m_val.columns:
        return []
    s = pd.to_numeric(m_val[feature_col], errors="coerce")
    m2 = m_val.loc[s.notna()].copy()
    if len(m2) < 30:
        return []
    s2 = pd.to_numeric(m2[feature_col], errors="coerce")
    out: list[dict[str, Any]] = []
    for b in bands:
        bb = float(b)
        if bb <= 0.0 or bb >= 0.5:
            continue
        lo = float(s2.quantile(bb))
        hi = float(s2.quantile(1.0 - bb))
        masks = {
            f"bottom_{int(bb * 100)}pct": s2 <= lo,
            f"top_{int(bb * 100)}pct": s2 >= hi,
        }
        for label, mk in masks.items():
            sub = m2.loc[mk.fillna(False)]
            if len(sub) < 5:
                continue
            sk, rho_sp, _ps = spm._skill_from_system_col(
                sub,
                gfr,
                system_col=system_col,
                shrink_weight=shrink_weight,
            )
            tm = compute_trade_metrics(
                sub,
                system_col=system_col,
                shrink_weight=shrink_weight,
                bars_per_year=bars_per_year,
            )
            out.append(
                {
                    "bucket": label,
                    "n": int(len(sub)),
                    "directional_hit_rate": sk.get("directional_hit_rate"),
                    "mae_ratio_sys_over_naive": sk.get("mae_ratio_sys_over_naive"),
                    "spearman_signed_sys_vs_fwd1": float(rho_sp),
                    **tm,
                }
            )
    return out
