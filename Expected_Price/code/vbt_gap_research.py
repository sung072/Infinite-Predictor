"""OHLCV + vectorbt + gap 메트릭 **최소 연구 러너** (배치/연구 전용)."""
from __future__ import annotations

import os
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import vectorbt as vbt  # noqa: F401  # Series/DataFrame `.vbt` accessor registration

from predictor_gap_metrics import (
    anchor_prices_for_ids,
    cohort_gap_scalars,
    mean_abs_pairwise_distance,
    pairwise_rel_gaps_flat,
    summarize_series,
)
import price_like
from repro_experiment import provenance_bundle, set_global_seeds
import system_price_rules as spr
from vbt_research_stub import research_pipeline_stub

Number = float | int


def load_ohlcv_csv(path: str | os.PathLike[str]) -> pd.DataFrame:
    p = Path(path)
    df = pd.read_csv(p)
    df.columns = [str(c).strip().lower() for c in df.columns]
    need = ("open", "high", "low", "close", "volume")
    for n in need:
        if n not in df.columns:
            raise ValueError(
                f"OHLCV CSV need columns {need}; have {list(df.columns)} (path {p!r})"
            )
    for k in ("time", "timestamp", "date", "datetime"):
        if k in df.columns:
            idx = pd.to_datetime(df[k], utc=True, errors="coerce")
            df = df.set_index(idx)
            df = df.drop(columns=[k])
            break
    return df[list(need)]


def synthetic_ohlcv_bars(
    n: int,
    *,
    seed: int = 0,
    start: str = "2024-01-01T00:00:00+00:00",
    freq: str = "1h",
) -> pd.DataFrame:
    """닫힘 기준 `close` — docs/abc_event_spec.md 캔들 t 정의와 맞게 UTC 인덱스."""
    if n < 2:
        raise ValueError("n must be at least 2 for gap series")
    set_global_seeds(seed)
    rng = np.random.default_rng(seed)
    rets = rng.normal(0.0, 0.008, n)
    close = 10_000.0 * np.cumprod(1.0 + rets)
    idx = pd.date_range(start=start, periods=n, freq=freq, tz="UTC")
    o = close * (1.0 + rng.normal(0, 0.0002, n))
    h = np.maximum(o, close) * (1.0 + abs(rng.normal(0, 0.0005, n)))
    l = np.minimum(o, close) * (1.0 - abs(rng.normal(0, 0.0005, n)))
    v = np.abs(rng.normal(100.0, 5.0, n))
    return pd.DataFrame(
        {"open": o, "high": h, "low": l, "close": close, "volume": v}, index=idx
    )


def default_predictor_prices(
    close: float, predictor_ids: list[str]
) -> dict[str, float]:
    """가격이 아닌 **골격 데모**: N개 id마다 `close` 주위에 잔 비율을 벌려 pair 거리>0이 되게 함."""
    n = len(predictor_ids)
    if n < 2:
        raise ValueError("need at least 2 predictors for pairwise distance")
    if n == 2:
        return {
            predictor_ids[0]: float(close) * 1.0015,
            predictor_ids[1]: float(close) * 0.9985,
    }
    out: dict[str, float] = {}
    for j, pid in enumerate(predictor_ids):
        t = 2.0 * j / (n - 1) - 1.0
        out[pid] = float(close) * (1.0 + 0.0010 * t)
    return out


def default_p_system(anchors: Mapping[str, float], p_now: float) -> float:  # noqa: ARG001
    vals = [float(x) for x in anchors.values()]
    return float(sum(vals) / len(vals))


