#!/usr/bin/env python3
# Stack 100%: run_ci (default fast) + verify. Korean doc: docs/STACK_100_CHECKLIST.md
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _run(args: list[str]) -> None:
    print("==", " ".join(args), flush=True)
    subprocess.check_call(args, cwd=ROOT)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="complete_100",
        description="Stack 100%: run_ci then verify (see docs/STACK_100_CHECKLIST.md).",
    )
    p.add_argument(
        "--full-ci",
        action="store_true",
        help="run_ci full: pip + unittest + JSONL (CI same, slower)",
    )
    a = p.parse_args(argv)
    py = sys.executable

    if a.full_ci:
        _run([py, str(ROOT / "scripts" / "run_ci.py")])
    else:
        _run(
            [
                py,
                str(ROOT / "scripts" / "run_ci.py"),
                "--skip-pip",
                "--no-jsonl",
                "-q",
            ]
        )
    _run(
        [
            py,
            str(ROOT / "scripts" / "verify_expected_price_stack.py"),
            "--skip-unittest",
        ]
    )
    print("STACK_100_COMPLETE: OK (see docs/STACK_100_CHECKLIST.md)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
