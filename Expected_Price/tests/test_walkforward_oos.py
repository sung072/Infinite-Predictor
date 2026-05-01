import importlib
import sys
import unittest
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
_CODE = _PKG / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

wfo = importlib.import_module("walkforward_oos")
rr = importlib.import_module("run_registry_research")
vg = importlib.import_module("vbt_gap_research")

oossplit_by_ratio = wfo.oossplit_by_ratio
iter_walkforward_folds = wfo.iter_walkforward_folds
run_wf_folds_from_registry = rr.run_wf_folds_from_registry
EXAMPLE = _PKG / "schemas" / "predictor_registry.example.json"


class TestWalkforwardOos(unittest.TestCase):
    def test_oos_split(self) -> None:
        ohlc = vg.synthetic_ohlcv_bars(30, seed=0)
        _a, m, b = oossplit_by_ratio(ohlc, train_ratio=0.5, embargo_bars=2)
        self.assertEqual(m.train_bars, 15)
        self.assertEqual(m.embargo_bars, 2)
        self.assertEqual(len(b), 13)

    def test_wf_iter(self) -> None:
        f = list(iter_walkforward_folds(40, n_train=10, n_test=5, n_embargo=1, step=5))
        self.assertTrue(len(f) >= 1)
        self.assertEqual(f[0].n_train, 10)

    def test_wf_registry_runs(self) -> None:
        ohlc = vg.synthetic_ohlcv_bars(48, seed=0)
        df, prov, ids, _reg, wrep = run_wf_folds_from_registry(
            EXAMPLE,
            ohlc,
            n_train=12,
            n_test=6,
            n_embargo=0,
            wf_step=6,
            seed=0,
        )
        self.assertIn("fold", df.columns)
        n_f = wrep["n_folds"]
        self.assertTrue(n_f >= 1)
        self.assertEqual(df["fold"].nunique(), n_f)
