import importlib
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

gbt = importlib.import_module("gap_baseline_train")


class TestGapBaselineTrain(unittest.TestCase):
    def test_train_synthetic(self) -> None:
        n = 50
        idx = pd.date_range("2020-01-01", periods=n, freq="h", tz="UTC")
        rng = np.random.default_rng(0)
        df = pd.DataFrame(
            {
                "mean_pairwise_rel": rng.random(n) * 0.02 + 0.01,
                "gap_system_to_now_rel": rng.random(n) * 0.01,
                "range_rel": rng.random(n) * 0.03,
            },
            index=idx,
        )
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "g.csv"
            df.to_csv(p)
            d = gbt.train_baseline(p)
        self.assertIn("r2_oos_holdout", d)
        self.assertIsNotNone(d.get("model"))


if __name__ == "__main__":
    unittest.main()
