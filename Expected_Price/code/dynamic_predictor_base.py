"""배치에서 `fit`·저장하고, **추론**만 반복(라이트) — **동적 예측가** 뼈대(연구 전용).

- 실서비스/Nautilus 경로: Registry **active** + **artifact**만 로드해 `predict` 1호출 수준(무거운 `fit` 금지)
- [dynamic_predictors.md](../docs/dynamic_predictors.md) 참고
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Literal

import joblib
import numpy as np
import pandas as pd

__all__ = [
    "TrainedRegressorArtifact",
    "save_artifact",
    "load_artifact",
]

Kind = Literal["sklearn_regressor"]


@dataclass
class TrainedRegressorArtifact:
    """`predict(X)` 를 갖는 sklearn+메타(피처이름, 스키마, 모델 해시)."""

    model: Any
    feature_columns: list[str]
    target_column: str
    kind: Kind = "sklearn_regressor"
    meta: dict[str, Any] = field(default_factory=dict)

    def to_sidecar(self) -> dict[str, Any]:
        return {
            "target_column": self.target_column,
            "feature_columns": self.feature_columns,
            "kind": self.kind,
            "meta": self.meta,
        }

    def predict_frame(self, X: pd.DataFrame) -> np.ndarray:
        cols = [c for c in self.feature_columns if c in X.columns]
        if not cols or len(cols) != len(self.feature_columns):
            raise ValueError(f"need columns {self.feature_columns}, have {list(X.columns)}")
        m = self.model
        if hasattr(m, "predict"):
            return np.asarray(
                m.predict(X[cols].to_numpy(dtype=np.float64)), dtype=np.float64
            )
        raise TypeError("model has no predict")

    def predict_to_series(
        self, ohlc_or_features: pd.DataFrame, build_features
    ) -> pd.Series:
        f = build_features(ohlc_or_features)
        a = self.predict_frame(f)
        return pd.Series(a, index=ohlc_or_features.index, name="dynamic_price")


def save_artifact(art: TrainedRegressorArtifact, path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(art, p)
    side = p.with_suffix(".sidecar.json")
    with side.open("w", encoding="utf-8") as fp:
        json.dump(art.to_sidecar(), fp, ensure_ascii=False, indent=2)


def load_artifact(path: str | Path) -> TrainedRegressorArtifact:
    return joblib.load(Path(path))
