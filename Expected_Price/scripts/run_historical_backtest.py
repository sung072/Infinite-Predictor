#!/usr/bin/env python3
"""
역사적 OHLCV CSV + Registry → gap 연구 (OOS 또는 워크포워드).
合성/전구간 `full` 이 아닌, train·embargo·test(롤) 로 시간 축을 나눈 실행.

실행: 프로젝트 루트(Expected_Price)에서
  python scripts/run_historical_backtest.py --mode wf --fetch
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--mode",
        choices=("wf", "oos"),
        default="wf",
        help="wf=롤링 walk-forward(여러 OOS test 창), oos=한 번의 hold-out",
    )
    p.add_argument(
        "--csv",
        type=Path,
        default=ROOT / "data" / "btcusdt_1h_30d.csv",
        help="OHLCV CSV (load_ohlcv_csv 호환)",
    )
    p.add_argument(
        "--registry",
        type=Path,
        default=ROOT / "schemas" / "predictor_registry.example.json",
    )
    p.add_argument(
        "--fetch",
        action="store_true",
        help="CSV가 없을 때 Binance 퍼블릭 API로 1h×720봉 저장 후 진행",
    )
    p.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "data" / "runs",
    )
    p.add_argument(
        "--btc-4p",
        action="store_true",
        help="BTC 4-예측가 데모: registry=predictor_registry.btc_4p + factors=derived/btc_factors_4p, gap-pairwise+system-variants",
    )
    p.add_argument(
        "--factors-csv",
        type=Path,
        default=None,
        help="절대가 factors CSV (없고 --btc-4p면 자동)",
    )
    p.add_argument(
        "--gap-pairwise",
        action="store_true",
        help="gpr__*__* 쌍 열 포함",
    )
    p.add_argument(
        "--system-variants",
        action="store_true",
        help="p_system_tension 등 시스템 변형 열",
    )
    p.add_argument(
        "--train-frac",
        type=float,
        default=0.72,
        help="(oos) train 비율",
    )
    p.add_argument(
        "--embargo",
        type=int,
        default=24,
        help="(oos/wf) train과 test 사이에 버릴 봉 수",
    )
    p.add_argument(
        "--wf-train",
        type=int,
        default=240,
        dest="wf_train",
        help="(wf) train 봉 수",
    )
    p.add_argument(
        "--wf-test",
        type=int,
        default=48,
        dest="wf_test",
        help="(wf) 각 fold의 OOS test 봉 수",
    )
    p.add_argument(
        "--wf-step",
        type=int,
        default=None,
        dest="wf_step",
        help="(wf) step (기본=wf_test)",
    )
    args = p.parse_args(argv)

    if args.btc_4p:
        args.registry = ROOT / "schemas" / "predictor_registry.btc_4p.json"
        if args.factors_csv is None:
            args.factors_csv = ROOT / "data" / "derived" / "btc_factors_4p.csv"
        args.gap_pairwise = True
        args.system_variants = True

    csvp = args.csv if args.csv.is_absolute() else (ROOT / args.csv).resolve()
    regp = args.registry if args.registry.is_absolute() else (ROOT / args.registry).resolve()
    fcsv: Path | None
    if args.factors_csv is not None:
        fcsv = args.factors_csv if args.factors_csv.is_absolute() else (ROOT / args.factors_csv).resolve()
    else:
        fcsv = None
    if not csvp.is_file():
        if not args.fetch:
            print("CSV not found:", csvp, "— use --fetch or pass --csv", file=sys.stderr)
            return 1
        fetch = ROOT / "scripts" / "fetch_btc_ohlcv.py"
        if not fetch.is_file():
            print("missing", fetch, file=sys.stderr)
            return 1
        subprocess.check_call(
            [sys.executable, str(fetch), "--out", str(csvp)],
            cwd=ROOT,
        )
    if not regp.is_file():
        print("registry not found:", regp, file=sys.stderr)
        return 1

    outd = args.out_dir if args.out_dir.is_absolute() else (ROOT / args.out_dir).resolve()
    outd.mkdir(parents=True, exist_ok=True)

    snap = "hist-wf-btc-1h" if args.mode == "wf" else "hist-oos-btc-1h"
    py = str(ROOT / "code" / "run_registry_research.py")
    cmd = [
        sys.executable,
        py,
        "--csv-ohlcv",
        str(csvp),
        "--registry",
        str(regp),
        "--n-bars",
        "0",
        "--snapshot",
        snap,
        "--out-csv",
        str(outd / f"historical_{args.mode}_gap_metrics.csv"),
        "--out-prov-json",
        str(outd / f"historical_{args.mode}_provenance.json"),
    ]
    if fcsv is not None:
        if not fcsv.is_file() and args.btc_4p and (ROOT / "scripts" / "build_btc_factor_csv.py").is_file():
            subprocess.check_call(
                [sys.executable, str(ROOT / "scripts" / "build_btc_factor_csv.py")],
                cwd=ROOT,
            )
        if not fcsv.is_file():
            print("factors-csv not found:", fcsv, file=sys.stderr)
            return 1
        cmd += ["--factors-csv", str(fcsv)]
    if args.gap_pairwise:
        cmd.append("--gap-pairwise")
    if args.system_variants:
        cmd.append("--system-variants")
    if args.mode == "oos":
        cmd += [
            "--split",
            "oos",
            "--train-frac",
            str(args.train_frac),
            "--embargo",
            str(args.embargo),
        ]
    else:
        cmd += [
            "--split",
            "wf",
            "--wf-train",
            str(args.wf_train),
            "--wf-test",
            str(args.wf_test),
            "--embargo",
            str(args.embargo),
        ]
        if args.wf_step is not None:
            cmd += ["--wf-step", str(args.wf_step)]

    print("==", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode == 0:
        print("== wrote:", outd / f"historical_{args.mode}_*.csv|json", flush=True)
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
