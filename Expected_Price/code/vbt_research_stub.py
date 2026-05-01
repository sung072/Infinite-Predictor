"""VectorBT 연구 루프 **스텁** — gap 피처로 시계열을 이어 붙이는 지점만 표시.

연구/배치에서만 사용. 실거래·실시간 루프에서 VectorBT 엔진 직접 호출 금지(프로젝트 규칙).
`vbt_gap_research.run_gap_research_ohlcv` 가 `system_gap_metrics` + ATR·쌍별 `gpr__*`(옵션) 를
DataFrame 열로 쌓는다 — 수평선 **간격 연구**의 입력 피처(배치 전용).
"""
from __future__ import annotations

# 이후: import vectorbt as vbt
from typing import Any, Mapping

from predictor_gap_metrics import (
    anchor_prices_for_ids,
    system_gap_metrics,
)

Number = float | int


def research_pipeline_stub(
    row: Mapping[str, Any],
    *,
    active_predictor_ids: list[str],
    p_system: Number,
) -> dict[str, float]:
    """한 bar(또는 스냅) `row`에서 gap 요약을 만드는 **형태만** 보여 준다.

    `row`는 `docs/abc_event_spec.md`의 `predictor_prices` + `P_now` 등을 풀어 둔 dict라고 가정.
    """
    pred_key = "predictor_prices"
    if pred_key not in row:
        raise KeyError(f"row must include {pred_key!r} (see docs/abc_event_spec.md)")
    p_now = row.get("P_now", row.get("p_now"))
    if p_now is None:
        raise KeyError("row must include P_now (or p_now)")

    prices: Mapping[str, float] = row[pred_key]  # type: ignore[assignment]
    anchors = anchor_prices_for_ids(prices, active_predictor_ids, strict=True)
    return system_gap_metrics(anchors, p_now=float(p_now), p_system=float(p_system))


__all__ = ["research_pipeline_stub"]
