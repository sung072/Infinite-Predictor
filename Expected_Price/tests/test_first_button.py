import importlib
import sys
import unittest
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

predictor_registry = importlib.import_module("predictor_registry")
predictor_gap_metrics = importlib.import_module("predictor_gap_metrics")
vbt_research_stub = importlib.import_module("vbt_research_stub")

load_registry_file = predictor_registry.load_registry_file
validate_registry = predictor_registry.validate_registry
all_predictor_ids = predictor_registry.all_predictor_ids
anchor_prices_for_ids = predictor_gap_metrics.anchor_prices_for_ids
research_pipeline_stub = vbt_research_stub.research_pipeline_stub

_EXAMPLE = _PKG / "schemas" / "predictor_registry.example.json"


class TestFirstButton(unittest.TestCase):
    def test_load_validate_example(self) -> None:
        d = load_registry_file(_EXAMPLE)
        validate_registry(d)
        self.assertIn("eth_beta_pair_1d", all_predictor_ids(d))

    def test_anchor_strict_missing_id(self) -> None:
        with self.assertRaises(KeyError):
            anchor_prices_for_ids(
                {"a": 1.0},
                ("a", "b"),
                strict=True,
            )

    def test_stub_end_to_end(self) -> None:
        row = {
            "P_now": 100.0,
            "predictor_prices": {
                "war_news_fwd_4h": 101.0,
                "eth_beta_pair_1d": 99.0,
            },
        }
        m = research_pipeline_stub(
            row,
            active_predictor_ids=["war_news_fwd_4h", "eth_beta_pair_1d"],
            p_system=100.5,
        )
        self.assertIn("mean_pairwise_rel", m)
        self.assertIn("scale_used", m)
