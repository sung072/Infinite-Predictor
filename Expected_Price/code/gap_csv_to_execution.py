"""갭 백테스트 CSV(저장본) → `execution_bridge` JSONL. Nautilus **이전** 배치 변환."""
from __future__ import annotations

import ast
from pathlib import Path
from typing import Any

import pandas as pd

import execution_bridge as exb

__all__ = [
    "parse_predictor_prices_cell",
    "prepare_gap_df_for_execution",
    "gap_csv_to_execution_jsonl",
]


def parse_predictor_prices_cell(v: Any) -> dict[str, float]:
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return {}
    if isinstance(v, dict):
        return {str(k): float(x) for k, x in v.items() if x is not None and pd.notna(x)}
    if isinstance(v, str) and v.strip().startswith("{"):
        try:
            d = ast.literal_eval(v)
        except (SyntaxError, ValueError, TypeError):
            return {}
        if isinstance(d, dict):
            return {str(k): float(x) for k, x in d.items() if x is not None}
    return {}


def prepare_gap_df_for_execution(df: pd.DataFrame) -> pd.DataFrame:
    """`write_execution_jsonl` 가능하도록 `predictor_prices` 를 dict 로."""
    o = df.copy()
    if "predictor_prices" in o.columns:
        o["predictor_prices"] = o["predictor_prices"].map(parse_predictor_prices_cell)
    return o


def gap_csv_to_execution_jsonl(
    csv_path: str | Path,
    out_jsonl: str | Path,
    *,
    last_n: int | None = None,
    header: dict[str, Any] | None = None,
) -> int:
    """CSV 를 읽어 JSONL; `last_n` 이면 마지막 N봉만. 반환: 바 수."""
    p = Path(csv_path)
    df = pd.read_csv(p, index_col=0, parse_dates=True)
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index, utc=True, errors="coerce")
    df = df.sort_index()
    if last_n is not None and last_n > 0 and len(df) > last_n:
        df = df.tail(int(last_n))
    df = prepare_gap_df_for_execution(df)
    exb.write_execution_jsonl(df, out_jsonl, header=header)
    return int(len(df))
