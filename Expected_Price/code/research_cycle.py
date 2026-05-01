"""2→4→4b→5→6 연구 **한 사이클** 명령 시퀀스 (subprocess 는 `scripts/run_research_cycle` 에서)."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

__all__ = [
    "CycleBuild",
    "build_cycle_steps",
]

_G = "scripts/gap_backtest_and_analyze.py"
_3B = "scripts/system_price_validation_matrix.py"
_4 = "scripts/build_ai_analysis_snapshot.py"
_4B = "scripts/llm_report_from_snapshot.py"
_5 = "scripts/nautilus_execution_dry_run.py"
_6 = "scripts/feedback_loop_plan.py"


@dataclass(frozen=True)
class CycleBuild:
    """`build_cycle_steps` 옵션."""

    skip_step2: bool
    nautilus_last_n: int | None
    no_plan: bool
    extra_gap_args: tuple[str, ...]
    skip_llm_report: bool


def build_cycle_steps(
    project_root: Path,
    py_exe: str,
    *,
    b: CycleBuild,
) -> list[tuple[str, list[str]]]:
    """
    `(표시이름, argv)` 리스트.

    `extra_gap_args` 는 gap 스크립트에만 (`--skip-oos` 등).
    """
    r = project_root.resolve()
    st: list[tuple[str, list[str]]] = []
    if not b.skip_step2:
        gcmd = [py_exe, str(r / _G)]
        gcmd.extend(b.extra_gap_args)
        st.append(("step2+3 gap_backtest+OOS+WF", gcmd))
        st.append(
            (
                "step3b system_price_validation_matrix",
                [py_exe, str(r / _3B), "--strict-oos-wf-only", "--ai-judge"],
            )
        )
    st.append(
        (
            "step4 build_ai_analysis_snapshot",
            [py_exe, str(r / _4)],
        )
    )
    if not b.skip_llm_report:
        st.append(
            (
                "step4b llm_report_from_snapshot",
                [py_exe, str(r / _4B)],
            )
        )
    cmd5 = [py_exe, str(r / _5)]
    if b.nautilus_last_n is not None and b.nautilus_last_n > 0:
        cmd5 += ["--last-n", str(b.nautilus_last_n)]
    st.append(("step5 nautilus_dry_run", cmd5))
    if not b.no_plan:
        st.append(
            (
                "step6 feedback_loop_plan",
                [py_exe, str(r / _6)],
            )
        )
    return st
