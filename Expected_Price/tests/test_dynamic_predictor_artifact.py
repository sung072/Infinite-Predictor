import importlib
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

d = importlib.import_module("dynamic_predictor_base")


class TestTrainedRegressorArtifact(unittest.TestCase):
    def test_sidecar(self) -> None:
        m = LinearRegression()
        m.fit(np.array([[1.0], [2.0]]), np.array([1.0, 2.0]))
        t = d.TrainedRegressorArtifact(
            model=m, feature_columns=["a"], target_column="y", meta={"v": 1}
        )
        c = t.to_sidecar()
        self.assertEqual(c["feature_columns"], ["a"])
        self.assertEqual(c["kind"], "sklearn_regressor")

    def test_predict_frame(self) -> None:
        m = LinearRegression()
        m.fit(np.array([[1.0], [2.0]]), np.array([1.0, 2.0]))
        t = d.TrainedRegressorArtifact(
            model=m, feature_columns=["a"], target_column="y", meta={}
        )
        X = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
        p = t.predict_frame(X)
        self.assertEqual(len(p), 3)

    def test_predict_frame_missing_col(self) -> None:
        m = LinearRegression()
        m.fit(np.array([[1.0]]), np.array([1.0]))
        t = d.TrainedRegressorArtifact(model=m, feature_columns=["a", "b"], target_column="y", meta={})
        with self.assertRaises(ValueError):
            t.predict_frame(pd.DataFrame({"a": [1.0]}))

    def test_save_load_roundtrip(self) -> None:
        m = LinearRegression()
        m.fit(np.array([[0.0], [1.0]]), np.array([0.0, 1.0]))
        t = d.TrainedRegressorArtifact(model=m, feature_columns=["a"], target_column="y", meta={})
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "m.joblib"
            d.save_artifact(t, p)
            t2 = d.load_artifact(p)
        self.assertIsInstance(t2, d.TrainedRegressorArtifact)


if __name__ == "__main__":
    unittest.main()
