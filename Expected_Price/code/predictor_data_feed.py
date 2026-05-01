"""Registry `meta.factor_column` + (선택) **정렬 factors CSV** → `predictor_prices` = 전부 **가격**.

`meta.model_artifact` + `meta.model_kind` 는 **배치 학습된 아티팩트**를 로드해 OHLCV 전 구간 **동적 예측가(Series)** 로 덮어쓴다(가장 마지막 우선).
OHLCV 인덱스에 맞게 join 후, 각 id에 **절대 가격(float)** 를 넣는다(수평선 1:1). 없으면 `price_like`·스프레드 fallback.
"""
from __future__ import annotations

import os
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pandas as pd
import vbt_gap_research as vg
from vbt_gap_research import default_predictor_prices, make_predictor_prices_fn_price_like

_PKG = Path(__file__).resolve().parent.parent

Number = float | int


def _meta_for_id(registry: dict[str, Any], pred_id: str) -> dict[str, Any]:
    for p in registry.get("predictors", []):
        if not isinstance(p, dict):
            continue
        if p.get("id") != pred_id:
            continue
        meta = p.get("meta") or {}
        return meta if isinstance(meta, dict) else {}
    return {}


def _column_name_for_id(registry: dict[str, Any], pred_id: str) -> str | None:
    m = _meta_for_id(registry, pred_id)
    return m.get("factor_column") or m.get("source_column")  # type: ignore[return-value]


def model_artifact_for_id(
    registry: dict[str, Any], pred_id: str
) -> tuple[str | None, str | None]:
    """`model_artifact`·`model_kind` 가 있으면 (path, kind), 없으면 (None, None). 둘 중 하나만 있으면 ValueError."""
    m = _meta_for_id(registry, pred_id)
    ap = m.get("model_artifact")
    k = m.get("model_kind")
    if not ap and not k:
        return None, None
    if not ap or not k:
        raise ValueError(
            f"predictor {pred_id!r}: model_artifact 와 model_kind 는 둘 다 필요합니다"
        )
    return str(ap), str(k)


def has_any_model_artifact(registry: dict[str, Any], active_ids: list[str]) -> bool:
    for pid in active_ids:
        p, _ = model_artifact_for_id(registry, pid)
        if p:
            return True
    return False


def resolve_model_artifact_path(
    rel_or_abs: str,
    *,
    project_root: Path,
    registry_path: Path | None = None,
) -> Path:
    p = Path(rel_or_abs)
    if p.is_file():
        return p.resolve()
    cands: list[Path] = []
    if registry_path is not None:
        cands.append((registry_path.parent / p).resolve())
    cands.append((project_root / p).resolve())
    for c in cands:
        if c.is_file():
            return c
    return cands[-1]


def load_dynamic_price_series(
    ohlcv: pd.DataFrame,
    registry: dict[str, Any],
    active_ids: list[str],
    *,
    project_root: Path,
    registry_path: Path | None = None,
) -> dict[str, pd.Series]:
    """각 id에 대해 joblib 아티팩트를 로드하고 OHLCV 전체에 대해 **가격** Series 를 만든다."""
    out: dict[str, pd.Series] = {}
    for pid in active_ids:
        path_s, kind = model_artifact_for_id(registry, pid)
        if not path_s or not kind:
            continue
        ap = resolve_model_artifact_path(
            path_s, project_root=project_root, registry_path=registry_path
        )
        if not ap.is_file():
            raise FileNotFoundError(
                f"model_artifact for {pid!r} not found: {ap} (from {path_s!r})"
            )
        from dynamic_predictor_base import load_artifact

        art = load_artifact(ap)
        if kind == "dynamic_volume_to_close":
            from dynamic_volume_spike import predict_dynamic_volume_price

            s = predict_dynamic_volume_price(art, ohlcv)
        else:
            raise ValueError(
                f"unknown model_kind {kind!r} for {pid!r} (known: dynamic_volume_to_close)"
            )
        out[pid] = s
    return out


def load_factors_table(path: str | os.PathLike[str]) -> pd.DataFrame:
    p = Path(path)
    d = pd.read_csv(p)
    d.columns = [str(c).strip().lower() for c in d.columns]
    tcol = None
    for k in ("time", "timestamp", "date", "datetime", "t"):
        if k in d.columns:
            tcol = k
            break
    if tcol is None and isinstance(d.index, pd.DatetimeIndex):
        f = d.copy()
    else:
        if tcol is None:
            raise ValueError(f"CSV {p!r} need time like column or DatetimeIndex")
        idx = pd.to_datetime(d[tcol], utc=True, errors="coerce")
        f = d.set_index(idx).drop(columns=[tcol], errors="ignore")
    f = f.sort_index()
    return f


def align_factors_to_ohlc(ohlc: pd.DataFrame, factors: pd.DataFrame) -> pd.DataFrame:
    """index 정렬(UTC) 일치. 없는 시각은 **앞** 값으로 ffill(연구·주의: 누수 조정은 호출 측)."""
    a = ohlc.index
    f = factors.copy()
    if f.index.tz is None and a.tz is not None:
        f = f.tz_localize("UTC", ambiguous="infer", nonexistent="shift_forward")
    return f.reindex(a).ffill()


def build_merged_predictor_prices_fn(
    ohlcv: pd.DataFrame,
    registry: dict[str, Any],
    active_ids: list[str],
    *,
    factors: pd.DataFrame | None = None,
    use_price_like_vol_time: bool = True,
    project_root: Path | None = None,
    registry_path: Path | None = None,
) -> Callable[[int, float], dict[str, float]]:
    """
    1) base: `use_price_like` 이면 vol/time 포함 `bar_anchors`, 아니면 `default_predictor_prices`만.
    2) `factors` 열이 `meta.factor_column` 과 맞는 id 는 **float 절대가** 로 덮어씀.
    3) `meta.model_artifact`+`model_kind` id 는 **학습 추론 Series** 로 덮어씀(마지막).
    """
    aids = list(active_ids)
    id_to_col = {pid: _column_name_for_id(registry, pid) for pid in aids}
    f_aligned = None
    if factors is not None and len(factors) > 0:
        f_aligned = align_factors_to_ohlc(ohlcv, factors)

    root = project_root or _PKG
    dyn = load_dynamic_price_series(
        ohlcv, registry, aids, project_root=root, registry_path=registry_path
    )

    if use_price_like_vol_time:
        pl_fn = make_predictor_prices_fn_price_like(ohlcv, aids, vol_rolling=20)
    else:

        def pl_fn(i: int, c: float) -> dict[str, float]:
            return default_predictor_prices(float(c), aids)

    def fn(i: int, c: float) -> dict[str, float]:
        c_val = float(c)
        d = dict(pl_fn(int(i), c_val))
        if f_aligned is not None:
            for pid in aids:
                col = id_to_col.get(pid)
                if not col or col not in f_aligned.columns:
                    continue
                v = f_aligned[col].iloc[int(i)]
                if pd.isna(v):
                    continue
                d[pid] = float(v)
        for pid, ser in dyn.items():
            v = ser.iloc[int(i)]
            if pd.isna(v):
                continue
            d[pid] = float(v)
        return d

    return fn


def factor_column_for_id(registry: dict[str, Any], pred_id: str) -> str | None:
    return _column_name_for_id(registry, pred_id)


__all__ = [
    "load_factors_table",
    "align_factors_to_ohlc",
    "build_merged_predictor_prices_fn",
    "factor_column_for_id",
    "model_artifact_for_id",
    "has_any_model_artifact",
    "resolve_model_artifact_path",
    "load_dynamic_price_series",
]
