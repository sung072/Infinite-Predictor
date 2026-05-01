import importlib.util
import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "system_price_shrink_tuning.py"
spec = importlib.util.spec_from_file_location("spst", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load system_price_shrink_tuning.py")
spst = importlib.util.module_from_spec(spec)
sys.modules["spst"] = spst
spec.loader.exec_module(spst)


class TestSystemPriceShrinkTuning(unittest.TestCase):
    def test_tuned_shrunk(self) -> None:
        ps = pd.Series([100.0, 110.0])
        pw = pd.Series([90.0, 90.0])
        out = spst.tuned_shrunk(ps, pw, 0.5)
        self.assertAlmostEqual(float(out.iloc[0]), 95.0)
        self.assertAlmostEqual(float(out.iloc[1]), 100.0)

    def test_tuned_tension_bounds(self) -> None:
        ps = pd.Series([100.0, 100.0])
        pw = pd.Series([90.0, 90.0])
        mpr = pd.Series([0.0, 10.0])
        out = spst.tuned_tension(ps, pw, mpr, cap=0.5, max_pull=0.5)
        self.assertAlmostEqual(float(out.iloc[0]), 100.0)
        self.assertAlmostEqual(float(out.iloc[1]), 95.0)

    def test_parse_float_list(self) -> None:
        vals = spst._parse_float_list("0, 0.1,0.2")
        self.assertEqual(vals, [0.0, 0.1, 0.2])

    def test_tuned_regime_shrunk(self) -> None:
        ps = pd.Series([100.0, 100.0, 100.0, 100.0])
        pw = pd.Series([90.0, 90.0, 90.0, 90.0])
        mpr = pd.Series([0.1, 0.2, 0.9, 1.0])
        out = spst.tuned_regime_shrunk(ps, pw, mpr, q=0.5, w_calm=0.9, w_stress=1.0)
        # calm -> 91, stress -> 90
        self.assertTrue(float(out.iloc[0]) >= 90.9)
        self.assertTrue(float(out.iloc[-1]) <= 90.1)


if __name__ == "__main__":
    unittest.main()
