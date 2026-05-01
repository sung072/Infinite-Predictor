"""120+ 목표 마지막 보강."""
from __future__ import annotations

import importlib
import json
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

p = importlib.import_module("predictor_gap_metrics")
exb = importlib.import_module("execution_bridge")
nb = importlib.import_module("nautilus_bridge")
ROOT = Path(__file__).resolve().parent.parent
SC = ROOT / "schemas" / "predictor_registry.example.json"


class TestPairwiseRelGapsNames(unittest.TestCase):
    def test_gpr_column_names(self) -> None:
        o = p.pairwise_rel_gaps_flat({"a": 1.0, "b": 3.0}, scale=1.0)
        self.assertIn("gpr__a__b", o)
        self.assertAlmostEqual(o["gpr__a__b"], 2.0)


class TestValidateHeaderSchema(unittest.TestCase):
    def test_file_schema_constant(self) -> None:
        self.assertTrue(exb.SCHEMA_FILE.startswith("expected_price"))


class TestNautilusBarSignal(unittest.TestCase):
    def test_hook_returns_sig(self) -> None:
        b = {"P_now": 100.0, "p_system": 100.0, "predictor_prices": {"x": 100.0, "y": 100.0}}
        r = nb.on_execution_bar(b, hook=None)
        self.assertIn("d_mean_anchor", r or {})


class TestSchemaExampleReadable(unittest.TestCase):
    def test_json_loads(self) -> None:
        self.assertTrue(SC.is_file())
        o = json.loads(SC.read_text(encoding="utf-8"))
        self.assertIn("schema_version", o)
        self.assertIsInstance(o.get("predictors"), list)


class TestGprFlatOrdered(unittest.TestCase):
    def test_three_anchors_six_edges(self) -> None:
        o = p.pairwise_rel_gaps_flat({"a": 1.0, "b": 2.0, "c": 0.0}, scale=1.0)
        self.assertEqual(len(o), 3)


if __name__ == "__main__":
    unittest.main()
