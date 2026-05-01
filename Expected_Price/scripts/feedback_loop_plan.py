#!/usr/bin/env python3
"""6단계: `feedback_events.jsonl` + (없으면 빈 이벤트) → `feedback_research_plan.json` (2~6 재실행 권장).

  python scripts/feedback_loop_plan.py
  python scripts/feedback_loop_plan.py --events data/runs/feedback_events.jsonl
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import feedback_loop as fl  # noqa: E402

_DEFAULT_EV = ROOT / "data" / "runs" / "feedback_events.jsonl"
_DEFAULT_PLAN = ROOT / "data" / "runs" / "feedback_research_plan.json"


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--events", type=Path, default=_DEFAULT_EV)
    p.add_argument("--out", type=Path, default=_DEFAULT_PLAN)
    p.add_argument(
        "--py",
        default="python",
        help="프랜 command 접두(venv면 python 경로)",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    a = _parse_args(argv)
    evs = list(fl.iter_feedback_events(a.events))
    plan = fl.build_research_plan(evs, project_root_cmd=a.py)
    fl.write_research_plan_json(a.out, plan)
    print("wrote:", a.out.resolve(), "events:", len(evs), "force_rerun:", plan.get("force_rerun_gaps"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
