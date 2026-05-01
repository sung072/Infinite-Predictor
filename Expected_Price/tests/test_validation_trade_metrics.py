import importlib
import math
import sys
import unittest
from pathlib import Path

import pandas as pd

_PKG = Path(__file__).resolve().parent.parent
for _p in (_PKG / "code", _PKG / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

vtm = importlib.import_module("validation_trade_metrics")
gfr = importlib.import_module("gap_forward_return_research")


class TestValidationTradeMetrics(unittest.TestCase):
    def test_empty_validation_frame(self) -> None:
        m = pd.DataFrame(columns=["P_now", "fwd_1", "p_system"])
        out = vtm.compute_trade_metrics(m, system_col="p_system", shrink_weight=0.96)
        self.assertEqual(out["n_trade_rows"], 0)
        self.assertTrue(math.isnan(float(out["mean_rr"])))

    def test_mean_rr_wins_and_losses(self) -> None:
        # ps > pw -> long; fwd_1 > 0 wins, < 0 losses
        m = pd.DataFrame(
            {
                "P_now": [100.0] * 6,
                "p_system": [101.0] * 6,
                "fwd_1": [0.02, 0.02, 0.02, -0.01, -0.01, -0.01],
            }
        )
        out = vtm.compute_trade_metrics(m, system_col="p_system", shrink_weight=0.96)
        self.assertEqual(out["n_trade_rows"], 6)
        self.assertAlmostEqual(float(out["mean_rr"]), 2.0, places=6)
        self.assertFalse(math.isnan(float(out["sharpe_per_bar"])))
        self.assertFalse(math.isnan(float(out["sharpe_annualized"])))
        self.assertGreater(float(out["sharpe_annualized"]), float(out["sharpe_per_bar"]))

    def test_regime_quintile_table_short(self) -> None:
        m = pd.DataFrame(
            {
                "P_now": [1.0] * 8,
                "p_system": [1.01] * 8,
                "fwd_1": [0.001] * 8,
                "mean_pairwise_per_atr": list(range(8)),
            }
        )
        t = vtm.regime_quintile_table(
            m,
            "mean_pairwise_per_atr",
            system_col="p_system",
            shrink_weight=0.96,
            gfr=gfr,
        )
        self.assertEqual(t, [])

    def test_regime_tail_band_table_short(self) -> None:
        m = pd.DataFrame(
            {
                "P_now": [1.0] * 8,
                "p_system": [1.01] * 8,
                "fwd_1": [0.001] * 8,
                "mean_pairwise_per_atr": list(range(8)),
            }
        )
        t = vtm.regime_tail_band_table(
            m,
            "mean_pairwise_per_atr",
            system_col="p_system",
            shrink_weight=0.96,
            gfr=gfr,
        )
        self.assertEqual(t, [])


if __name__ == "__main__":
    unittest.main()
