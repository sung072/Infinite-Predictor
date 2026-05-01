import importlib
import sys
import unittest
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

rr = importlib.import_module("run_registry_research")
vg = importlib.import_module("vbt_gap_research")
EX = _PKG / "schemas" / "predictor_registry.example.json"


class TestPriceLikePipeline(unittest.TestCase):
    def test_fused_ids_include_vol_time(self) -> None:
        from predictor_registry import load_registry_file

        d = load_registry_file(EX)
        ids = rr.resolve_predictor_ids_fused(d, use_statuses=None, use_price_like=True)
        self.assertIn("vol_as_price_demo", ids)
        self.assertIn("time_as_price_demo", ids)
        self.assertIn("war_news_fwd_4h", ids)

    def test_run_from_registry_price_like(self) -> None:
        out, _prov, ids, _ = rr.run_from_registry(
            EX, n_synthetic_bars=12, seed=0, use_price_like=True
        )
        self.assertGreaterEqual(len(ids), 2)
        self.assertIn("mean_pairwise_rel", out.columns)
        self.assertTrue(len(out) == 12)
        self.assertIn("gpr_cohort_intra_rel", out.columns)
        self.assertTrue(out["gpr_cohort_intra_rel"].notna().any())

    def test_make_fn(self) -> None:
        ohlc = vg.synthetic_ohlcv_bars(8, seed=0)
        fn = vg.make_predictor_prices_fn_price_like(ohlc, ["vol_as_price_demo", "time_as_price_demo"])
        d0 = fn(0, float(ohlc["close"].iloc[0]))
        self.assertIn("vol_as_price_demo", d0)
        self.assertIn("time_as_price_demo", d0)
