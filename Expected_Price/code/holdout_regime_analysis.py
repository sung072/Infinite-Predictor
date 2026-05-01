"""검증 구간(m_val)에서 갭·변동성 분위별 시스템가 스킬(연구용)."""
from __future__ import annotations

import math
from typing import Any

import numpy as np
import pandas as pd

__all__ = ["quintile_skill_breakdown"]


def quintile_skill_breakdown(
    m_val: pd.DataFrame,
    feature_col: str,
    gfr: Any,
    spm: Any,
    *,
    system_col: str,
    shrink_weight: float,
    q: int = 5,
) -> list[dict[str, Any]]:
    """
    `feature_col` 값으로 검증 행을 분위(qcut)로 나눈 뒤, 구간별 `_skill_from_system_col`.
    """
    if feature_col not in m_val.columns:
        raise KeyError(f"missing column: {feature_col}")
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
        sk, rho, _ps = spm._skill_from_system_col(
            sub,
            gfr,
            system_col=system_col,
            shrink_weight=shrink_weight,
        )
        lo = float(np.nanmin(pd.to_numeric(sub[feature_col], errors="coerce")))
        hi = float(np.nanmax(pd.to_numeric(sub[feature_col], errors="coerce")))
        out.append(
            {
                "quintile": qi,
                "n": int(len(sub)),
                f"{feature_col}_min": lo,
                f"{feature_col}_max": hi,
                "directional_hit_rate": sk.get("directional_hit_rate"),
                "mae_ratio_sys_over_naive": sk.get("mae_ratio_sys_over_naive"),
                "spearman_signed_sys_vs_fwd1": float(rho) if rho == rho else float("nan"),
            }
        )
    return out


def format_quintile_markdown(
    rows: list[dict[str, Any]],
    *,
    title: str,
    feature_col: str,
) -> str:
    if not rows:
        return f"## {title}\n\n_(표본 부족 또는 분위 실패)_\n"
    keys = [
        "quintile",
        "n",
        f"{feature_col}_min",
        f"{feature_col}_max",
        "directional_hit_rate",
        "mae_ratio_sys_over_naive",
        "spearman_signed_sys_vs_fwd1",
    ]
    header = "| " + " | ".join(keys) + " |"
    sep = "| " + " | ".join(["---"] * len(keys)) + " |"
    lines = [f"## {title}", "", header, sep]
    for r in sorted(rows, key=lambda x: x.get("quintile", 0)):
        cells = []
        for k in keys:
            v = r.get(k)
            if v is None or (isinstance(v, float) and (math.isnan(v))):
                cells.append("n/a")
            elif isinstance(v, float):
                cells.append(f"{v:.4f}")
            else:
                cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"
