#!/usr/bin/env python3
"""**한 방** 연구 사이클: 2+3 (갭·OOS·WF) → 3b (검증매트릭스+AI보조) → 4 (스냅샷) → 4b (LLM/규칙 리포) → 5 (드라이런) → 6 (피드백 플랜).

1단계(데이터·Registry)는 이미 갖췄다는 가정. **주문·실거래 없음.**

  python scripts/run_research_cycle.py --dry-run
  python scripts/run_research_cycle.py
  python scripts/run_research_cycle.py --skip-step2
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import research_cycle as rc  # noqa: E402


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="명령만 출력, 실행 안 함",
    )
    p.add_argument(
        "--skip-step2",
        action="store_true",
        help="갭 백테스트 생략 (4/4b→5→6만, 이미 갭 CSV 갱신됨을 가정)",
    )
    p.add_argument(
        "--no-plan",
        action="store_true",
        help="6단계 feedback_loop_plan 생략",
    )
    p.add_argument(
        "--skip-llm-report",
        action="store_true",
        help="4b llm_report_from_snapshot 생략(규칙+LLM 리포트 없이 스냅샷만)",
    )
    p.add_argument(
        "--nautilus-last-n",
        type=int,
        default=48,
        help="nautilus_execution_dry_run --last-n (0이면 옵션 생략=전체 봉)",
    )
    p.add_argument(
        "gap_extra",
        nargs="*",
        help="gap_backtest_and_analyze.py 에 그대로 전달 (예: --skip-wf)",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    a = _parse_args(argv)
    n = a.nautilus_last_n
    b = rc.CycleBuild(
        skip_step2=a.skip_step2,
        nautilus_last_n=None if n == 0 else n,
        no_plan=a.no_plan,
        extra_gap_args=tuple(a.gap_extra or ()),
        skip_llm_report=a.skip_llm_report,
    )
    steps = rc.build_cycle_steps(ROOT, sys.executable, b=b)
    for name, cmd in steps:
        print("==", name, flush=True)
        print("  ", " ".join(cmd), flush=True)
        if not a.dry_run:
            subprocess.check_call(cmd, cwd=ROOT)
    if a.dry_run:
        print("== (dry-run: 미실행)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