def make_predictor_prices_fn_price_like(
    ohlcv: pd.DataFrame,
    active_ids: list[str],
    *,
    vol_rolling: int = 20,
) -> Callable[[int, float], dict[str, float]]:
    """OHLCV 행 + `price_like.bar_anchors` — *모든 id* 를 가격(앵커)으로 채움 ('모든 것은 예측가')."""
    vmed = ohlcv["volume"].rolling(int(vol_rolling), min_periods=1).median() if "volume" in ohlcv.columns else None
    aids = list(active_ids)

    def fn(i: int, c: float) -> dict[str, float]:
        c_val = float(c)
        if vmed is not None:
            vr = float(vmed.iloc[i]) if not pd.isna(vmed.iloc[i]) else c_val
        else:
            vr = c_val
        return price_like.bar_anchors_from_ohlcv(ohlcv, int(i), sorted(aids), max(vr, 1e-9), c_val)

    return fn


def _rolling_vbt_feature(close: pd.Series, window: int) -> pd.Series:
    return close.pct_change().vbt.rolling_std(window)  # type: ignore[no-untyped-call]


def atr_wilder(ohlcv: pd.DataFrame, window: int = 14) -> pd.Series:
    """ATR(연구용): TR의 Wilder RMA(α=1/w). OHLCV 필수. 실거래 엔진과 1:1이 아닐 수 있음."""
    w = int(window)
    if w < 1:
        raise ValueError("ATR window must be >= 1")
    h = ohlcv["high"].astype(float)
    l = ohlcv["low"].astype(float)
    c = ohlcv["close"].astype(float)
    prev = c.shift(1)
    tr = pd.concat(
        [(h - l).abs(), (h - prev).abs(), (l - prev).abs()],
        axis=1,
    ).max(axis=1)
    alpha = 1.0 / w
    return tr.ewm(alpha=alpha, min_periods=w, adjust=False).mean()


