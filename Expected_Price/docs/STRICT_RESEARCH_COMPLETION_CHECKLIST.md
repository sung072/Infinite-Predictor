# Strict 연구 시스템 — “완성 선언” 체크리스트

한 실험(또는 한 종목 배치)을 **내부 리포트·재현 가능한 스냅샷**으로 고정할 때 아래를 채우면 된다.  
(실거래·슬리피지·체결 등은 이 목록 범위 밖이다.)

## 1. 재현성

- [ ] **Git 커밋 해시** 기록 (또는 태그). 결과 JSON/MD 상단 메모에 붙여도 된다.
- [ ] **실행 명령 전체** 보존: `strict_multi_cycle_research.py` / `strict_multi_cycle_batch.py` 인자, `--composite-config` 경로, `--seed`.
- [ ] **데이터 스냅샷**: 사용한 OHLCV·factors CSV 경로와 (가능하면) 파일 수정 시각 또는 체크섬.
- [ ] **스키마**: `predictor_registry` 경로와 버전(파일명/해시).
- [ ] **결과 산출물**: `out-json`, `out-md`, 배치 시 `strict_multi_cycle_summary_50.json` 등 경로 고정.

## 2. 데이터·계보 (Lineage)

- [ ] **`strict_unseen_guard`** 확인: `unseen_starts_at_index`, `final_eval_uses_unseen_slice_only`, `unseen_used_in_discovery_or_meta_validation=false`.
- [ ] **`ranking_policy`**: `meta_composite_norm`, `final_composite_norm`, `why_final_raw_default_ko`가 의도와 일치하는지.
- [ ] **Holdout**: `train_bars`, `val_bars`, `embargo`, `bars_per_year` 기록.

## 3. 지표·선정 논리

- [ ] **메타**: `composite_norm`, `weights_equal_to_preset` 또는 커스텀 가중치 명시.
- [ ] **최종 unseen**: `comp_raw` vs `rank_score` (`composite_norm_final=raw`면 동일해야 함).
- [ ] **코호트**: `dev_cohort_top_fraction` + 필요 시 `--cohort-sensitivity` 및 `vs all` 해석 한 줄.
- [ ] **`risk_metrics_legend`** 및 `composite_formula` (예시: `schemas/strict_multi_cycle_composite.example.json`)와 결과가 모순 없는지.

## 4. 한 페이지 Executive 요약 (권장)

- [ ] 심볼·기간(또는 바 수)·**best cluster_key**.
- [ ] **Final unseen**: hit, mae_ratio, mean_rr, sharpe_ann, calmar, comp_raw.
- [ ] **한 줄 결론**: “dev 상위 코호트 대비 unseen이 유지/악화/샘플부족” 중 무엇에 가까운지 (수치 인용).
- [ ] **한 줄 한계**: 짧은 val 창, 단일 심볼, 비용 미포함 등 스스로 제약 명시.

## 5. 자동 검증 (이 저장소)

- [ ] `python -m pytest tests/ -q` 통과 (CI 또는 로컬).
- [ ] (선택) `python scripts/strict_multi_cycle_research.py ...` 단일 심볼 스모크로 JSON 스키마 확인.

---

위 **1~4를 한 번에 채우면** “이 연구 설정으로는 우리 strict 파이프라인은 완료했다”고 말해도 된다.  
**5**는 그 선언이 깨지지 않게 하는 안전장치다.

**다종목(50종) 요약 해석·Gap/Tension·MAE·앙상블 로드맵:** `STRICT_MULTI_CYCLE_ANALYSIS_AND_NEXT_STEPS.md`

---

## 자동 채움 스냅샷 (에이전트 실행 · 로컬 · 2026-05-01)

아래는 이 워크스페이스에서 **실제로 실행해 채운 값**이다. Git이 없으면 해시는 비움.  
**원 스냅샷 JSON 전문:** `data/runs/completion_snapshot_strict.json` · MD: `data/runs/completion_snapshot_strict.md`

### 1. 재현성

