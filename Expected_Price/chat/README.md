# 무한 예측가 · 수평선 간격(distant topology) 패키지

대화·계획·연구 코드를 한곳에 모은 폴더입니다.

**빠른 링크:** [루트 README (시작)](../README.md) · [로컬/CI 셋업 (QUICKSTART)](../docs/QUICKSTART.md) · [scripts/ (run_ci·부트스트랩)](../scripts/)

## 포함 파일

| 파일 | 설명 |
|------|------|
| [무한_예측가_운영_설계.md](./무한_예측가_운영_설계.md) | Cursor 계획서 원본 복사본. 운영 모토, 가격 환산, gap topology, 역사 이벤트 채굴, 검증·합성·청산 게이트 등 전체 설계. |
| [대화_요약.md](./대화_요약.md) | 본 주제로 나눈 대화 요약(산출물이 하나가 아님을 정리). |
| [code/predictor_gap_metrics.py](./code/predictor_gap_metrics.py) | 연구 레이어 스칼라(간격·응집도). `anchor_prices_for_ids` = Registry `id` 키 계약. |
| [code/predictor_registry.py](./code/predictor_registry.py) | Registry JSON 로드·검증(표준 라이브러리). |
| [code/vbt_research_stub.py](./code/vbt_research_stub.py) | VectorBT 전 `research_pipeline_stub` (gap 행만). |
| [../schemas/](../schemas/) | `predictor_registry` JSON Schema + 예시. |
| [../docs/abc_event_spec.md](../docs/abc_event_spec.md) | `abc` / `abc+de` 바·누수 1p 스펙. |
| [../docs/price_unification.md](../docs/price_unification.md) | “모든 축 → 가격 수평선”·거래량/시간 가격화·FDR 링크. |
| [../docs/dynamic_predictors.md](../docs/dynamic_predictors.md) | **동적(학습) 예측가**·무한 후보 vs 유한 실행·첫 RF 스파이크. |
| [../code/dynamic_volume_spike.py](../code/dynamic_volume_spike.py) | `train_volume_to_close`·artifact 저장(배치). |
| [../code/price_like.py](../code/price_like.py) | `volume_as_price` / `time_as_price` 등(합의·재현). |
| [../code/fdr_exploration.py](../code/fdr_exploration.py) | BH FDR, 탐색 cap, provenance `exploration`. |
| [../code/predictor_data_feed.py](../code/predictor_data_feed.py) | `--factors-csv` + `meta.factor_column` → 예측가(절대가) 머지. |
| [../data/sample_factors.csv](../data/sample_factors.csv) | [sample_ohlcv](data/sample_ohlcv.csv)과 짝(데모). |
| [../code/repro_experiment.py](../code/repro_experiment.py) | 시드·config SHA256·`data_snapshot_id`·실험 지문. |
| [../code/vbt_gap_research.py](../code/vbt_gap_research.py) | OHLCV(합성/CSV) + vbt rolling + gap 시계열 + provenance. |
| [../code/run_registry_research.py](../code/run_registry_research.py) | Registry id → gap (CLI: `--split full|oos|wf`, `--train-frac`, `--wf-train`/`--wf-test`, …). |
| [../code/walkforward_oos.py](../code/walkforward_oos.py) | OOS 슬라이스·롤 WF 폴드(바 기준) 정의. |
| [../data/sample_ohlcv.csv](../data/sample_ohlcv.csv) | `load_ohlcv_csv`·Registry 연동 스모크용. |
| [../requirements-research.txt](../requirements-research.txt) | `vectorbt` / `pandas` / `numpy` (연구용). |

## 다른 위치에만 있는 것

- **계획서 원본(YAML 헤더 포함)**: `%USERPROFILE%\.cursor\plans\무한_예측가_운영_설계_daf4287d.plan.md`
- (선택) **다른 모노레포의 `research/predictor_gap_metrics.py`**: 이 패키지 `code/`가 소스이면 **여기**를 정본으로 쓰면 됨.

## 연결 상태

- **실거래·서비스 경로**: 이 패키지 내용은 문서·연구 참고용입니다. `predictor_gap_metrics`는 `services/` 에서 호출하지 않습니다(프로젝트 규칙: 실시간에서 VectorBT 등 연구 엔진 금지와 동일한 취지로 연구 모듈만 유지).
- **구현된 것**: [schemas/](../schemas/) + [abc_event_spec](../docs/abc_event_spec.md) + [vbt_gap_research.py](../code/vbt_gap_research.py) + [repro_experiment.py](../code/repro_experiment.py) + `--price-like` ( [price_unification.md](../docs/price_unification.md) ) + [run_ci.py](../scripts/run_ci.py) (`unittest` + [execution_bridge](../code/execution_bridge.py) JSONL export·`replay` 검증). `python code/vbt_gap_research.py` 로 데모. **다음(미구현)**: 뉴스/페어 **실제** 가격 식, 대량·큐, 세션·Nautilus(연동은 [nautilus_bridge.py](../code/nautilus_bridge.py) 뼈대만).

## 스크린샷

계획서에서 참조하는 시각 모형 이미지(`스크린샷(244).png`)는 필요 시 이 폴더에 직접 넣으면 됩니다. 현재 저장소 스냅샷에는 해당 파일이 없었습니다.
