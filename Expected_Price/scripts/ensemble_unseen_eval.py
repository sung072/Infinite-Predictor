#!/usr/bin/env python3
r"""strict_multi_cycle_research JSON 의 `final_unseen` 상위 K 공식에 대한 **프록시 앙상블** 요약.

바 단위 재평가(투표·가격 블렌드)는 하지 않는다. 동일 unseen 창에서 이미 계산된 지표만 집계해
분산(불일치)과 평균을 본다.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from pathlib import Path
from typing import Any


def _json_scrub(obj: Any) -> Any:
    """JSON 호환: float nan → null."""
    if isinstance(obj, dict):
        return {str(k): _json_scrub(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_json_scrub(v) for v in obj]
    if isinstance(obj, float) and math.isnan(obj):
        return None
    return obj


def _rank_key(row: dict[str, Any]) -> float:
    m = row.get("metrics") or {}
    for k in ("composite_rank_score", "composite_score"):
        v = m.get(k)
        if isinstance(v, (int, float)) and math.isfinite(float(v)):
            return float(v)
    return float("nan")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--json", type=Path, required=True, help="strict_multi_cycle_*.json 경로")
    p.add_argument("--top-k", type=int, default=3, help="final_unseen 에서 상위 K (rank_score 우선)")
    p.add_argument(
        "--out-json",
        type=Path,
        default=None,
        help="요약 JSON 저장(미지정 시 stdout 만)",
    )
    args = p.parse_args(argv)

    if not args.json.is_file():
        print("file not found:", args.json.resolve(), file=sys.stderr)
        return 2
    raw = json.loads(args.json.read_text(encoding="utf-8"))
    rows = raw.get("final_unseen") or []
    if not isinstance(rows, list) or not rows:
        print("no final_unseen in json", file=sys.stderr)
        return 2

    scored = [( _rank_key(r), i, r) for i, r in enumerate(rows)]
    scored.sort(key=lambda t: (-t[0] if math.isfinite(t[0]) else float("-inf"), t[1]))
    top = [t[2] for t in scored[: max(1, int(args.top_k))]]

    def pull(k: str) -> list[float]:
        out: list[float] = []
        for r in top:
            m = r.get("metrics") or {}
            v = m.get(k)
            if isinstance(v, (int, float)) and math.isfinite(float(v)):
                out.append(float(v))
        return out

    hits = pull("directional_hit_rate")
    maes = pull("mae_ratio_sys_over_naive")
    maep = pull("mae_ratio_sys_over_naive_p90")
    covs = pull("trust_coverage")

    summary: dict[str, Any] = {
        "source_json": str(args.json.resolve()),
        "symbol": raw.get("symbol"),
        "top_k_requested": int(args.top_k),
        "n_finalists_used": len(top),
        "cluster_keys": [r.get("cluster_key") for r in top],
        "proxy_ensemble": {
            "note_ko": "동일 JSON 내 final_unseen 지표 평균·분산. 바 단위 앙상블 아님.",
            "mean_directional_hit_rate": statistics.mean(hits) if hits else float("nan"),
            "pstdev_directional_hit_rate": statistics.pstdev(hits) if len(hits) > 1 else 0.0,
            "mean_mae_ratio": statistics.mean(maes) if maes else float("nan"),
            "pstdev_mae_ratio": statistics.pstdev(maes) if len(maes) > 1 else 0.0,
            "mean_mae_ratio_p90": statistics.mean(maep) if maep else float("nan"),
            "mean_trust_coverage": statistics.mean(covs) if covs else float("nan"),
        },
    }

    text = json.dumps(_json_scrub(summary), ensure_ascii=False, indent=2)
    if args.out_json is not None:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(text + "\n", encoding="utf-8")
        print("wrote", args.out_json.resolve())
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
