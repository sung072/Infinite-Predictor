"""연구 `gap` DataFrame → 외부 실행기(Nautilus 등)로 넘기기 쉬운 **JSON/JSONL** (배치·오프라인).

NautilusTrader **의존성 없음** — 시리얼라이즈만 담당. 라이브 경로는 별 프로세스에서 이 스키마를 읽어 주문.
"""
from __future__ import annotations

import json
import math
from collections.abc import Mapping
from pathlib import Path
from typing import Any, Iterator

import numpy as np
import pandas as pd

SCHEMA_BAR = "expected_price.execution_bar.v1"
SCHEMA_FILE = "expected_price.execution_jsonl.v1"

__all__ = [
    "json_safe",
    "pack_bar_record",
    "write_execution_jsonl",
    "read_execution_jsonl",
    "iter_bar_records",
    "iter_bar_records_streaming",
    "validate_execution_jsonl",
    "SCHEMA_BAR",
    "SCHEMA_FILE",
]

_CORE_SKIP = frozenset({"predictor_prices", "P_now", "p_system"})


def json_safe(v: Any) -> Any:
    if v is None:
        return None
    if isinstance(v, (str, bool)):
        return v
    if isinstance(v, dict):
        return {str(k): json_safe(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [json_safe(x) for x in v]
    if isinstance(v, float):
        if math.isnan(v) or math.isinf(v):
            return None
        return v
    if isinstance(v, (int, np.integer)):
        return int(v)
    if isinstance(v, (float, np.floating)):
        x = float(v)
        if math.isnan(x) or math.isinf(x):
            return None
        return x
    if isinstance(v, np.ndarray):
        return v.tolist()
    return str(v)


def pack_bar_record(
    ts: Any,
    row: Mapping[str, Any] | pd.Series,
) -> dict[str, Any]:
    """한 바: 시각 + `P_now` + `p_system` + `predictor_prices` + 나머지 **스칼라** 메트릭."""
    r = dict(row) if isinstance(row, Mapping) else row.to_dict()
    pp = r.get("predictor_prices")
    if isinstance(pp, dict):
        pred = {str(k): float(v) for k, v in pp.items()}
    else:
        pred = {}
    metrics: dict[str, Any] = {}
    for k, v in r.items():
        if k in _CORE_SKIP or k == "predictor_prices":
            continue
        if isinstance(v, dict):
            continue
        metrics[str(k)] = json_safe(v)
    return {
        "schema": SCHEMA_BAR,
        "t": pd.Timestamp(ts).isoformat() if not isinstance(ts, str) else ts,
        "P_now": json_safe(r.get("P_now")),
        "p_system": json_safe(r.get("p_system")),
        "predictor_prices": pred,
        "metrics": metrics,
    }


def write_execution_jsonl(
    df: pd.DataFrame,
    path: str | Path,
    *,
    header: Mapping[str, Any] | None = None,
) -> None:
    """1행째: 파일 헤더(`schema`, `n_bars`, + `header` 인자). 이후: `pack_bar_record` per row."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    h: dict[str, Any] = {
        "schema": SCHEMA_FILE,
        "n_bars": int(len(df)),
    }
    if header:
        h["run"] = json_safe(dict(header))
    with p.open("w", encoding="utf-8") as fp:
        fp.write(json.dumps(h, ensure_ascii=False) + "\n")
        for ts, row in df.iterrows():
            rec = pack_bar_record(ts, row)
            fp.write(json.dumps(rec, ensure_ascii=False) + "\n")


def read_execution_jsonl(
    path: str | Path,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """`write_execution_jsonl` 이 만든 파일을 읽는다. 반환: (첫 행 헤더, `execution_bar` 레코드 목록)."""
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if not text.strip():
        return {}, []
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return {}, []
    header = json.loads(lines[0])
    bars: list[dict[str, Any]] = []
    for ln in lines[1:]:
        o = json.loads(ln)
        if o.get("schema") == SCHEMA_BAR:
            bars.append(o)
    return header, bars


def iter_bar_records(path: str | Path) -> Iterator[dict[str, Any]]:
    """`execution_bar.v1` 레코드만 순회 — **전체**를 읽는 구현(작은·중간 파일)."""
    yield from iter_bar_records_streaming(path)


def iter_bar_records_streaming(path: str | Path) -> Iterator[dict[str, Any]]:
    """같은 스키마, **한 줄씩** 파싱(대용량 JSONL에 유리)."""
    p = Path(path)
    with p.open(encoding="utf-8") as fp:
        _hdr = fp.readline()
        for ln in fp:
            if not ln.strip():
                continue
            o = json.loads(ln)
            if o.get("schema") == SCHEMA_BAR:
                yield o


def validate_execution_jsonl(path: str | Path) -> list[str]:
    """스키마·필드 검사. 문제 없으면 `[]` — CI·배포 전 `replay_execution_jsonl` 에서도 호출."""
    errs: list[str] = []
    p = Path(path)
    if not p.is_file():
        return [f"not a file: {p}"]
    try:
        text = p.read_text(encoding="utf-8")
    except OSError as e:
        return [str(e)]
    if not text.strip():
        return ["empty file"]
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return ["no non-empty lines"]
    try:
        h = json.loads(lines[0])
    except json.JSONDecodeError as e:
        return [f"line 1 (header): {e}"]
    if h.get("schema") != SCHEMA_FILE:
        errs.append(
            f"line 1: header schema {h.get('schema')!r} (expected {SCHEMA_FILE!r})"
        )
    for j, ln in enumerate(lines[1:], start=2):
        try:
            o = json.loads(ln)
        except json.JSONDecodeError as e:
            errs.append(f"line {j}: {e}")
            continue
        if o.get("schema") != SCHEMA_BAR:
            errs.append(
                f"line {j}: bar schema {o.get('schema')!r} (expected {SCHEMA_BAR!r})"
            )
            continue
        for req in ("t", "predictor_prices"):
            if req not in o:
                errs.append(f"line {j}: missing {req!r}")
        pp = o.get("predictor_prices")
        if not isinstance(pp, dict):
            errs.append(f"line {j}: predictor_prices must be a dict, got {type(pp).__name__}")
    return errs
