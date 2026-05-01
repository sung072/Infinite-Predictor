#!/usr/bin/env bash
# 한 번에: pip(연구+dev) -> CI 전체 -> (Git 있으면) pre-commit
#   chmod +x scripts/run_all.sh && ./scripts/run_all.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 -m pip install -U pip wheel
python3 -m pip install -r requirements-research.txt
if [[ -f requirements-dev.txt ]]; then
  python3 -m pip install -r requirements-dev.txt
fi
python3 scripts/run_ci.py --skip-pip
python3 scripts/verify_expected_price_stack.py --skip-unittest
if [[ -d .git ]]; then
  pre-commit run --all-files
else
  echo "== pre-commit skipped: no .git (normal if you are not using Git)"
fi
