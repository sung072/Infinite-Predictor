# Expected_Price (연구 패키지)

**gap 연구·Registry·execution JSONL** 파이프. 실거래 경로는 이 repo 밖에서 별도로 연결한다.  
*원칙:* **유효한 시스템가**는 **예측가–예측가 간 갭**을 (full·OOS·WF 등으로) **충분히 연구·분석**한 뒤에만 의미가 붙는다. [`docs/BACKTEST_HISTORICAL.md`](docs/BACKTEST_HISTORICAL.md) 상단·[`code/predictor_gap_metrics.py`](code/predictor_gap_metrics.py) 참고.  
*운영(시각 우선):* 이 시스템은 **차트에 수평(가격)선으로 올리는 예측가**와 **그 사이 간격(갭)을 중심**으로 측정하므로, **항상 먼저 Streamlit**으로 **현재가·예측가(앵커)·시스템가**를 겹쳐 보고, **그다음** CLI 백테스트·리포트로 검증하는 순서를 권장한다.

## 바로 시작

1. **눈(대시보드) — 먼저:** `pip install -r requirements-streamlit.txt` → `python scripts/build_btc_unified_factor_csv.py` → `streamlit run dashboard/btc_research_app.py` (프리셋 **btc_unified**, **기본 포트 7520**, `7000–7999` 권장 — `.streamlit/config.toml`) / Windows: `pwsh -File scripts\run_streamlit_btc.ps1` — **<http://127.0.0.1:7520>** 에서 **캔들(현재가) ↔ 예측가 선 ↔ p_system(합의) ↔ 갭(하단)** 를 비교한다.  
2. **백테스트·검증(그 다음):** [docs/BACKTEST_HISTORICAL.md](docs/BACKTEST_HISTORICAL.md) · `gap_backtest_and_analyze.py` · `gap_forward_return_research.py` 등.

- **의존성 + 검증(CI):** [docs/QUICKSTART.md](docs/QUICKSTART.md) — 한 번에: `make all` / `pwsh -File scripts\run_all.ps1` (`make help` 참고)
- **CI 한 줄:** `python scripts/run_ci.py` (로컬·GitHub 동일) — `tests/` **unittest 136** (discover, `python -m unittest discover -s tests -p "test_*.py"`)
- **100% 완성(이 repo):** 프로젝트 루트에서 `python scripts/complete_100.py` → `STACK_100_COMPLETE: OK` (`scripts` 폴더 **안**에 있으면 `Set-Location ..` 후 실행 또는 `python .\complete_100.py`) / [docs/STACK_100_CHECKLIST.md](docs/STACK_100_CHECKLIST.md) / `make complete`
- **다음 할 일(우선순위):** [docs/TODO.md](docs/TODO.md) — 코드만 바꾼 뒤 반복은 `pwsh -File scripts\run_fast.ps1` (= `make ci-fast`). P0를 **자동 체크 + 기록**하려면 `python scripts/complete_todo.py` (또는 `--full`)
- **로컬 스택 “완주” 검증(1~6 도구 + 테스트, 네트워크 없음·선택):** `python scripts/verify_expected_price_stack.py`  
  - **한 방 연구 사이클(2+3→3b 검증매트릭스→4→4b LLM리포→5→6):** `python scripts/run_research_cycle.py` (길이 나가면 `run_research_cycle.py --dry-run` / gap 생략 `--skip-step2` / LLM 리포 생략 `--skip-llm-report`)  
  - **4단계:** 스냅샷 `build_ai_analysis_snapshot` → `llm_report_from_snapshot` (규칙+선택 `OPENAI_API_KEY`) → Ridge 베이스 `train_gap_baseline.py`  
  - **5단계:** `nautilus_execution_dry_run` + [code/nautilus_on_bar_template.py](code/nautilus_on_bar_template.py) (Nautilus 쪽 복사용 훅)  
  - **6단계:** `feedback_loop_ingest` / `--from-jsonl` → `feedback_loop_plan` → `feedback_research_plan.json`
- **역사적 OHLCV·OOS/WF “백테스팅”(gap 연구):** [docs/BACKTEST_HISTORICAL.md](docs/BACKTEST_HISTORICAL.md) — `run_historical_backtest.py` (`--btc-4p` 권장) / **4개 예측가·수평선 간 갭 (full+OOS+WF):** `python scripts/gap_backtest_and_analyze.py` → [data/runs/gap_meaning_report.md](data/runs/gap_meaning_report.md) / **갭 vs 선행 수익률 점검:** `python scripts/gap_forward_return_research.py` → [data/runs/gap_forward_return_report.md](data/runs/gap_forward_return_report.md) / **시스템가 검증 매트릭스(다종목·분할 비교):** `python scripts/system_price_validation_matrix.py` → `data/runs/system_price_validation_matrix.md`
- **맥락·파일 맵:** [chat/README.md](chat/README.md)

(위 1번과 동일) **Streamlit = 운영 시 기본 창**으로 쓰고, **백테스팅 → 예측가(간격) → 시스템가 → 현재가** 해석은 대시보드(시각)를 기준으로 CLI 리포트를 곁들인다.

Python **3.11+** (`.python-version`).
