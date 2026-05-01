"""예측가 수평선 간 거리·응집도 스칼라 (연구 레이어).

시스템가(p_system)나 축소된 단일 “합의가”는,
반드시 **예측가–예측가 쌍**의 상대 간격·응집·코호트 구조를
실증적으로 파악한 뒤에만 **해석·신뢰**가 붙는다(입력이 서로 뭉쳤는지, 어느 쌍이 지배하는지 모르면
합의 가격은 껍질뿐이다). 이 모듈은 그 1봉·1스냅샷 단위 측정에 쓴다.

실거래 서비스 경로에서 VectorBT 호출 금지 — 이 모듈은 피처 계산만 제공한다.
동일 시점에서 동일 지평선 t·동일 자산 기준 앵커 가격만 넣는다.
"""
from __future__ import annotations

from collections.abc import Iterable
from typing import Any, Mapping, MutableMapping

Number = float | int


def _scale(default: Number | None, values: list[float]) -> float:
    if default is not None and float(default) > 0:
        return float(default)
    if not values:
        raise ValueError("scale이 없고 앵커가 비었습니다")
    m = sum(values) / len(values)
    if m <= 0:
        raise ValueError("양수 스케일이 필요합니다(P_now 또는 앵커 평균)")
    return float(m)


def pairwise_relative_distances(
    anchors: Mapping[str, Number],
    *,
    scale: Number | None = None,
) -> dict[tuple[str, str], float]:
    """앵커 쌍 (i<j) 에 대해 |pi-pj|/scale."""
    keys = sorted(anchors.keys())
    vals = [float(anchors[k]) for k in keys]
    s = _scale(scale, vals)
    out: dict[tuple[str, str], float] = {}
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            d = abs(vals[i] - vals[j]) / s
            out[(keys[i], keys[j])] = d
    return out


def mean_pairwise_distance(
    anchors: Mapping[str, Number],
    *,
    scale: Number | None = None,
) -> float:
    pw = pairwise_relative_distances(anchors, scale=scale)
    if not pw:
        return 0.0
    return sum(pw.values()) / len(pw)


def variance_of_anchors(anchors: Mapping[str, Number]) -> float:
    vals = [float(v) for v in anchors.values()]
    if len(vals) < 2:
        return 0.0
    mu = sum(vals) / len(vals)
    return sum((x - mu) ** 2 for x in vals) / len(vals)


def range_spread(anchors: Mapping[str, Number]) -> float:
    vals = [float(v) for v in anchors.values()]
    if not vals:
        return 0.0
    return max(vals) - min(vals)


def mean_abs_pairwise_distance(anchors: Mapping[str, Number]) -> float:
    """i<j 쌍에 대한 |pi-pj| 산술 평균(스케일 없음) — ATR·실제 틱 단위로 나눈 정규화에 사용."""
    keys = sorted(anchors.keys())
    n = len(keys)
    if n < 2:
        return 0.0
    vals = [float(anchors[k]) for k in keys]
    s = 0.0
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            s += abs(vals[i] - vals[j])
            c += 1
    return s / c


def pairwise_rel_gaps_flat(
    anchors: Mapping[str, Number],
    *,
    scale: float,
) -> dict[str, float]:
    """각 쌍에 대해 |pi-pj|/scale. 열 이름 `gpr__<id1>__<id2>` (id 정렬, 상대)."""
    if not scale or float(scale) <= 0:
        raise ValueError("scale must be positive")
    keys = sorted(anchors.keys())
    vals = [float(anchors[k]) for k in keys]
    out: dict[str, float] = {}
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            d = abs(vals[i] - vals[j]) / float(scale)
            out[f"gpr__{keys[i]}__{keys[j]}"] = d
    return out


