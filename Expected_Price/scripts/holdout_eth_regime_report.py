#!/usr/bin/env python3
r"""ETH 단일 홀드아웃 후 검증 구간을 갭·변동성 분위별로 나눠 스킬 비교(연구용).

예:
  python scripts/holdout_eth_regime_report.py --out-md data/runs/eth_regime_holdout.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
_SCRIPTS = ROOT / "scripts"
for _p in (_CODE, _SCRIPTS):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import gap_forward_return_research as gfr  # noqa: E402
import system_price_validation_matrix as spm  # noqa: E402
import vbt_gap_research as vg  # noqa: E402
from holdout_regime_analysis import format_quintile_markdown, quintile_skill_breakdown  # noqa: E402
from temporal_validation import run_holdout_validation  # noqa: E402

FEATURES_DEFAULT = "mean_pairwise_per_atr,atr_14,vbt_rolling_return_std"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--registry",
        type=Path,
        default=ROOT / "schemas" / "predictor_registry.btc_4p.json",
    )
    p.add_argument("--ohlcv", type=Path, default=ROOT / "data" / "ethusdt_1h_30d.csv")
    p.add_argument(
        "--factors-csv",
        type=Path,
        default=ROOT / "data" / "derived" / "ethusdt_factors_4p.csv",
    )
    p.add_argument("--train-bars", type=int, default=500)
    p.add_argument("--embargo", type=int, default=24)
    p.add_argument("--val-bars", type=int, default=120)
    p.add_argument("--shrink", type=float, default=0.96)
    p.add_argument("--system-col", default="p_system_shrunk_custom")
    p.add_argument("--features", default=FEATURES_DEFAULT, help="콤마 구분 검증 DF 열 이름")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument(
        "--out-md",
        type=Path,
        default=ROOT / "data" / "runs" / "eth_regime_holdout.md",
    )
    args = p.parse_args(argv)

    if not args.ohlcv.is_file():
        print("missing OHLCV:", args.ohlcv, file=sys.stderr)
        return 2
    if not args.factors_csv.is_file():
        print("missing factors:", args.factors_csv, file=sys.stderr)
        return 2

    ohl = vg.load_ohlcv_csv(args.ohlcv)
    need = args.train_bars + args.embargo + args.val_bars
    if len(ohl) < need:
        print(f"need {need} bars, have {len(ohl)}", file=sys.stderr)
        return 2

    ho = run_holdout_validation(
        args.registry,
        ohl,
        n_train_bars=args.train_bars,
        n_embargo_bars=args.embargo,
        n_val_bars=args.val_bars,
        seed=args.seed,
        factors_path=args.factors_csv,
        include_pairwise_columns=True,
        include_system_variants=True,
        system_col=args.system_col,
        shrink_weight=float(args.shrink),
    )
    m_val = ho["merged_validation_df"]
    base_m = ho["metrics_validation"]

    lines = [
        "# ETH 홀드아웃 · 검증 구간 분위별 분석",
        "",
        f"- OHLCV: `{args.ohlcv.relative_to(ROOT)}`",
        f"- train={args.train_bars}, embargo={args.embargo}, val={args.val_bars}",
        f"- shrink={args.shrink}, system_col=`{args.system_col}`",
        "",
        "## 전체 검증 구간(단일 지표)",
        "",
        "```json",
        __import__("json").dumps(base_m, ensure_ascii=False, indent=2),
        "```",
        "",
        ho.get("accuracy_summary_ko", ""),
        "",
        "---",
        "",
        "**해석:** 분위별로 hit_rate·mae_ratio가 들쭉날쭉하면 레인지/추세·갭 크기에 따라 시스템가 유효성이 달라짐을 시사.",
        "",
    ]

    feats = [x.strip() for x in args.features.split(",") if x.strip()]
    for feat in feats:
        if feat not in m_val.columns:
            lines.append(f"## 스킵: 열 없음 `{feat}`\n")
            continue
        rows = quintile_skill_breakdown(
            m_val,
            feat,
            gfr,
            spm,
            system_col=args.system_col,
            shrink_weight=float(args.shrink),
            q=5,
        )
        lines.append(
            format_quintile_markdown(
                rows,
                title=f"분위별 스킬 — `{feat}`",
                feature_col=feat,
            )
        )
        lines.append("")

    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text("\n".join(lines), encoding="utf-8")
    print("wrote", args.out_md.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
