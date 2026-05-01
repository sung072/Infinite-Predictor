"""predictor_gap_metrics — 순수 수치/스칼라 (느슨·엣지 포함)."""
from __future__ import annotations

import importlib
import math
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

p = importlib.import_module("predictor_gap_metrics")


class TestScaleAndPairwise(unittest.TestCase):
    def test_pairwise_two(self) -> None:
        d = p.pairwise_relative_distances({"a": 100.0, "b": 102.0}, scale=100.0)
        self.assertAlmostEqual(d[("a", "b")], 0.02)

    def test_pairwise_single(self) -> None:
        d = p.pairwise_relative_distances({"x": 1.0})
        self.assertEqual(d, {})

    def test_pairwise_uses_default_scale(self) -> None:
        d = p.pairwise_relative_distances({"a": 9.0, "b": 11.0})
        s = 10.0
        self.assertAlmostEqual(d[("a", "b")], 2.0 / s)

    def test_mean_pairwise_zero(self) -> None:
        self.assertEqual(
            p.mean_pairwise_distance({"a": 5.0, "b": 5.0, "c": 5.0}, scale=1.0), 0.0
        )

    def test_mean_pairwise_three_anchors(self) -> None:
        m = p.mean_pairwise_distance({"a": 0.0, "b": 1.0, "c": 0.0}, scale=1.0)
        self.assertGreater(m, 0.0)

    def test_variance_one(self) -> None:
        self.assertEqual(p.variance_of_anchors({"a": 1.0}), 0.0)

    def test_range_empty(self) -> None:
        self.assertEqual(p.range_spread({}), 0.0)

    def test_range_two(self) -> None:
        self.assertEqual(p.range_spread({"a": 0.0, "b": 3.0}), 3.0)

    def test_mean_abs_one(self) -> None:
        self.assertEqual(p.mean_abs_pairwise_distance({"a": 1.0}), 0.0)

    def test_gpr_flat_bad_scale(self) -> None:
        with self.assertRaises(ValueError):
            p.pairwise_rel_gaps_flat({"a": 1.0, "b": 2.0}, scale=0.0)


class TestCohort(unittest.TestCase):
    def test_cohort_missing_in_map(self) -> None:
        o = p.cohort_gap_scalars(
            {"a": 1.0, "b": 2.0},
            {"a": "t"},
            scale=1.0,
        )
        self.assertTrue(math.isnan(o["gpr_cohort_inter_rel"]))
        self.assertTrue(math.isnan(o["gpr_cohort_intra_rel"]))

    def test_cohort_inter_intra(self) -> None:
        a = {"x": 100.0, "y": 104.0, "z": 200.0}
        m = {"x": "A", "y": "A", "z": "B"}
        o = p.cohort_gap_scalars(a, m, scale=100.0)
        self.assertTrue(math.isfinite(o["gpr_cohort_intra_rel"]))
        self.assertTrue(math.isfinite(o["gpr_cohort_inter_rel"]))

    def test_cohort_needs_positive_scale(self) -> None:
        with self.assertRaises(ValueError):
            p.cohort_gap_scalars(
                {"a": 1.0, "b": 2.0},
                {"a": "x", "b": "y"},
                scale=-1.0,
            )


class TestSystemMetrics(unittest.TestCase):
    def test_relative_gap(self) -> None:
        g = p.relative_gap_to_now(100.0, 102.0, scale=100.0)
        self.assertAlmostEqual(g, 0.02)

    def test_system_gap_keys(self) -> None:
        o = p.system_gap_metrics(
            {"a": 100.0, "b": 102.0},
            p_now=101.0,
            p_system=101.0,
            scale=100.0,
        )
        for k in (
            "scale_used",
            "mean_pairwise_rel",
            "variance_anchors",
            "range_rel",
            "gap_system_to_now_rel",
            "n_anchors",
        ):
            self.assertIn(k, o)

    def test_anchor_prices_strict(self) -> None:
        with self.assertRaises(KeyError):
            p.anchor_prices_for_ids({"a": 1.0}, ["a", "b"], strict=True)

    def test_anchor_prices_loose(self) -> None:
        o = p.anchor_prices_for_ids({"a": 1.0}, ["a", "b"], strict=False)
        self.assertEqual(o, {"a": 1.0})


class TestCompression(unittest.TestCase):
    def test_ratio_normal(self) -> None:
        self.assertAlmostEqual(p.compression_ratio(0.1, 0.05), 0.5)

    def test_ratio_zero_prev_infinite(self) -> None:
        r = p.compression_ratio(1e-20, 0.1, eps=1e-10)
        self.assertEqual(r, float("inf"))

    def test_ratio_both_tiny(self) -> None:
        r = p.compression_ratio(1e-20, 1e-20, eps=1e-30)
        self.assertEqual(r, 1.0)

    def test_summarize_series(self) -> None:
        s = p.summarize_series(
            [
                {"mean_pairwise_rel": 0.1, "gap_system_to_now_rel": 0.0},
                {"mean_pairwise_rel": 0.2, "gap_system_to_now_rel": 0.0},
            ]
        )
        self.assertEqual(len(s), 2)
        self.assertIn("compression_mean_pairwise", s[1])


if __name__ == "__main__":
    unittest.main()
