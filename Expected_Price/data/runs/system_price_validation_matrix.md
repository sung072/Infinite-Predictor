# 시스템가 검증 매트릭스 리포트 (연구용)

- 목적: 종목·구간(full/OOS/WF)별로 시스템가가 단순 기준(`P_now`)보다 일관되게 나은지 점검
- 시스템가 열: `p_system_shrunk_custom`
- custom shrink weight: `0.960` (system_col=`p_system_shrunk_custom` 일 때 사용)
- 판정 규칙(연구용): `hit_rate >= min_hit_rate` AND `mae_ratio <= max_mae_ratio`
- 현재 임계값: `min_hit_rate=0.505`, `max_mae_ratio=1.000`
- PASS 집계 범위: `OOS/WF only`

## 케이스별 결과

| case | n_used | hit_rate | 95% CI | p(hit>0.5) | mae_ratio | mae_gain% | spearman(signed_sys,fwd_1) | pass |
|------|--------|----------|--------|------------|-----------|-----------|----------------------------|------|
| `BTC-oos` | 177 | 0.5424 | [0.4689, 0.6141] | 0.1298 | 0.9824 | 1.76 | 0.1552 | PASS |
| `BTC-full` | 719 | 0.5216 | [0.4850, 0.5579] | 0.1238 | 0.9967 | 0.33 | 0.0593 | PASS |
| `ETH-oos` | 177 | 0.5227 | [0.4492, 0.5952] | 0.2732 | 0.9974 | 0.26 | 0.1032 | PASS |
| `ETH-wf` | 431 | 0.5058 | [0.4587, 0.5529] | 0.4046 | 0.9987 | 0.13 | 0.0264 | PASS |
| `ETH-full` | 716 | 0.4902 | [0.4537, 0.5268] | 0.6998 | 0.9996 | 0.04 | 0.0154 | FAIL |
| `BTC-wf` | 431 | 0.5081 | [0.4611, 0.5550] | 0.3680 | 1.0000 | 0.00 | 0.0465 | PASS |

## 요약

- hit_rate 기준 통과: **4/4**
- mae_ratio 기준 통과: **4/4**
- 동시 통과(PASS): **4/4**

## 실패 원인 분해(간단)

- `BTC` best-case=`BTC-oos`: mae_ratio=0.9824, hit_rate=0.5424
- `ETH` best-case=`ETH-oos`: mae_ratio=0.9974, hit_rate=0.5227

## 해석 주의

- 본 리포트는 연구용 검증 요약이며, 매매 권고/수익 보장을 의미하지 않음.
- WF/OOS를 우선 신뢰하고, full은 참고치로만 사용 권장.
- p(hit>0.5)는 정규근사 기반 단순값(독립성 가정)으로 참고용임.

## AI 추천(보조)

- 기본 원칙: `mae_ratio <= 1`을 우선, `hit_rate`는 보조 지표로 유지
- OOS/WF PASS가 유지되면 임계값 고정, 깨지면 `symbol_shrink_weights`만 소폭 재튜닝
- full 구간 FAIL은 경보 참고치로만 사용(운영 판정은 OOS/WF 우선)
- (LLM 호출 실패 또는 키 미설정: 규칙 추천으로 대체)
