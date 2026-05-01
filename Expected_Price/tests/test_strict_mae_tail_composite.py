import importlib.util
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "strict_multi_cycle_research.py"
spec = importlib.util.spec_from_file_location("smcr_tail", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load strict_multi_cycle_research.py")
smcr = importlib.util.module_from_spec(spec)
sys.modules["smcr_tail"] = smcr
spec.loader.exec_module(smcr)


class TestCompositeMaeTail(unittest.TestCase):
    def test_tail_weight_changes_score_when_p90_differs(self) -> None:
        m = {
            "mae_ratio_sys_over_naive": 1.0,
            "mae_ratio_sys_over_naive_p90": 2.0,
            "directional_hit_rate": 0.5,
            "mean_rr": 0.0,
            "sharpe_annualized": 0.0,
            "calmar_proxy": 0.0,
        }
        a = smcr._composite_score(
            m, w_mae=0.4, w_mae_tail=0.0, w_hit=0.2, w_rr=0.15, w_sharpe=0.15, w_calmar=0.1
        )
        b = smcr._composite_score(
            m, w_mae=0.2, w_mae_tail=0.2, w_hit=0.2, w_rr=0.15, w_sharpe=0.15, w_calmar=0.1
        )
        self.assertTrue(math.isfinite(a) and math.isfinite(b))
        self.assertNotAlmostEqual(a, b, places=6)


if __name__ == "__main__":
    unittest.main()
