"""FDR(BH) + **탐색(가설) 횟수 상한** — 연구·provenance에 끼워넣는 최소 도우미."""
from __future__ import annotations

import math
from typing import Any, Sequence

__all__ = [
    "benjamini_hochberg",
    "assert_exploration_cap",
    "exploration_provenance",
]


def benjamini_hochberg(
    p_values: Sequence[float], *, fdr_q: float
) -> tuple[list[bool], float | None]:
    """BH(FDR) 단계. (원 순서에 맞는 `reject` 플래그, 임계 p·없으면 `None`).

    p 는 [0,1], nan·범위 밖은 ValueError.
    """
    m = len(p_values)
    q = float(fdr_q)
    if not 0.0 < q < 1.0:
        raise ValueError("fdr_q must be in (0,1)")
    for p_ in p_values:
        if math.isnan(p_) or p_ < 0.0 or p_ > 1.0:
            raise ValueError("p must be in [0,1] and not nan")
    if m == 0:
        return [], None
    p_sorted = sorted(p_values)
    k = 0
    for i in range(m, 0, -1):
        if p_sorted[i - 1] <= (i * q) / m:
            k = i
            break
    if k == 0:
        return [False] * m, None
    p_cut = p_sorted[k - 1]
    return [p <= p_cut for p in p_values], p_cut


def assert_exploration_cap(
    n_hypotheses: int, cap: int | None, *, label: str = "exploration"
) -> None:
    if cap is None:
        return
    if n_hypotheses > int(cap):
        raise ValueError(
            f"{label}: {n_hypotheses} 가설/시도 > 상한 {cap} — FDR·탐색 예산 흐름을 먼저 정하세요"
        )


def exploration_provenance(
    n_hypotheses: int,
    *,
    fdr_q: float | None = None,
    p_values: list[float] | None = None,
    cap: int | None = None,
) -> dict[str, Any]:
    """`config`·provenance json에 병합할 딕셔너리. p가 없으면 FDR은 생략."""
    d: dict[str, Any] = {
        "n_hypotheses": n_hypotheses,
        "exploration_cap": cap,
        "fdr_q": fdr_q,
    }
    if fdr_q is not None and p_values is not None:
        if len(p_values) != n_hypotheses:
            d["fdr_error"] = "p_values length != n_hypotheses"
        else:
            flags, p_cut = benjamini_hochberg(p_values, fdr_q=fdr_q)
            d["fdr_p_cut"] = p_cut
            d["fdr_n_reject"] = int(sum(1 for x in flags if x))
    return d
