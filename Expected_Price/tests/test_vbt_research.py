import importlib
import sys
import unittest
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

repro_experiment = importlib.import_module("repro_experiment")
vbt_gap_research = importlib.import_module("vbt_gap_research")
pmetrics = importlib.import_module("predictor_gap_metrics")

config_sha256 = repro_experiment.config_sha256
provenance_bundle = repro_experiment.provenance_bundle
synthetic_ohlcv_bars = vbt_gap_research.synthetic_ohlcv_bars
run_gap_research_ohlcv = vbt_gap_research.run_gap_research_ohlcv


class TestVbtGap(unittest.TestCase):
    def test_config_hash_determinism(self) -> None:
        a = config_sha256({"a": 1, "b": 2})
        b = config_sha256({"b": 2, "a": 1})
        self.assertEqual(a, b)

    def test_run_produces_provenance(self) -> None:
        ohlc = synthetic_ohlcv_bars(8, seed=0)
        cfg = {"k": 1, "n": 8}
        out, prov = run_gap_research_ohlcv(
            ohlc,
            active_predictor_ids=["p_a", "p_b"],
            research_config=cfg,
            data_snapshot_id="t-snap",
            seed=0,
        )
        self.assertEqual(len(out), 8)
        for k in (
            "config_sha256",
            "seed",
            "data_snapshot_id",
            "experiment_fingerprint",
            "experiment_id_short",
        ):
            self.assertIn(k, prov)
        self.assertIn("vbt_rolling_return_std", out.columns)
        self.assertIn("mean_pairwise_rel", out.columns)
        self.assertIn("atr_14", out.columns)
        self.assertIn("mean_pairwise_per_atr", out.columns)
        self.assertIn("p_system", out.columns)

    def test_pairwise_metrics_helpers(self) -> None:
        a = {"p_a": 100.0, "p_b": 102.0, "p_c": 100.0}
        self.assertAlmostEqual(pmetrics.mean_abs_pairwise_distance(a), 4.0 / 3.0)
        fl = pmetrics.pairwise_rel_gaps_flat(a, scale=100.0)
        self.assertIn("gpr__p_a__p_b", fl)
        self.assertAlmostEqual(fl["gpr__p_a__p_b"], 0.02)

    def test_include_pairwise_column(self) -> None:
        ohlc = synthetic_ohlcv_bars(10, seed=1)
        out, _ = run_gap_research_ohlcv(
            ohlc,
            active_predictor_ids=["p_a", "p_b"],
            research_config={},
            data_snapshot_id="t2",
            seed=1,
            include_pairwise_columns=True,
        )
        self.assertIn("gpr__p_a__p_b", out.columns)

    def test_include_system_variants(self) -> None:
        ohlc = synthetic_ohlcv_bars(8, seed=1)
        out, _ = run_gap_research_ohlcv(
            ohlc,
            active_predictor_ids=["p_a", "p_b"],
            research_config={},
            data_snapshot_id="t3",
            seed=1,
            include_system_variants=True,
        )
        self.assertIn("p_system", out.columns)
        self.assertIn("p_system_shrunk", out.columns)
        self.assertIn("p_system_tension", out.columns)
