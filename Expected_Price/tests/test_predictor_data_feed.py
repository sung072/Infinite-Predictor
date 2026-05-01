import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

try:
    importlib.import_module("sklearn")
    _SK = True
except Exception:  # noqa: S110
    _SK = False

pdf = importlib.import_module("predictor_data_feed")
rr = importlib.import_module("run_registry_research")
vg = importlib.import_module("vbt_gap_research")

EX = _PKG / "schemas" / "predictor_registry.example.json"
OH = _PKG / "data" / "sample_ohlcv.csv"
FCT = _PKG / "data" / "sample_factors.csv"


class TestPredictorDataFeed(unittest.TestCase):
    def test_load_align(self) -> None:
        o = vg.load_ohlcv_csv(OH)
        f = pdf.load_factors_table(FCT)
        a = pdf.align_factors_to_ohlc(o, f)
        self.assertEqual(len(a), len(o))

    def test_run_ohlc_factors_merged(self) -> None:
        o = vg.load_ohlcv_csv(OH)
        df, _p, _ids, reg = rr.run_from_registry(
            EX, ohlcv=o, n_synthetic_bars=6, seed=0, factors_path=FCT, use_price_like=True
        )
        self.assertEqual(
            pdf.factor_column_for_id(reg, "war_news_fwd_4h"), "p_war"
        )
        self.assertIn("mean_pairwise_rel", df.columns)
        self.assertEqual(len(df), 6)

    @unittest.skipUnless(_SK, "scikit-learn")
    def test_run_with_model_artifact_only(self) -> None:
        dvs = importlib.import_module("dynamic_volume_spike")
        dpb = importlib.import_module("dynamic_predictor_base")
        o = vg.synthetic_ohlcv_bars(16, seed=2)
        art = dvs.train_volume_to_close(o, random_state=0)
        with tempfile.TemporaryDirectory() as tmp:
            ap = Path(tmp) / "m.joblib"
            dpb.save_artifact(art, ap)
            reg = {
                "schema_version": "1.0.0",
                "predictors": [
                    {
                        "id": "dyn_vol",
                        "name": "d",
                        "horizon": {"kind": "bar", "spec": "1", "timezone": "UTC"},
                        "status": "active",
                        "version": "0",
                        "meta": {
                            "model_artifact": str(ap.resolve()),
                            "model_kind": "dynamic_volume_to_close",
                        },
                    },
                    {
                        "id": "p_b",
                        "name": "b",
                        "horizon": {"kind": "bar", "spec": "1", "timezone": "UTC"},
                        "status": "active",
                        "version": "0",
                    },
                ],
            }
            rpath = Path(tmp) / "r.json"
            rpath.write_text(json.dumps(reg), encoding="utf-8")
            df, _prov, _ids, _ = rr.run_from_registry(
                rpath, ohlcv=o, use_price_like=False
            )
        self.assertTrue(pdf.has_any_model_artifact(reg, rr.resolve_predictor_ids(reg)))
        self.assertIn("mean_pairwise_rel", df.columns)
        self.assertEqual(len(df), 16)
