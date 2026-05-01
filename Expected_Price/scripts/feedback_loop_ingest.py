#!/usr/bin/env python3
"""6단계: 피드백/메모를 JSONL 한 줄로 추가 (실전 로그 import 전 단계·수동 운용).

  python scripts/feedback_loop_ingest.py --notes "OOS 퍼짐 이상" --rerun
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

import feedback_loop as fl  # noqa: E402

_DEFAULT_OUT = ROOT / "data" / "runs" / "feedback_events.jsonl"


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", default="manual", help="출처 라벨")
    p.add_argument("--symbol", default="BTCUSDT")
    p.add_argument("--run-id", default="local-1", dest="run_id")
    p.add_argument(
        "--rerun",
        action="store_true",
        help="갭·OOS·WF 재연구(2+3) 권장 플래그",
    )
    p.add_argument("--notes", default="", help="한 줄 메모")
    p.add_argument("--out", type=Path, default=_DEFAULT_OUT)
    p.add_argument(
        "--from-jsonl",
        type=Path,
        default=None,
        help="이 파일(한 줄에 JSON)마다 `FeedbackEvent` 필드·또는 전체 이벤트",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    a = _parse_args(argv)
    if a.from_jsonl is not None:
        if not a.from_jsonl.is_file():
            print("missing", a.from_jsonl, file=sys.stderr)
            return 1
        n = 0
        for ln in a.from_jsonl.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            o = json.loads(ln)
            if o.get("schema") == fl.SCHEMA_EVENT and "suggest_rerun_gaps" in o:
                o = {k: v for k, v in o.items() if k in ("source", "symbol", "run_id", "suggest_rerun_gaps", "notes", "extra")}
                e = fl.FeedbackEvent(
                    source=str(o.get("source", "import")),
                    symbol=str(o.get("symbol", "BTCUSDT")),
                    run_id=str(o.get("run_id", "import-1")),
                    suggest_rerun_gaps=bool(o.get("suggest_rerun_gaps", False)),
                    notes=str(o.get("notes", "")),
                    extra=o.get("extra") if o.get("extra") else None,
                )
            else:
                e = fl.FeedbackEvent(
                    source=a.source,
                    symbol=str(o.get("symbol", a.symbol)),
                    run_id=str(o.get("run_id", a.run_id)),
                    suggest_rerun_gaps=bool(o.get("suggest_rerun_gaps", a.rerun)),
                    notes=str(o.get("notes", a.notes)),
                    extra=o if isinstance(o, dict) else None,
                )
            fl.append_feedback_event(a.out, e)
            n += 1
        print("appended", n, "lines ->", a.out.resolve())
        return 0
    e = fl.FeedbackEvent(
        source=a.source,
        symbol=a.symbol,
        run_id=a.run_id,
        suggest_rerun_gaps=a.rerun,
        notes=a.notes,
    )
    fl.append_feedback_event(a.out, e)
    print("appended ->", a.out.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
