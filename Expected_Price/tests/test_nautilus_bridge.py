import importlib
import sys
import tempfile
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

exb = importlib.import_module("execution_bridge")
nb = importlib.import_module("nautilus_bridge")
vg = importlib.import_module("vbt_gap_research")


class TestNautilusBridge(unittest.TestCase):
    def test_iter_and_reduce(self) -> None:
        o = vg.synthetic_ohlcv_bars(3, seed=0)
        df, _ = vg.run_gap_research_ohlcv(
            o,
            active_predictor_ids=["p_a", "p_b"],
            research_config={},
            data_snapshot_id="n1",
            seed=0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "x.jsonl"
            exb.write_execution_jsonl(df, p, header={"test": 1})
            bars = list(nb.iter_execution_bars(p))
        self.assertEqual(len(bars), 3)
        r = nb.reduce_anchor_signal(bars[0], p_now=float(bars[0]["P_now"]))
        self.assertIn("d_mean_anchor", r)
        self.assertIn("p_system", r)
        v = nb.on_execution_bar(
            bars[0], hook=lambda b, s: s["d_mean_anchor"]
        )
        self.assertIsNotNone(v)

    def test_nautilus_spec_safe(self) -> None:
        # 환경에 설치돼 있을 수도/없을 수도 있음
        s = nb.nautilus_trader_spec()
        self.assertTrue(s is None or isinstance(s, str))
