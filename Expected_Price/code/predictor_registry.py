"""Predictor Registry 로드·검증(표준 라이브러리만). 앵커 딕 키 = predictors[].id."""
from __future__ import annotations

import json
from collections.abc import Iterator, Mapping, Sequence
from pathlib import Path
from typing import Any, Literal, cast

PredictorStatus = Literal["candidate", "active", "retired", "challenger"]


def load_registry_file(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    with p.open(encoding="utf-8") as f:
        return cast(dict[str, Any], json.load(f))


def validate_registry(data: Mapping[str, Any], *, min_predictors: int = 0) -> None:
    if not isinstance(data, Mapping):
        raise TypeError("registry must be a mapping")
    for k in ("schema_version", "predictors"):
        if k not in data:
            raise ValueError(f"registry missing required key: {k!r}")
    if not isinstance(data["schema_version"], str):
        raise ValueError("schema_version must be a string")
    p = data["predictors"]
    if not isinstance(p, list):
        raise ValueError("predictors must be a list")
    if len(p) < min_predictors:
        raise ValueError(f"expected at least {min_predictors} predictors, got {len(p)}")
    seen: set[str] = set()
    for i, ent in enumerate(p):
        if not isinstance(ent, Mapping):
            raise ValueError(f"predictors[{i}] is not an object")
        e = ent
        for req in ("id", "name", "horizon", "status", "version"):
            if req not in e:
                raise ValueError(f"predictors[{i}] missing {req!r}")
        pid = e["id"]
        if not isinstance(pid, str) or not pid:
            raise ValueError(f"predictors[{i}].id must be non-empty string")
        if pid in seen:
            raise ValueError(f"duplicate predictor id: {pid!r}")
        seen.add(pid)
        h = e["horizon"]
        if not isinstance(h, Mapping) or "kind" not in h or "spec" not in h:
            raise ValueError(f"predictors[{i}].horizon must have kind and spec")
        st = e["status"]
        if st not in ("candidate", "active", "retired", "challenger"):
            raise ValueError(f"predictors[{i}].status invalid: {st!r}")


def all_predictor_ids(data: Mapping[str, Any]) -> list[str]:
    p = data["predictors"]
    if not isinstance(p, Sequence) or isinstance(p, (str, bytes)):
        raise TypeError("predictors must be a list")
    out: list[str] = []
    for ent in p:
        if isinstance(ent, Mapping) and "id" in ent:
            out.append(str(ent["id"]))
    return out


def predictor_ids_by_status(
    data: Mapping[str, Any], statuses: set[PredictorStatus]
) -> set[str]:
    p = data["predictors"]
    out: set[str] = set()
    for ent in p:
        if not isinstance(ent, Mapping):
            continue
        st = ent.get("status")
        if st in statuses and "id" in ent:
            out.add(str(ent["id"]))
    return out


def iter_active_like(data: Mapping[str, Any]) -> Iterator[str]:
    s: set[PredictorStatus] = {"active", "challenger", "candidate"}
    return iter(predictor_ids_by_status(data, s))


def anchor_cohort_map_for_ids(
    data: Mapping[str, Any], active_ids: Sequence[str]
) -> dict[str, str] | None:
    """`predictors[].meta.anchor_cohort` 가 **이번 run의 active_id 전부**에 있으면 id→군(예: abc, de) 맵, 아니면 None (옵트인)."""
    want = {str(x) for x in active_ids}
    out: dict[str, str] = {}
    p = data.get("predictors")
    if not isinstance(p, list):
        return None
    for ent in p:
        if not isinstance(ent, Mapping) or "id" not in ent:
            continue
        pid = str(ent["id"])
        if pid not in want:
            continue
        meta = ent.get("meta")
        c: str | None = None
        if isinstance(meta, dict):
            raw = meta.get("anchor_cohort")
            if raw is not None and str(raw).strip():
                c = str(raw).strip()
        if c is None:
            return None
        out[pid] = c
    if set(out.keys()) != want:
        return None
    return out


__all__ = [
    "load_registry_file",
    "validate_registry",
    "all_predictor_ids",
    "predictor_ids_by_status",
    "iter_active_like",
    "anchor_cohort_map_for_ids",
    "PredictorStatus",
]
