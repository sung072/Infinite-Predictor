#!/usr/bin/env python3
"""4단계: `ai_analysis_snapshot.json` → `data/runs/ai_analysis_report.md` (규칙 + 선택 LLM).

  OPENAI_API_KEY 가 있으면 API 한 번 호출(실패해도 규칙 본문은 기록).

  python scripts/llm_report_from_snapshot.py
  python scripts/llm_report_from_snapshot.py --no-llm
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import llm_report_from_snapshot as lr  # noqa: E402

_DEFAULT_IN = ROOT / "data" / "runs" / "ai_analysis_snapshot.json"
_DEFAULT_OUT = ROOT / "data" / "runs" / "ai_analysis_report.md"


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--in", dest="in_path", type=Path, default=_DEFAULT_IN)
    p.add_argument("--out", type=Path, default=_DEFAULT_OUT)
    p.add_argument("--no-llm", action="store_true", help="API 호출 안 함")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    a = _parse_args(argv)
    if not a.in_path.is_file():
        print("missing:", a.in_path, file=sys.stderr)
        return 1
    used, err = lr.write_merged_report(
        a.in_path,
        a.out,
        try_llm=not a.no_llm,
    )
    print("wrote:", a.out.resolve(), "llm_used:", used, flush=True)
    if err:
        print("note:", err, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
