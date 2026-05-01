"""추가 엣지·한 줄 — 120+ 목표."""
from __future__ import annotations

import importlib
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

lr = importlib.import_module("llm_report_from_snapshot")
fl = importlib.import_module("feedback_loop")
rc = importlib.import_module("research_cycle")
g2e = importlib.import_module("gap_csv_to_execution")
wfo = importlib.import_module("walkforward_oos")
exb = importlib.import_module("execution_bridge")
ROOT = Path(__file__).resolve().parent.parent


class TestLlmNoKey(unittest.TestCase):
    @patch.dict(os.environ, {}, clear=True)
    def test_openai_returns_none(self) -> None:
        r = lr.llm_openai_chat_completion([{"role": "user", "content": "x"}])
        self.assertIsNone(r)


class TestFeedbackPlanKeys(unittest.TestCase):
    def test_has_stack_keys(self) -> None:
        p = fl.build_research_plan([], project_root_cmd="py")
        self.assertIn("step4b_llm_report", p)
        self.assertIn("stack_verify", p)


class TestResearchCycleLlmFlag(unittest.TestCase):
    def test_len_without_llm(self) -> None:
        b = rc.CycleBuild(
            skip_step2=True,
            nautilus_last_n=None,
            no_plan=True,
            extra_gap_args=(),
            skip_llm_report=True,
        )
        st = rc.build_cycle_steps(ROOT, "python", b=b)
        self.assertEqual(len(st), 2)

    def test_len_with_llm(self) -> None:
        b = rc.CycleBuild(
            skip_step2=True,
            nautilus_last_n=10,
            no_plan=False,
            extra_gap_args=(),
            skip_llm_report=False,
        )
        st = rc.build_cycle_steps(ROOT, "p", b=b)
        self.assertIn("llm_report", st[1][0])


class TestGap2ePrepare(unittest.TestCase):
    def test_dict_pp(self) -> None:
        import pandas as pd

        d = g2e.prepare_gap_df_for_execution(
            pd.DataFrame({"predictor_prices": [{"a": 1.0}]}, index=pd.date_range("2020-1-1", periods=1, freq="h", tz="UTC"))
        )
        self.assertIsInstance(d["predictor_prices"].iloc[0], dict)


class TestOosMeta(unittest.TestCase):
    def test_to_dict_time(self) -> None:
        import pandas as pd

        o = pd.DataFrame(
            {
                "open": [1, 1],
                "high": [1, 1],
                "low": [1, 1],
                "close": [1, 1],
                "volume": [1, 1],
            },
            index=pd.date_range("2020-1-1", periods=2, freq="h", tz="UTC"),
        )
        tr, m, oos = wfo.oossplit_by_ratio(o, train_ratio=0.5, embargo_bars=0)
        d = m.to_dict()
        self.assertIn("n_total", d)
        self.assertIn("train_bars", d)
        self.assertIn("oos_bars", d)


class TestExbFileHeader(unittest.TestCase):
    def test_iter_streaming(self) -> None:
        import tempfile

        import vbt_gap_research as vg

        o = vg.synthetic_ohlcv_bars(2, seed=0)
        df, _ = vg.run_gap_research_ohlcv(
            o,
            active_predictor_ids=["a", "b"],
            research_config={},
            data_snapshot_id="x",
            seed=0,
        )
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "x.jsonl"
            exb.write_execution_jsonl(df, p)
            rows = list(exb.iter_bar_records_streaming(p))
        self.assertEqual(len(rows), 2)


if __name__ == "__main__":
    unittest.main()
