#!/usr/bin/env python3
r"""**스택 완성 검증(로컬·CI)**: unittest + 핵심 import + 스냅샷·규칙 리포트(네트워크 **없음**).

  python scripts/verify_expected_price_stack.py
  python scripts/verify_expected_price_stack.py --skip-unittest   # `run_ci` 직후 — 테스트 중복 생략
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

_EXPECTED_N_TESTS = 121


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--skip-unittest",
        action="store_true",
        help="이미 `run_ci` 를 통과한 뒤 — import+스냅샷만(테스트 2중 실행 방지)",
    )
    a = p.parse_args(argv)

    if not a.skip_unittest:
        sub = [sys.executable, "-m", "unittest", "discover", "-q", "-s", "tests", "-p", "test_*.py"]
        subprocess.check_call(sub, cwd=ROOT)
    import importlib  # noqa: I001  # after tests

    importlib.import_module("nautilus_bridge")
    importlib.import_module("nautilus_on_bar_template")
    importlib.import_module("llm_report_from_snapshot")
    importlib.import_module("gap_baseline_train")
    importlib.import_module("feedback_loop")
    from llm_report_from_snapshot import load_snapshot_json, render_rule_markdown  # type: ignore

    sjson = ROOT / "data" / "runs" / "ai_analysis_snapshot.json"
    if sjson.is_file():
        t = render_rule_markdown(load_snapshot_json(sjson))
        if len(t) < 10:
            print("rule report unexpectedly short", file=sys.stderr)
            return 1
    else:
        print("skip snapshot rule check: no", sjson, file=sys.stderr)
    print("verify_expected_price_stack: OK", f"(expected>={_EXPECTED_N_TESTS} tests if unittest ran)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
