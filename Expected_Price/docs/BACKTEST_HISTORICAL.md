# 역사적(과거) 데이터로 “백테스팅”

이 repo에서 **백테스팅**이란: **가격(및 optional 요인)의 과거 봉이 주어진 상태**에서, Registry id별 예측가(앵커)와의 **gap(간격) 연구 시계열**을 만들고, **시간·재현( provenance )**을 남기는 것을 말한다. (브로커 PnL·슬리피지·체결 시뮬은 **이 패키지 범위 밖**; README “실거래 경로는 별도”와 동일.)

### 갭(예측가–예측가)이 선행하는 이유

**유효한 시스템가**(`p_system` 등)는, 여러 **수평 예측가**를 한 점수로 **합성·축소**한 결과이므로, 그 **입력끼리의 거리·구조(쌍·코호트·시간 fold)** 를 먼저 밝히지 않으면 “합의”가 **검증 가능한 기준**이 되지 못한다.  
이 문서·스크립트의 OOS/WF·`mean_pairwise_rel`·`gpr__*__*` 연구는 **시스템가를 쓰기 전에** 예측가–예측가 갭이 **어떤 국면에서 어떻게 퍼지는지**를 체계적으로 보기 위한 것이다.

## 1) 역사적 OHLCV를 준다

- **CSV 형식:** `open, high, low, close, volume` + 시간 열 `timestamp` (또는 `time` / `date` / `datetime`)  
  - 로더: `code/vbt_gap_research.py` → `load_ohlcv_csv`
- **샘플:** [data/sample_ohlcv.csv](../data/sample_ohlcv.csv)
- **BTC(바이낸스) 예시(공개 API):** [scripts/fetch_btc_ohlcv.py](../scripts/fetch_btc_ohlcv.py) → `data/btcusdt_1h_30d.csv` (기본: 1h, 720봉 ≈ 30일)

## 2) “진짜로” 과거만 보고 싶을 때 — `split` 두 가지

| `split` | 의미 | 언제 쓰나 |
|--------|------|----------|
| `oos` | 앞 구간 n·비율 = **train(참고만, gap 출력 안 씀)** → embargo → **나머지 한 번의 OOS**에만 `run_gap_research_ohlcv` | 단일 **홀드아웃** (역사 끝쪽만 검증) |
| `wf`  | **롤링**으로 train봉 n_train → embargo → test봉 n_test 를 시간축에서 반복, 각 **test** 구간만 gap 계산, `fold` 열로 합침 | **워크포워드** (여러 “미래” 구간을 순서대로 검증) |

CLI는 모두 [code/run_registry_research.py](../code/run_registry_research.py)  
- `oos` 예: `--split oos --train-frac 0.72 --embargo 24`  
- `wf` 예: `--split wf --wf-train 240 --wf-test 48 --embargo 12` (1h봉 기준이면 train≈10일, test≈2일)

## 3) 여러 예측가 + 간격(gap) 의미 분석 (BTC 데모)

- **4개 절대가(EMA/밴드) + 쌍·코호트·시스템 열**까지 돌리고, **전 구간(full)** + **홀드아웃(OOS)** + **워크포워드(WF)** 를 한 번에 돌린 뒤, 지표 정의 + 통계 + (full/OOS) 쌍 랭킹 + (WF) fold별 평균을 [data/runs/gap_meaning_report.md](../data/runs/gap_meaning_report.md)에 씀.

```bash
python scripts/gap_backtest_and_analyze.py
# OOS·WF만 끄려면: --skip-oos / --skip-wf
# OOS/WF 하이퍼: --train-frac, --embargo, --wf-train, --wf-test, --wf-step
```

( `data/btcusdt_1h_30d.csv` 가 없으면 이 스크립트가 `fetch_btc_ohlcv` 로 받음. )

산출 CSV: `data/runs/btc_4p_gap_backtest.csv` (full), `btc_4p_gap_oos.csv`, `btc_4p_gap_wf.csv` + 각 provenance json.

### 갭 vs **이후** 수익률 (가설 점검)

갭이 **크면/작으면** 다음 봉·N봉 수익이 **어떤 경향**인지 Spearman·퀸타일로 **탐색**한다(인과 아님, 레짐·표본에 민감).

```bash
# 먼저 gap CSV가 있어야 함(위 `gap_backtest_and_analyze` 또는 full 런)
python scripts/gap_forward_return_research.py
```

→ [data/runs/gap_forward_return_report.md](../data/runs/gap_forward_return_report.md)  
`signed_sys_vs_now_rel`(시스템가vs현재 **부호**), `min_anchor_to_now_rel`(가장 가까운 예측가–현재), `d_gap_system_rel`(갭 **변화**) 등을 `fwd_1` / `fwd_4` / `fwd_24` 와 같이 본다. **특정 id**(예: 뉴스 예측가)만 보려면 `--anchor-id <registry의 id>`.

## 4) 한 방에 (OOS / WF 래퍼)

```bash
# 워크포워드(기본). CSV 없으면 --fetch로 Binance에서 받음
python scripts/run_historical_backtest.py --mode wf --fetch

# BTC 4-예측가 데모(Registry+factors+gap-pairwise+system, factors 없으면 build 시도)
python scripts/run_historical_backtest.py --mode wf --fetch --btc-4p

# 단일 OOS
python scripts/run_historical_backtest.py --mode oos --csv data/btcusdt_1h_30d.csv
```

산출: `data/runs/` 아래 `historical_*.csv` / `historical_*.json` (또는 `--btc-4p` 시 factors·쌍 열까지 동일 스타일)

## 5) 직접 `run_registry_research` 쓰기 (동일)

```bash
python code/run_registry_research.py \
  --csv-ohlcv data/btcusdt_1h_30d.csv \
  --registry schemas/predictor_registry.example.json \
  --split oos --train-frac 0.72 --embargo 24 \
  --snapshot hist-oos-btc-1h \
  --out-csv data/runs/gap_oos.csv --out-prov-json data/runs/gap_oos.json
```

Registry·예측가가 **해당 히스토리와 맞는지**(심볼, 타임프레임, `meta.data_snapshot_id`)는 사용자가 맞출 책임이 있다. 상세: [chat/README.md](../chat/README.md), [code/run_registry_research.py](../code/run_registry_research.py)
