"""4단계(AI/LLM·학습)용: 갭 백테스트 CSV·provenance 를 **하나의 JSON-직렬** 스냅샷으로 합친다.

실시간·실거래 루프에서 이 모듈을 직접 쓰지는 않는 것을 권장(배치·노트북·CI 오프라인)."""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

import numpy as np
import pandas as pd

__all__ = [
    "KEY_GAP_METRICS",
    "AnalysisSnapshotConfig",
    "load_gap_csv",
    "build_snapshot_dict",
    "write_snapshot_dict",
]

# 대시보드/연구에서 공통으로 보는 갭·합성 열(있으면 포함)
KEY_GAP_METRICS: tuple[str, ...] = (
    "mean_pairwise_rel",
    "mean_pairwise_per_atr",
    "gap_system_to_now_rel",
    "range_rel",
    "p_system",
    "p_system_shrunk",
    "p_system_tension",
    "n_anchors",
    "P_now",
)


@dataclass(frozen=True)
class AnalysisSnapshotConfig:
    """스냅샷에 넣을 tail 행 수·컬럼."""
    last_n_bars: int = 48
    include_predictor_prices_str: bool = True


def to_jsonable(obj: Any) -> Any:
    if obj is None or isinstance(obj, (str, int, bool)):
        return obj
    if isinstance(obj, float):
        return obj if math.isfinite(obj) else None
    if isinstance(obj, (np.floating,)):
        v = float(obj)
        return v if math.isfinite(v) else None
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, dict):
        return {str(k): to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(x) for x in obj]
    if isinstance(obj, (pd.Timestamp, datetime)):
        t = pd.Timestamp(obj)
        if pd.isna(t):
            return None
        if t.tz is None:
            t = t.tz_localize("UTC")
        return t.isoformat()
    if hasattr(obj, "item") and not isinstance(obj, (bytes, bytearray, str)):
        try:
            return to_jsonable(obj.item())
        except (ValueError, TypeError, AttributeError):
            pass
    if isinstance(obj, (np.bool_, bool)):
        return bool(obj)
    if isinstance(obj, (bytes, bytearray, memoryview)):
        return str(obj)[:20_000]
    return str(obj) if obj is not None else None


def load_gap_csv(path: Path, *, index_col: int = 0) -> pd.DataFrame:
    p = path.resolve()
    if not p.is_file():
        raise FileNotFoundError(p)
    df = pd.read_csv(p, index_col=index_col, parse_dates=True)
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index, utc=True, errors="coerce")
    return df.sort_index()


def _row_dict(df: pd.DataFrame, i: int) -> dict[str, Any]:
    s = df.iloc[i]
    out: dict[str, Any] = {}
    for c in s.index:
        v = s[c]
        if pd.isna(v):
            out[str(c)] = None
        else:
            out[str(c)] = to_jsonable(v)
    out["timestamp"] = to_jsonable(s.name)
    return out


def _describe_block(df: pd.DataFrame, cols: list[str]) -> dict[str, Any]:
    present = [c for c in cols if c in df.columns]
    if not present:
        return {}
    d = df[present].replace([np.inf, -np.inf], np.nan)
    st = d.describe(percentiles=[0.1, 0.5, 0.9]).T
    return to_jsonable(st.to_dict(orient="index"))


def _provenance_file(path: Path | None) -> Any:
    if path is None or not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def build_snapshot_dict(
    *,
    full: pd.DataFrame,
    cfg: AnalysisSnapshotConfig,
    oos: pd.DataFrame | None = None,
    wf: pd.DataFrame | None = None,
    full_prov: Path | None = None,
    oos_prov: Path | None = None,
    wf_prov: Path | None = None,
    registry_path: Path | None = None,
) -> dict[str, Any]:
    """학습/LLM 배치에 넣을 구조화 dict (투자 권고 없음, 관측 요약)."""
    key_cols: list[str] = list(KEY_GAP_METRICS)
    gpr = [c for c in full.columns if str(c).startswith("gpr__")]
    key_cols = list(dict.fromkeys([*key_cols, *gpr[:12]]))  # 너무 길면 잘라도 됨(전체만)

    n = min(cfg.last_n_bars, len(full))
    tail = full.tail(n) if n else full

    if not cfg.include_predictor_prices_str and "predictor_prices" in tail.columns:
        tail = tail.drop(columns=["predictor_prices"])

    last = _row_dict(full, -1) if len(full) else {}
    out: dict[str, Any] = {
        "schema": "ai_analysis_snapshot.v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "bars": {"full": int(len(full)), "tail_included": int(n)},
        "summary_numeric_full": _describe_block(full, key_cols),
        "last_bar": last,
        "tail_rows": [_row_dict(tail, i) for i in range(len(tail))],
    }

    if oos is not None and len(oos):
        out["summary_numeric_oos"] = _describe_block(oos, key_cols)
        out["last_bar_oos"] = _row_dict(oos, -1) if len(oos) else None
        out["bars_oos"] = int(len(oos))
    if wf is not None and len(wf):
        out["summary_numeric_wf_all"] = _describe_block(wf, key_cols)
        out["bars_wf"] = int(len(wf))
        if "fold" in wf.columns:
            fm = (
                wf.groupby("fold", sort=True)[
                    [c for c in key_cols if c in wf.columns]
                ]
                .mean()
                if any(c in wf.columns for c in key_cols)
                else None
            )
            if fm is not None and not fm.empty:
                out["wf_fold_means"] = to_jsonable(fm.to_dict(orient="index"))

    out["provenance"] = {
        "full": _provenance_file(full_prov),
        "oos": _provenance_file(oos_prov),
        "wf": _provenance_file(wf_prov),
    }
    if registry_path and registry_path.is_file():
        out["registry"] = {"path": str(registry_path.resolve())}
    return out


def write_snapshot_dict(path: Path, d: Mapping[str, Any]) -> None:
    path = path.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    j = to_jsonable(dict(d))
    path.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding="utf-8")
