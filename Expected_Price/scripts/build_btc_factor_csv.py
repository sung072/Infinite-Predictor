#!/usr/bin/env python3
"""OHLCV CSV( load_ohlcv_csv 와 동일 열) → 4개 예측가용 절대가 factor 열(시간 정렬)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--ohlcv", type=Path, default=ROOT / "data" / "btcusdt_1h_30d.csv"
    )
    p.add_argument(
        "--out",
        type=Path,
        default=ROOT / "data" / "derived" / "btc_factors_4p.csv",
    )
    args = p.parse_args(argv)

    sys.path.insert(0, str(ROOT / "code"))
    from vbt_gap_research import load_ohlcv_csv  # noqa: E402

    o = load_ohlcv_csv(args.ohlcv)
    c = o["close"].astype(float)
    p_ema_fast = c.ewm(span=8, adjust=False).mean()
    p_ema_slow = c.ewm(span=48, adjust=False).mean()
    p_high_band = o["high"].rolling(24, min_periods=1).max() * 1.0005
    p_low_band = o["low"].rolling(24, min_periods=1).min() * 0.9995
    out = p_ema_fast.to_frame("p_ema_fast")
    out["p_ema_slow"] = p_ema_slow
    out["p_high_band"] = p_high_band
    out["p_low_band"] = p_low_band
    out.insert(0, "timestamp", out.index.strftime("%Y-%m-%dT%H:%M:%SZ"))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)
    print("wrote", args.out.resolve(), "rows", len(out), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
