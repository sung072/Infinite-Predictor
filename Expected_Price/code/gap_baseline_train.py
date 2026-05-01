"""4단계(ML 베이스라인): 갭 CSV 의 스칼라 → 다음 봉 대상(간단 Ridge). **연구·오프라인**."""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

__all__ = ["train_baseline", "default_feature_cols", "default_target"]


def default_feature_cols(df: pd.DataFrame) -> list[str]:
    c = [
        "mean_pairwise_rel",
        "gap_system_to_now_rel",
        "range_rel",
    ]
    return [x for x in c if x in df.columns]


def default_target() -> str:
    return "mean_pairwise_rel"


def train_baseline(
    gap_csv: str | Path,
    *,
    test_size: float = 0.25,
    random_state: int = 0,
) -> dict[str, Any]:
    p = Path(gap_csv)
    if not p.is_file():
        raise FileNotFoundError(p)
    df0 = pd.read_csv(p, index_col=0, parse_dates=True)
    df = df0.sort_index().apply(pd.to_numeric, errors="coerce")
    tgt = default_target()
    y = df[tgt].shift(-1)
    feats = default_feature_cols(df)
    if not feats or tgt not in df.columns:
        raise ValueError("need mean_pairwise_rel, gap_system_to_now_rel, range_rel")
    X = df[feats]
    m = y.notna() & X.notna().all(axis=1)
    X = X[m]
    yv = y[m]
    if len(yv) < 30:
        raise ValueError(f"too few rows: {len(yv)} (need 30+)")
    Xtr, Xte, ytr, yte = train_test_split(
        X.values, yv.values, test_size=test_size, random_state=random_state, shuffle=False
    )
    mdl = Pipeline(
        [
            ("s", StandardScaler()),
            (
                "m",
                Ridge(alpha=1.0),
            ),
        ]
    )
    mdl.fit(Xtr, ytr)
    pred = mdl.predict(Xte)
    r2 = float(r2_score(yte, pred)) if len(yte) else float("nan")
    if not math.isfinite(r2):
        r2 = None
    return {
        "n_total": int(len(yv)),
        "n_test": int(len(yte)),
        "features": feats,
        "target": f"next({tgt})",
        "r2_oos_holdout": r2,
        "model": mdl,
    }
