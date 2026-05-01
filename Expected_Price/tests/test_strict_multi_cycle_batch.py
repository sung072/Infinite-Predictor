import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "strict_multi_cycle_batch.py"
spec = importlib.util.spec_from_file_location("smcb", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load strict_multi_cycle_batch.py")
smcb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(smcb)


class TestStrictMultiCycleBatch(unittest.TestCase):
    def test_pair_similarity(self) -> None:
        a = {
            "family": "trust_low40",
            "embargo_bars": 12,
            "trust_feature": "mean_pairwise_per_atr",
            "trust_q_low": 0.0,
            "trust_q_high": 0.4,
        }
        b = {
            "family": "trust_low40",
            "embargo_bars": 12,
            "trust_feature": "mean_pairwise_per_atr",
            "trust_q_low": 0.0,
            "trust_q_high": 0.4,
        }
        c = {"family": "base", "embargo_bars": 24, "trust_feature": None}
        self.assertAlmostEqual(smcb._pair_similarity(a, b), 1.0)
        self.assertLess(smcb._pair_similarity(a, c), 1.0)

    def test_load_symbols_file(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "s.txt"
            p.write_text("# c\n\nBTCUSDT\nETH\n", encoding="utf-8")
            got = smcb._load_symbols_file(p)
            self.assertEqual(got, ["BTC", "ETH"])


if __name__ == "__main__":
    unittest.main()

