# 할 일 (우선순위)

Git 없이도 쓰는 전제. **의미 없는 반복**은 `run_all` 대신 **빠른 검증**(`run_fast`)을 쓴다.

**100% (한 방):** `python scripts/complete_100.py` — 자세한 정의: [STACK_100_CHECKLIST.md](STACK_100_CHECKLIST.md).

## 로드맵(6단계) ↔ 이 저장소

| 단계 | 목적 | 이 repo에서의 위치 / 다음 액션 |
|------|------|--------------------------------|
| **1** 역사 데이터 + 초기 Anchor | 과거 OHLCV·후보 예측가(Registry) | `scripts/fetch_btc_ohlcv.py`, `build_btc_factor_csv.py`, `schemas/predictor_registry*.json` — 대시보드는 1·갭 결과 **시각화** |
| **2** 대규모 백테스트·간격 연구 (VectorBT) | 앵커 조합·수평 간격 패턴 | `code/vbt_gap_research.py`, `code/run_registry_research.py`, **`python scripts/gap_backtest_and_analyze.py`** (full 갭 시계열 + 리포트) — **실행은 여기** |
| **3** Walk-Forward + OOS | 과적합 방지·시간순 검증 | **2와 동일 스크립트**가 OOS·WF 포함 (`--skip-oos` / `--skip-wf` 로 끄기). `code/walkforward_oos.py` — 구간 정의. `docs/BACKTEST_HISTORICAL.md` |
| **4** AI 종합분석 엔진 | 간격·시스템가 학습/판단 | `build_ai_analysis_snapshot` → `llm_report_from_snapshot` (규칙+선택 `OPENAI_API_KEY`) → `ai_analysis_report.md` · `train_gap_baseline.py` (Ridge) — 대시보드 AI 힌트는 규칙 |
| **5** 실시간 실행 | Nautilus·선별 앵커 | `nautilus_bridge` + `nautilus_on_bar_template` + `nautilus_execution_dry_run` (주문 **없음**). 실 주문은 repo 밖(P2) |
| **6** 지속 학습·피드백 | 실전→재학습→2 | `feedback_loop_ingest` / `--from-jsonl` → `feedback_loop_plan` + `run_research_cycle` / `verify_expected_price_stack` — 자동 트레이딩 **아님** |

- **그림(대시보드) 직후의 “다음”** = **2 + 3** 을 돌려 갭·WF·OOS 리포트를 갱신하는 것 (`gap_backtest_and_analyze` 한 방에 포함).
- **2→4→5→6 한 번에**: `python scripts/run_research_cycle.py` (또는 `--dry-run` / `--skip-step2`). `code/research_cycle.py` 가 명령 시퀀스 정의.

## P0 — 언제 무엇을 돌릴지 (에이전트/본인 공통)

| 우선 | 상황 | 명령 (프로젝트 루트) |
|------|------|----------------------|
| 1 | 의존성 바꿈 / 처음 세팅 / “전부” | `pwsh -File scripts\run_all.ps1` (또는 `make all` on Unix) |
| 2 | **코드만** 바꾼 뒤 반복 점검 | `pwsh -File scripts\run_fast.ps1` (= `make ci-fast`, pip·JSONL 생략) |
| 3 | 더 가볍게(조용한 unittest) | `pwsh -File scripts\run_ci_local.ps1 --skip-pip --no-jsonl -q` |

- **P0 완료(도구)**: `scripts/run_fast.ps1`, `scripts/run_fast.sh` — `make ci-fast`와 동일.

## P0 — 자동 완료(스크립트)

검증이 **성공**하면 [`docs/todo_state.json`](todo_state.json)이 갱신되고, 아래 **자동 항목**만 `[x]`로 바뀐다. (P1~P3 수동 항목은 **절대** 자동으로 체크하지 않는다.)

- [x] <!-- auto:p0-fast-ok --> **자동**: `run_fast`와 동일한 점검(`complete_todo` 기본).  
  - `pwsh -File scripts\complete_todo.ps1` / `python scripts/complete_todo.py` / `./scripts/complete_todo.sh`
- [x] <!-- auto:p0-full-ok --> **자동**: `run_all`과 유사(의존성 + unittest + JSONL, pre-commit 제외).  
  - `python scripts/complete_todo.py --full` / `pwsh -File scripts\complete_todo.ps1 -- --full`

## P1 — 사용자(연구) 쪽 다음 단계

- [ ] `schemas/predictor_registry.example.json`을 **복사·수정**해 본인 predictor 집합 정의
- [ ] **역사적 OHLCV**로 OOS/WF “백테스팅”(gap 연구): [BACKTEST_HISTORICAL.md](BACKTEST_HISTORICAL.md) — `python scripts/gap_backtest_and_analyze.py`(BTC 4p full+OOS+WF+리포트) 또는 `python scripts/run_historical_backtest.py --mode wf --fetch --btc-4p`
- [ ] **4단계(스냅샷)**: `python scripts/build_ai_analysis_snapshot.py` — 갭·provenance·tail 를 LLM/학습용 JSON으로 (API 키 불필요)
- [ ] **5단계(드라이런)**: `python scripts/nautilus_execution_dry_run.py` — `execution_*.jsonl` + Nautilus 브릿지 시그널 확인 (거래 **아님**)
- [ ] **6단계(루프)**: `feedback_loop_ingest` → `feedback_loop_plan` — 피드백 JSONL + 연구 재실행 플랜 (수동/배치)
- [ ] **한 사이클**: `python scripts/run_research_cycle.py` — 2+3 → 4 → 5 → 6 (`--dry-run` 으로 목록만)
- [ ] **실제 OHLCV 경로**로 `code/run_registry_research.py` 실행 (합성·샘플만이 아닌지 확인)
- [ ] 코드/Registry 손댄 뒤 **P0 표**대로 `run_fast` 또는 `run_all` 한 번

## P2 — 리포지토리 밖 (README 경계)

- [ ] 실거래·브로커·실행 스택은 **이 repo가 아닌** 별도 경로에서 연결 (필요 시 `requirements-execution.txt` 등)

## P3 — 선택 (Git을 쓰기 시작할 때만)

- [ ] 루트에 `.git` + `pre-commit install` — 그 후 `run_all` 끝에 pre-commit이 붙음

---

*이 파일은 우선순위 작업 목록이다. “ㄱㄱ”만으로 같은 `run_all`을 무한 반복하는 것은 P0 표의 **2번**이 아닐 때는 이득이 없다.*
