"""scripts/gap_forward_return_research — 작은 단위 점검."""
from __future__ import annotations

import unittest

import pandas as pd

from scripts.gap_forward_return_research import (
    _signed_system_vs_now,
    add_features_and_forwards,
)


class TestGapForwardResearch(unittest.TestCase):
    def test_signed_system_vs_now(self) -> None:
        m = pd.DataFrame(
            {
                "p_system": [100.0, 90.0],
                "P_now": [100.0, 100.0],
                "scale_used": [10.0, 10.0],
            }
        )
        s = _signed_system_vs_now(m)
        self.assertAlmostEqual(s.iloc[0], 0.0)
        self.assertAlmostEqual(s.iloc[1], -1.0)

    def test_add_forward_1(self) -> None:
        m = pd.DataFrame(
            {
                "close_ohlc": [100.0, 110.0, 105.0],
                "p_system": [100.0, 100.0, 100.0],
                "P_now": [100.0, 100.0, 100.0],
                "scale_used": [10.0, 10.0, 10.0],
                "gap_system_to_now_rel": [0.0, 0.1, 0.1],
                "mean_pairwise_rel": [0.01, 0.02, 0.01],
            }
        )
        o = add_features_and_forwards(m)
        self.assertIn("fwd_1", o.columns)
        self.assertAlmostEqual(float(o["fwd_1"].iloc[0]), 0.1)
        self.assertTrue(pd.isna(o["fwd_1"].iloc[-1]))


if __name__ == "__main__":
    unittest.main()
