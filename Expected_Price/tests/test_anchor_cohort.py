import importlib
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

pg = importlib.import_module("predictor_gap_metrics")
pr = importlib.import_module("predictor_registry")
EX = Path(__file__).resolve().parent.parent / "schemas" / "predictor_registry.example.json"


class TestCohortGaps(unittest.TestCase):
    def test_cohort_scalars(self) -> None:
        a = {"x": 100.0, "y": 100.0, "z": 200.0}
        co = {"x": "g1", "y": "g1", "z": "g2"}
        d = pg.cohort_gap_scalars(a, co, scale=100.0)
        self.assertAlmostEqual(d["gpr_cohort_intra_rel"], 0.0)
        self.assertGreater(d["gpr_cohort_inter_rel"], 0.0)

    def test_registry_cohort_map_complete(self) -> None:
        data = pr.load_registry_file(EX)
        m = pr.anchor_cohort_map_for_ids(data, ["eth_beta_pair_1d", "war_news_fwd_4h"])
        self.assertIsNotNone(m)
        self.assertEqual(m.get("war_news_fwd_4h"), "abc")
        self.assertEqual(m.get("eth_beta_pair_1d"), "de")

    def test_missing_cohort_returns_none(self) -> None:
        data = pr.load_registry_file(EX)
        m = pr.anchor_cohort_map_for_ids(data, ["nope_a", "nope_b"])
        self.assertIsNone(m)
