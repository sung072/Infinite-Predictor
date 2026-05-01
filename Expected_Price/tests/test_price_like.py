"""price_like — log_ratio, bps, time modes."""
from __future__ import annotations

import importlib
import math
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

pl = importlib.import_module("price_like")


class TestVolumeAsPrice(unittest.TestCase):
    def test_log_ratio_unity(self) -> None:
        x = pl.volume_as_price(100.0, p_ref=50_000.0, vol_ref=100.0, mode="log_ratio")
        self.assertAlmostEqual(x, 50_000.0, places=0)

    def test_bps_mode(self) -> None:
        x = pl.volume_as_price(200.0, p_ref=10.0, vol_ref=200.0, mode="bps_of_ref")
        self.assertGreater(x, 0.0)

    def test_bad_ref(self) -> None:
        with self.assertRaises(ValueError):
            pl.volume_as_price(1.0, p_ref=0.0, vol_ref=1.0)

    def test_negative_volume(self) -> None:
        with self.assertRaises(ValueError):
            pl.volume_as_price(-1.0, p_ref=1.0, vol_ref=1.0)

    def test_invalid_mode(self) -> None:
        with self.assertRaises(ValueError):
            pl.volume_as_price(1.0, p_ref=1.0, vol_ref=1.0, mode="bogus")  # type: ignore[arg-type]


class TestTimeAsPrice(unittest.TestCase):
    def test_cycle_is_float(self) -> None:
        x = pl.time_as_price(0.0, p_ref=1.0, mode="cycle_utc_day")
        self.assertIsInstance(x, float)
        self.assertTrue(math.isfinite(x))

    def test_duration_log(self) -> None:
        t = pl.time_as_price(3600.0, p_ref=100.0, mode="duration_log")
        self.assertGreater(t, 100.0)

    def test_p_ref_nonpositive(self) -> None:
        with self.assertRaises(ValueError):
            pl.time_as_price(1.0, p_ref=0.0, mode="duration_log")

    def test_bad_time_mode(self) -> None:
        with self.assertRaises(ValueError):
            pl.time_as_price(1.0, p_ref=1.0, mode="nope")  # type: ignore[arg-type]


class TestDemoIds(unittest.TestCase):
    def test_frozen_ids(self) -> None:
        self.assertIn("vol", str(pl.PRED_ID_VOL).lower() or "vol")
        self.assertIn(pl.PRED_ID_TIME, pl.PRICE_LIKE_DEMO_IDS)


if __name__ == "__main__":
    unittest.main()
