"""Registry 앵커(모두 **가격**) → **시스템가** 후보(연구용, 단일 스칼라/바).

- `gpr__*__*`: 앵커 *끼리*의 상대 간격(= 수평선이 얼마나 퍼져 있는지).
- `p_system`(기본 `default_p_system` = 앵커 **산술 평균**): `gap_system_to_now_rel`·신호·추가 규칙의 기준.
- 이 모듈: 평균이 아닌 **대체 시스템가**(현재가 쏠림, 텐션)를 같은 축(가격)에 추가 정의.
"""
from __future__ import annotations

__all__ = [
    "p_system_shrunk_to_now",
    "p_system_tension_blend",
]

Number = float | int


def p_system_shrunk_to_now(
    p_system: Number, p_now: Number, weight_to_now: float = 0.15
) -> float:
    """시스템가를 `p_now` 쪽으로 **고정 비율** 쏠림(베이지·리지 스타일 연구용)."""
    w = max(0.0, min(1.0, float(weight_to_now)))
    ps, pn = float(p_system), float(p_now)
    return (1.0 - w) * ps + w * pn


def p_system_tension_blend(
    p_system: Number,
    p_now: Number,
    mean_pairwise_rel: Number,
    *,
    cap: float = 0.5,
) -> float:
    """`mean_pairwise_rel`이 클수록(앵커끼리 **상대** 간격 큼) `p_now` 쪽으로 더 민다.

    혼잡(간격 축소) → 평균에 가깝고, 이탈(간격 큼) → 현재가에 가깝게 — 연구 휴리스틱일 뿐, 최적 가중은 데이터로 추정.
    """
    ps, pn = float(p_system), float(p_now)
    t = min(max(0.0, float(mean_pairwise_rel)), float(cap)) / max(float(cap), 1e-12)
    t = min(t, 1.0) * 0.5
    return (1.0 - t) * ps + t * pn
