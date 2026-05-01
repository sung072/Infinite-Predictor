"""replay_execution_jsonl main — JSONL 이 있을 때 validate-only."""
from __future__ import annotations

import importlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))
exb = importlib.import_module("execution_bridge")
vg = importlib.import_module("vbt_gap_research")
ROOT = Path(__file__).resolve().parent.parent


class TestReplayJsonl(unittest.TestCase):
    def _make_jsonl(self) -> Path:
        o = vg.synthetic_ohlcv_bars(3, seed=2)
        df, _ = vg.run_gap_research_ohlcv(
            o,
            active_predictor_ids=["p1", "p2"],
            research_config={},
            data_snapshot_id="r1",
            seed=2,
        )
        d = tempfile.mkdtemp()
        p = Path(d) / "e.jsonl"
        exb.write_execution_jsonl(df, p)
        return p

    def test_validate_only_zero(self) -> None:
        p = self._make_jsonl()
        r = subprocess.run(
            [sys.executable, str(ROOT / "code" / "replay_execution_jsonl.py"), str(p), "--validate-only"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_cli_help(self) -> None:
        r = subprocess.run(
            [sys.executable, str(ROOT / "code" / "replay_execution_jsonl.py"), "-h"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0)
        self.assertIn("validate", r.stdout.lower() or r.stderr.lower())

    def test_validate_rejects_bad(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "bad.jsonl"
            p.write_text(
                '{"schema": "expected_price.execution_jsonl.v1", "n_bars": 1}\n'
                '{"schema": "not_bar"}\n',
                encoding="utf-8",
            )
            r = subprocess.run(
                [sys.executable, str(ROOT / "code" / "replay_execution_jsonl.py"), str(p), "--validate-only"],
                cwd=ROOT,
                stderr=subprocess.DEVNULL,
            )
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
