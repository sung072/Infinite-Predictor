import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

fl = importlib.import_module("feedback_loop")


class TestFeedbackLoop(unittest.TestCase):
    def test_plan_empty_events(self) -> None:
        p = fl.build_research_plan([])
        self.assertEqual(p["schema"], fl.SCHEMA_PLAN)
        self.assertFalse(p["force_rerun_gaps"])
        self.assertIn("gap_backtest_and_analyze", p["step2_gap_vectorbt"][0])

    def test_plan_force_rerun(self) -> None:
        ev = [
            {
                "schema": fl.SCHEMA_EVENT,
                "suggest_rerun_gaps": True,
                "notes": "x",
            }
        ]
        p = fl.build_research_plan(ev)
        self.assertTrue(p["force_rerun_gaps"])

    def test_append_and_iter(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "f.jsonl"
            fl.append_feedback_event(
                p,
                fl.FeedbackEvent(
                    source="manual",
                    symbol="X",
                    run_id="r1",
                    suggest_rerun_gaps=False,
                    notes="n",
                ),
            )
            rows = list(fl.iter_feedback_events(p))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["notes"], "n")

    def test_write_plan(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "plan.json"
            pl = fl.build_research_plan([])
            fl.write_research_plan_json(out, pl)
            o = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(o["schema"], fl.SCHEMA_PLAN)


if __name__ == "__main__":
    unittest.main()
