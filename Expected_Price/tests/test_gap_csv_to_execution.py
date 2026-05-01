import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

g2e = importlib.import_module("gap_csv_to_execution")
exb = importlib.import_module("execution_bridge")


class TestGapCsvToExecution(unittest.TestCase):
    def test_parse_pp_string(self) -> None:
        s = "{'a': 1.0, 'b': 2.0}"
        d = g2e.parse_predictor_prices_cell(s)
        self.assertEqual(d, {"a": 1.0, "b": 2.0})

    def test_roundtrip_jsonl(self) -> None:
        idx = pd.date_range("2026-01-01", periods=2, freq="h", tz="UTC")
        df = pd.DataFrame(
            {
                "P_now": [100.0, 101.0],
                "p_system": [100.5, 100.2],
                "mean_pairwise_rel": [0.01, 0.02],
                "predictor_prices": [
                    "{'p_a': 100.0, 'p_b': 101.0}",
                    "{'p_a': 101.0, 'p_b': 100.0}",
                ],
            },
            index=idx,
        )
        with tempfile.TemporaryDirectory() as tmp:
            cd = Path(tmp) / "g.csv"
            jo = Path(tmp) / "e.jsonl"
            df.to_csv(cd)
            n = g2e.gap_csv_to_execution_jsonl(cd, jo)
            self.assertEqual(n, 2)
            e = exb.validate_execution_jsonl(jo)
            self.assertEqual(e, [])
            h, bars = exb.read_execution_jsonl(jo)
            self.assertEqual(h.get("n_bars"), 2)
            self.assertIsInstance(bars[0]["predictor_prices"], dict)


if __name__ == "__main__":
    unittest.main()
