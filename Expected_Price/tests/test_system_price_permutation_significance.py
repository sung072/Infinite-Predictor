import importlib.util
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "system_price_permutation_significance.py"
spec = importlib.util.spec_from_file_location("spps", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load system_price_permutation_significance.py")
spps = importlib.util.module_from_spec(spec)
sys.modules["spps"] = spps
spec.loader.exec_module(spps)


class TestSystemPricePermutationSignificance(unittest.TestCase):
    def test_perm_test_output_keys(self) -> None:
        n = 40
        m = pd.DataFrame(
            {
                "p_system": np.linspace(101, 102, n),
                "P_now": np.linspace(100, 101, n),
                "close_ohlc": np.linspace(100, 101, n),
                "fwd_1": np.full(n, 0.001),
                "scale_used": np.full(n, 1.0),
            }
        )
        out = spps._perm_test_one(
            m,
            system_col="p_system",
            shrink_weight=0.96,
            n_perm=20,
            seed=1,
        )
        self.assertIn("p_joint", out)
        self.assertIn("obs_ratio", out)


if __name__ == "__main__":
    unittest.main()
