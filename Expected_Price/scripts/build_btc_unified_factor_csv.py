#!/usr/bin/env python3
"""
BTC OHLCV → 4p EMA/밴드 + (연구) 뉴스·감성·페어 절대가 열.
`schemas/predictor_registry.btc_unified.json` 의 `meta.factor_column` 과 열 이름을 맞춤.

실행(프로젝트 루트):
  python scripts/build_btc_unified_factor_csv.py
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ohlcv", type=Path, default=ROOT / "data" / "btcusdt_1h_30d.csv")
    p.add_argument(
        "--out",
        type=Path,
        default=ROOT / "data" / "derived" / "btc_factors_unified.csv",
    )
    args = p.parse_args(argv)

    sys.path.insert(0, str(ROOT / "code"))
    from vbt_gap_research import load_ohlcv_csv  # noqa: E402

    o = load_ohlcv_csv(args.ohlcv)
    c = o["close"].astype(float)
    n = len(c)
    idx = np.arange(n, dtype=float)
    p_ema_fast = c.ewm(span=8, adjust=False).mean()
    p_ema_slow = c.ewm(span=48, adjust=False).mean()
    p_high_band = o["high"].rolling(24, min_periods=1).max() * 1.0005
    p_low_band = o["low"].rolling(24, min_periods=1).min() * 0.9995
    # 연구용 데모: 실제 뉴스/감성 API 아님 — 재현 가능·가격눈금에만 맞춤
    p_war = c * (1.0 + 0.0006 * np.sin(idx / 6.0))
    p_eth = c * (1.012 + 0.0004 * np.cos(idx / 20.0))
    ch = c.pct_change(6).fillna(0.0)
    p_sentiment = c * (1.0 + 0.0015 * np.tanh(ch.to_numpy(dtype=float) * 25.0))
    out = p_ema_fast.to_frame("p_ema_fast")
    out["p_ema_slow"] = p_ema_slow
    out["p_high_band"] = p_high_band
    out["p_low_band"] = p_low_band
    out["p_war"] = p_war
    out["p_eth"] = p_eth
    out["p_sentiment"] = p_sentiment
    out.insert(0, "timestamp", out.index.strftime("%Y-%m-%dT%H:%M:%SZ"))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)
    print("wrote", args.out.resolve(), "rows", len(out), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
