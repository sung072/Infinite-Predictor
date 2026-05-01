#!/usr/bin/env python3
r"""strict multi-cycle summary에서 심볼쌍 기반 클러스터/공통공식 리포트 생성."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent


def _connected_components(nodes: list[str], edges: list[tuple[str, str]]) -> list[list[str]]:
    g: dict[str, set[str]] = {n: set() for n in nodes}
    for a, b in edges:
        if a in g and b in g:
            g[a].add(b)
            g[b].add(a)
    seen: set[str] = set()
    comps: list[list[str]] = []
    for n in nodes:
        if n in seen:
            continue
        st = [n]
        comp: list[str] = []
        while st:
            x = st.pop()
            if x in seen:
                continue
            seen.add(x)
            comp.append(x)
            st.extend(sorted(g[x] - seen))
        comps.append(sorted(comp))
    comps.sort(key=lambda c: (-len(c), c))
    return comps


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--from-summary-json",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_summary_50.json",
    )
    p.add_argument(
        "--sim-threshold",
        type=float,
        default=1.0,
        help="공식 유사도 임계값 (기본 1.0 = 완전 일치)",
    )
    p.add_argument(
        "--hit-gap-max",
        type=float,
        default=0.08,
        help="쌍의 hit_rate 차 허용 상한",
    )
    p.add_argument(
        "--out-md",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_symbol_pairs.md",
    )
    p.add_argument(
        "--out-json",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_symbol_pairs.json",
    )
    args = p.parse_args(argv)

    d = json.loads(args.from_summary_json.read_text(encoding="utf-8"))
    rows = list(d.get("best_by_symbol", []))
    pairs = list(d.get("similar_pairs_top20", []))
    nodes = sorted([str(r.get("symbol")) for r in rows if r.get("symbol")])
    by_symbol = {str(r["symbol"]): r for r in rows if r.get("symbol")}

    use_pairs = []
    edges: list[tuple[str, str]] = []
    for pz in pairs:
        sim = float(pz.get("formula_similarity", 0.0) or 0.0)
        hg = float(pz.get("hit_gap_abs", 999.0) or 999.0)
        if sim >= args.sim_threshold and hg <= args.hit_gap_max:
            a = str(pz.get("symbol_a"))
            b = str(pz.get("symbol_b"))
            if a and b:
                edges.append((a, b))
                use_pairs.append(pz)

    comps = _connected_components(nodes, edges)
    groups: list[dict[str, Any]] = []
    for i, comp in enumerate(comps, start=1):
        ck = [str(by_symbol[s].get("cluster_key")) for s in comp if s in by_symbol]
        common = ck[0] if ck and all(x == ck[0] for x in ck) else None
        fams = sorted(
            {
                str((by_symbol[s].get("best_formula") or {}).get("family"))
                for s in comp
                if s in by_symbol
            }
        )
        groups.append(
            {
                "group_id": i,
                "symbols": comp,
                "size": len(comp),
                "common_cluster_key": common,
                "formula_families": fams,
            }
        )

    out = {
        "source": str(args.from_summary_json),
        "sim_threshold": args.sim_threshold,
        "hit_gap_max": args.hit_gap_max,
        "n_symbols": len(nodes),
        "n_pairs_used": len(use_pairs),
        "groups": groups,
        "pairs_used": use_pairs,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    srcp = args.from_summary_json
    src_label = str(srcp.resolve())
    try:
        src_label = str(srcp.resolve().relative_to(ROOT.resolve()))
    except Exception:  # noqa: BLE001
        src_label = str(srcp)

    md = [
        "# 심볼쌍/그룹 연구 리포트",
        "",
        f"- source: `{src_label}`",
        f"- sim_threshold={args.sim_threshold}, hit_gap_max={args.hit_gap_max}",
        f"- symbols={len(nodes)}, pairs_used={len(use_pairs)}",
        "",
        "## 그룹(연결요소)",
        "",
        "| group | size | symbols | common_cluster_key | formula_families |",
        "|---:|---:|---|---|---|",
    ]
    for g in groups:
        md.append(
            f"| {g['group_id']} | {g['size']} | {','.join(g['symbols'])} | "
            f"`{g['common_cluster_key']}` | {','.join(g['formula_families'])} |"
        )
    md += [
        "",
        "## 사용된 심볼쌍",
        "",
        "| pair | sim | hit_gap | mae_ratio_gap |",
        "|---|---:|---:|---:|",
    ]
    for pz in use_pairs:
        md.append(
            f"| `{pz.get('pair')}` | {float(pz.get('formula_similarity', 0.0)):.4f} | "
            f"{float(pz.get('hit_gap_abs', 0.0)):.4f} | {float(pz.get('mae_ratio_gap_abs', 0.0)):.4f} |"
        )
    args.out_md.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("wrote", args.out_json.resolve())
    print("wrote", args.out_md.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

