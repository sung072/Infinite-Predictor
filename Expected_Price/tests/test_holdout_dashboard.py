import importlib
import sys
import unittest
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

hd = importlib.import_module("holdout_dashboard")


class TestHoldoutDashboard(unittest.TestCase):
    def test_build_markdown_minimal(self) -> None:
        jout = {
            "predictor_ids": ["a", "b"],
            "holdout_metrics": {
                "n_used": 10,
                "directional_hit_rate": 0.5,
                "mae_ratio_sys_over_naive": 0.95,
                "system_col": "p_system",
            },
            "holdout_accuracy_summary_ko": "요약\n줄",
            "holdout_run_info": {
                "registry": "/x/registry.json",
                "factors_csv": None,
                "csv_ohlcv": "/x/ohlc.csv",
                "gap_pairwise": True,
                "system_variants": True,
            },
            "provenance": {
                "experiment_id_short": "abcd1234",
                "temporal_holdout": {
                    "split": {
                        "n_window": 100,
                        "n_train": 60,
                        "n_embargo": 4,
                        "n_val": 36,
                    },
                    "candle_alignment": {
                        "median_step_between_rows": "0 days 01:00:00",
                        "train": {
                            "n_bars": 60,
                            "first_bar_label": "2024-01-01T00:00:00",
                            "last_bar_label": "2024-01-03T11:00:00",
                        },
                        "embargo": {"n_bars": 4},
                        "validation": {
                            "n_bars": 36,
                            "first_bar_label": "2024-01-03T16:00:00",
                            "last_bar_label": "2024-01-05T03:00:00",
                        },
                    },
                    "note": "테스트 노트",
                },
            },
        }
        md = hd.build_holdout_dashboard_markdown(jout)
        self.assertIn("## 1.", md)
        self.assertIn("## 4.", md)
        self.assertIn("요약", md)
        self.assertIn("directional_hit_rate", md)
        html = hd.build_holdout_dashboard_html(md)
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("요약", html)


if __name__ == "__main__":
    unittest.main()
