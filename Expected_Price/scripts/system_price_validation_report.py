#!/usr/bin/env python3
r"""시스템가 **맞았는지/틀렸는지**를 숫자로 요약 (연구용, 매매 권고 아님).

- 갭 CSV + OHLCV 정렬 후 **다음 봉 종가**와 비교
- 산출: 방향 적중률, 시스템가 MAE vs 현재가 MAE, Spearman(부호 있는 괴리 vs 선행수익)

다종목: 같은 스크립트로 `--gap-csv` / `--ohlcv` 만 바꿈 (예: ETH는 `fetch_btc_ohlcv.py --symbol ETHUSDT --out data/ethusdt_1h_30d.csv` 후 Registry·갭 러너).

  python scripts/system_price_validation_report.py
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import system_price_skill as sps  # noqa: E402


def _load_gfr():
    p = ROOT / "scripts" / "gap_forward_return_research.py"
    spec = importlib.util.spec_from_file_location("gap_forward_return_research", p)
    if spec is None or spec.loader is None:
        raise ImportError(p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv: list[str] | None = None) -> int:
    gfr = _load_gfr()
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--gap-csv",
        type=Path,
        default=ROOT / "data" / "runs" / "btc_4p_gap_backtest.csv",
    )
    p.add_argument(
        "--ohlcv",
        type=Path,
        default=ROOT / "data" / "btcusdt_1h_30d.csv",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=ROOT / "data" / "runs" / "system_price_validation_report.md",
    )
    args = p.parse_args(argv)

    gpath = args.gap_csv.resolve()
    opath = args.ohlcv.resolve()
    if not gpath.is_file():
        print("missing gap csv:", gpath, file=sys.stderr)
        return 1
    if not opath.is_file():
        print("missing ohlcv:", opath, file=sys.stderr)
        return 1

    gap = gfr._read_gap_csv(gpath)
    raw = gfr._read_ohlcv(opath)
    m0 = gfr._align(raw, gap)
    m0 = gfr.add_features_and_forwards(m0, anchor_id=None)

    sk = sps.compute_system_price_skill(m0)
    sp = gfr._spearman(m0["signed_sys_vs_now_rel"], m0["fwd_1"])

    sym = opath.stem.replace("_", " ").upper()
    lines = [
        "# 시스템가 검증 리포트 (연구용)",
        "",
        f"- **갭 CSV:** `{gpath.relative_to(ROOT)}`",
        f"- **OHLCV:** `{opath.relative_to(ROOT)}`",
        f"- **표본 봉:** {sk['n_used']} (정렬·NaN 제거 후)",
        "",
        "## 시스템가 vs 다음 봉 종가",
        "",
        "| 지표 | 값 | 해석(비유) |",
        "|------|-----|------------|",
        f"| 방향 적중률 | **{sk['directional_hit_rate']:.4f}** | 시스템가가 현재가 **위/아래** 중 어디에 있었는지와, 다음 종가가 현재가 대비 **같은 쪽**으로 움직인 비율(무작위면 ~0.5 근처일 수 있음) |",
        f"| MAE\\|시스템가−다음종가\\| | **{sk['mae_sys_next_close']:.4f}** USDT | 시스템가가 **실제 다음 종가**에 얼마나 가까웠는지 평균 절대 오차 |",
        f"| MAE\\|현재가−다음종가\\| (단순) | **{sk['mae_naive_now_next_close']:.4f}** USDT | 비교 기준: ‘그냥 현재가만 본다’면 다음 종가까지 평균 오차 |",
        f"| 비율 (시스템/단순) | **{sk['mae_ratio_sys_over_naive']:.4f}** | **1 미만**이면 시스템가가 다음 종가에 **평균적으로 더 근접**(레짐·표본에 민감) |",
        "",
        "## 선행 1봉 수익 vs 부호 있는 시스템–현재 괴리",
        "",
        f"- Spearman(`signed_sys_vs_now_rel`, `fwd_1`) = **{sp:+.4f}** (유한하지 않으면 nan)",
        "",
        "## 주의",
        "",
        "- 이 수치는 **과거 표본**에서의 요약이며, **미래 수익·매매 적합성을 보장하지 않음**.",
        "- 퍼짐·갭·시스템가 정의가 바뀌면 결과도 바뀜. **OOS/WF** 구간에서 따로 돌려 보는 것을 권장.",
        "",
    ]
    outp = args.out.resolve()
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text("\n".join(lines), encoding="utf-8")
    print("== wrote:", outp, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
