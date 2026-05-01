import importlib
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))


class TestNautilusTemplate(unittest.TestCase):
    def test_import(self) -> None:
        m = importlib.import_module("nautilus_on_bar_template")
        b = {
            "P_now": 100.0,
            "p_system": 99.0,
            "predictor_prices": {"a": 101.0, "b": 99.0},
        }
        r = m.example_use_bar_dict(b)
        self.assertIsNotNone(r)
        self.assertIn("d_mean_anchor", r or {})


if __name__ == "__main__":
    unittest.main()
