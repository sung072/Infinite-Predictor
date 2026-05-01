#!/usr/bin/env python3
"""CI 와 동일(로컬·Linux·macOS·Windows): pip → unittest → execution JSONL 스모크.

옵션 예: `--skip-pip` (빠른 반복), `--no-jsonl` (스모크 생략), `-q` (간단한 테스트 출력)
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _run(args: list[str]) -> None:
    print("==", " ".join(args), flush=True)
    subprocess.check_call(args, cwd=ROOT)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--skip-pip",
        action="store_true",
        help="pip install 생략(의존성 이미 맞췄을 때)",
    )
    p.add_argument(
        "--no-jsonl",
        action="store_true",
        help="Registry JSONL export/검증 스모크 생략",
    )
    p.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="unittest 를 -q 로(상세 -v 대신)",
    )
    args = p.parse_args(argv)

    print("== run_ci  root:", ROOT, flush=True)
    py = sys.executable
    if not args.skip_pip:
        _run([py, "-m", "pip", "install", "-r", "requirements-research.txt"])
    ut_verbosity: list[str] = ["-q"] if args.quiet else ["-v"]
    _run(
        [
            py,
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
            "-p",
            "test_*.py",
            *ut_verbosity,
        ]
    )
    if not args.no_jsonl:
        fd, pth = tempfile.mkstemp(suffix=".jsonl", prefix="ci_")
        os.close(fd)
        tmp = Path(pth)
        try:
            _run(
                [
                    py,
                    str(ROOT / "code" / "run_registry_research.py"),
                    "--n-bars",
                    "5",
                    "--out-execution-jsonl",
                    str(tmp),
                ]
            )
            _run(
                [
                    py,
                    str(ROOT / "code" / "replay_execution_jsonl.py"),
                    str(tmp),
                    "--validate-only",
                ]
            )
        finally:
            tmp.unlink(missing_ok=True)
    print("== OK", flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as e:
        raise SystemExit(e.returncode) from e
