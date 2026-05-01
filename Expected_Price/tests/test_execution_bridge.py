import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

exb = importlib.import_module("execution_bridge")
vg = importlib.import_module("vbt_gap_research")


class TestExecutionBridge(unittest.TestCase):
    def test_write_jsonl_roundtrip(self) -> None:
        o = vg.synthetic_ohlcv_bars(4, seed=0)
        df, _ = vg.run_gap_research_ohlcv(
            o,
            active_predictor_ids=["p_a", "p_b"],
            research_config={},
            data_snapshot_id="e1",
            seed=0,
        )
        self.assertIn("predictor_prices", df.columns)
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "e.jsonl"
            exb.write_execution_jsonl(df, p, header={"registry": "x.json"})
            lines = p.read_text(encoding="utf-8").strip().split("\n")
            self.assertGreaterEqual(len(lines), 2)
            head = json.loads(lines[0])
            self.assertIn("n_bars", head)
            bar = json.loads(lines[1])
            self.assertEqual(bar.get("schema"), "expected_price.execution_bar.v1")
            self.assertIn("predictor_prices", bar)
            self.assertIn("p_a", bar["predictor_prices"])
            self.assertIn("metrics", bar)
            h2, bars2 = exb.read_execution_jsonl(p)
            self.assertEqual(h2.get("n_bars"), 4)
            self.assertEqual(len(bars2), 4)
            self.assertEqual(bars2[0]["P_now"], bar["P_now"])
            self.assertEqual(bars2[0]["p_system"], bar["p_system"])
            self.assertEqual(exb.validate_execution_jsonl(p), [])

    def test_validate_bad_line(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "b.jsonl"
            p.write_text(
                '{"schema": "expected_price.execution_jsonl.v1", "n_bars": 1}\n'
                '{"schema": "bad"}\n',
                encoding="utf-8",
            )
            e = exb.validate_execution_jsonl(p)
        self.assertTrue(any("bar schema" in x for x in e))

    def test_streaming_matches_read(self) -> None:
        o = vg.synthetic_ohlcv_bars(5, seed=1)
        df, _ = vg.run_gap_research_ohlcv(
            o,
            active_predictor_ids=["a", "b"],
            research_config={},
            data_snapshot_id="s1",
            seed=1,
        )
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "t.jsonl"
            exb.write_execution_jsonl(df, p)
            a = list(exb.read_execution_jsonl(p)[1])
            b = list(exb.iter_bar_records_streaming(p))
        self.assertEqual(len(a), len(b))
        self.assertEqual(a[0]["t"], b[0]["t"])
