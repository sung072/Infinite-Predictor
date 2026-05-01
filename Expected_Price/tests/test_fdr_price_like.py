import importlib
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

fdr = importlib.import_module("fdr_exploration")
pl = importlib.import_module("price_like")


class TestFdr(unittest.TestCase):
    def test_bh(self) -> None:
        r, p_cut = fdr.benjamini_hochberg([0.01, 0.4, 0.4], fdr_q=0.1)
        self.assertEqual(p_cut, 0.01)
        self.assertEqual(r, [True, False, False])

    def test_cap(self) -> None:
        fdr.assert_exploration_cap(1, 5)
        with self.assertRaises(ValueError):
            fdr.assert_exploration_cap(10, 3)


class TestPriceLike(unittest.TestCase):
    def test_volume(self) -> None:
        p = pl.volume_as_price(100.0, p_ref=50_000.0, vol_ref=100.0, mode="log_ratio")
        self.assertGreater(p, 0)

    def test_time(self) -> None:
        p = pl.time_as_price(0.0, p_ref=50_000.0, mode="cycle_utc_day")
        self.assertAlmostEqual(p, 50_000.0, delta=1.0)

    def test_row(self) -> None:
        m = pl.predictors_from_ohlc_row(100.0, 1_000.0, 43_200.0, vol_ref=1_000.0)
        self.assertIn("vol_as_price_demo", m)
        self.assertIn("time_as_price_demo", m)
