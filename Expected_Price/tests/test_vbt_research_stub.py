import importlib
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

v = importlib.import_module("vbt_research_stub")


class TestVbtStub(unittest.TestCase):
    def test_happy(self) -> None:
        o = v.research_pipeline_stub(
            {
                "P_now": 100.0,
                "predictor_prices": {"a": 99.0, "b": 101.0},
            },
            active_predictor_ids=["a", "b"],
            p_system=100.0,
        )
        self.assertIn("mean_pairwise_rel", o)

    def test_missing_prices(self) -> None:
        with self.assertRaises(KeyError):
            v.research_pipeline_stub({"P_now": 1.0}, active_predictor_ids=["a"], p_system=1.0)

    def test_missing_p_now(self) -> None:
        with self.assertRaises(KeyError):
            v.research_pipeline_stub(
                {"predictor_prices": {"a": 1.0}}, active_predictor_ids=["a"], p_system=1.0
            )

    def test_strict_ids(self) -> None:
        with self.assertRaises(KeyError):
            v.research_pipeline_stub(
                {
                    "P_now": 1.0,
                    "predictor_prices": {"a": 1.0},
                },
                active_predictor_ids=["a", "missing"],
                p_system=1.0,
            )


if __name__ == "__main__":
    unittest.main()
