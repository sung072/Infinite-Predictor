#!/usr/bin/env python3
"""
Binance 공개 REST (키 불필요) → OHLCV CSV. `vbt_gap_research.load_ohlcv_csv` / run_registry_research --csv-ohlcv 용.

기본: BTCUSDT, 1h, 720봉 ≈ 30일.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--out",
        type=Path,
        default=Path("data/btcusdt_1h_30d.csv"),
        help="출력 CSV (time, open, high, low, close, volume)",
    )
    p.add_argument("--symbol", default="BTCUSDT", help="예: BTCUSDT")
    p.add_argument(
        "--interval",
        default="1h",
        help="Binance interval (1h, 4h, 1d, …)",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=720,
        help="봉 개수 (1h 720 ≈ 30일, 최대 1000)",
    )
    args = p.parse_args(argv)

    lim = max(1, min(1000, args.limit))
    q = f"https://api.binance.com/api/v3/klines?symbol={args.symbol}&interval={args.interval}&limit={lim}"
    try:
        with urllib.request.urlopen(q, timeout=60) as resp:
            raw = resp.read()
    except urllib.error.URLError as e:
        print("fetch failed:", e, file=sys.stderr)
        return 1

    klines = json.loads(raw.decode("utf-8"))
    if not isinstance(klines, list) or not klines:
        print("empty or bad response", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as f:
        f.write("timestamp,open,high,low,close,volume\n")
        for row in klines:
            # [ open time ms, o, h, l, c, v, ... ]
            ts_ms = int(row[0])
            ts = datetime.fromtimestamp(ts_ms / 1000.0, tz=timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
            o, h, lo, c, v = row[1], row[2], row[3], row[4], row[5]
            f.write(f"{ts},{o},{h},{lo},{c},{v}\n")
    print("wrote", args.out.resolve(), "rows", len(klines), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
