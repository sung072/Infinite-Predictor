"""NautilusTrader **이전/옆**에서 쓰는 **어댑터 뼈대** (기본: `nautilus_trader` **미설치**).

- 연구 `execution_bridge` JSONL → `iter_execution_bars` 로 바 단위 `dict` 재생
- 실제 `Strategy`·`order_factory`·데이터 흡수는 Nautilus 프로젝트 쪽에 두고, 이 모듈은 **스키마 + 훅**만 유지
"""
from __future__ import annotations

import importlib.util
from collections.abc import Callable, Iterator, Mapping
from pathlib import Path
from typing import Any, TypeVar

T = TypeVar("T")

__all__ = [
    "nautilus_trader_spec",
    "on_execution_bar",
    "reduce_anchor_signal",
    "iter_execution_bars",
]


def nautilus_trader_spec() -> str | None:
    """`nautilus_trader` 모듈 경로(있다면). 없으면 None — `requirements-execution.txt` 참고."""
    s = importlib.util.find_spec("nautilus_trader")
    if s is None or s.origin is None:
        return None
    return str(s.origin)


def iter_execution_bars(path: str | Path) -> Iterator[dict[str, Any]]:
    """`--out-execution-jsonl` 파일에서 `expected_price.execution_bar.v1`만 순회."""
    from execution_bridge import SCHEMA_BAR, iter_bar_records

    for b in iter_bar_records(path):
        if b.get("schema") == SCHEMA_BAR:
            yield b


def reduce_anchor_signal(
    bar: Mapping[str, Any], *, p_now: float
) -> dict[str, float]:
    """MVP: 각 앵커 vs `P_now` **상대 괴리**(팀이 원하면 시그ма/ATR로 나눈 값으로 교체)."""
    p_now = float(p_now)
    s = 0.0
    c = 0.0
    for _pid, v in (bar.get("predictor_prices") or {}).items():
        c += 1.0
        s += float(v) - p_now
    p_sys = bar.get("p_system")
    center = float(p_sys) if p_sys is not None else (s / c if c else p_now)
    return {
        "d_mean_anchor": s / c if c else 0.0,
        "p_system": center,
    }


def on_execution_bar(
    bar: Mapping[str, Any],
    hook: Callable[[Mapping[str, Any], dict[str, float]], T] | None = None,
) -> T | None:
    """Nautilus `on_bar` 대체: 한 레코드 처리. `hook(bar, reduce_anchor_signal)` 넘기면 시그널로 연결."""
    pn = bar.get("P_now")
    if pn is None:
        return None
    sig = reduce_anchor_signal(bar, p_now=float(pn))
    if hook is not None:
        return hook(bar, sig)
    return sig
