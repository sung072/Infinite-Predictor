import importlib
import json
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

exb = importlib.import_module("execution_bridge")


class TestJsonSafe(unittest.TestCase):
    def test_inf_becomes_none(self) -> None:
        self.assertIsNone(exb.json_safe(float("inf")))

    def test_nested_dict(self) -> None:
        self.assertEqual(exb.json_safe({"a": 1.0})["a"], 1.0)

    def test_list(self) -> None:
        self.assertEqual(exb.json_safe([1, 2, 3.0]), [1, 2, 3.0])


class TestPackBar(unittest.TestCase):
    def test_p_now_alias_metrics(self) -> None:
        idx = pd.to_datetime(["2020-01-01"], utc=True)
        s = pd.Series(
            {
                "P_now": 1.0,
                "p_system": 1.1,
                "mean_pairwise_rel": 0.1,
            }
        )
        b = exb.pack_bar_record(idx[0], s)
        self.assertEqual(b["schema"], exb.SCHEMA_BAR)
        self.assertIn("metrics", b)
        self.assertIn("mean_pairwise_rel", b["metrics"])


if __name__ == "__main__":
    unittest.main()
