"""strict_multi_cycle_research: Gap/Tension 검증행 필터 헬퍼."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "strict_multi_cycle_research.py"
spec = importlib.util.spec_from_file_location("smcr_gap", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load strict_multi_cycle_research.py")
smcr = importlib.util.module_from_spec(spec)
sys.modules["smcr_gap"] = smcr
spec.loader.exec_module(smcr)


class TestStrictMultiCycleGapFilter(unittest.TestCase):
    def test_subset_inactive_when_no_bounds(self) -> None:
        df = pd.DataFrame({"mean_pairwise_per_atr": [1.0, 2.0], "x": [1, 2]})
        out, meta = smcr._subset_validation_by_gap_intensity(
            df, column="mean_pairwise_per_atr", vmin=None, vmax=None
        )
        self.assertFalse(meta.get("eval_gap_filter_active"))
        self.assertIs(out, df)

    def test_subset_min_keeps_rows(self) -> None:
        df = pd.DataFrame(
            {
                "mean_pairwise_per_atr": [0.1, 0.5, 1.0, 1.5, 2.0, 2.5],
                "P_now": [100.0] * 6,
            }
        )
        out, meta = smcr._subset_validation_by_gap_intensity(
            df, column="mean_pairwise_per_atr", vmin=0.5, vmax=None
        )
        self.assertTrue(meta.get("eval_gap_filter_active"))
        self.assertEqual(len(out), 5)
        self.assertAlmostEqual(float(meta["eval_gap_filter_coverage"]), 5.0 / 6.0)

    def test_subset_missing_column_no_crash(self) -> None:
        df = pd.DataFrame({"P_now": [1.0, 2.0]})
        out, meta = smcr._subset_validation_by_gap_intensity(
            df, column="mean_pairwise_per_atr", vmin=0.5, vmax=None
        )
        self.assertIn("missing_column", str(meta.get("eval_gap_filter_error", "")))
        self.assertFalse(meta.get("eval_gap_filter_active"))
        self.assertIs(out, df)

    def test_subset_too_few_returns_empty(self) -> None:
        df = pd.DataFrame({"mean_pairwise_per_atr": [10.0, 11.0, 12.0], "P_now": [1.0, 2.0, 3.0]})
        out, meta = smcr._subset_validation_by_gap_intensity(
            df, column="mean_pairwise_per_atr", vmin=100.0, vmax=None
        )
        self.assertTrue(meta.get("eval_gap_filter_too_few_rows"))
        self.assertEqual(len(out), 0)


if __name__ == "__main__":
    unittest.main()
