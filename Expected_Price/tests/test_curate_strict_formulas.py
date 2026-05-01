import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURATE = ROOT / "scripts" / "curate_strict_formulas.py"


class TestCurateStrictFormulas(unittest.TestCase):
    def test_cli_shortlist(self) -> None:
        summary = {
            "best_by_symbol": [
                {
                    "symbol": "BTC",
                    "hit_rate": 0.6,
                    "mae_ratio": 0.98,
                    "coverage": 0.5,
                    "cluster_key": "base|emb=12|sh=0.95",
                    "best_formula": {"family": "base", "embargo_bars": 12},
                    "composite_rank_score": 0.5,
                },
                {
                    "symbol": "ETH",
                    "hit_rate": 0.55,
                    "mae_ratio": 1.02,
                    "coverage": 0.8,
                    "cluster_key": "base|emb=12|sh=0.95",
                    "best_formula": {"family": "base", "embargo_bars": 12},
                    "composite_rank_score": 0.45,
                },
                {
                    "symbol": "SOL",
                    "hit_rate": 0.4,
                    "mae_ratio": 0.99,
                    "coverage": 0.9,
                    "cluster_key": "other|emb=24|sh=0.94",
                    "best_formula": {"family": "trust_high40"},
                    "composite_rank_score": 0.3,
                },
            ]
        }
        with tempfile.TemporaryDirectory() as td:
            sj = Path(td) / "s.json"
            oj = Path(td) / "out.json"
            sj.write_text(json.dumps(summary), encoding="utf-8")
            r = subprocess.run(
                [sys.executable, str(CURATE), "--summary-json", str(sj), "--out-json", str(oj), "--min-hit", "0.5", "--shortlist-k", "5"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(r.returncode, 0, msg=r.stderr + r.stdout)
            out = json.loads(oj.read_text(encoding="utf-8"))
            self.assertEqual(out["counts"]["symbols_after_filter"], 2)
            self.assertGreaterEqual(len(out["shortlist_global_top_k"]), 1)
            ck0 = out["shortlist_global_top_k"][0]["cluster_key"]
            self.assertIn("base", ck0)


if __name__ == "__main__":
    unittest.main()
