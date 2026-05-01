# 스택 100% 완성 (이 **저장소** 기준)

**“100%”의 의미:** `Expected_Price/` 안에서 **개발 순서 1~6이 끊기지 않고 도구·스크립트·테스트로 닫힌 상태**이다.  
**제외(의도):** 실계좌 주문, 거래소 API 키, 별도 Nautilus 프로덕션 프로세스, LSTM/Transformer **풀 트레이닝** 파이프(베이스라인/훅만 제공), 온체인·CCXT **대량** 앵커 자동 팜.

| 단계 | 목표 (개발 순서) | 이 repo에서의 “완료” 산출물 | 검증 |
|------|------------------|-----------------------------|------|
| 1 | 역사 데이터 + Anchor | `fetch_btc_ohlcv` · `build_btc_factor_csv` · `schemas/predictor_registry*.json` · Streamlit | 대시보드 + 샘플/데모 Registry |
| 2 | VectorBT·간격 연구 | `run_registry_research` · `vbt_gap_research` · `gap_backtest_and_analyze.py` | `data/runs/*gap*.csv` · `gap_meaning_report.md` |
| 3 | WFO + OOS | 2와 동일 스크립트 내 `oos` / `wf` | `btc_4p_gap_oos.csv` · `btc_4p_gap_wf.csv` |
| 4 | AI/ML + 시스템가 고도화 | `build_ai_analysis_snapshot` · `llm_report_from_snapshot` (규칙+선택 API) · `train_gap_baseline` (Ridge) | `ai_analysis_snapshot.json` · `ai_analysis_report.md` · `gap_baseline_artifact.json` |
| 5 | Nautilus 실시간 | `execution_bridge` · `nautilus_bridge` · `nautilus_on_bar_template` · `nautilus_execution_dry_run` | JSONL + 드라이런 (주문 없음) |
| 6 | 지속 학습·피드백 | `feedback_loop_ingest` / `--from-jsonl` · `feedback_loop_plan` · `run_research_cycle` | `feedback_research_plan.json` |

## 한 방에 “100%” (권장 — **이것만**)

**작업 디렉터리:** `scripts/`·`code/` 안이 아니라, **`requirements-research.txt`와 `scripts/`가 같이 있는 프로젝트 루트**에서 실행한다.

```bash
cd Expected_Price   # 상위에서 들어올 때만 (이미 ...\Expected_Price\Expected_Price 이면 생략)
python scripts/complete_100.py
```

**PowerShell 예 (지금 `...\Expected_Price\Expected_Price\scripts>` 에 있다면):**

```powershell
Set-Location ..
python .\scripts\complete_100.py
```

또는 그 자리에서: `python .\complete_100.py` (`complete_100.py` 가 있는 `scripts` 폴더일 때).

- 끝에 `STACK_100_COMPLETE: OK` + 앞서 `121` tests `OK` 가 찍히면 **이 repo 기준 100% 완성**으로 본다.
- CI와 **완전 동일**하게 돌리려면: `python scripts/complete_100.py --full-ci`
- `make complete` / `make stack100` = 위와 동일 (`complete_100.py`).

`pwsh -File scripts\run_all.ps1` / `./scripts/run_all.sh` = pip + `run_ci` + verify (초기 셋업 + 동일 ‘완성’ 검증).

(선택) **연구 파이프**만 훑기: `python scripts/run_research_cycle.py --dry-run`

## “완료” 판정(수동 체크)

- [ ] `python scripts/complete_100.py` → `STACK_100_COMPLETE: OK`  
- [ ] (선택) `python scripts/run_research_cycle.py --dry-run` → 2+3,4,4b,5,6 명령이 모두 찍힘  

위를 통과하면 **이 리포지토리 범위의 100%** 로 본다. 실서비스 연결은 [README.md](../README.md) 의 “실거래 경로는 repo 밖”을 따른다.