def run_gap_research_ohlcv(
    ohlcv: pd.DataFrame,
    *,
    active_predictor_ids: list[str],
    research_config: Mapping[str, Any],
    data_snapshot_id: str,
    seed: int = 0,
    predictor_prices_fn: (
        Callable[[int, float], dict[str, float]] | None
    ) = None,
    p_system_fn: (Callable[[Mapping[str, float], float], float] | None) = None,
    vol_window: int = 5,
    use_price_like: bool = False,
    atr_window: int = 14,
    include_pairwise_columns: bool = False,
    include_system_variants: bool = False,
    anchor_cohort: Mapping[str, str] | None = None,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    """
    * 각 바에서 `P_now` = `close` (캔들 *종가*), 앵커 = `predictor_prices_fn` (기본: 스프레드 2자리).
    * vbt: 변동성 스칼라(rolling std of returns) — **VectorBT “전략 백테스트” 전부가 아니라** 이 루프·특성 래핑.
    * `use_price_like=True` 이면 `make_predictor_prices_fn_price_like` 를 쓴다(Registry에 vol·time id 포함).
    * ATR(기본 14)로 `mean_pairwise_per_atr`(절대 쌍간격/ATR) = 탐색용 **정규화 간격** 스칼라.
    * `include_pairwise_columns=True` 는 각 쌍의 상대 간격 열 `gpr__*__*` 를 쌓는다(다음 단계: 대규모·필터 피처).
    * `p_system` = `p_system_fn(앵커, P_now)` 스칼라(기본: 앵커 산술 평균) — `gpr__` 와 **직접** 같지는 않고, “간격(앵커 간) vs 괴리(시스템-현재)”를 동시에 본다.
    * `include_system_variants=True` 는 `system_price_rules`로 `p_system_shrunk`·`p_system_tension` 열을 추가(연구용).
    * `anchor_cohort`: id → 군 라벨(예: abc·de) — Registry `meta.anchor_cohort` 와 맞추면 `gpr_cohort_inter_rel` / `gpr_cohort_intra_rel`.
    """
    set_global_seeds(seed)
    if "close" not in ohlcv.columns:
        raise ValueError("ohlcv must have 'close'")
    prov = provenance_bundle(research_config, seed=seed, data_snapshot_id=data_snapshot_id)

    if predictor_prices_fn is not None and use_price_like:
        raise ValueError("predictor_prices_fn 이 있으면 use_price_like 는 False 로 두세요")
    p_prices = predictor_prices_fn
    if p_prices is None and use_price_like:
        p_prices = make_predictor_prices_fn_price_like(ohlcv, list(active_predictor_ids))
    if p_prices is None:
        ap = list(active_predictor_ids)
        p_prices = lambda _i, c, _ap=ap: default_predictor_prices(c, _ap)  # noqa: E731
    p_sys = p_system_fn or default_p_system

    need_oh = {"open", "high", "low", "close"}.issubset(ohlcv.columns)
    if not need_oh:
        raise ValueError("ohlcv need open, high, low, close for ATR + gap research")
    close = ohlcv["close"]
    vbt_ret_vol = _rolling_vbt_feature(close, vol_window)
    atr = atr_wilder(ohlcv, window=atr_window)

    raw: list[dict[str, Any]] = []
    for i, c in enumerate(close):
        c_val = float(c)
        pprice = p_prices(i, c_val)
        anchor = p_sys(pprice, c_val)
        row: dict[str, Any] = {
            "P_now": c_val,
            "predictor_prices": pprice,
        }
        m = research_pipeline_stub(
            row,
            active_predictor_ids=active_predictor_ids,
            p_system=anchor,
        )
        m["P_now"] = float(c_val)
        an = anchor_prices_for_ids(pprice, active_predictor_ids, strict=True)
        s_used = float(m["scale_used"])
        m["i"] = float(i)
        m["vbt_rolling_return_std"] = (
            float(vbt_ret_vol.iloc[i]) if not pd.isna(vbt_ret_vol.iloc[i]) else float("nan")
        )
        atr_v = float(atr.iloc[i]) if not pd.isna(atr.iloc[i]) else float("nan")
        m["atr_14"] = atr_v
        m["mean_abs_pairwise"] = float(mean_abs_pairwise_distance(an))
        if not pd.isna(atr_v) and atr_v > 0:
            m["mean_pairwise_per_atr"] = m["mean_abs_pairwise"] / max(atr_v, 1e-12)
        else:
            m["mean_pairwise_per_atr"] = float("nan")
        if include_pairwise_columns:
            m.update(pairwise_rel_gaps_flat(an, scale=s_used))
        if anchor_cohort is not None and len(anchor_cohort) > 0:
            m.update(
                cohort_gap_scalars(
                    an, dict(anchor_cohort), scale=s_used
                )
            )
        m["p_system"] = float(anchor)
        if include_system_variants:
            mpr = float(m.get("mean_pairwise_rel", 0.0))
            m["p_system_shrunk"] = float(
                spr.p_system_shrunk_to_now(anchor, c_val, weight_to_now=0.15)
            )
            m["p_system_tension"] = float(
                spr.p_system_tension_blend(anchor, c_val, mpr, cap=0.5)
            )
        m["predictor_prices"] = {k: float(v) for k, v in pprice.items()}
        raw.append(m)

    with_compression = summarize_series(raw)
    out = pd.DataFrame(with_compression, index=ohlcv.index[: len(with_compression)])
    return out, prov


def demo_run() -> None:
    cfg = {
        "runner": "vbt_gap_research",
        "n_bars": 32,
        "active_predictor_ids": ["p_a", "p_b"],
    }
    ohlc = synthetic_ohlcv_bars(cfg["n_bars"], seed=7)
    df, prov = run_gap_research_ohlcv(
        ohlc,
        active_predictor_ids=cfg["active_predictor_ids"],
        research_config=cfg,
        data_snapshot_id="synth-demo-001",
        seed=7,
    )
    print("provenance", prov)
    print(df.head(3))
    print("...", df.tail(2))


if __name__ == "__main__":
    demo_run()

__all__ = [
    "load_ohlcv_csv",
    "synthetic_ohlcv_bars",
    "run_gap_research_ohlcv",
    "make_predictor_prices_fn_price_like",
    "default_predictor_prices",
    "default_p_system",
    "demo_run",
    "atr_wilder",
]
