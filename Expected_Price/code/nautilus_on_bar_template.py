"""
5단계(Nautilus **옆**): 이 파일은 Nautilus 프로젝트로 **복사**해 `Strategy` 안에 붙이는 훅 예시뿐.
이 repo에는 `nautilus_trader` **의존성 없이** `execution_bridge` JSONL 또는 dict 와 **동일 키** 를 맞출 때 사용.

연결 방법(개념):
  * 데이터 피드/바: `P_now`, `predictor_prices`, `p_system` (스키마 `expected_price.execution_bar.v1` 와 동일)
  * 한 바마다: `nautilus_bridge.on_execution_bar(bar, hook=...)` — 주문/사이징 훅에서 사용

투자 권고·주문 **아님** — **샘플**이다.
"""
from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any

from nautilus_bridge import on_execution_bar, reduce_anchor_signal


def example_use_bar_dict(bar: Mapping[str, Any]) -> dict[str, float] | None:
    """Nautilus `on_bar` 에서 `bar` dict 를 `execution` 스키마와 맞췄다고 가정."""
    pn = bar.get("P_now")
    if pn is None:
        return None
    return reduce_anchor_signal(bar, p_now=float(pn))


def example_hook_sizing_d_mean_anchor(
    _bar: Mapping[str, Any], sig: dict[str, float]
) -> str:
    """훅 예: **이름만** (실제 사이징/주문 **구현은 Nautilus 측**)."""
    d = float(sig.get("d_mean_anchor") or 0.0)
    if abs(d) < 1e-9:
        return "FLAT"
    if d > 0:
        return "LONG_BIAS"  # 예시·비트
    return "SHORT_BIAS"


def example_on_bar_nautilus_style(
    bar: Mapping[str, Any], *, on_signal: Callable[[str], None] | None = None
) -> str | None:
    """Nautilus 스타일 한 줄 호출 — `on_signal` 에 라벨만 전달(주문 아님)."""

    def _h(_b: Mapping[str, Any], s: dict[str, float]) -> str:
        lab = example_hook_sizing_d_mean_anchor(_b, s)
        if on_signal is not None:
            on_signal(lab)
        return lab

    return on_execution_bar(bar, hook=_h)
