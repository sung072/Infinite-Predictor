import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "strict_multi_cycle_research.py"
spec = importlib.util.spec_from_file_location("smcr", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load strict_multi_cycle_research.py")
smcr = importlib.util.module_from_spec(spec)
sys.modules["smcr"] = smcr
spec.loader.exec_module(smcr)


class TestStrictMultiCycleCompositeZscore(unittest.TestCase):
    def test_zscore_vector_center(self) -> None:
        zs = smcr._zscore_vector([1.0, 2.0, 3.0])
        self.assertAlmostEqual(zs[1], 0.0, places=6)
        self.assertLess(zs[0], 0.0)
        self.assertGreater(zs[2], 0.0)

    def test_attach_meta_raw_maps_mean(self) -> None:
        rows = [{"composite_mean": 1.5}, {"composite_mean": 2.0}]
        smcr._attach_composite_rank_meta(
            rows,
            composite_norm="raw",
            w_mae=1.0,
            w_hit=0.0,
            w_rr=0.0,
            w_sharpe=0.0,
            w_calmar=0.0,
        )
        self.assertAlmostEqual(float(rows[0]["composite_rank_score"]), 1.5)
        self.assertAlmostEqual(float(rows[1]["composite_rank_score"]), 2.0)

    def test_attach_meta_zscore_prefers_lower_mae_when_weight_mae_only(self) -> None:
        rows = [
            {
                "mae_ratio_mean": 0.9,
                "hit_mean": float("nan"),
                "mean_rr_mean": float("nan"),
                "sharpe_annualized_mean": float("nan"),
                "calmar_mean": float("nan"),
                "composite_mean": 0.0,
            },
            {
                "mae_ratio_mean": 1.1,
                "hit_mean": float("nan"),
                "mean_rr_mean": float("nan"),
                "sharpe_annualized_mean": float("nan"),
                "calmar_mean": float("nan"),
                "composite_mean": 0.0,
            },
        ]
        smcr._attach_composite_rank_meta(
            rows,
            composite_norm="zscore_within_run",
            w_mae=1.0,
            w_hit=0.0,
            w_rr=0.0,
            w_sharpe=0.0,
            w_calmar=0.0,
        )
        self.assertGreater(float(rows[0]["composite_rank_score"]), float(rows[1]["composite_rank_score"]))


if __name__ == "__main__":
    unittest.main()
