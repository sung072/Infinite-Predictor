#!/usr/bin/env python3
"""
1) BTC OHLCV(없으면 fetch)  2) factor CSV 생성
3) Registry gap 백테스트: **full** + (기본) **OOS** + **워크포워드** — 쌍·시스템 열
4) `data/runs/gap_meaning_report.md` 한국어 요약 (섹션별)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

KEY_COLS = [
    "mean_pairwise_rel",
    "mean_pairwise_per_atr",
    "gap_system_to_now_rel",
    "range_rel",
    "variance_anchors",
    "gpr_cohort_inter_rel",
    "gpr_cohort_intra_rel",
    "p_system_tension",
]


def _run(cmd: list[str]) -> None:
    print("==", " ".join(cmd), flush=True)
    subprocess.check_call(cmd, cwd=ROOT)


def _md_escape(s: str) -> str:
    return s.replace("|", "\\|")


def _present_key_cols(df: pd.DataFrame) -> list[str]:
    return [c for c in KEY_COLS if c in df.columns]


def _section_stats_gpr(
    lines: list[str], heading: str, df: pd.DataFrame, *, subheading: str = ""
) -> None:
    lines.append(f"## {heading}")
    if subheading:
        lines += ["", subheading, ""]
    n = len(df)
    present = _present_key_cols(df)
    desc = df[present].describe(percentiles=[0.1, 0.5, 0.9]).T if present else None
    if desc is not None and not desc.empty:
        lines += [f"**봉 수:** {n}", ""]
        lines.append("```")
        lines.append(desc.to_string())
        lines.append("```")
        lines.append("")

    gpr_cols = [c for c in df.columns if c.startswith("gpr__")]
    if gpr_cols:
        sub = df[gpr_cols].agg(["mean", "std", "min", "max"])
        means = sub.loc["mean"].sort_values(ascending=False)
        lines += ["**쌍별 `gpr__*__*` (평균 큰 순, 상위 6)**", ""]
        for col in means.index[:6]:
            lines.append(f"- **{_md_escape(str(col))}** mean={means[col]:.4f}")
        lines.append("")


def _section_wf_folds(
    lines: list[str], df: pd.DataFrame, *, n_train: int, n_test: int, embargo: int
) -> None:
    lines += [
        "## 워크포워드 (각 fold = train 뒤 **test 구간**만 갭 시계열)",
        "",
        f"파라미터: `n_train`={n_train}, `n_test`={n_test}, `embargo`={embargo} (1h봉 기준).",
        "",
    ]
    if "fold" not in df.columns or df.empty:
        lines.append("*(fold 열 없음 또는 빈 DataFrame — WF 스킵)*", "")
        return
    present = _present_key_cols(df)
    if not present:
        lines.append("*(핵심 갭 열 없음)*", "")
        return
    g_mean = df.groupby("fold", sort=True)[present].mean()
    ncols = 1 + len(present)
    lines += [
        "| fold | " + " | ".join(present) + " |",
        "| " + " | ".join(["---"] * ncols) + " |",
    ]
    for fold_id, row in g_mean.iterrows():
        cells = [str(fold_id)] + [f"{row[c]:.6f}" for c in present]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append("```")
    lines.append(g_mean.to_string())
    lines.append("```")
    lines.append("")


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--skip-oos",
        action="store_true",
        help="홀드아웃 OOS split 생략 (full+WF만)",
    )
    p.add_argument(
        "--skip-wf",
        action="store_true",
        help="워크포워드 생략 (full+OOS만)",
    )
    p.add_argument("--train-frac", type=float, default=0.72, help="(OOS) train 비율")
    p.add_argument("--embargo", type=int, default=24, help="(OOS/WF) train~test 사이 봉 수")
    p.add_argument("--wf-train", type=int, default=240, help="(WF) train 봉 수")
    p.add_argument("--wf-test", type=int, default=48, help="(WF) 각 fold test 봉 수")
    p.add_argument(
        "--wf-step",
        type=int,
        default=None,
        help="(WF) step (기본=wf-test)",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    ohl = ROOT / "data" / "btcusdt_1h_30d.csv"
    fcsv = ROOT / "data" / "derived" / "btc_factors_4p.csv"
    reg = ROOT / "schemas" / "predictor_registry.btc_4p.json"
    out_dir = ROOT / "data" / "runs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "btc_4p_gap_backtest.csv"
    out_prov = out_dir / "btc_4p_gap_provenance.json"
    out_oos = out_dir / "btc_4p_gap_oos.csv"
    out_oos_prov = out_dir / "btc_4p_gap_oos_provenance.json"
    out_wf = out_dir / "btc_4p_gap_wf.csv"
    out_wf_prov = out_dir / "btc_4p_gap_wf_provenance.json"
    report = out_dir / "gap_meaning_report.md"

    if not ohl.is_file():
        print("== fetching OHLCV (Binance public API)", flush=True)
        _run([sys.executable, str(ROOT / "scripts" / "fetch_btc_ohlcv.py"), "--out", str(ohl)])
    if not fcsv.is_file() or ohl.stat().st_mtime > fcsv.stat().st_mtime:
        _run([sys.executable, str(ROOT / "scripts" / "build_btc_factor_csv.py")])
    if not reg.is_file():
        print("missing", reg, file=sys.stderr)
        return 1

    common = [
        sys.executable,
        str(ROOT / "code" / "run_registry_research.py"),
        "--csv-ohlcv",
        str(ohl),
        "--factors-csv",
        str(fcsv),
        "--registry",
        str(reg),
        "--n-bars",
        "0",
        "--gap-pairwise",
        "--system-variants",
        "--snapshot",
        "btc-4p-backtest-001",
    ]

    _run(
        common
        + [
            "--split",
            "full",
            "--out-csv",
            str(out_csv),
            "--out-prov-json",
            str(out_prov),
        ]
    )
    if not args.skip_oos:
        _run(
            common
            + [
                "--split",
                "oos",
                "--train-frac",
                str(args.train_frac),
                "--embargo",
                str(args.embargo),
                "--snapshot",
                "btc-4p-oos-001",
                "--out-csv",
                str(out_oos),
                "--out-prov-json",
                str(out_oos_prov),
            ]
        )
    if not args.skip_wf:
        wf_cmd = (
            common
            + [
                "--split",
                "wf",
                "--wf-train",
                str(args.wf_train),
                "--wf-test",
                str(args.wf_test),
                "--embargo",
                str(args.embargo),
                "--snapshot",
                "btc-4p-wf-001",
                "--out-csv",
                str(out_wf),
                "--out-prov-json",
                str(out_wf_prov),
            ]
        )
        if args.wf_step is not None:
            wf_cmd += ["--wf-step", str(args.wf_step)]
        _run(wf_cmd)

    df_full = pd.read_csv(out_csv, index_col=0, parse_dates=True)
    n_full = len(df_full)

    lines: list[str] = []
    lines += [
        "# Gap(간격) 백테스팅 요약 — BTC 1h × 4 예측가 (수평 앵커 간 거리)",
        "",
        "이 문서는 **자동 생성**됩니다. (`scripts/gap_backtest_and_analyze.py` — full + OOS + WF)",
        "",
        "## 데이터",
        f"- **OHLCV:** `{ohl.relative_to(ROOT)}` (Binance 1h, ~30일, 720봉 권장)",
        f"- **Registry:** `{reg.relative_to(ROOT)}` — 예측가: `btc_ema_fast`, `btc_ema_slow` (trend), `btc_resist_24h`, `btc_support_24h` (range)",
        f"- **Factors:** `{fcsv.relative_to(ROOT)}` — EMA(8,48) 절대가, 24봉 high/low 밴드",
        f"- **전 구간(full) 봉 수:** {n_full}",
        "",
        "## 간격이 의미하는 것 (이 프로젝트 기준)",
        "",
        "| 지표 | 의미 |",
        "|------|------|",
        "| `mean_pairwise_rel` | 각 바에서 4개 앵커 쌍에 대해 **(가격차/scale)의 평균**. 1이 ‘나쁨’이 아니라 **퍼짐(분산) 정도**(스케일 정규) |",
        "| `mean_pairwise_per_atr` | 위 쌍 **절대** 간격의 평균 ÷ `atr_14`. **변동성(캔들) 대비** 퍼짐—가격이 출렁일수록 ATR이 커져 **비교가 가능** |",
        "| `gap_system_to_now_rel` | `p_system`(기본: 앵커 산술평균) vs **현재가** — ‘합의한 중심’이 시장이 어디에 있는지와 괴리 |",
        "| `range_rel` | 앵커 min~max / scale — **한눈에** 가장 멀 떨어진 두 예측가 사이 폭 |",
        "| `gpr_cohort_inter_rel` / `gpr_cohort_intra_rel` | Registry `meta.anchor_cohort`가 trend vs range이면, **군(코호트) 간/내** 쌍의 상대 간격 평균 |",
        "| `gpr__A__B` | id A,B 쌍 **한 쌍씩** 상대간격(스케일) — **누가 누구에 붙는지** 추적 |",
        "| `p_system_tension` (옵션) | 시스템가·현재가·`mean_pairwise_rel` 블렌드 — **팽팽함** 연구용 |",
        "| `compression_mean_pairwise` | 직전 봉 대비 `mean_pairwise_rel` 비 — **&lt;1** 이면 구간이 좁혀짐(압축) |",
        "",
    ]

    _section_stats_gpr(
        lines,
        "전 구간 (full) — 항상 **과거 전체**에 대한 갭 시계열",
        df_full,
    )

    if not args.skip_oos:
        df_oos = pd.read_csv(out_oos, index_col=0, parse_dates=True)
        oos_sub = (
            f"**OOS 설정:** `train_frac`={args.train_frac}, `embargo`={args.embargo}봉 — **시간 끝 쪽** 홀드아웃에만 갭(미래로 치면 ‘검증 구간’)."
        )
        _section_stats_gpr(lines, "홀드아웃 OOS (끝 구간만)", df_oos, subheading=oos_sub)
    if not args.skip_wf:
        df_wf = pd.read_csv(out_wf, index_col=0, parse_dates=True)
        _section_wf_folds(
            lines,
            df_wf,
            n_train=args.wf_train,
            n_test=args.wf_test,
            embargo=args.embargo,
        )
        if not df_wf.empty and "fold" in df_wf.columns:
            _section_stats_gpr(
                lines,
                "워크포워드 전체 (모든 test 봉 합쳐서)",
                df_wf,
                subheading="아래는 fold에 관계없이 **OOS test 바만** 쌓은 분포(동일 봉이 여러 fold에 겹치지 않음).",
            )

    lines += [
        "## 읽는 법 (한 문장)",
        "**full**은 전기간 **스냅샷**이고, **OOS**는 ‘미알 끝’ 한 번만, **WF**는 시간을 **여러 창**으로 밀어가며 반복한 갭이다. "
        "세 결과를 **나란히** 보면, 수평 예측가 간 **퍼짐·코호트 간격**이 **한 구간에만** 특이한지 **꾸준한지** 구분할 수 있다.",
        "",
    ]

    report.write_text("\n".join(lines), encoding="utf-8")
    print("== report:", report.resolve(), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
