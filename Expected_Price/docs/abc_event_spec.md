# abc(백테스팅) 이벤트·스펙 — 1p 계약 (v0)

**목적**: `abc`는 **한 번의 백테 실험에서** 넣는 **조건·이벤트·구간(라벨)**의 집합. **지금(실측+메타) = `abc+de`**.  
같은 파이프라인에서 `Registry`의 예측가 `id`와, 바·시각·스냅 **행(row)** 키가 **한 줄로 맞게** 쓰인다.

## 1) 시간축 (필수)

- **캔들(바) 타임존**: 기본 `UTC`로 고정(문서/코드 동일). 다른 TZ를 쓰면 `abc`에 **이름+오프셋**을 쓴다.
- **캔들 `t`**: 인덱스는 **캔들 *종가/완성 시각*** 기준(정의는 한 가지만 쓴다) → OHLCV 소스·리샘플 규칙이 같아야 **재현**이 된다.
- **이벤트 시각(정보도착)**: `event_time` / `informed_time` / `candle_t` 를 **최소 둘** 쓰면 누수·오정렬이 줄어든다.
  - *정보도착(뉴스, 공시, 체인 인식)*: 그 시각 **이전** 캔들/피처는 사용 가능(사후에 확정된 **라벨**은 `abc` **내부**에서만, 피처로 섞는지 **체크리스트**로 끈다).

## 2) `abc` 한 행에 들어갈 식별자(최소)

| 필드 | 의미 |
|------|------|
| `bar_t` (또는 `timestamp`) | 위 정의에 맞는 캔들 끝 시각 |
| `symbol` (필요 시) | `Registry.predictors[].symbol` / 베뉴와 맞는 심볼 |
| `predictor_prices` | `predictor_id` → `float` (해당 `bar_t` 스냅에서 **동일 수평선(같은 horizon 맥락)**끼리만 비교) |
| (선택) `event_id` / `regime` | ab 구간·조건 풀 키(재현·FDR·탐색 횟수 합산에 씀) |

`predictor_prices` 키는 **반드시** [schemas/predictor_registry.schema.json](../schemas/predictor_registry.schema.json)의 `predictors[].id`와 동일해야 한다. gap 메트릭 `anchors` 딕셔너리 = 이 맵(부분집합 가능).

## 3) `de`(실측 확장) — `abc+de`일 때

- `de`는 **모델 밖**에서 쌓이는 **실시간/추가 메타**(API 지연, 펀딩, 유지증거금, 체인 플로우…). `abc` **재현**에는 넣지 않으면, **오프라인 동일** 실험을 **나중에** 다시 돌릴 수 있다(문서/스냅에 `data_snapshot_id` 권장).

## 4) 누수(한 줄 체크)

- [ ] 미래 캔들/미래 **확정 라벨**이 **과거** 피처/점수에 들어가지 않는가  
- [ ] 이벤트 DB "사실 확정" 시각이 **뉴스 도달**보다 늦다면, train 기준은 **정보가 시장에 도달한 t**  
- [ ] `horizon`이 다르면 **같은 bar_t에 넣지 않는다** (패널/창 분리)

**스키마/예**: [../schemas/](../schemas/)  
**gap 계산**: `code/predictor_gap_metrics.py` — `anchors` 키 = `predictor_id`.

## 5) OOS / 워크포워드(최소, 코드)

- **단일 OOS**: `code/run_registry_research.py --split oos --train-frac 0.7 --embargo N` — 앞 구간 train(버리기), `embargo` 뒤만 gap 연구. `oos` 메타·시간이 **provenance `config`에** 들어감.  
- **롤 WF**: `--split wf --wf-train ... --wf-test ... --embargo ...` — 각 **test** 구간만 gap 시계열, `fold` 열로 합침.

## 6) “다 축 → 가격”

거래량·시간·거시·감정 등 **모든 후보를 최종적으로 [가격 눈금(예측가)](price_unification.md) 위**에 올려 `predictor_prices` / gap과 맞출지(합의·`price_like`).

## 7) FDR / 탐색 (CLI)

- `code/run_registry_research.py` 에 `--n-hypotheses` · `--explore-cap` · `--fdr-q` + 출력 json 의 `exploration` 필드. p값·세부 FDR은 후속 **실제 통계**가 채움.
