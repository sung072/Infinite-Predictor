"""complete_100.py --help (스크립트 손상 방지; 전체 러너는 CI/수동)."""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestComplete100Script(unittest.TestCase):
    def test_help_exits_zero(self) -> None:
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "complete_100.py"), "-h"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0)
        out = (r.stdout or "") + (r.stderr or "")
        self.assertTrue("100" in out or "Stack" in out or "complete" in out.lower())


if __name__ == "__main__":
    unittest.main()
