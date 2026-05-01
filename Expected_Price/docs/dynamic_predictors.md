# 동적 예측가 (AI 생성) — 연구·운영 합의

**모든 예측가 수평선은, 고정 수식(예: VWAP만)이 아닐 수 있으며, 최종 형태는  
「과거 데이터로 학습한 모델이 **상황(피처)에 따라** 실시간(또는 틱마다) 출력한 **하나의 가격(float)**」**으로 통일될 수 있다.  
(당장 구현이 전부 AI일 필요는 없다 — [price_unification.md](price_unification.md)의 **정적 `price_like`**·**factors CSV** 는 **배선·골격·감사**용일 수 있음.)

## 1) 정적 vs 동적(당신이 정한 쪽)

| 구분 | 정적(골격·감사) | 동적(대상) |
|------|----------------|------------|
| 규칙 | 합의된 **명시** 식/열 | **학습**으로 바뀌는 $f$ : 피처 → 가격 |
| 거래량·시간가 | [price_like.py](../code/price_like.py) 수준(연구·재현) | “이전과 비슷한 패턴일 때 **과거**가 **알려준** 가격/분포” (RF/LSTM·…) |
| 적응 | 수동 리밸런싱 | **배치 재학습** + Registry **version / model_id** |
| 비용(실행) | 낮음 | **유한 Active** + 경량 `predict`만 라이브(무한 **후보**는 **오프라인/연구**에서만) |

## 2) 무한 후보 + 유한 실행(당신이 정한 쪽)

- **생성(연구·AI·그리드)**: 후보 예측 함수·모델·가설은 **많이** 뽑을 수 있음(재학습·FDR·탐색 예산 [fdr_exploration.py](../code/fdr_exploration.py)).  
- **실행(Nautilus/세션)**: OOS·비용·게이트로 **Top-K Active**만(이미 [무한_예측가_운영_설계.md](../chat/무한_예측가_운영_설계.md)에 정렬).  
- **누수·과적합**: OOS/워크포워드(이미 `walkforward_oos`·OOS split) + “동적”일수록 **version·스냅** 필수 [repro_experiment.py](../code/repro_experiment.py).

## 3) 첫 구현(코드) — “거래량→가격” RF **스파이크**

- [dynamic_volume_spike.py](../code/dynamic_volume_spike.py) : OHLCV에서 `log1p(volume)`·lag 등으로 **배치 학습** → [dynamic_predictor_base.py](../code/dynamic_predictor_base.py)에 저장.  
- 목적은 “정답 SOTA”가 아니라 **간격 연구**에 넣을 **float 한 줄(예측가)** 을 **재현 가능**하게 뽑는 것(일관성 > 절대 MAE).  
- 다음 후보: **시간** 피처만 추가, LSTM(역시 `research/`·배치), **뉴스/임베딩**은 `factor_column`/별 테이블과 합침.

## 4) Q/A (요지만)

- **과적합?** → OOS·유한 실행·FDR이 모델이 “동적”일 때 **더** 중요(구조는 이미 수용).  
- **비용?** → **무한** = 오프라인. **라이브** = 학습된 $f$의 `predict` 한 번(가벼우면 **상수**와 같음).  
- **첫으로 고를 것** → **거래량→가격 RF 스파이크**가 **피처 적고·붙이기 쉬움**(이미 이 저장소에 추가).

## 5) Registry `meta` (구현됨)

`predictors[].meta`에 **둘 다** 넣는다(상대 경로는 **프로젝트 루트** 또는 **Registry 파일과 동일 폴더** 기준):

- `"model_artifact"`: `joblib` 경로(예: `artifacts/vol_to_close_spike.joblib`)
- `"model_kind"`: `"dynamic_volume_to_close"` — [dynamic_volume_spike.py](../code/dynamic_volume_spike.py) 추론

[run_registry_research.py](../code/run_registry_research.py) + [predictor_data_feed.py](../code/predictor_data_feed.py) 가 factors CSV **없이** `model_artifact`만 있어도 **병합 `predictor_prices_fn`** 을 켠다. 예: [predictor_registry.model_artifact.example.json](../schemas/predictor_registry.model_artifact.example.json).

**거래량가·시간가**의 “최종 형태”는 (B) **과거로 학습한 동적 예측가**가 기본이며, [price_unification.md](price_unification.md)의 `price_like`·factors는 **감사·골격**으로 병행 가능하다.
