#!/usr/bin/env python3
r"""strict_multi_cycle 배치 요약(`strict_multi_cycle_summary_*.json`)에서 **운용 후보 공식**을 추린다.

- 종목별 `best_by_symbol` 행을 컷( hit / coverage / mae )로 거른 뒤,
- `cluster_key` 별로 몇 종목이 채택했는지 집계하고,
- **전역 단기 리스트**(`shortlist_global`): 등장 빈도·평균 hit 기준 상위 K개 공식 구조.

배치 산출물과 동일 계보를 유지하며, “우리가 쓸 공식 N개”를 고르는 1차 필터로 쓴다.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent


def _finite(x: Any) -> bool:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return False
    return math.isfinite(v)


def _sf(x: Any) -> float:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return float("nan")
    return float(v) if math.isfinite(float(v)) else float("nan")


def _load_summary(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _pick_representative(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """동일 cluster_key 그룹에서 composite_rank_score 최대 행."""
    best = None
    best_s = float("-inf")
    for r in rows:
        s = _sf(r.get("composite_rank_score"))
        if not math.isfinite(s):
            s = _sf(r.get("composite_score"))
        if math.isfinite(s) and s > best_s:
            best_s = s
            best = r
        elif best is None:
            best = r
    return best if best is not None else rows[0]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--summary-json",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_summary_50.json",
        help="strict_multi_cycle_batch 가 쓴 요약 JSON",
    )
    p.add_argument(
        "--out-json",
        type=Path,
        default=ROOT / "data" / "runs" / "curated_formula_shortlist.json",
    )
    p.add_argument(
        "--out-md",
        type=Path,
        default=ROOT / "data" / "runs" / "curated_formula_shortlist.md",
    )
    p.add_argument(
        "--min-hit",
        type=float,
        default=0.0,
        help="directional_hit_rate 하한(미만 제외, NaN 행 제외)",
    )
    p.add_argument(
        "--min-coverage",
        type=float,
        default=0.0,
        help="trust_coverage 하한(미만 제외; 0이면 컷 없음)",
    )
    p.add_argument(
        "--max-mae-ratio",
        type=float,
        default=99.0,
        help="mae_ratio_sys_over_naive 상한(초과 제외, naive 대비)",
    )
    p.add_argument(
        "--shortlist-k",
        type=int,
        default=8,
        help="cluster_key 기준 전역 상위 K개 (빈도·평균 hit)",
    )
    args = p.parse_args(argv)

    if not args.summary_json.is_file():
        print("summary not found:", args.summary_json.resolve(), file=sys.stderr)
        return 2

    raw = _load_summary(args.summary_json)
    rows_in: list[dict[str, Any]] = list(raw.get("best_by_symbol") or [])
    if not rows_in:
        print("best_by_symbol empty", file=sys.stderr)
        return 2

    kept: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []
    for r in rows_in:
        h = _sf(r.get("hit_rate"))
        c = _sf(r.get("coverage"))
        m = _sf(r.get("mae_ratio"))
        reason: str | None = None
        if not _finite(r.get("hit_rate")) or not math.isfinite(h):
            reason = "nan_hit"
        elif h < float(args.min_hit):
            reason = "low_hit"
        elif math.isfinite(c) and c < float(args.min_coverage):
            reason = "low_coverage"
        elif math.isfinite(m) and m > float(args.max_mae_ratio):
            reason = "high_mae_ratio"
        if reason:
            dropped.append({"symbol": r.get("symbol"), "reason": reason, "cluster_key": r.get("cluster_key")})
            continue
        kept.append(r)

    by_ck: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in kept:
        ck = str(r.get("cluster_key") or "")
        by_ck[ck].append(r)

    cluster_stats: list[dict[str, Any]] = []
    for ck, rs in by_ck.items():
        hits = [_sf(x.get("hit_rate")) for x in rs]
        hits_f = [x for x in hits if math.isfinite(x)]
        maes = [_sf(x.get("mae_ratio")) for x in rs]
        maes_f = [x for x in maes if math.isfinite(x)]
        rep = _pick_representative(rs)
        cluster_stats.append(
            {
                "cluster_key": ck,
                "n_symbols": len(rs),
                "symbols": sorted({str(x.get("symbol")) for x in rs}),
                "mean_hit_rate": float(statistics.mean(hits_f)) if hits_f else float("nan"),
                "mean_mae_ratio": float(statistics.mean(maes_f)) if maes_f else float("nan"),
                "representative": {
                    "symbol": rep.get("symbol"),
                    "hit_rate": rep.get("hit_rate"),
                    "mae_ratio": rep.get("mae_ratio"),
                    "coverage": rep.get("coverage"),
                    "best_formula": rep.get("best_formula"),
                    "json_path": rep.get("json_path"),
                },
            }
        )

    cluster_stats.sort(
        key=lambda x: (
            -int(x["n_symbols"]),
            -(_sf(x["mean_hit_rate"]) if math.isfinite(_sf(x["mean_hit_rate"])) else -1.0),
        )
    )
    shortlist = cluster_stats[: max(1, int(args.shortlist_k))]

    out: dict[str, Any] = {
        "source_summary": str(args.summary_json.resolve()),
        "filters": {
            "min_hit": float(args.min_hit),
            "min_coverage": float(args.min_coverage),
            "max_mae_ratio": float(args.max_mae_ratio),
            "shortlist_k": int(args.shortlist_k),
        },
        "counts": {
            "symbols_in_summary": len(rows_in),
            "symbols_after_filter": len(kept),
            "symbols_dropped": len(dropped),
            "distinct_cluster_keys_after_filter": len(by_ck),
        },
        "dropped_symbols": dropped,
        "curated_rows": kept,
        "cluster_aggregates": cluster_stats,
        "shortlist_global_top_k": shortlist,
        "note_ko": (
            "shortlist_global_top_k 는 종목 수·평균 hit 로 정렬한 공식 구조 후보. "
            "실거래 전에는 동일 설정으로 단일 종목 재검증·비용 반영이 필요."
        ),
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Curated formula shortlist",
        "",
        f"- source: `{args.summary_json}`",
        f"- after filter: {len(kept)}/{len(rows_in)} symbols, {len(by_ck)} distinct cluster_keys",
        "",
        "## Filters",
        "",
        f"- min_hit≥{args.min_hit}, min_coverage≥{args.min_coverage}, mae_ratio≤{args.max_mae_ratio}, shortlist_k={args.shortlist_k}",
        "",
        "## Global shortlist (top cluster_key structures)",
        "",
        "| rank | n_symbols | mean_hit | mean_mae | cluster_key |",
        "|---|---:|---:|---:|---|",
    ]
    for i, s in enumerate(shortlist, start=1):
        lines.append(
            f"| {i} | {s['n_symbols']} | {_fmt(s['mean_hit_rate'])} | {_fmt(s['mean_mae_ratio'])} | `{s['cluster_key']}` |"
        )
    lines += ["", "## Representative formula (first row of shortlist)", ""]
    if shortlist:
        rep = shortlist[0]["representative"].get("best_formula")
        lines.append("```json")
        lines.append(json.dumps(rep, ensure_ascii=False, indent=2))
        lines.append("```")

    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("wrote", args.out_json.resolve())
    print("wrote", args.out_md.resolve())
    return 0


def _fmt(x: Any, nd: int = 4) -> str:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return "n/a"
    if not math.isfinite(v):
        return "n/a"
    return f"{v:.{nd}f}"


if __name__ == "__main__":
    raise SystemExit(main())
