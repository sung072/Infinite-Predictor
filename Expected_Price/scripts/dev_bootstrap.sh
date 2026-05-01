#!/usr/bin/env bash
# 의존성 설치 + 빠른 CI(테스트). 사용:
#   chmod +x scripts/dev_bootstrap.sh && ./scripts/dev_bootstrap.sh
#   ./scripts/dev_bootstrap.sh --venv   # ./.venv 생성·활성화(존재하면 재사용)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ "${1:-}" == "--venv" ]]; then
  if [[ ! -d .venv ]]; then
    python3 -m venv .venv
  fi
  # shellcheck disable=SC1091
  . .venv/bin/activate
fi

python3 -c "import sys; assert sys.version_info >= (3, 11), 'Python 3.11+ required'; print('python', sys.version.split()[0])"
python3 -m pip install -U pip wheel
python3 -m pip install -r requirements-research.txt
if [[ -f requirements-dev.txt ]]; then
  python3 -m pip install -r requirements-dev.txt
fi
python3 scripts/run_ci.py --skip-pip --no-jsonl -q

echo "OK — 다음: 전체 CI( pip + JSONL ) → python3 scripts/run_ci.py 또는 make ci"
