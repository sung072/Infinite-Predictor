"""비가격 신호 → **가격 수평선(예측가)으로 환산** (연구 규칙/합의층).

모든 “축(거래량, 시간, 감정 …)”을 **동일한 세로(가격) 눈금** 위의 선으로 둬서
`predictor_gap_metrics` / Registry `predictor_prices`에 넣는다. 변환은 **팀·실험마다 합의**하며
여기서는 **재현 가능한** 기본식만 쓴다.

실거래 경로·실시간 루프에서 VectorBT/이 모듈 **직접 호출 금지**는 기존 프로젝트 규칙과 같다.
"""
from __future__ import annotations

import math
from typing import Any, Literal

Number = float | int

VolumeMode = Literal["log_ratio", "bps_of_ref"]
TimeMode = Literal["cycle_utc_day", "duration_log"]

# Registry / `predictor_prices` / gap 앵커 id (데모, 합의·확장 가능)
PRED_ID_VOL = "vol_as_price_demo"
PRED_ID_TIME = "time_as_price_demo"
PRICE_LIKE_DEMO_IDS: frozenset[str] = frozenset((PRED_ID_VOL, PRED_ID_TIME))


def volume_as_price(
    volume: Number,
    *,
    p_ref: Number,
    vol_ref: Number,
    mode: VolumeMode = "log_ratio",
    bps_sensitivity: float = 5.0,
) -> float:
    """거래량을 **같은 자산 가격 눈금** 위의 한 점(선)으로 둔다.

    *log_ratio*: ``p_ref * (1 + s * (log1p(v/vo) - log1p(1)) )`` with ``s=1e-4`` (조정 가능).
    *bps_of_ref*: (log1p v - log1p v_ref) 를 bps 스케일로만 반영.
    """
    v, vo, p = float(volume), float(vol_ref), float(p_ref)
    if vo <= 0 or v < 0 or p <= 0:
        raise ValueError("volume_as_price: need vol_ref>0, v>=0, p_ref>0")
    if mode == "log_ratio":
        s = 1.0e-4
        z = math.log1p(v / vo) - math.log1p(1.0)
        return p * (1.0 + s * z)
    if mode == "bps_of_ref":
        z = math.log1p(v) - math.log1p(vo)
        return p * (1.0 + (bps_sensitivity * 1e-4) * z)
    raise ValueError(f"unknown mode: {mode!r}")


def time_as_price(
    t_seconds: Number,
    *,
    p_ref: Number,
    mode: TimeMode = "cycle_utc_day",
    day_seconds: float = 86_400.0,
) -> float:
    """“시간”을 가격 눈금에 올려 둔다 (샘플 규칙 2가지).

    *cycle_utc_day*: 0~day_s 주기를 **사인**으로 p_ref에 비례한 미세 변동(한 바가 어디쯤인지).
    *duration_log*: 잔여/경과 **초**에 대해 ``p_ref * (1 + 1e-4 * log1p(t_s))`` — *단조* (해석=합의).
    """
    t = float(t_seconds)
    p = float(p_ref)
    if p <= 0:
        raise ValueError("p_ref>0")
    if mode == "cycle_utc_day":
        th = 2.0 * math.pi * (t % day_seconds) / day_seconds
        return p * (1.0 + 1.0e-4 * math.sin(th))
    if mode == "duration_log":
        return p * (1.0 + 1.0e-4 * math.log1p(max(t, 0.0)))
    raise ValueError(f"unknown mode: {mode!r}")


def _spread_non_price_like_cheap(p_now: float, pids: list[str]) -> dict[str, float]:
    """`vol`·`time` id가 아닌 나머지(뉴스·페어 등)에 **임시**로 얇은 수평선(연구·미연결)."""
    if not pids:
        return {}
    if len(pids) == 1:
        return {pids[0]: p_now * 1.0002}
    n = len(pids)
    return {
        pids[j]: p_now * (1.0 + 0.0010 * (2.0 * j / (n - 1) - 1.0)) for j in range(n)
    }


def bar_anchors_from_ohlcv(
    ohlcv: Any,
    bar_i: int,
    active_ids: list[str],
    vol_ref: float,
    p_now: float,
) -> dict[str, float]:
    """한 바: **모든** `active_ids` 를 가격(앵커)으로 채움. `vol`·`time` id는 [price_unification] 규칙, 나머지는 희미한 스프레드."""
    c = float(p_now)
    wr = max(float(vol_ref), 1e-12)
    v = float(ohlcv["volume"].iloc[bar_i]) if "volume" in ohlcv.columns else 0.0
    ts = ohlcv.index[bar_i]
    tsec: float
    if hasattr(ts, "timestamp"):
        tsec = float(ts.timestamp())  # type: ignore[no-untyped-call]
    else:
        tsec = float(getattr(ts, "value", 0.0)) * 1e-9
    out: dict[str, float] = {}
    other: list[str] = []
    for pid in active_ids:
        if pid == PRED_ID_VOL:
            out[pid] = volume_as_price(v, p_ref=c, vol_ref=wr)
        elif pid == PRED_ID_TIME:
            out[pid] = time_as_price(tsec, p_ref=c, mode="cycle_utc_day")
        else:
            other.append(pid)
    out.update(_spread_non_price_like_cheap(c, other))
    return {k: out[k] for k in active_ids if k in out}


def predictors_from_ohlc_row(
    p_now: float,
    volume: float,
    t_seconds_from_epoch: float,
    *,
    vol_ref: float,
) -> dict[str, float]:
    """데모: *량가·시간가* 두 id만(Registry 이 이름으로 등록)."""
    return {
        PRED_ID_VOL: volume_as_price(volume, p_ref=p_now, vol_ref=vol_ref),
        PRED_ID_TIME: time_as_price(
            t_seconds_from_epoch, p_ref=p_now, mode="cycle_utc_day"
        ),
    }


__all__ = [
    "volume_as_price",
    "time_as_price",
    "predictors_from_ohlc_row",
    "bar_anchors_from_ohlcv",
    "PRED_ID_VOL",
    "PRED_ID_TIME",
    "PRICE_LIKE_DEMO_IDS",
    "VolumeMode",
    "TimeMode",
]
