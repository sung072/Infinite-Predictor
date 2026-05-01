"""`--out-execution-jsonl` 산출물 검증·리플레이(배치). Nautilus 없이 동작."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import execution_bridge as exb
import nautilus_bridge as nb


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("jsonl", type=Path, help="execution JSONL 경로")
    p.add_argument(
        "--max",
        type=int,
        default=0,
        help="리플레이할 상한 바 수(0=전부, 검증만이면 --validate-only)",
    )
    p.add_argument(
        "--validate-only",
        action="store_true",
        help="스키마만 검사하고 종료(성공 시 0)",
    )
    p.add_argument(
        "--print-signal",
        action="store_true",
        help="`nautilus_bridge.reduce_anchor_signal` 요약 출력(모듈 있을 때)",
    )
    a = p.parse_args(argv)

    errs = exb.validate_execution_jsonl(a.jsonl)
    if errs:
        for e in errs:
            print("error:", e, file=sys.stderr)
        return 1
    if a.validate_only:
        print("ok", a.jsonl)
        return 0

    h, bars = exb.read_execution_jsonl(a.jsonl)
    n = len(bars) if a.max <= 0 else min(len(bars), a.max)
    print("header", json.dumps(h, ensure_ascii=False)[:200], "...")
    print("n_bars", n, "of", len(bars))
    for i in range(n):
        b = bars[i]
        line = f"{b.get('t')} P_now={b.get('P_now')} p_system={b.get('p_system')} n_pred={len(b.get('predictor_prices') or {})}"
        print(i, line)
        if a.print_signal and b.get("P_now") is not None:
            s = nb.reduce_anchor_signal(b, p_now=float(b["P_now"]))
            print("  signal", s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
