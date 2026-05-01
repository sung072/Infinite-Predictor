#!/usr/bin/env bash
# P0 TODO auto-complete (see complete_todo.py)
#   chmod +x scripts/complete_todo.sh && ./scripts/complete_todo.sh
#   ./scripts/complete_todo.sh --full
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 scripts/complete_todo.py "$@"
