import importlib
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

sps = importlib.import_module("system_price_skill")


class TestSystemPriceSkill(unittest.TestCase):
    def test_perfect_direction(self) -> None:
        # 최소 표본(코드에서 n>=5) 만족
        m = pd.DataFrame(
            {
                "p_system": [102.0, 98.0, 101.0, 99.0, 100.5],
                "P_now": [100.0] * 5,
                "close_ohlc": [100.0] * 5,
                "fwd_1": [0.02, -0.02, 0.01, -0.01, 0.005],
            }
        )
        o = sps.compute_system_price_skill(m)
        self.assertGreaterEqual(o["n_used"], 5)
        self.assertAlmostEqual(o["directional_hit_rate"], 1.0)

    def test_mae_ratio(self) -> None:
        # 다음 종가 = 110: 시스템가 109 가 현재가 100 보다 110에 가깝게
        m = pd.DataFrame(
            {
                "p_system": [109.0] * 5,
                "P_now": [100.0] * 5,
                "close_ohlc": [100.0] * 5,
                "fwd_1": [0.1] * 5,
            }
        )
        o = sps.compute_system_price_skill(m)
        self.assertLess(o["mae_sys_next_close"], o["mae_naive_now_next_close"])

    def test_mae_ratio_p90_key(self) -> None:
        m = pd.DataFrame(
            {
                "p_system": [109.0] * 5,
                "P_now": [100.0] * 5,
                "close_ohlc": [100.0] * 5,
                "fwd_1": [0.1] * 5,
            }
        )
        o = sps.compute_system_price_skill(m)
        self.assertIn("mae_ratio_sys_over_naive_p90", o)
        self.assertTrue(np.isfinite(o["mae_ratio_sys_over_naive_p90"]))


if __name__ == "__main__":
    unittest.main()
