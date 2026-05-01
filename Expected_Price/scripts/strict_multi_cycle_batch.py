#!/usr/bin/env python3
r"""다종목 strict multi-cycle 배치 실행 + 종목별 best 공식 + 심볼쌍 유사도 리포트.

기본 심볼: 50개 (`strict_multi_cycle_universe.DEFAULT_SYMBOLS_50`).

거래대금 상위 100 등: `scripts/fetch_binance_top_usdt_by_volume.py` 로 목록 파일을 만든 뒤
`--symbols-file` 로 넘기면 동일하게 OHLCV(klines 캔들) 수집 후 strict 연구를 돌린다.
"""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import strict_multi_cycle_universe as _u  # noqa: E402

DEFAULT_SYMBOLS = _u.DEFAULT_SYMBOLS_50


def _parse_symbols(raw: str) -> list[str]:
    out = [x.strip().upper() for x in raw.split(",") if x.strip()]
    if not out:
        raise ValueError("empty symbols")
    return out


def _load_symbols_file(path: Path) -> list[str]:
    """한 줄에 BASE 하나(예: BTC) 또는 `BTCUSDT` 형태. `#` 주석·빈 줄 무시."""
    raw = path.read_text(encoding="utf-8")
    out: list[str] = []
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        u = s.upper()
        if u.endswith("USDT") and len(u) > len("USDT"):
            u = u[: -len("USDT")]
        if u:
            out.append(u)
    if not out:
        raise ValueError(f"empty symbols file: {path}")
    return out


def _pair_similarity(a: dict[str, Any], b: dict[str, Any]) -> float:
    # 공식 구조 유사도(0~1): family, emb, trust feature, q-range 일치 정도
    ka = (
        str(a.get("family")),
        int(a.get("embargo_bars", -1)),
        str(a.get("trust_feature")),
        float(a.get("trust_q_low", -1.0) or -1.0),
        float(a.get("trust_q_high", -1.0) or -1.0),
    )
    kb = (
        str(b.get("family")),
        int(b.get("embargo_bars", -1)),
        str(b.get("trust_feature")),
        float(b.get("trust_q_low", -1.0) or -1.0),
        float(b.get("trust_q_high", -1.0) or -1.0),
    )
    m = sum(1 for x, y in zip(ka, kb) if x == y)
    return m / len(ka)


