import importlib
import json
import sys
import unittest
from pathlib import Path

_CODE = Path(__file__).resolve().parent.parent / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

re = importlib.import_module("repro_experiment")


class TestReproExperiment(unittest.TestCase):
    def test_config_canonical_order(self) -> None:
        a = re.config_canonical_json({"b": 1, "a": 2})
        b = re.config_canonical_json({"a": 2, "b": 1})
        self.assertEqual(a, b)

    def test_sha256_stable(self) -> None:
        h1 = re.config_sha256({"x": 1})
        h2 = re.config_sha256({"x": 1})
        self.assertEqual(h1, h2)
        self.assertEqual(len(h1), 64)

    def test_fingerprint_changes_with_seed(self) -> None:
        a = re.experiment_fingerprint({"c": 1}, seed=0, data_snapshot_id="s")
        b = re.experiment_fingerprint({"c": 1}, seed=1, data_snapshot_id="s")
        self.assertNotEqual(a, b)

    def test_fingerprint_changes_with_snap(self) -> None:
        a = re.experiment_fingerprint({}, seed=0, data_snapshot_id="a")
        b = re.experiment_fingerprint({}, seed=0, data_snapshot_id="b")
        self.assertNotEqual(a, b)

    def test_id_short_prefix(self) -> None:
        s = re.experiment_id_short({"k": 1}, seed=0, data_snapshot_id="x", length=8)
        f = re.experiment_fingerprint({"k": 1}, seed=0, data_snapshot_id="x")
        self.assertEqual(s, f[:8])

    def test_provenance_bundle_keys(self) -> None:
        b = re.provenance_bundle({"a": 1}, seed=3, data_snapshot_id="z")
        for k in (
            "config_sha256",
            "seed",
            "data_snapshot_id",
            "experiment_fingerprint",
            "experiment_id_short",
        ):
            self.assertIn(k, b)
        self.assertEqual(b["seed"], 3)

    def test_set_seeds_runs(self) -> None:
        re.set_global_seeds(42)
        re.set_global_seeds(0)

    def test_canonical_json_unicode(self) -> None:
        s = re.config_canonical_json({"한": "가"})
        self.assertIn("한", s)
        json.loads(s)


if __name__ == "__main__":
    unittest.main()
