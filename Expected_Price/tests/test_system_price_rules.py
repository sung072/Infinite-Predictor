import importlib
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

spr = importlib.import_module("system_price_rules")


class TestSystemPriceRules(unittest.TestCase):
    def test_shrunk(self) -> None:
        self.assertAlmostEqual(
            spr.p_system_shrunk_to_now(100.0, 200.0, weight_to_now=0.0), 100.0
        )
        self.assertAlmostEqual(
            spr.p_system_shrunk_to_now(100.0, 200.0, weight_to_now=1.0), 200.0
        )
        self.assertAlmostEqual(
            spr.p_system_shrunk_to_now(100.0, 200.0, weight_to_now=0.1), 110.0
        )

    def test_tension_zero_mpr(self) -> None:
        r = spr.p_system_tension_blend(100.0, 10_000.0, 0.0, cap=0.5)
        self.assertAlmostEqual(r, 100.0)

    def test_tension_increases_toward_now(self) -> None:
        a = spr.p_system_tension_blend(100.0, 10_000.0, 0.0, cap=0.5)
        b = spr.p_system_tension_blend(100.0, 10_000.0, 0.5, cap=0.5)
        self.assertLess(a, b)
        self.assertLess(b, 10_000.0)
