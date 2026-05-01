"""최소 **동적(학습) 거래량→가격** RF 스파이크 — *간격 연구*용 (절대 정확도 1급은 아님)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# 프로젝트
_CODE = Path(__file__).resolve().parent
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))
import vbt_gap_research as vg
from dynamic_predictor_base import TrainedRegressorArtifact, save_artifact


def build_volume_features(ohlc: pd.DataFrame) -> pd.DataFrame:
    v = ohlc["volume"].astype(float)
    d = {
        "log1p_v": np.log1p(v),
        "log1p_v_l1": np.log1p(v).shift(1),
        "log1p_v_l2": np.log1p(v).shift(2),
    }
    return pd.DataFrame(d, index=ohlc.index)


def train_volume_to_close(
    ohlc: pd.DataFrame, *, n_estimators: int = 48, max_depth: int = 6, random_state: int = 0
) -> TrainedRegressorArtifact:
    fe = build_volume_features(ohlc)
    m = fe.notna().all(axis=1) & ohlc["close"].notna()
    fe = fe.loc[m]
    y = ohlc.loc[fe.index, "close"].astype(float)
    r = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        n_jobs=-1,
    )
    cols = [c for c in fe.columns]
    r.fit(fe[cols].to_numpy(), y.to_numpy())
    return TrainedRegressorArtifact(
        model=r,
        feature_columns=cols,
        target_column="close",
        kind="sklearn_regressor",
        meta={"spike": "dynamic_volume_to_close", "n_rows": int(len(fe))},
    )


def predict_dynamic_volume_price(art: TrainedRegressorArtifact, ohlc: pd.DataFrame) -> pd.Series:
    f = build_volume_features(ohlc)
    f = f.ffill().bfill()  # 첫 2봉 — 스파이크: 경계 0누수 방지용(운영이면 window 설계)
    a = art.predict_frame(f)
    return pd.Series(a, index=ohlc.index, name="vol_dynamic_price")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", type=Path, default=Path("artifacts/vol_to_close_spike.joblib"))
    p.add_argument("--n-bars", type=int, default=500)
    p.add_argument("--seed", type=int, default=0)
    a = p.parse_args()
    ohlc = vg.synthetic_ohlcv_bars(int(a.n_bars), seed=int(a.seed))
    art = train_volume_to_close(ohlc, random_state=int(a.seed))
    s = predict_dynamic_volume_price(art, ohlc)
    print("train_meta", art.meta, "p_head", s.head(3).tolist(), "n", len(s))
    save_artifact(art, a.out)
    print("saved", a.out.resolve())
    return 0


if __name__ == "__main__":
    main()
