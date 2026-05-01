# “모든 축 → 가격(수평선)” 통일 (연구 합의)

> **보완(동적)**: 수식·CSV가 아닌 **학습된 모델**이 바를 읽고 **float 예측가**를 뽑는 경로는 [dynamic_predictors.md](dynamic_predictors.md) + [dynamic_volume_spike.py](../code/dynamic_volume_spike.py) (RF 스파이크).

**원칙**: 뉴스·감성·**거래량**·**시간(장 세션, 이벤트 잔여)**·온체인·교차자산·레짬 등 *어떤* 후보나, 최종적으로 **같은 심볼(또는 합의된 기준)** 의 **가격 눈금(세로 축) 위에 한 점(라인)으로** 환산한 뒤, 그 값을 **예측가 `P_pred` / `predictor_prices[id]`** 로 쓴다. “데이터가 다 가격”이란 **차트·간격·시스템가 합성**이 한 캔버스에 모이기 위한 **의사결정 합의**이지, “모든 열을 OHLCV로 쓰라”는 뜻이 아니다(원시 유지·감사는 `meta`에 둔다).

## 1) 왜

- [predictor_gap_metrics](../code/predictor_gap_metrics.py)는 `anchors: id → **가격(양수)**` 를 전제로 **pairwise 거리**를 쓴다.  
- Registry의 `id`·`predictor_prices` 키·한 바 스냅 **모두** 같은 “가격” 단위이면, **FDR·OOS·퇴출**이 섞이지 않는다.

## 2) 대표 맵(코드: [../code/price_like.py](../code/price_like.py))

| 원천(직관)        | `price_like` 예시 함수            | 아이디어 |
|-------------------|------------------------------------|----------|
| 거래량 (volume)   | `volume_as_price`                 | `p_ref`·`vol_ref` 대비 **log_ratio / bps**로 미세 **가격** 오프셋 |
| 시간(주기·잔여)  | `time_as_price` (`cycle_utc_day` / `duration_log`) | *한 바*가 24h 중 어디/얼마나 “남았다”는 것을 **가격 축**에 띄움(해석=합의) |
| (원·환산)         | (별도) macro→자산, 스테이블/페어   | 합의된 **fx / basis** 뒤 **대상 자산** 가격으로 끝 |

**필수**: `docs/abc_event_spec.md` 의 **캔들 t·누수** 규칙을 끊지 말 것. “시간을 가격에 올렸다”해도, **지평·horizon**이 섞이면 **같은 `bar_t`에 넣지 말기**.

## 3) Registry

- `predictors[].id` = `predictor_prices` 키 = `anchors` 키.  
- “량가·시간가” 류도 **id 하나당 한 수평선**; 변환 식·`vol_ref`는 `meta` 또는 `version`·실험 `config`에 남겨 **재현**할 것.

## 4) FDR / 탐색

- [../code/fdr_exploration.py](../code/fdr_exploration.py) — `benjamini_hochberg`, `assert_exploration_cap`, `exploration_provenance`.  
- CLI: `run_registry_research.py` 의 `--n-hypotheses` / `--explore-cap` / `--fdr-q` 와 `out` json 의 `exploration` 필드.

## 5) 한 번에 켜기 (CLI)

```bash
python code/run_registry_research.py --price-like --n-bars 64
```

- Registry 예시 [predictor_registry.example.json](../schemas/predictor_registry.example.json) 에 `vol_as_price_demo` / `time_as_price_demo` 가 **등록**돼 있고, `resolve`에 **강제로 합류**되면(옵션 `--price-like`) OHLCV에서 **각 바** `bar_anchors_from_ohlcv` → gap. 나머지 id(뉴스·페어 등)는 **아직** 합의 전이면 `price_like` 모듈이 임시 스프레드로 **가격**만 맞춘다.
- **외부 예측가(절대가)**: [predictor_data_feed.py](../code/predictor_data_feed.py) + `predictors[].meta.factor_column` + `--factors-csv` ( [sample_factors.csv](../data/sample_factors.csv) + [sample_ohlcv.csv](../data/sample_ohlcv.csv) ) — `p_war` / `p_eth` 열이 **최종 수평선(가격)**.
