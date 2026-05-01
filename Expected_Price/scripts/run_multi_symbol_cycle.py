#!/usr/bin/env python3
r"""여러 종목 연구+검증+AI보조 사이클(실거래 제외).

각 심볼에 대해:
1) OHLCV fetch
2) factor CSV 생성
3) gap backtest full/oos/wf 생성
4) 통합 검증 매트릭스(+AI보조) 리포트 생성
5) 퍼뮤테이션 유의성(OOS/WF, 라벨 셔플 p-value)

예시:
  python scripts/run_multi_symbol_cycle.py
  python scripts/run_multi_symbol_cycle.py --symbols BTCUSDT,ETHUSDT,SOLUSDT
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _run(cmd: list[str]) -> None:
    print("==", " ".join(cmd), flush=True)
    subprocess.check_call(cmd, cwd=ROOT)


def _parse_symbols(raw: str) -> list[str]:
    out: list[str] = []
    for x in raw.split(","):
        s = x.strip().upper()
        if not s:
            continue
        out.append(s)
    if not out:
        raise ValueError("empty --symbols")
    return out


def _sym_slug(sym: str) -> str:
    return sym.lower()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--symbols",
        default="BTCUSDT,ETHUSDT",
        help="콤마 구분 심볼 목록 (예: BTCUSDT,ETHUSDT,SOLUSDT)",
    )
    p.add_argument("--interval", default="1h")
    p.add_argument("--limit", type=int, default=720)
    p.add_argument("--train-frac", type=float, default=0.72)
    p.add_argument("--embargo", type=int, default=24)
    p.add_argument("--wf-train", type=int, default=240)
    p.add_argument("--wf-test", type=int, default=48)
    p.add_argument("--wf-step", type=int, default=None)
    p.add_argument(
        "--validation-out",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_validation_matrix_multi.md",
    )
    p.add_argument(
        "--validation-ai-no-llm",
        action="store_true",
        help="검증 AI보조에서 LLM 호출 없이 규칙 추천만",
    )
    p.add_argument(
        "--skip-permutation",
        action="store_true",
        help="5단계 퍼뮤테이션 유의성 리포트 생략",
    )
    p.add_argument(
        "--permutation-out",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_permutation_significance.md",
    )
    p.add_argument(
        "--permutation-out-json",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_permutation_significance.json",
    )
    p.add_argument("--n-perm", type=int, default=300, help="퍼뮤테이션 반복 수")
    p.add_argument("--perm-seed", type=int, default=42, help="퍼뮤테이션 RNG 시드")
    args = p.parse_args(argv)

    symbols = _parse_symbols(args.symbols)
    reg = ROOT / "schemas" / "predictor_registry.btc_4p.json"
    if not reg.is_file():
        print("missing registry:", reg, file=sys.stderr)
        return 1

    cases: list[str] = []
    symbol_weights: list[str] = []
    for sym in symbols:
        slug = _sym_slug(sym)
        prefix = sym.replace("USDT", "")

        ohl = ROOT / "data" / f"{slug}_1h_30d.csv"
        fcsv = ROOT / "data" / "derived" / f"{slug}_factors_4p.csv"
        out_full = ROOT / "data" / "runs" / f"{slug}_4p_gap_backtest.csv"
        out_oos = ROOT / "data" / "runs" / f"{slug}_4p_gap_oos.csv"
        out_wf = ROOT / "data" / "runs" / f"{slug}_4p_gap_wf.csv"
        prov_full = ROOT / "data" / "runs" / f"{slug}_4p_gap_provenance.json"
        prov_oos = ROOT / "data" / "runs" / f"{slug}_4p_gap_oos_provenance.json"
        prov_wf = ROOT / "data" / "runs" / f"{slug}_4p_gap_wf_provenance.json"

        _run(
            [
                sys.executable,
                str(ROOT / "scripts" / "fetch_btc_ohlcv.py"),
                "--symbol",
                sym,
                "--interval",
                args.interval,
                "--limit",
                str(args.limit),
                "--out",
                str(ohl),
            ]
        )
        _run(
            [
                sys.executable,
                str(ROOT / "scripts" / "build_btc_factor_csv.py"),
                "--ohlcv",
                str(ohl),
                "--out",
                str(fcsv),
            ]
        )

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
        ]

        _run(
            common
            + [
                "--snapshot",
                f"{slug}-4p-backtest-001",
                "--split",
                "full",
                "--out-csv",
                str(out_full),
                "--out-prov-json",
                str(prov_full),
            ]
        )
        _run(
            common
            + [
                "--snapshot",
                f"{slug}-4p-oos-001",
                "--split",
                "oos",
                "--train-frac",
                str(args.train_frac),
                "--embargo",
                str(args.embargo),
                "--out-csv",
                str(out_oos),
                "--out-prov-json",
                str(prov_oos),
            ]
        )
        wf_cmd = (
            common
            + [
                "--snapshot",
                f"{slug}-4p-wf-001",
                "--split",
                "wf",
                "--wf-train",
                str(args.wf_train),
                "--wf-test",
                str(args.wf_test),
                "--embargo",
                str(args.embargo),
                "--out-csv",
                str(out_wf),
                "--out-prov-json",
                str(prov_wf),
            ]
        )
        if args.wf_step is not None:
            wf_cmd += ["--wf-step", str(args.wf_step)]
        _run(wf_cmd)

        cases.extend(
            [
                f"{prefix}-full|{out_full.relative_to(ROOT)}|{ohl.relative_to(ROOT)}",
                f"{prefix}-oos|{out_oos.relative_to(ROOT)}|{ohl.relative_to(ROOT)}",
                f"{prefix}-wf|{out_wf.relative_to(ROOT)}|{ohl.relative_to(ROOT)}",
            ]
        )
        # 현재 연구 결과: 비 BTC는 0.99가 더 안정적
        symbol_weights.append(f"{prefix}=0.96" if prefix == "BTC" else f"{prefix}=0.99")

    vcmd = [
        sys.executable,
        str(ROOT / "scripts" / "system_price_validation_matrix.py"),
        "--strict-oos-wf-only",
        "--ai-judge",
        "--out",
        str(args.validation_out),
        "--symbol-shrink-weights",
        ",".join(symbol_weights),
    ]
    if args.validation_ai_no_llm:
        vcmd.append("--ai-no-llm")
    for c in cases:
        vcmd += ["--case", c]
    _run(vcmd)

    if not args.skip_permutation:
        perm_cases: list[str] = []
        for sym in symbols:
            slug = _sym_slug(sym)
            prefix = sym.replace("USDT", "")
            ohl = ROOT / "data" / f"{slug}_1h_30d.csv"
            out_oos = ROOT / "data" / "runs" / f"{slug}_4p_gap_oos.csv"
            out_wf = ROOT / "data" / "runs" / f"{slug}_4p_gap_wf.csv"
            perm_cases.append(
                f"{prefix}-oos|{out_oos.relative_to(ROOT)}|{ohl.relative_to(ROOT)}"
            )
            perm_cases.append(
                f"{prefix}-wf|{out_wf.relative_to(ROOT)}|{ohl.relative_to(ROOT)}"
            )
        pcmd = [
            sys.executable,
            str(ROOT / "scripts" / "system_price_permutation_significance.py"),
            "--n-perm",
            str(args.n_perm),
            "--seed",
            str(args.perm_seed),
            "--system-col",
            "p_system_shrunk_custom",
            "--shrink-weight",
            "0.96",
            "--symbol-shrink-weights",
            ",".join(symbol_weights),
            "--out",
            str(args.permutation_out),
            "--out-json",
            str(args.permutation_out_json),
        ]
        for c in perm_cases:
            pcmd += ["--case", c]
        _run(pcmd)

    print("== done multi-symbol cycle:", ",".join(symbols), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
