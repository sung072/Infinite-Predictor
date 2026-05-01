#!/usr/bin/env python3
r"""Binance Spot 공개 REST — 24h `quoteVolume`(USDT 기준 거래대금) 상위 N개 USDT 마켓 BASE 목록.

출력 한 줄에 BASE 하나(예: `BTC`). `strict_multi_cycle_batch.py --symbols-file` 에 넣는다.

데이터: `GET /api/v3/ticker/24hr` 전체 티커 후 필터·정렬. 이후 OHLCV는 `fetch_btc_ohlcv.py` 가 **동일 심볼의 klines 캔들**로 받는다.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


def _base_from_usdt_symbol(symbol: str) -> str:
    s = symbol.upper().strip()
    if not s.endswith("USDT"):
        return s
    return s[: -len("USDT")]


def _exclude_leveraged_spot(sym: str) -> bool:
    """Binance 레버리지·롱숏 토큰(UP/DOWN 접미) 등은 기본 제외."""
    u = sym.upper()
    if u.endswith("UPUSDT") or u.endswith("DOWNUSDT"):
        return True
    if "BULL" in u or "BEAR" in u:
        return True
    return False


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--top", type=int, default=100, help="상위 N개 (BASE)")
    p.add_argument(
        "--out",
        type=Path,
        default=None,
        help="BASE 심볼 한 줄에 하나(미지정 시 data/universe/binance_usdt_top{N}_by_quote_volume.txt)",
    )
    p.add_argument(
        "--include-leveraged",
        action="store_true",
        help="UP/DOWN/BULL/BEAR 패턴 심볼도 포함(기본은 제외)",
    )
    p.add_argument(
        "--exclude-bases",
        default="USDC,FDUSD,TUSD,BUSD,USDP,USDD,DAI",
        help="BASE 가 이 목록(쉼표)에 있으면 스킵. 비우면 스테이블 베이스 필터 끔.",
    )
    args = p.parse_args(argv)
    if args.out is None:
        args.out = Path(f"data/universe/binance_usdt_top{int(args.top)}_by_quote_volume.txt")
    ex_raw = str(args.exclude_bases or "").strip()
    exclude_bases: set[str] = (
        {x.strip().upper() for x in ex_raw.split(",") if x.strip()} if ex_raw else set()
    )

    url = "https://api.binance.com/api/v3/ticker/24hr"
    try:
        with urllib.request.urlopen(url, timeout=120) as resp:
            raw = resp.read()
    except urllib.error.URLError as e:
        print("fetch failed:", e, file=sys.stderr)
        return 1

    data = json.loads(raw.decode("utf-8"))
    if not isinstance(data, list):
        print("unexpected response shape", file=sys.stderr)
        return 1

    rows: list[tuple[float, str, str]] = []
    for t in data:
        if not isinstance(t, dict):
            continue
        sym = str(t.get("symbol", "")).upper()
        if not sym.endswith("USDT"):
            continue
        if not args.include_leveraged and _exclude_leveraged_spot(sym):
            continue
        try:
            qv = float(t.get("quoteVolume", 0) or 0.0)
        except (TypeError, ValueError):
            qv = 0.0
        base = _base_from_usdt_symbol(sym)
        if not base:
            continue
        if base in exclude_bases:
            continue
        rows.append((qv, sym, base))

    rows.sort(key=lambda x: -x[0])
    seen: set[str] = set()
    bases: list[str] = []
    for qv, _sym, base in rows:
        if base in seen:
            continue
        seen.add(base)
        bases.append(base)
        if len(bases) >= int(args.top):
            break

    if len(bases) < int(args.top):
        print(
            "warning: only",
            len(bases),
            "unique bases after filter (wanted",
            args.top,
            ")",
            file=sys.stderr,
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(bases) + "\n", encoding="utf-8")
    print("wrote", args.out.resolve(), "n=", len(bases), "top_quote_vol_usdt", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
