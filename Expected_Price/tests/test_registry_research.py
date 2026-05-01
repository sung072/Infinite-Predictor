import importlib
import sys
import unittest
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

rr = importlib.import_module("run_registry_research")
run_from_registry = rr.run_from_registry
EXAMPLE = _PKG / "schemas" / "predictor_registry.example.json"
SAMPLE_CSV = _PKG / "data" / "sample_ohlcv.csv"


class TestRegistryGap(unittest.TestCase):
    def test_synthetic(self) -> None:
        out, prov, ids, _reg = run_from_registry(EXAMPLE, n_synthetic_bars=6, seed=1)
        self.assertEqual({*ids}, {"eth_beta_pair_1d", "war_news_fwd_4h"})
        self.assertIn("config_sha256", prov)
        self.assertEqual(len(out), 6)
        self.assertIn("mean_pairwise_rel", out.columns)
        self.assertIn("gpr_cohort_inter_rel", out.columns)
        self.assertFalse(out["gpr_cohort_inter_rel"].isna().all())
        self.assertTrue(out["gpr_cohort_intra_rel"].isna().all())

    def test_csv_ohlcv(self) -> None:
        from vbt_gap_research import load_ohlcv_csv

        ohlc = load_ohlcv_csv(SAMPLE_CSV)
        out, prov, ids, _reg = run_from_registry(
            EXAMPLE, ohlcv=ohlc, n_synthetic_bars=0, seed=0
        )
        self.assertEqual(len(out), len(ohlc))
        self.assertIn("experiment_fingerprint", prov)

    def test_gap_pairwise_from_registry(self) -> None:
        out, _prov, ids, _reg = run_from_registry(
            EXAMPLE, n_synthetic_bars=8, seed=0, include_pairwise_columns=True
        )
        a, b = sorted(ids)[:2]
        col = f"gpr__{a}__{b}"
        self.assertIn(col, out.columns)