- [x] **Git 커밋 해시**: 워크스페이스에 `.git` 없음 → `N/A` (저장소를 git으로 관리하면 여기에 `git rev-parse HEAD` 기록)
- [x] **실행 명령 (스냅샷 생성)**  
  `python scripts/strict_multi_cycle_research.py --symbol BTC --out-json data/runs/completion_snapshot_strict.json --out-md data/runs/completion_snapshot_strict.md --seed 0`  
  (실행 시 `--cohort-sensitivity` 가 켜진 채로 기록됨 → JSON의 `config.cohort_sensitivity` 참고. 동일 조건 재현 시 명시 권장.)
- [x] **데이터 스냅샷**
  - OHLCV: `data/btcusdt_1h_30d.csv` (크기 67827 bytes, UTC 수정시각 `2026-04-30T15:51:12.9523960Z`)
  - Factors: `data/derived/btcusdt_factors_4p.csv`
- [x] **스키마**: `schemas/predictor_registry.btc_4p.json` (스크립트 기본)
- [x] **결과 산출물**: 위 `completion_snapshot_strict.json` / `.md`

### 2. 데이터·계보 (Lineage)

스냅샷 JSON `strict_unseen_guard` 발췌:

- [x] `unseen_starts_at_index`: **540**
- [x] `final_eval_uses_unseen_slice_only`: **[0, 180]**
- [x] `unseen_used_in_discovery_or_meta_validation`: **false**
- [x] `ranking_policy`: `meta_composite_norm` **raw**, `final_composite_norm` **raw** (의도: 최종 peer z 미사용)

### 3. 지표·선정 논리

- [x] **메타**: `composite_norm` **raw**, `weights_equal_to_preset` **balanced** (`w_mae`…`w_calmar` 기본과 일치)
- [x] **최종 unseen (`best_final` 콘솔 기준, 유한 지표가 있는 첫 후보와 일치)**:  
  `hit_rate 0.5429`, `mae_ratio 0.9797`, `coverage 1.0`, `mean_rr 0.8150`, `sharpe_ann -1.1170`, `calmar -0.1120`, `comp_raw 0.4995`, `rank_score 0.4995` → **raw 일치**
- [x] **대표 cluster_key (동일 수치의 JSON 행)**: `base|emb=24|sh=0.97`  
  (`final_unseen` 배열 순서는 degenerate trust 행이 앞에 올 수 있음 → **순위는 `rank_score` 정렬 결과·콘솔 best_final 기준**으로 읽을 것)
- [x] **코호트 (primary fraction 0.1)**: `n_eligible=372`, `top_n=38`, `cutoff_rank_score≈0.8222`  
  **vs all (해석)**: hit 약 **+14.8pp** (0.639 vs 0.491 근사), mae_ratio 상대 개선 약 **+3.7%rel** (전체 대비 top이 더 낮음)

### 4. 한 페이지 Executive 요약

- **심볼·바**: BTC, 전체 `n_total_rows` 등은 스냅샷 JSON `counts` 참고.
- **Best (unseen, 위 수치)**: `base|emb=24|sh=0.97` — hit≈0.54, mae_ratio≈0.98, comp_raw≈0.50.
- **한 줄 결론**: dev 상위 10% 코호트는 hit·mae가 전체 평균보다 유리하게 보이나, **최종 unseen 한 창**에서는 Sharpe/Calmar가 음수로 나와 **짧은 검증 구간·단일 슬라이스** 해석 한계가 큼.
- **한 줄 한계**: 비용·슬리피지·체결 없음, 단일 심볼·고정 레지스트리, trust 규칙 일부는 unseen에서 coverage 0으로 붕괴 가능.

### 5. 자동 검증

- [x] `python -m pytest tests/ -q` → **161 passed** (경고 1: Spearman 상수 입력)
- [x] `python scripts/verify_expected_price_stack.py` → **OK** (161 tests)

### 재실행 한 줄

```text
cd Expected_Price
python scripts/strict_multi_cycle_research.py --symbol BTC --out-json data/runs/completion_snapshot_strict.json --out-md data/runs/completion_snapshot_strict.md --seed 0
```
