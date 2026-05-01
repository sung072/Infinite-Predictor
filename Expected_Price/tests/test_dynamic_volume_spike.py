import importlib
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

try:
    dvs = importlib.import_module("dynamic_volume_spike")
    vg = importlib.import_module("vbt_gap_research")
    _OK = True
except Exception:  # noqa: S110
    _OK = False


@unittest.skipUnless(_OK, "scikit-learn / dynamic_volume_spike import")
class TestDynamicVolumeSpike(unittest.TestCase):
    def test_train_predict(self) -> None:
        o = vg.synthetic_ohlcv_bars(64, seed=1)
        art = dvs.train_volume_to_close(o, random_state=0)
        s = dvs.predict_dynamic_volume_price(art, o)
        self.assertEqual(len(s), len(o))
        self.assertTrue(s.notna().all())
        self.assertIn("log1p_v", art.feature_columns)
