# Strict Multi-Cycle — 결과 분석 프레임워크 (A) 및 후속 설계 (B·C·D)

50종 배치(`strict_multi_cycle_batch.py`)와 단일 연구(`strict_multi_cycle_research.py`) 산출물을 **같은 기준**으로 읽고, 다음 개선 작업을 **코드 위치와 함께** 고정한다.

---

## A. 결과 분석 프레임워크 (운영 체크리스트)

### A.1 재현·산출물

| 항목 | 내용 |
|------|------|
| 배치 기본 유니버스 | `scripts/strict_multi_cycle_universe.py` → `DEFAULT_SYMBOLS_50` |
| 50종 요약 JSON/MD | `data/runs/strict_multi_cycle_summary_50.json`, `.md` |
| 종목별 상세 | `data/runs/strict_multi_cycle_{slug}.json` / `.md` |
| 재실행 예시 | `python scripts/strict_multi_cycle_batch.py --fetch-missing --parallel 2` |

상세 체크리스트(완성 선언·계보)는 **`docs/STRICT_RESEARCH_COMPLETION_CHECKLIST.md`** 와 `data/runs/completion_snapshot_strict.*` 를 함께 본다.

### A.2 배치 집계(`accuracy_summary`) 읽는 순서

1. **`n_success` / `failed`** — 데이터·팩터·연구 단계 실패 여부.
2. **`n_symbols_finite_hit`**, **`mean_directional_hit_rate`**, **`median_directional_hit_rate`**  
   - 배치는 `final_unseen`에서 **유한 `directional_hit_rate`·`mae_ratio_sys_over_naive`를 가진 첫 행**을 종목 대표로 쓴다(`strict_multi_cycle_batch._pick_best_final_row`).  
   - JSON 전체의 `rank_score` 최댓값 행과 다를 수 있으므로, **종목별 깊은 비교는 해당 심볼의 `strict_multi_cycle_*.json`의 `final_unseen` 정렬·`rank_score`를 직접 확인**한다.
3. **`mean_mae_ratio_sys_over_naive`** — **1에 가까울수록** naive(현재가 유지) 대비 수준 오차가 비슷함. **1 미만**이면 수준 예측에서 상대 개선 후보.
4. **`best_by_symbol` 테이블** — 심볼별 `hit_rate`, `mae_ratio`, **`coverage`(trust_coverage)**  
   - hit만 높고 coverage가 매우 낮으면 **거래/신호 빈도가 실전 기여도와 분리**될 수 있음 → “좋은 숫자”로 오판하지 않기.
5. **`similar_pairs_top20`** — 공식 구조 유사도·hit/mae 갭; **과적합 복제** 여부 탐색용.

### A.3 실전 해석 시 반드시 덧붙일 문장 (가정)

- 본 파이프라인 지표는 **수수료·슬리피지·펀딩·체결**을 포함하지 않는다.
- **메이저 vs 알트**는 변동성·유동성이 다르므로, 집계 평균만으로 “전 종목 엣지”를 말하지 말고 **버킷 분리**(BTC/ETH/SOL 등 vs 나머지)를 권장한다.
- **단기 창·단일 주기(예: 1h·30d 스냅샷)** 이면 regime 변화에 취약하다.

### A.4 “통과/보류” 휴리스틱 (내부 기준 예시, 고정 아님)

| 구분 | 보수적 참고 |
|------|----------------|
| 집계 hit | 비용 감안 시 **64%대 이상**을 별도 실험으로 검증 목표로 두기 쉬움 |
| MAE ratio | **0.92 이하**를 “수준 예측 강화” 후보로 두고, 달성 시 naive 대비 의미 검증 |
| coverage | hit 해석 시 **최소 coverage 하한**(예: 0.3) 미만은 “보조 지표”로만 취급 검토 |

---

## B. Gap / Tension 기반 필터링 전략 설계 (구현 전 스펙)

### B.1 이미 있는 코드 (재사용)

- **간격·분산 요약**: `code/predictor_gap_metrics.py` — `system_gap_metrics`, `mean_pairwise_rel`, 시스템가 대비 현재가 괴리 등.
- **텐션 블렌드(시스템가)**: `code/system_price_rules.py` — `p_system_tension_blend` (`mean_pairwise_rel` 클수록 현재가 쪽).
- **바 단위 갭 리서치 프레임**: `code/vbt_gap_research.py` — `include_system_variants=True` 시 `p_system_tension` 등 컬럼 생성.

### B.2 strict multi-cycle에 넣을 때의 계층 (권장)