def cohort_gap_scalars(
    anchors: Mapping[str, Number],
    id_to_cohort: Mapping[str, str],
    *,
    scale: float,
) -> dict[str, float]:
    """`meta.anchor_cohort` 가 id마다 있을 때, **군 간(inter)** / **군 내(intra)** 쌍의 상대 간격 평균.

    * 서로 다른 군: `gpr_cohort_inter_rel` (쌍이 없으면 `nan`)
    * 동일 군(같은 라벨): `gpr_cohort_intra_rel` (2명 미만이면 `nan`)
    * `scale` = 해당 바의 `scale_used` 와 맞출 것(전역 비교).
    * `anchors` 키는 `id_to_cohort` 에 **전부** 있어야 하며, 아니면 `nan` 반환.
    """
    if not scale or float(scale) <= 0:
        raise ValueError("scale must be positive")
    co = {k: str(v).strip() for k, v in id_to_cohort.items()}
    keys = sorted(anchors.keys())
    for k in keys:
        if k not in co:
            return {
                "gpr_cohort_inter_rel": float("nan"),
                "gpr_cohort_intra_rel": float("nan"),
            }
    inter: list[float] = []
    intra: list[float] = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            d = abs(float(anchors[a]) - float(anchors[b])) / float(scale)
            if co[a] != co[b]:
                inter.append(d)
            else:
                intra.append(d)
    return {
        "gpr_cohort_inter_rel": (sum(inter) / len(inter)) if inter else float("nan"),
        "gpr_cohort_intra_rel": (sum(intra) / len(intra)) if intra else float("nan"),
    }


def relative_gap_to_now(p_anchor: Number, p_now: Number, *, scale: Number | None = None) -> float:
    s = _scale(scale, [float(p_now), float(p_anchor)])
    return abs(float(p_anchor) - float(p_now)) / s


def system_gap_metrics(
    anchors: Mapping[str, Number],
    *,
    p_now: Number,
    p_system: Number,
    scale: Number | None = None,
) -> dict[str, float]:
    """요약: 예측가들 분산·평균쌍거리·시스템가-현재가 괴리."""
    vals = [float(v) for v in anchors.values()]
    s = _scale(scale, vals + [float(p_now), float(p_system)])
    mpw = mean_pairwise_distance(anchors, scale=s)
    var_p = variance_of_anchors(anchors)
    gap_sys = abs(float(p_system) - float(p_now)) / s
    rng = range_spread(anchors) / s if anchors else 0.0
    return {
        "scale_used": s,
        "mean_pairwise_rel": mpw,
        "variance_anchors": var_p,
        "range_rel": rng,
        "gap_system_to_now_rel": gap_sys,
        "n_anchors": float(len(anchors)),
    }


def anchor_prices_for_ids(
    price_by_predictor_id: Mapping[str, Number],
    predictor_ids: Iterable[str],
    *,
    strict: bool = True,
) -> dict[str, float]:
    """Registry `predictors[].id`와 동일한 키로 가격이 들어 있어야 `system_gap_metrics`에 넣을 `anchors`가 된다.

    *strict=True*: 요청 id 중 하나라도 없으면 KeyError.
    *strict=False*: 없는 id는 생략(빈 dict 가능).
    """
    out: dict[str, float] = {}
    for pid in predictor_ids:
        if pid not in price_by_predictor_id:
            if strict:
                raise KeyError(
                    f"missing price for predictor_id {pid!r} — keys must match Registry id"
                )
            continue
        out[pid] = float(price_by_predictor_id[pid])
    return out


def compression_ratio(prev_metric: float, curr_metric: float, *, eps: float = 1e-12) -> float:
    """이전 대비 간격 스칼라 비율. <1 이면 축소(압축)."""
    if prev_metric <= eps:
        return float("inf") if curr_metric > eps else 1.0
    return curr_metric / prev_metric


def summarize_series(metrics_series: Iterable[Mapping[str, float]]) -> list[dict[str, Any]]:
    """연속 스냅샷에서 압축률 등을 붙이기 위한 보조(프레임 없이 최소 구현)."""
    rows: list[dict[str, Any]] = []
    prev: MutableMapping[str, float] | None = None
    for row in metrics_series:
        d = dict(row)
        if prev is not None and "mean_pairwise_rel" in prev and "mean_pairwise_rel" in d:
            d["compression_mean_pairwise"] = compression_ratio(
                float(prev["mean_pairwise_rel"]), float(d["mean_pairwise_rel"])
            )
        rows.append(d)
        prev = {k: float(d[k]) for k in ("mean_pairwise_rel", "gap_system_to_now_rel") if k in d}
    return rows


__all__ = [
    "pairwise_relative_distances",
    "mean_pairwise_distance",
    "variance_of_anchors",
    "range_spread",
    "mean_abs_pairwise_distance",
    "pairwise_rel_gaps_flat",
    "cohort_gap_scalars",
    "relative_gap_to_now",
    "system_gap_metrics",
    "anchor_prices_for_ids",
    "compression_ratio",
    "summarize_series",
]