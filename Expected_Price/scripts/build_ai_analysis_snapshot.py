#!/usr/bin/env python3
"""4단계: 갭 full·OOS·WF CSV + provenance → `data/runs/ai_analysis_snapshot.json` (+ LLM용 짧은 프롬프트 스텁).

  python scripts/build_ai_analysis_snapshot.py
  python scripts/build_ai_analysis_snapshot.py --last-n 96
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import ai_analysis_snapshot as aas  # noqa: E402

_DEFAULTS = {
    "full": ROOT / "data" / "runs" / "btc_4p_gap_backtest.csv",
    "oos": ROOT / "data" / "runs" / "btc_4p_gap_oos.csv",
    "wf": ROOT / "data" / "runs" / "btc_4p_gap_wf.csv",
    "full_prov": ROOT / "data" / "runs" / "btc_4p_gap_provenance.json",
    "oos_prov": ROOT / "data" / "runs" / "btc_4p_gap_oos_provenance.json",
    "wf_prov": ROOT / "data" / "runs" / "btc_4p_gap_wf_provenance.json",
    "registry": ROOT / "schemas" / "predictor_registry.btc_4p.json",
    "out_json": ROOT / "data" / "runs" / "ai_analysis_snapshot.json",
    "out_prompt": ROOT / "data" / "runs" / "ai_analysis_llm_prompt_stub.txt",
}


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--full-csv", type=Path, default=_DEFAULTS["full"])
    p.add_argument("--oos-csv", type=Path, default=_DEFAULTS["oos"])
    p.add_argument("--wf-csv", type=Path, default=_DEFAULTS["wf"])
    p.add_argument("--full-prov", type=Path, default=_DEFAULTS["full_prov"])
    p.add_argument("--oos-prov", type=Path, default=_DEFAULTS["oos_prov"])
    p.add_argument("--wf-prov", type=Path, default=_DEFAULTS["wf_prov"])
    p.add_argument("--registry", type=Path, default=_DEFAULTS["registry"])
    p.add_argument("--out-json", type=Path, default=_DEFAULTS["out_json"])
    p.add_argument("--out-prompt", type=Path, default=_DEFAULTS["out_prompt"])
    p.add_argument("--last-n", type=int, default=48, help="tail_rows·tail 집계 봉 수")
    p.add_argument(
        "--no-predictor-prices",
        action="store_true",
        help="predictor_prices 문자열 열 제외(용량)",
    )
    return p.parse_args(argv)


def _prompt_stub_ko() -> str:
    return """[역할] 당신은 **관측 요약**만 한다. 매수·매도·수익률 **권고 금지**.

[입력] JSON `ai_analysis_snapshot` — 수평 **예측가(앵커)** 들의 상대 **간격(mean_pairwise_*)**,
시스템가·현재가 괴리(gap_system_to_now_rel), OOS·WF provenance. 이는 **인과 실험 아님**.

[과제] 1) last_bar / tail_rows 로 **최근 국면**을 3~5문장 한국어로.
2) OOS·WF 요약이 있으면 **과적합·구간 민감**을 한 문장으로.
3) 불확실성·한계(샘플 짧음, 데모 앵커) 명시.
"""


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    full = aas.load_gap_csv(args.full_csv)
    oos = aas.load_gap_csv(args.oos_csv) if args.oos_csv.is_file() else None
    wf = aas.load_gap_csv(args.wf_csv) if args.wf_csv.is_file() else None

    cfg = aas.AnalysisSnapshotConfig(
        last_n_bars=args.last_n,
        include_predictor_prices_str=not args.no_predictor_prices,
    )
    d = aas.build_snapshot_dict(
        full=full,
        cfg=cfg,
        oos=oos,
        wf=wf,
        full_prov=args.full_prov,
        oos_prov=args.oos_prov,
        wf_prov=args.wf_prov,
        registry_path=args.registry,
    )
    aas.write_snapshot_dict(args.out_json, d)
    args.out_prompt.write_text(
        _prompt_stub_ko(),
        encoding="utf-8",
    )
    print("== written:", args.out_json.resolve(), flush=True)
    print("== prompt:", args.out_prompt.resolve(), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
