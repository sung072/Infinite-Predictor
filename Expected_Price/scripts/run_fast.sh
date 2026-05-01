#!/usr/bin/env bash
# Fast local check: same as: make ci-fast
#   chmod +x scripts/run_fast.sh && ./scripts/run_fast.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 scripts/run_ci.py --skip-pip --no-jsonl "$@"
