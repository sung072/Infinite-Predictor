import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "run_multi_symbol_cycle.py"
spec = importlib.util.spec_from_file_location("rmsc", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load run_multi_symbol_cycle.py")
rmsc = importlib.util.module_from_spec(spec)
sys.modules["rmsc"] = rmsc
spec.loader.exec_module(rmsc)


class TestRunMultiSymbolCycle(unittest.TestCase):
    def test_parse_symbols(self) -> None:
        s = rmsc._parse_symbols("BTCUSDT, ethusdt ,SOLUSDT")
        self.assertEqual(s, ["BTCUSDT", "ETHUSDT", "SOLUSDT"])

    def test_parse_symbols_empty(self) -> None:
        with self.assertRaises(ValueError):
            rmsc._parse_symbols(" , ")

    def test_sym_slug(self) -> None:
        self.assertEqual(rmsc._sym_slug("BTCUSDT"), "btcusdt")


if __name__ == "__main__":
    unittest.main()
