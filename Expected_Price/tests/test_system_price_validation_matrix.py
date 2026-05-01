import importlib.util
import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "system_price_validation_matrix.py"
spec = importlib.util.spec_from_file_location("spvm", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load system_price_validation_matrix.py")
spvm = importlib.util.module_from_spec(spec)
sys.modules["spvm"] = spvm
spec.loader.exec_module(spvm)


class TestSystemPriceValidationMatrix(unittest.TestCase):
    def test_parse_case_relative_paths(self) -> None:
        c = spvm.parse_case("BTC-full|data/runs/a.csv|data/btcusdt_1h_30d.csv")
        self.assertEqual(c.name, "BTC-full")
        self.assertTrue(str(c.gap_csv).endswith("data\\runs\\a.csv"))

    def test_parse_case_bad_format(self) -> None:
        with self.assertRaises(ValueError):
            spvm.parse_case("bad-format")

    def test_wilson_interval_basic(self) -> None:
        lo, hi = spvm.wilson_interval(50, 100)
        self.assertTrue(0.0 <= lo <= 1.0)
        self.assertTrue(0.0 <= hi <= 1.0)
        self.assertLess(lo, 0.51)
        self.assertGreater(hi, 0.49)

    def test_p_value_directional(self) -> None:
        p_good = spvm.one_sided_p_hit_rate_gt_half(70, 100)
        p_rand = spvm.one_sided_p_hit_rate_gt_half(50, 100)
        self.assertLess(p_good, 0.01)
        self.assertGreater(p_rand, 0.3)

    def test_directional_stats(self) -> None:
        ps = pd.Series([101.0, 99.0, 101.0, 99.0])
        pw = pd.Series([100.0, 100.0, 100.0, 100.0])
        cn = pd.Series([102.0, 98.0, 101.0, 100.0])  # 마지막은 near-zero 제외
        n_dir, k_dir, _lo, _hi, _p = spvm._directional_stats(ps, pw, cn)
        self.assertEqual(n_dir, 3)
        self.assertEqual(k_dir, 3)

    def test_build_markdown_strict_oos_wf_only(self) -> None:
        rows = [
            {"name": "BTC-full", "n_used": 10, "hit_rate": 1.0, "hit_ci_lo": 0.8, "hit_ci_hi": 1.0, "p_hit_gt_half": 0.01, "mae_ratio": 0.9, "mae_gain_pct": 10.0, "spearman_signed_sys_vs_fwd1": 0.1},
            {"name": "BTC-oos", "n_used": 10, "hit_rate": 0.4, "hit_ci_lo": 0.2, "hit_ci_hi": 0.6, "p_hit_gt_half": 0.8, "mae_ratio": 1.2, "mae_gain_pct": -20.0, "spearman_signed_sys_vs_fwd1": 0.0},
        ]
        md = spvm.build_markdown(
            rows,
            min_hit_rate=0.52,
            max_mae_ratio=1.0,
            system_col="p_system",
            strict_oos_wf_only=True,
            shrink_weight=0.96,
            ai_block="",
        )
        self.assertIn("동시 통과(PASS): **0/1**", md)

    def test_custom_shrink_series(self) -> None:
        m = pd.DataFrame(
            {
                "p_system": [100.0, 110.0],
                "P_now": [90.0, 90.0],
                "scale_used": [1.0, 1.0],
                "fwd_1": [0.0, 0.0],
                "close_ohlc": [100.0, 100.0],
            }
        )
        class _Gfr:
            @staticmethod
            def _spearman(_a, _b):
                return 0.0
        _sk, _sp, ps = spvm._skill_from_system_col(
            m, _Gfr(), system_col="p_system_shrunk_custom", shrink_weight=0.5
        )
        self.assertAlmostEqual(float(ps.iloc[0]), 95.0)
        self.assertAlmostEqual(float(ps.iloc[1]), 100.0)

    def test_parse_symbol_weights(self) -> None:
        d = spvm.parse_symbol_weights("BTC=0.96, ETH=0.99")
        self.assertAlmostEqual(d["BTC"], 0.96)
        self.assertAlmostEqual(d["ETH"], 0.99)

    def test_resolve_shrink_weight(self) -> None:
        w = spvm.resolve_shrink_weight("ETH-wf", 0.96, {"ETH": 0.99})
        self.assertAlmostEqual(w, 0.99)
        w2 = spvm.resolve_shrink_weight("BTC-oos", 0.96, {"ETH": 0.99})
        self.assertAlmostEqual(w2, 0.96)

    def test_ai_advice_rule_fallback(self) -> None:
        rows = [{"name": "BTC-oos", "hit_rate": 0.55, "mae_ratio": 0.98}]
        s = spvm.build_ai_advice_block(
            rows,
            min_hit_rate=0.505,
            max_mae_ratio=1.0,
            try_llm=False,
        )
        self.assertIn("LLM 미사용", s)


if __name__ == "__main__":
    unittest.main()