def _pick_best_final_row(final_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """final_unseen 배열에서 유한 hit·mae 인 첫 행(연구 스크립트 best_final 규칙과 동일 취지)."""
    for r in final_rows:
        if not isinstance(r, dict):
            continue
        m = r.get("metrics") or {}
        h = m.get("directional_hit_rate")
        mr = m.get("mae_ratio_sys_over_naive")
        if isinstance(h, (int, float)) and isinstance(mr, (int, float)):
            if not math.isnan(float(h)) and not math.isnan(float(mr)):
                return r
    return final_rows[0] if final_rows else {}


def _run_one(
    sym: str,
    *,
    interval: str,
    limit: int,
    fetch_missing: bool,
    train_bars: int,
    val_bars: int,
    cycle_step: int,
    embargos: str,
    shrinks: str,
    top_k: int,
    min_evals: int,
    unseen_ratio: float,
    seed: int,
    eval_gap_filter_column: str = "",
    eval_gap_filter_min: float | None = None,
    eval_gap_filter_max: float | None = None,
) -> tuple[str, Path]:
    slug = sym.lower()
    ohl = ROOT / "data" / f"{slug}usdt_{interval}_{int(limit/24) if interval=='1h' else limit}.csv"
    # 파일명 일관성 유지: 기존 관례는 *_1h_30d.csv
    if interval == "1h" and limit == 720:
        ohl = ROOT / "data" / f"{slug}usdt_1h_30d.csv"
    fac = ROOT / "data" / "derived" / f"{slug}usdt_factors_4p.csv"

    if fetch_missing and (not ohl.is_file()):
        cmd = [
            sys.executable,
            str(ROOT / "scripts" / "fetch_btc_ohlcv.py"),
            "--symbol",
            f"{sym}USDT",
            "--interval",
            interval,
            "--limit",
            str(limit),
            "--out",
            str(ohl),
        ]
        subprocess.check_call(cmd, cwd=ROOT)
    if fetch_missing and (not fac.is_file()):
        cmd = [
            sys.executable,
            str(ROOT / "scripts" / "build_btc_factor_csv.py"),
            "--ohlcv",
            str(ohl),
            "--out",
            str(fac),
        ]
        subprocess.check_call(cmd, cwd=ROOT)
    if not ohl.is_file() or not fac.is_file():
        raise FileNotFoundError(f"{sym}: missing files ohl={ohl} factors={fac}")

    out_json = ROOT / "data" / "runs" / f"strict_multi_cycle_{slug}.json"
    out_md = ROOT / "data" / "runs" / f"strict_multi_cycle_{slug}.md"
    cmd2 = [
        sys.executable,
        str(ROOT / "scripts" / "strict_multi_cycle_research.py"),
        "--symbol",
        sym,
        "--ohlcv",
        str(ohl),
        "--factors-csv",
        str(fac),
        "--train-bars",
        str(train_bars),
        "--val-bars",
        str(val_bars),
        "--cycle-step",
        str(cycle_step),
        "--embargos",
        embargos,
        "--shrinks",
        shrinks,
        "--top-k",
        str(top_k),
        "--min-evals",
        str(min_evals),
        "--unseen-ratio",
        str(unseen_ratio),
        "--seed",
        str(seed),
        "--out-json",
        str(out_json),
        "--out-md",
        str(out_md),
    ]
    egc = (eval_gap_filter_column or "").strip()
    if egc and (eval_gap_filter_min is not None or eval_gap_filter_max is not None):
        cmd2 += ["--eval-gap-filter-column", egc]
        if eval_gap_filter_min is not None:
            cmd2 += ["--eval-gap-filter-min", str(eval_gap_filter_min)]
        if eval_gap_filter_max is not None:
            cmd2 += ["--eval-gap-filter-max", str(eval_gap_filter_max)]
    subprocess.check_call(cmd2, cwd=ROOT)
    return sym, out_json


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--symbols", default=DEFAULT_SYMBOLS)
    p.add_argument(
        "--symbols-file",
        type=Path,
        default=None,
        help="BASE 심볼 한 줄에 하나(또는 XXXUSDT). 지정 시 --symbols 보다 우선.",
    )
    p.add_argument("--parallel", type=int, default=4, help="동시 실행 워커 수")
    p.add_argument("--fetch-missing", action="store_true")
    p.add_argument("--interval", default="1h")
    p.add_argument("--limit", type=int, default=720)
    p.add_argument("--train-bars", type=int, default=120)
    p.add_argument("--val-bars", type=int, default=36)
    p.add_argument("--cycle-step", type=int, default=20)
    p.add_argument("--embargos", default="12,24")
    p.add_argument("--shrinks", default="0.94,0.95,0.96,0.97")
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--min-evals", type=int, default=3)
    p.add_argument("--unseen-ratio", type=float, default=0.25)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument(
        "--eval-gap-filter-column",
        default="",
        help="strict_multi_cycle_research 에 전달(비우면 미사용). min/max 와 함께.",
    )
    p.add_argument("--eval-gap-filter-min", type=float, default=None)
    p.add_argument("--eval-gap-filter-max", type=float, default=None)
    p.add_argument(
        "--out-summary-md",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_summary_50.md",
    )
    p.add_argument(
        "--out-summary-json",
        type=Path,
        default=ROOT / "data" / "runs" / "strict_multi_cycle_summary_50.json",
    )
    args = p.parse_args(argv)

    if args.symbols_file is not None:
        if not args.symbols_file.is_file():
            print("symbols-file not found:", args.symbols_file.resolve(), file=sys.stderr)
            return 2
        syms = _load_symbols_file(args.symbols_file)
    else:
        syms = _parse_symbols(args.symbols)
    results: dict[str, Path] = {}
    errors: dict[str, str] = {}

    with ThreadPoolExecutor(max_workers=max(1, int(args.parallel))) as ex:
        futs = [
            ex.submit(
                _run_one,
                s,
                interval=args.interval,
                limit=args.limit,
                fetch_missing=bool(args.fetch_missing),
                train_bars=args.train_bars,
                val_bars=args.val_bars,
                cycle_step=args.cycle_step,
                embargos=args.embargos,
                shrinks=args.shrinks,
                top_k=args.top_k,
                min_evals=args.min_evals,
                unseen_ratio=args.unseen_ratio,
                seed=args.seed,
                eval_gap_filter_column=str(args.eval_gap_filter_column),
                eval_gap_filter_min=args.eval_gap_filter_min,
                eval_gap_filter_max=args.eval_gap_filter_max,
            )
            for s in syms
        ]
        for f in as_completed(futs):
            try:
                s, outj = f.result()
                results[s] = outj
                print("done", s, outj, flush=True)
            except Exception as e:  # noqa: BLE001
                msg = str(e)
                # symbol extraction fallback
                key = "unknown"
                for s in syms:
                    if s in msg:
                        key = s
                        break
                errors[key] = msg
                print("failed", key, msg, file=sys.stderr, flush=True)

    rows: list[dict[str, Any]] = []
    for s in sorted(results):
        d = json.loads(results[s].read_text(encoding="utf-8"))
        fr = d.get("final_unseen", [])
        best = _pick_best_final_row(fr) if isinstance(fr, list) else {}
        m = best.get("metrics", {}) if isinstance(best, dict) else {}
        formula = best.get("formula", {}) if isinstance(best, dict) else {}
        rows.append(
            {
                "symbol": s,
                "hit_rate": m.get("directional_hit_rate"),
                "mae_ratio": m.get("mae_ratio_sys_over_naive"),
                "coverage": m.get("trust_coverage"),
                "mean_rr": m.get("mean_rr"),
                "sharpe_per_bar": m.get("sharpe_per_bar"),
                "sharpe_annualized": m.get("sharpe_annualized"),
                "calmar_proxy": m.get("calmar_proxy"),
                "composite_score": m.get("composite_score"),
                "composite_rank_score": m.get("composite_rank_score"),
                "cluster_key": best.get("cluster_key"),
                "best_formula": formula,
                "json_path": str(results[s].relative_to(ROOT)),
            }
        )

    # pair research (similar symbols)
    pairs: list[dict[str, Any]] = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            a, b = rows[i], rows[j]
            sim = _pair_similarity(a.get("best_formula", {}), b.get("best_formula", {}))
            pairs.append(
                {
                    "pair": f"{a['symbol']}-{b['symbol']}",
                    "symbol_a": a["symbol"],
                    "symbol_b": b["symbol"],
                    "formula_similarity": sim,
                    "hit_gap_abs": abs((a.get("hit_rate") or 0.0) - (b.get("hit_rate") or 0.0)),
                    "mae_ratio_gap_abs": abs(
                        (a.get("mae_ratio") or 0.0) - (b.get("mae_ratio") or 0.0)
                    ),
                }
            )
    pairs.sort(key=lambda x: (-float(x["formula_similarity"]), float(x["hit_gap_abs"])))

    hits = [
        float(r["hit_rate"])
        for r in rows
        if isinstance(r.get("hit_rate"), (int, float)) and not math.isnan(float(r["hit_rate"]))
    ]
    maes = [
        float(r["mae_ratio"])
        for r in rows
        if isinstance(r.get("mae_ratio"), (int, float)) and not math.isnan(float(r["mae_ratio"]))
    ]
    acc: dict[str, Any] = {
        "n_symbols_reported": len(rows),
        "n_symbols_finite_hit": len(hits),
        "n_symbols_finite_mae_ratio": len(maes),
        "mean_directional_hit_rate": float(sum(hits) / len(hits)) if hits else float("nan"),
        "median_directional_hit_rate": float(sorted(hits)[len(hits) // 2]) if hits else float("nan"),
        "mean_mae_ratio_sys_over_naive": float(sum(maes) / len(maes)) if maes else float("nan"),
        "median_mae_ratio_sys_over_naive": float(sorted(maes)[len(maes) // 2]) if maes else float("nan"),
        "note_ko": "hit_rate 는 final unseen best 행 기준; mae_ratio 는 1에 가까울수록 naive 대비 오차 유사.",
    }

    out = {
        "symbols": syms,
        "n_success": len(rows),
        "n_failed": len(errors),
        "failed": errors,
        "best_by_symbol": rows,
        "accuracy_summary": acc,
        "similar_pairs_top20": pairs[:20],
    }
    args.out_summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_summary_json.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        f"# Strict Multi-Cycle 요약 ({len(syms)}종목)",
        "",
        f"- success={len(rows)}, failed={len(errors)}",
        f"- symbols={','.join(syms)}",
        "",
        "## 집계 정확도·오차 (finite만)",
        "",
        f"- n_finite_hit: {acc['n_symbols_finite_hit']}, mean_hit: "
        f"{acc['mean_directional_hit_rate'] if hits else float('nan'):.4f}, median_hit: "
        f"{acc['median_directional_hit_rate'] if hits else float('nan'):.4f}",
        f"- n_finite_mae_ratio: {acc['n_symbols_finite_mae_ratio']}, mean_mae_ratio: "
        f"{acc['mean_mae_ratio_sys_over_naive'] if maes else float('nan'):.4f}, median_mae_ratio: "
        f"{acc['median_mae_ratio_sys_over_naive'] if maes else float('nan'):.4f}",
        "",
        "## 종목별 best 공식",
        "",
        "| symbol | hit_rate | mae_ratio | coverage | mean_rr | sharpe_ann | calmar | comp_raw | rank_score | cluster_key |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        h = r.get("hit_rate")
        m = r.get("mae_ratio")
        c = r.get("coverage")
        rr = r.get("mean_rr")
        sp = r.get("sharpe_annualized")
        cp = r.get("calmar_proxy")
        scr = r.get("composite_score")
        srk = r.get("composite_rank_score")

        def _cell(x: Any) -> str:
            if x is None:
                return "n/a"
            try:
                v = float(x)
            except (TypeError, ValueError):
                return "n/a"
            if v != v:  # NaN
                return "n/a"
            return f"{v:.4f}"

        md.append(
            f"| {r['symbol']} | {_cell(h)} | {_cell(m)} | {_cell(c)} | {_cell(rr)} | "
            f"{_cell(sp)} | {_cell(cp)} | {_cell(scr)} | {_cell(srk)} | `{r.get('cluster_key')}` |"
        )
    if errors:
        md += ["", "## 실패 종목", ""]
        for k, v in sorted(errors.items()):
            md.append(f"- `{k}`: {v}")
    md += [
        "",
        "## 심볼쌍 연구 (공식 유사도 상위 20)",
        "",
        "| pair | formula_similarity | hit_gap_abs | mae_ratio_gap_abs |",
        "|---|---:|---:|---:|",
    ]
    for pz in pairs[:20]:
        md.append(
            f"| `{pz['pair']}` | {float(pz['formula_similarity']):.4f} | "
            f"{float(pz['hit_gap_abs']):.4f} | {float(pz['mae_ratio_gap_abs']):.4f} |"
        )
    args.out_summary_md.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("wrote", args.out_summary_json.resolve())
    print("wrote", args.out_summary_md.resolve())
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

