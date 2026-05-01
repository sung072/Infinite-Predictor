import importlib
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
_SCRIPTS = _PKG / "scripts"
for _p in (_CODE, _SCRIPTS):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

hre = importlib.import_module("holdout_regime_analysis")
import gap_forward_return_research as gfr  # noqa: E402
import system_price_validation_matrix as spm  # noqa: E402


class TestHoldoutRegimeAnalysis(unittest.TestCase):
    def test_quintile_skill_breakdown_smoke(self) -> None:
        n = 80
        rng = np.random.default_rng(0)
        m_val = pd.DataFrame(
            {
                "p_system": rng.uniform(100, 110, n),
                "P_now": rng.uniform(99, 109, n),
                "scale_used": np.full(n, 10.0),
                "close_ohlc": rng.uniform(98, 108, n),
                "fwd_1": rng.normal(0.0, 0.01, n),
                "mean_pairwise_per_atr": rng.uniform(0.1, 3.0, n),
            }
        )
        rows = hre.quintile_skill_breakdown(
            m_val,
            "mean_pairwise_per_atr",
            gfr,
            spm,
            system_col="p_system",
            shrink_weight=1.0,
            q=5,
        )
        self.assertTrue(len(rows) >= 1)


if __name__ == "__main__":
    unittest.main()
