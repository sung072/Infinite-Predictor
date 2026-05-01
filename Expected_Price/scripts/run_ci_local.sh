#!/usr/bin/env bash
# CI 와 동일. 옵션 전달 예:  ./scripts/run_ci_local.sh --skip-pip --no-jsonl -q
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
exec python3 scripts/run_ci.py "$@"
