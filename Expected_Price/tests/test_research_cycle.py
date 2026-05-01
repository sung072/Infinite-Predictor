import importlib
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

rc = importlib.import_module("research_cycle")
ROOT = Path(__file__).resolve().parent.parent


class TestResearchCycle(unittest.TestCase):
    def test_steps_default(self) -> None:
        b = rc.CycleBuild(
            skip_step2=False,
            nautilus_last_n=48,
            no_plan=False,
            extra_gap_args=(),
            skip_llm_report=False,
        )
        st = rc.build_cycle_steps(ROOT, "python", b=b)
        self.assertEqual(len(st), 6)
        self.assertIn("gap_backtest", st[0][1][1])
        self.assertIn("system_price_validation_matrix", st[1][1][1])
        self.assertIn("--ai-judge", st[1][1])
        self.assertIn("llm_report", st[3][1][1])
        self.assertIn("--last-n", st[4][1])

    def test_skip_step2(self) -> None:
        b = rc.CycleBuild(
            skip_step2=True,
            nautilus_last_n=None,
            no_plan=True,
            extra_gap_args=(),
            skip_llm_report=True,
        )
        st = rc.build_cycle_steps(ROOT, "py", b=b)
        self.assertEqual(len(st), 2)  # 4 + 5 only
        self.assertIn("build_ai", st[0][1][1])


if __name__ == "__main__":
    unittest.main()