1. **필터 레이어(연구 외)**  
   - 바마다 `gap_sys`(또는 `mean_pairwise_per_atr`)가 **임계 이상일 때만** “신호 유효”로 카운트하거나, 백테스트 진입 조건으로 제한.  
   - 목표: **hit는 낮아도 되니 거래 횟수 대비 기대값**을 올리거나, **노이즈 구간 제외**로 hit 자체 상승.
2. **피처 레이어**  
   - factors CSV 또는 연구 입력에 **갭·롤링 갭 변화율** 컬럼을 추가해, trust 분위(`trust_q_*`)와 **교차**되게 탐색.
3. **검증**  
   - 필터를 켠 채로 **동일 unseen 슬라이스**에서만 hit/mae/coverage를 재산출하는 스크립트 분기(새 CLI 플래그 또는 별도 리포트)를 두어, 필터 없음과 **동일 계보**로 비교.

### B.3 구현됨: `strict_multi_cycle_research` CLI

Trust(또는 전체 val) 적용 **이후** `merged_validation_df` 행에 대해 한 번 더 필터한다.

| 인자 | 의미 |
|------|------|
| `--eval-gap-filter-column` | 예: `mean_pairwise_per_atr`, `mean_pairwise_rel`, `p_system_tension` |
| `--eval-gap-filter-min` | 해당 컬럼 ≥ 값인 봉만 hit/mae/Spearman/trade 집계 |
| `--eval-gap-filter-max` | 해당 컬럼 ≤ 값 (상한·밴드와 병행 가능) |

컬럼만 주고 min/max 없으면 **비활성**(경고). min/max만 있고 컬럼 없으면 **비활성**(경고).  
JSON `config` 및 MD 상단에 동일 설정이 기록되며, 메트릭에 `eval_gap_filter_coverage`, `n_rows_after_eval_gap_filter` 등이 붙는다.

### B.4 배치 래퍼

`strict_multi_cycle_batch.py`에 동일 이름의 `--eval-gap-filter-column|min|max` 가 있으면 각 종목 `strict_multi_cycle_research` 호출에 그대로 넘긴다.

### B.5 다음 확장(선택)

- `temporal_validation` 층 공용 마스크 API로 분리해 다른 러너에서 재사용.

---

## C. MAE Ratio 개선 + Level Prediction 강화 방향

### C.1 코드·개념 연결

- **Shrink 가중**: 이미 공식군에 `shrink_weight`(예: 0.94–0.97) 그리드가 있음 — **현재가 쏠림**과 MAE·hit 트레이드오프 탐색 축.
- **Tension 시스템가**: `p_system_tension_blend` — 앵커 분산(긴장)이 클 때 레벨을 **현재가 쪽으로 당김** → 급변장에서 MAE 완화 vs 방향 왜곡 트레이드오프.
- **복합 점수**: `strict_multi_cycle_research` 내 `_composite_score` — MAE 항은 `1/mae` 형태로 **낮은 MAE에 보수**; 가중치는 `schemas/strict_multi_cycle_composite.example.json` 등으로 조정 가능.

### C.2 개선 방향 (설계)

1. **캘리브레이션 층**: 시스템가 대비 실현 수익 구간이 아닌 **가격 오차 분포**를 구간별로 맞추는(quantile mapping 등) 연구는 `research/` 측에 두고, strict JSON에는 **추가 메트릭**만 기록하는 방식 권장.  
2. **손실 가중 MAE**: 큰 오차 바에 가중을 두어 **꼬리 리스크**를 composite에 반영하는 옵션.  
3. **Regime별 shrink**: 변동성 레짐(예: ATR 분위)별로 `shrink_weight`·`trust` q 범위를 스위칭 — **D와 연계** 가능.

### C.3 구현됨

- `system_price_skill.compute_system_price_skill` 가 **`mae_ratio_sys_over_naive_p90`**(봉별 오차비율의 90%분위)를 반환.
- `strict_multi_cycle_research` 에 **`--w-mae-tail`** 및 `composite_weights.w_mae_tail`(기본 0).  
  `composite_score` = `w_mae * (1/mae_mean) + w_mae_tail * (1/mae_p90) + …` (p90 비유한 시 tail 항은 mean 항과 동일 스케일로 대체).

---

## D. Ensemble / Multi-Formula Strategy 설계

### D.1 데이터 소스

- 단일 종목 `strict_multi_cycle_*.json`의 **`final_unseen`** 다행은 이미 **여러 (family, embargo, shrink, trust) 조합**에 대한 메트릭을 담는다.
- 배치 `best_by_symbol`은 현재 **대표 1행**(배치 규칙상 유한 hit·mae 첫 행)만 요약한다.

### D.2 앙상블 패턴 (권장 순서)

