"""최소 재현: 시드, config JSON 해시, `data_snapshot_id`를 한 틀에 담는다."""
from __future__ import annotations

import hashlib
import json
import random
from typing import Any

import numpy as np


def config_canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def config_sha256(obj: Any) -> str:
    s = config_canonical_json(obj)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def experiment_fingerprint(
    obj: Any,
    *,
    seed: int,
    data_snapshot_id: str,
) -> str:
    """config + 시드 + 데이터 스냅을 섞은 전체 휴리스틱 지문(짧지 않게 쓰려면 64hex 그대로)."""
    s = f"{config_canonical_json(obj)}|seed={int(seed)}|snap={data_snapshot_id}"
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def experiment_id_short(
    obj: Any,
    *,
    seed: int,
    data_snapshot_id: str,
    length: int = 16,
) -> str:
    h = experiment_fingerprint(obj, seed=seed, data_snapshot_id=data_snapshot_id)
    return h[: int(length)]


def provenance_bundle(
    config: Any,
    *,
    seed: int,
    data_snapshot_id: str,
) -> dict[str, Any]:
    return {
        "config_sha256": config_sha256(config),
        "seed": int(seed),
        "data_snapshot_id": str(data_snapshot_id),
        "experiment_fingerprint": experiment_fingerprint(
            config, seed=seed, data_snapshot_id=data_snapshot_id
        ),
        "experiment_id_short": experiment_id_short(
            config, seed=seed, data_snapshot_id=data_snapshot_id
        ),
    }


def set_global_seeds(seed: int) -> None:
    r = int(seed) % (2**32)
    random.seed(r)
    np.random.seed(r)


__all__ = [
    "config_canonical_json",
    "config_sha256",
    "experiment_fingerprint",
    "experiment_id_short",
    "provenance_bundle",
    "set_global_seeds",
]
