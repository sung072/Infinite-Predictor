import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "strict_multi_cycle_research.py"
spec = importlib.util.spec_from_file_location("smcr2", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load strict_multi_cycle_research.py")
smcr = importlib.util.module_from_spec(spec)
sys.modules["smcr2"] = smcr
spec.loader.exec_module(smcr)


class TestStrictMultiCycleCohortReport(unittest.TestCase):
    def test_top_fraction_cutoff(self) -> None:
        vals = []
        for i in range(30):
            vals.append(
                {
                    "metrics": {
                        "composite_score": float(i),
                        "directional_hit_rate": 0.5 + i * 0.001,
                        "mae_ratio_sys_over_naive": 1.0 - i * 0.01,
                    }
                }
            )
        r = smcr._dev_top_fraction_cohort_report(vals, fraction=0.1, rank_key="composite_score")
        self.assertEqual(r["n_eligible"], 30)
        self.assertEqual(r["top_n"], 3)
        self.assertAlmostEqual(float(r["cutoff_rank_score"]), 27.0, places=6)

    def test_final_rank_raw_decouples_from_meta_zscore(self) -> None:
        rows = [
            {"metrics": {"composite_score": 1.0, "mae_ratio_sys_over_naive": 0.9, "directional_hit_rate": 0.5}},
            {"metrics": {"composite_score": 2.0, "mae_ratio_sys_over_naive": 1.1, "directional_hit_rate": 0.6}},
        ]
        smcr._attach_composite_rank_final(
            rows,
            composite_norm="raw",
            w_mae=1.0,
            w_hit=0.0,
            w_rr=0.0,
            w_sharpe=0.0,
            w_calmar=0.0,
        )
        self.assertAlmostEqual(float(rows[0]["metrics"]["composite_rank_score"]), 1.0)
        self.assertAlmostEqual(float(rows[1]["metrics"]["composite_rank_score"]), 2.0)

    def test_cohort_sensitivity_multi_fraction(self) -> None:
        vals = []
        for i in range(40):
            vals.append(
                {
                    "metrics": {
                        "composite_score": float(i),
                        "directional_hit_rate": 0.5,
                        "mae_ratio_sys_over_naive": 1.0,
                    }
                }
            )
        r05 = smcr._dev_top_fraction_cohort_report(vals, fraction=0.05, rank_key="composite_score")
        r20 = smcr._dev_top_fraction_cohort_report(vals, fraction=0.2, rank_key="composite_score")
        self.assertEqual(r05["top_n"], 2)
        self.assertEqual(r20["top_n"], 8)

    def test_improvement_vs_all_cell(self) -> None:
        tb = {"directional_hit_rate": {"mean": 0.6}, "mae_ratio_sys_over_naive": {"mean": 0.9}}
        ab = {"directional_hit_rate": {"mean": 0.5}, "mae_ratio_sys_over_naive": {"mean": 1.0}}
        s = smcr._improvement_vs_all_cell(tb, ab)
        self.assertIn("hit", s)
        self.assertIn("mae", s)
        self.assertIn("+10.00pp", s)
        self.assertIn("+10.0%rel", s)


if __name__ == "__main__":
    unittest.main()
