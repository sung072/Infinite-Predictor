#!/usr/bin/env python3
r"""연구 사이클 한 바퀴: (1) `strict_multi_cycle_batch` (2) `curate_strict_formulas`.

알 수 없는 인자는 **배치**에만 전달된다(`parse_known_args`). 큐레이션 전용 옵션은
`curate_strict_formulas.py` 를 직접 실행하는 것이 안전하다.

예::

  python scripts/strict_research_cycle.py --fetch-missing --parallel 2
  python scripts/strict_research_cycle.py --skip-batch --summary-json data/runs/strict_multi_cycle_summary_50.json
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--skip-batch", action="store_true", help="배치 생략(이미 요약이 있을 때)")
    p.add_argument("--skip-curate", action="store_true", help="큐레이션만 생략")
    p.add_argument(
        "--summary-json",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_summary_50.json",
        help="큐레이션 입력(배치 기본 산출과 동일 경로)",
    )
    args, batch_argv = p.parse_known_args(argv)

    py = sys.executable
    if not args.skip_batch:
        cmd = [py, str(ROOT / "scripts" / "strict_multi_cycle_batch.py"), *batch_argv]
        print("running:", " ".join(cmd), flush=True)
        subprocess.check_call(cmd, cwd=ROOT)

    if not args.skip_curate:
        cur = [
            py,
            str(ROOT / "scripts" / "curate_strict_formulas.py"),
            "--summary-json",
            str(args.summary_json),
        ]
        print("running:", " ".join(cur), flush=True)
        subprocess.check_call(cur, cwd=ROOT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
