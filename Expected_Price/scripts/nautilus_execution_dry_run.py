#!/usr/bin/env python3
"""5단계(실행기 **드라이런**): 갭 CSV → execution JSONL → `nautilus_bridge` 시그널 요약.

  주문·브로커 **없음**. `nautilus_trader` 없어도 동작.

  python scripts/nautilus_execution_dry_run.py
  python scripts/nautilus_execution_dry_run.py --last-n 24
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import execution_bridge as exb  # noqa: E402
import gap_csv_to_execution as g2e  # noqa: E402
import nautilus_bridge as nb  # noqa: E402

_DEFAULT_GAP = ROOT / "data" / "runs" / "btc_4p_gap_backtest.csv"
_DEFAULT_OUT = ROOT / "data" / "runs" / "execution_from_gap_dry_run.jsonl"


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--gap-csv", type=Path, default=_DEFAULT_GAP, help="갭 백테스트 CSV")
    p.add_argument(
        "--out-jsonl",
        type=Path,
        default=_DEFAULT_OUT,
        help="변환된 execution JSONL (Nautilus/리플레이 공용)",
    )
    p.add_argument(
        "--last-n",
        type=int,
        default=None,
        help="마지막 N봉만 (기본: 전체)",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    if not args.gap_csv.is_file():
        print("missing:", args.gap_csv, file=sys.stderr)
        return 1

    n_bars = g2e.gap_csv_to_execution_jsonl(
        args.gap_csv,
        args.out_jsonl,
        last_n=args.last_n,
        header={
            "source": "gap_csv_to_execution",
            "gap_csv": str(args.gap_csv.resolve()),
        },
    )
    errs = exb.validate_execution_jsonl(args.out_jsonl)
    if errs:
        for e in errs:
            print("validate:", e, file=sys.stderr)
        return 1

    nautilus_path = nb.nautilus_trader_spec()
    print("nautilus_trader:", nautilus_path or "(미설치 — 드라이런만)")
    print("jsonl:", args.out_jsonl.resolve())
    print("bars:", n_bars)

    last_sig: dict | None = None
    k = 0
    for bar in nb.iter_execution_bars(args.out_jsonl):
        sig = nb.on_execution_bar(bar)
        last_sig = sig
        k += 1
    print("iter_execution_bars:", k)
    if last_sig is not None:
        print("last reduce_anchor_signal:", json.dumps(last_sig, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
