"""6단계: 실전(또는 수동) 피드백 → **연구 재실행 플랜** (VectorBT/배치 쪽으로 되돌리기).

실거래·Nautilus 런타임 **의존 없음**. 로그/메모를 JSONL 로 쌓고 `build_research_plan` 으로 2~5 스텝 권장 커맨드 manifest 생성."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

__all__ = [
    "SCHEMA_EVENT",
    "SCHEMA_PLAN",
    "FeedbackEvent",
    "append_feedback_event",
    "iter_feedback_events",
    "build_research_plan",
]

SCHEMA_EVENT = "expected_price.feedback_event.v1"
SCHEMA_PLAN = "expected_price.research_plan.v1"


@dataclass
class FeedbackEvent:
    """한 번의 ‘루프 입력’(실전 PnL이 없어도: 주간 점검, 드리프트 의심, 앵커 제안 메모)."""

    source: str
    """`manual` | `nautilus_log` | `import` 등"""

    symbol: str
    run_id: str
    suggest_rerun_gaps: bool
    """True 이면 2+3(갭·OOS·WF) 재돌 권장."""

    notes: str
    extra: dict[str, Any] | None = None


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def event_to_dict(e: FeedbackEvent) -> dict[str, Any]:
    d = asdict(e)
    d["schema"] = SCHEMA_EVENT
    d["recorded_at_utc"] = _now_iso()
    d["extra"] = d.get("extra") or {}
    return d


def append_feedback_event(path: str | Path, e: FeedbackEvent) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(event_to_dict(e), ensure_ascii=False) + "\n"
    with p.open("a", encoding="utf-8") as f:
        f.write(line)


def iter_feedback_events(path: str | Path) -> Iterator[dict[str, Any]]:
    p = Path(path)
    if not p.is_file():
        return
    for ln in p.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        try:
            o = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if o.get("schema") == SCHEMA_EVENT:
            yield o


def build_research_plan(
    events: list[dict[str, Any]] | None,
    *,
    project_root_cmd: str = "python",
) -> dict[str, Any]:
    """
    룰 기반 플랜(학습 아님). `events` 가 비어 있어도 **기본 연구 사이클** 명령을 채운다.

    `suggest_rerun_gaps` 가 True 인 이벤트가 있으면 step2/3 를 **강조** 플래그.
    """
    ev = list(events or [])
    force_rerun = any(bool(x.get("suggest_rerun_gaps")) for x in ev)

    step2: list[str] = [
        f"{project_root_cmd} scripts/gap_backtest_and_analyze.py",
    ]
    if force_rerun:
        step2.append("*(이번 피드백에서 `suggest_rerun_gaps` 가 있어 full+OOS+WF 를 우선 확인)*")
    plan: dict[str, Any] = {
        "schema": SCHEMA_PLAN,
        "created_at_utc": _now_iso(),
        "force_rerun_gaps": force_rerun,
        "n_feedback_events": len(ev),
        "step1_note": "OHLCV/Registry/팩터는 사용자 데이터 스냅샷에 맞게",
        "step2_gap_vectorbt": step2,
        "step3_note": "OOS·WF 는 step2 스크립트에 포함(별도 끄기: --skip-oos / --skip-wf)",
        "step4_snapshot": [f"{project_root_cmd} scripts/build_ai_analysis_snapshot.py"],
        "step4b_llm_report": [
            f"{project_root_cmd} scripts/llm_report_from_snapshot.py",
            f"{project_root_cmd} scripts/llm_report_from_snapshot.py --no-llm  # offline",
        ],
        "step4c_sklearn_baseline": [f"{project_root_cmd} scripts/train_gap_baseline.py"],
        "step5_dry_run": [f"{project_root_cmd} scripts/nautilus_execution_dry_run.py"],
        "one_shot_cycle": [f"{project_root_cmd} scripts/run_research_cycle.py --dry-run"],
        "stack_verify": [f"{project_root_cmd} scripts/verify_expected_price_stack.py"],
        "step6_feedback_append": f"{project_root_cmd} scripts/feedback_loop_ingest.py --source manual --notes '...' ",
        "step6_import_jsonl": f"{project_root_cmd} scripts/feedback_loop_ingest.py --from-jsonl <path.jsonl>",
        "feedback_events_tail": ev[-5:],
    }
    return plan


def write_research_plan_json(path: str | Path, plan: dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        json.dumps(plan, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
