import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

lr = importlib.import_module("llm_report_from_snapshot")


class TestLlmRuleReport(unittest.TestCase):
    def test_render_minimal(self) -> None:
        t = lr.render_rule_markdown(
            {
                "schema": "ai_analysis_snapshot.v1",
                "generated_at_utc": "x",
                "bars": {"full": 1, "tail_included": 1},
                "last_bar": {
                    "mean_pairwise_rel": 0.01,
                    "timestamp": "2026-01-01T00:00:00+00:00",
                },
            }
        )
        self.assertIn("스키마", t)

    def test_write_merged_no_llm(self) -> None:
        snap = {
            "schema": "ai_analysis_snapshot.v1",
            "generated_at_utc": "t",
            "bars": {"full": 0},
            "last_bar": {},
        }
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "a.json"
            p.write_text(json.dumps(snap), encoding="utf-8")
            o = Path(td) / "o.md"
            u, e = lr.write_merged_report(p, o, try_llm=False)
            body = o.read_text(encoding="utf-8")
        self.assertFalse(u)
        self.assertIn("스키마", body)


if __name__ == "__main__":
    unittest.main()