1. **투표/다수결**: unseen 슬라이스에서 상위 K개 공식의 **방향 부호 일치율**이 임계 이상일 때만 포지션.  
2. **가중 평균 가격**: `composite_rank_score` 또는 역 MAE로 가중한 **시스템가 블렌드** → 단일 공식 대비 MAE·hit 재평가.  
3. **스택 메타**: 종목별로 “언제 어떤 cluster_key가 안정적인지”를 **holdout 메타 레이어**에서 학습(샘플 수 부족 시 보류).

### D.3 구현됨(프록시)

- **`scripts/ensemble_unseen_eval.py`**: `--json data/runs/strict_multi_cycle_btc.json --top-k 3` → `final_unseen` 상위 K의 hit·mae·p90·coverage **평균·표준편차**(바 단위 앙상블 아님).
- 배치 JSON에 `ensemble_summary` 자동 병합은 **미구현**(필요 시 배치 후 스크립트만 돌리면 됨).

---

## 문서·코드 상호 참조

| 주제 | 파일 |
|------|------|
| 완성 체크리스트 | `docs/STRICT_RESEARCH_COMPLETION_CHECKLIST.md` |
| 50종 유니버스 | `scripts/strict_multi_cycle_universe.py` |
| 배치·집계 | `scripts/strict_multi_cycle_batch.py` |
| 단일 연구·composite | `scripts/strict_multi_cycle_research.py` |
| 프록시 앙상블 요약 | `scripts/ensemble_unseen_eval.py` |
| 갭 메트릭 | `code/predictor_gap_metrics.py` |
| 텐션·쏠림 | `code/system_price_rules.py` |
| 갭 시계열 연구 | `code/vbt_gap_research.py` |
| 간격 토폴로지 설계 메모 | `chat/무한_예측가_운영_설계.md` (0-1절) |

---

**정리:** A는 위 프레임으로 **50종 요약 + 종목별 coverage + 체크리스트**를 묶어 읽는다. B·C·D는 **이 저장소에 이미 있는 갭/텐션/shrink/composite**를 기준으로 한 **구현 순서가 있는 설계**이며, 실제 코드 변경은 B → C → D 순으로 작은 PR 단위를 권장한다.

---

## 반복 사이클 · 공식 추림 (운영 루프)

### 바이낸스 거래대금(quoteVolume) 상위 N — 실제 캔들 데이터

1. **유니버스 파일**(BASE 한 줄에 하나, Binance 24h 티커 기준):
   ```text
   python scripts/fetch_binance_top_usdt_by_volume.py --top 100
   ```
   (기본 출력: `data/universe/binance_usdt_top100_by_quote_volume.txt`)

2. **배치**(각 종목은 `fetch_btc_ohlcv.py` 가 **klines 캔들**로 CSV 저장 → 동일 캔들로 strict 검증):
   ```text
   python scripts/strict_multi_cycle_batch.py --symbols-file data/universe/binance_usdt_top100_by_quote_volume.txt --fetch-missing --parallel 2 --out-summary-json data/runs/strict_multi_cycle_summary_top100.json --out-summary-md data/runs/strict_multi_cycle_summary_top100.md
   ```

3. **시드별 여러 번(요약 파일 분리)**:
   ```text
   python scripts/run_top_volume_research_repeated.py --top 100 --repeats 3 --parallel 2 --fetch-missing
   ```
   산출 예: `data/runs/strict_multi_cycle_summary_top100_run0.json` … `run2.json` (일부 신규 종목은 캔들 부족으로 실패할 수 있음 → 스크립트는 기본적으로 다음 repeat 계속)

4. **배치 재실행** (데이터·설정 갱신 시마다):
   ```text
   python scripts/strict_multi_cycle_batch.py --fetch-missing --parallel 2
   ```
   산출: `data/runs/strict_multi_cycle_summary_50.json`

5. **한 번에 배치 + 큐레이션**:
   ```text
   python scripts/strict_research_cycle.py --fetch-missing --parallel 2
   ```
   배치만 생략: `--skip-batch` / 큐레이션만 생략: `--skip-curate`

6. **우리 공식 후보 추리기** (`min_hit`·coverage·mae 컷 + 전역 상위 K개 `cluster_key`):
   ```text
   python scripts/curate_strict_formulas.py --summary-json data/runs/strict_multi_cycle_summary_50.json --min-hit 0.55 --min-coverage 0.2 --max-mae-ratio 1.05 --shortlist-k 8
   ```
   산출: `data/runs/curated_formula_shortlist.json`, `.md`

`shortlist_global_top_k` 가 **여러 종목에서 반복 등장하는 공식 구조**를 우선 보여 주므로, 그중에서 운용용 **소수(예: 3~5개)** 를 팀 기준으로 확정하면 된다.
