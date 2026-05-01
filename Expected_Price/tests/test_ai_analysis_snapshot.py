"""ai_analysis_snapshot — JSON 직렬·갭 요약."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import ai_analysis_snapshot as aas  # noqa: E402


class TestAiAnalysisSnapshot(unittest.TestCase):
    def test_to_jsonable_numpy(self) -> None:
        self.assertEqual(aas.to_jsonable(np.float64(1.5)), 1.5)
        self.assertIsNone(aas.to_jsonable(np.float64(np.nan)))

    def test_build_snapshot_minimal(self) -> None:
        idx = pd.date_range("2026-01-01", periods=5, freq="h", tz="UTC")
        full = pd.DataFrame(
            {
                "mean_pairwise_rel": [0.01, 0.02, 0.015, 0.011, 0.012],
                "gap_system_to_now_rel": [0.001] * 5,
                "p_system": [100.0 + i for i in range(5)],
                "P_now": [99.0 + i for i in range(5)],
            },
            index=idx,
        )
        d = aas.build_snapshot_dict(
            full=full,
            cfg=aas.AnalysisSnapshotConfig(last_n_bars=3),
            oos=None,
            wf=None,
        )
        self.assertEqual(d["schema"], "ai_analysis_snapshot.v1")
        self.assertEqual(d["bars"]["full"], 5)
        self.assertEqual(len(d["tail_rows"]), 3)
        self.assertIn("last_bar", d)
        # JSON dump
        json.dumps(aas.to_jsonable(d))

    def test_write_roundtrip(self) -> None:
        idx = pd.date_range("2026-01-01", periods=3, freq="h", tz="UTC")
        full = pd.DataFrame({"mean_pairwise_rel": [0.1, 0.2, 0.15]}, index=idx)
        d = aas.build_snapshot_dict(
            full=full,
            cfg=aas.AnalysisSnapshotConfig(last_n_bars=2),
        )
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "s.json"
            aas.write_snapshot_dict(p, d)
            o = json.loads(p.read_text(encoding="utf-8"))
        self.assertEqual(o["bars"]["full"], 3)


if __name__ == "__main__":
    unittest.main()
