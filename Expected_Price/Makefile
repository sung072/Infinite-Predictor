# make help | all | ci | complete | ci-fast | fast | bootstrap | dashboard | verify
.PHONY: help all complete stack100 ci ci-fast fast bootstrap dashboard verify
help:
	@echo "make all       - pip(연구+dev) + full run_ci (Unix). Windows: pwsh -File scripts\\run_all.ps1"
	@echo "make ci        - pip + unittest -v + execution JSONL (GitHub CI 와 동일)"
	@echo "make ci-fast   - unittest + JSONL 생략 (반복). Windows: pwsh -File scripts\\run_fast.ps1"
	@echo "make fast      - same as ci-fast. scripts/run_fast.sh (Unix)"
	@echo "make dashboard - streamlit: 시각(현재가·예측가·시스템가) 먼저 (연구/운영 권장 순서)"
	@echo "make bootstrap - bash scripts/dev_bootstrap.sh (pip + dev + ci-fast)"
	@echo "Windows bootstrap:  pwsh -File scripts\\dev_bootstrap.ps1"
	@echo "make verify   - full: unittest(120) + import + 스냅샷 (scripts/verify_expected_price_stack.py)"
	@echo "make complete / make stack100 - python scripts/complete_100.py (100% 한 방)"
	@echo "Priorities / when to use what: docs/TODO.md"
	@echo "Auto P0  pass + todo_state:  python scripts/complete_todo.py | --full"

all:
	bash scripts/run_all.sh

# 100%: run_ci(빠름) + verify — CI 전부는: python scripts/complete_100.py --full-ci
complete: stack100

stack100:
	python scripts/complete_100.py

ci:
	python scripts/run_ci.py

dashboard:
	@test -f data/derived/btc_factors_unified.csv || python scripts/build_btc_unified_factor_csv.py; \
	exec streamlit run dashboard/btc_research_app.py

ci-fast:
	python scripts/run_ci.py --skip-pip --no-jsonl

fast: ci-fast

verify:
	python scripts/verify_expected_price_stack.py

# 의존성 + 빠른 CI( Unix ). Windows → pwsh -File scripts\dev_bootstrap.ps1
bootstrap:
	bash scripts/dev_bootstrap.sh
