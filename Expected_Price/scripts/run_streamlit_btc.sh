#!/usr/bin/env bash
# BTC 갭 연구 Streamlit (프로젝트 루트 = repo)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if ! command -v streamlit >/dev/null 2>&1; then
  echo "Install: pip install -r requirements-streamlit.txt" >&2
  exit 1
fi
# 기본 포트: .streamlit/config.toml (7520, 7000–7999)
exec streamlit run "$ROOT/dashboard/btc_research_app.py" "$@"
