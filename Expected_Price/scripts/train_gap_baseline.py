#!/usr/bin/env python3
"""4단계(베이스라인): Ridge+스케일 on 갭 CSV → `data/runs/gap_baseline_artifact.json` + .joblib.

  python scripts/train_gap_baseline.py
  python scripts/train_gap_baseline.py --gap-csv data/runs/btc_4p_gap_backtest.csv
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import joblib

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import gap_baseline_train as gbt  # noqa: E402

_DEFAULT = ROOT / "data" / "runs" / "btc_4p_gap_backtest.csv"
_OUT = ROOT / "data" / "runs" / "gap_baseline_artifact.json"
_MODEL = ROOT / "data" / "runs" / "gap_baseline_model.joblib"


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--gap-csv", type=Path, default=_DEFAULT)
    p.add_argument("--out-json", type=Path, default=_OUT)
    p.add_argument("--out-model", type=Path, default=_MODEL)
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    a = _parse_args(argv)
    if not a.gap_csv.is_file():
        print("run gap_backtest first; missing", a.gap_csv, file=sys.stderr)
        return 1
    d = gbt.train_baseline(a.gap_csv)
    m = d.pop("model")
    a.out_model.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(m, a.out_model, compress=3)
    w = {k: v for k, v in d.items() if k != "model"}
    w["model_path"] = str(a.out_model.resolve())
    a.out_json.write_text(
        json.dumps(w, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("wrote:", a.out_json.resolve(), "r2:", w.get("r2_oos_holdout"), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
