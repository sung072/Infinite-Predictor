import importlib
import sys
import unittest
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

wfo = importlib.import_module("walkforward_oos")
vg = importlib.import_module("vbt_gap_research")
tv = importlib.import_module("temporal_validation")

EXAMPLE = _PKG / "schemas" / "predictor_registry.example.json"


class TestTemporalValidation(unittest.TestCase):
    def test_holdout_split_by_bars(self) -> None:
        s = wfo.holdout_split_by_bars(100, n_train=40, n_embargo=5, n_val=20)
        self.assertEqual(s.n_window, 65)
        self.assertEqual(s.val_slice.start, 45)
        self.assertEqual(s.val_slice.stop, 65)

    def test_holdout_split_by_bars_raises(self) -> None:
        with self.assertRaises(ValueError):
            wfo.holdout_split_by_bars(10, n_train=5, n_embargo=2, n_val=10)

    def test_holdout_candle_alignment_summary(self) -> None:
        ohl = vg.synthetic_ohlcv_bars(80, seed=0)
        sp = wfo.holdout_split_by_bars(80, n_train=30, n_embargo=2, n_val=20)
        sm = wfo.holdout_candle_alignment_summary(ohl, sp)
        self.assertTrue(sm["same_bar_grid_as_backtest"])
        self.assertEqual(sm["n_validation_bars"], 20)
        self.assertEqual(sm["validation"]["n_bars"], 20)

    def test_run_holdout_validation_smoke(self) -> None:
        ohl = vg.synthetic_ohlcv_bars(120, seed=3)
        out = tv.run_holdout_validation(
            EXAMPLE,
            ohl,
            n_train_bars=50,
            n_embargo_bars=4,
            n_val_bars=24,
            seed=3,
            include_system_variants=True,
            system_col="p_system",
            shrink_weight=1.0,
        )
        self.assertIn("metrics_validation", out)
        self.assertIn("directional_hit_rate", out["metrics_validation"])
        self.assertEqual(len(out["validation_gap_df"]), 24)
        self.assertEqual(len(out["full_gap_df"]), 50 + 4 + 24)
        self.assertIn("candle_alignment", out["provenance"]["temporal_holdout"])
        self.assertIn("accuracy_summary_ko", out)
        self.assertIn("방향 적중률", out["accuracy_summary_ko"])

    def test_format_system_price_accuracy_ko(self) -> None:
        txt = tv.format_system_price_accuracy_ko(
            {
                "n_used": 100,
                "directional_hit_rate": 0.55,
                "mae_ratio_sys_over_naive": 0.92,
                "spearman_signed_sys_vs_fwd1": 0.1,
                "system_col": "p_system",
            }
        )
        self.assertIn("0.5500", txt)
        self.assertIn("0.9200", txt)


if __name__ == "__main__":
    unittest.main()
