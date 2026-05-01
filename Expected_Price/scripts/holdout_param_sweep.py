#!/usr/bin/env python3
r"""BTC/SOL(기본) 홀드아웃: shrink × embargo 그리드 스윕 → CSV + Markdown.

예:
  python scripts/holdout_param_sweep.py --symbols BTC,SOL
  python scripts/holdout_param_sweep.py --symbols BTC --shrinks 0.94,0.95,0.96,0.97 --embargos 12,24,48
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
_SCRIPTS = ROOT / "scripts"
for _p in (_CODE, _SCRIPTS):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import vbt_gap_research as vg  # noqa: E402
from temporal_validation import run_holdout_validation  # noqa: E402

SYMBOL_FILES: dict[str, tuple[str, str]] = {
    "BTC": ("data/btcusdt_1h_30d.csv", "data/derived/btcusdt_factors_4p.csv"),
    "ETH": ("data/ethusdt_1h_30d.csv", "data/derived/ethusdt_factors_4p.csv"),
    "SOL": ("data/solusdt_1h_30d.csv", "data/derived/solusdt_factors_4p.csv"),
}


def _parse_floats(raw: str) -> list[float]:
    out: list[float] = []
    for x in raw.split(","):
        x = x.strip()
        if x:
            out.append(float(x))
    return out


def _parse_ints(raw: str) -> list[int]:
    out: list[int] = []
    for x in raw.split(","):
        x = x.strip()
        if x:
            out.append(int(x))
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--symbols", default="BTC,SOL", help="콤마 구분: BTC, SOL, ETH …")
    p.add_argument(
        "--registry",
        type=Path,
        default=ROOT / "schemas" / "predictor_registry.btc_4p.json",
    )
    p.add_argument("--train-bars", type=int, default=500)
    p.add_argument("--val-bars", type=int, default=120)
    p.add_argument("--embargos", default="12,24,48", help="콤마 구분 embargo 봉 수")
    p.add_argument("--shrinks", default="0.94,0.95,0.96,0.97", help="콤마 구분 shrink")
    p.add_argument("--system-col", default="p_system_shrunk_custom")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument(
        "--out-csv",
        type=Path,
        default=ROOT / "data" / "runs" / "holdout_sweep_btc_sol.csv",
    )
    p.add_argument(
        "--out-md",
        type=Path,
        default=ROOT / "data" / "runs" / "holdout_sweep_btc_sol.md",
    )
    args = p.parse_args(argv)

    embargos = _parse_ints(args.embargos)
    shrinks = _parse_floats(args.shrinks)
    symbols = [x.strip().upper() for x in args.symbols.split(",") if x.strip()]

    rows: list[dict[str, object]] = []
    for sym in symbols:
        if sym not in SYMBOL_FILES:
            print("unknown symbol:", sym, "known:", list(SYMBOL_FILES.keys()), file=sys.stderr)
            return 2
        ohl_rel, fac_rel = SYMBOL_FILES[sym]
        ohl_path = ROOT / ohl_rel
        fac_path = ROOT / fac_rel
        if not ohl_path.is_file():
            print("missing", ohl_path, file=sys.stderr)
            return 2
        if not fac_path.is_file():
            print("missing", fac_path, file=sys.stderr)
            return 2

        ohl = vg.load_ohlcv_csv(ohl_path)
        n_need = args.train_bars + max(embargos) + args.val_bars
        if len(ohl) < n_need:
            print(
                f"{sym}: need {n_need} bars, have {len(ohl)} — 줄이거나 데이터를 늘리세요.",
                file=sys.stderr,
            )
            return 2

        for emb in embargos:
            for shrink in shrinks:
                ho = run_holdout_validation(
                    args.registry,
                    ohl,
                    n_train_bars=args.train_bars,
                    n_embargo_bars=emb,
                    n_val_bars=args.val_bars,
                    seed=args.seed,
                    factors_path=fac_path,
                    include_pairwise_columns=True,
                    include_system_variants=True,
                    system_col=args.system_col,
                    shrink_weight=float(shrink),
                )
                m = ho["metrics_validation"]
                rows.append(
                    {
                        "symbol": sym,
                        "embargo_bars": emb,
                        "shrink_weight": shrink,
                        "train_bars": args.train_bars,
                        "val_bars": args.val_bars,
                        "n_used": m.get("n_used"),
                        "directional_hit_rate": m.get("directional_hit_rate"),
                        "mae_ratio_sys_over_naive": m.get("mae_ratio_sys_over_naive"),
                        "spearman_signed_sys_vs_fwd1": m.get(
                            "spearman_signed_sys_vs_fwd1"
                        ),
                    }
                )
                print(
                    sym,
                    "emb",
                    emb,
                    "shrink",
                    shrink,
                    "hit",
                    m.get("directional_hit_rate"),
                    "mae_ratio",
                    m.get("mae_ratio_sys_over_naive"),
                    flush=True,
                )

    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        keys = list(rows[0].keys())
        with args.out_csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(rows)
        print("wrote", args.out_csv.resolve())

    md_lines = [
        "# 홀드아웃 파라미터 스윕 (BTC/SOL 등)",
        "",
        f"- train_bars={args.train_bars}, val_bars={args.val_bars}",
        f"- embargos={embargos}",
        f"- shrinks={shrinks}",
        f"- system_col=`{args.system_col}`",
        "",
        "| symbol | embargo | shrink | n_used | hit_rate | mae_ratio | spearman |",
        "|--------|---------|--------|--------|----------|-----------|----------|",
    ]
    for r in rows:
        hr = r["directional_hit_rate"]
        mr = r["mae_ratio_sys_over_naive"]
        sp = r["spearman_signed_sys_vs_fwd1"]
        md_lines.append(
            f"| {r['symbol']} | {r['embargo_bars']} | {r['shrink_weight']} | "
            f"{r['n_used']} | "
            f"{hr if hr == hr else 'n/a'} | "
            f"{mr if mr == mr else 'n/a'} | "
            f"{sp if sp == sp else 'n/a'} |"
        )
    md_lines.append("")
    md_lines.append(
        "해석: `mae_ratio_sys_over_naive` < 1 이면 다음 종가까지 naive(`P_now`)보다 시스템가 오차가 작음."
    )
    args.out_md.write_text("\n".join(md_lines), encoding="utf-8")
    print("wrote", args.out_md.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
