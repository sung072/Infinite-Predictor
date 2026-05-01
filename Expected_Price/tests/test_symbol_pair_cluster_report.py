import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "symbol_pair_cluster_report.py"
spec = importlib.util.spec_from_file_location("spcr", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load symbol_pair_cluster_report.py")
spcr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(spcr)


class TestSymbolPairClusterReport(unittest.TestCase):
    def test_connected_components(self) -> None:
        nodes = ["A", "B", "C", "D"]
        edges = [("A", "B"), ("B", "C")]
        comps = spcr._connected_components(nodes, edges)
        self.assertEqual(comps[0], ["A", "B", "C"])
        self.assertEqual(comps[1], ["D"])


if __name__ == "__main__":
    unittest.main()

