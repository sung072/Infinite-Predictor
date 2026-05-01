# ETH 홀드아웃 · 검증 구간 분위별 분석

- OHLCV: `data\ethusdt_1h_30d.csv`
- train=500, embargo=24, val=120
- shrink=0.96, system_col=`p_system_shrunk_custom`

## 전체 검증 구간(단일 지표)

```json
{
  "n_used": 119,
  "directional_hit_rate": 0.5169491525423728,
  "mae_sys_next_close": 5.952918711983291,
  "mae_naive_now_next_close": 5.926974789915974,
  "mae_ratio_sys_over_naive": 1.0043772620918614,
  "spearman_signed_sys_vs_fwd1": 0.04240848881925652,
  "system_col": "p_system_shrunk_custom",
  "shrink_weight": 0.96,
  "n_rows_validation": 120
}
```

[시스템가 검증 결과] (바로 직전까지 백테스트·예측가·시스템가 산출 후, 다음 검증 캔들들만 채점)
  · 검증에 사용한 표본 수(유효 행): 119
  · 방향 적중률 directional_hit_rate: 0.5169 (시스템가 방향과 다음 종가 방향이 같은 비율)
  · 대비 단순 기준 대비 오차 비율 mae_ratio_sys_over_naive: 1.0044 (< 1 이면 시스템가가 다음 종가에 더 가깝다)
  · Spearman(signed_sys_vs_now, fwd_1): 0.0424
  · 적용 시스템가 정의: `p_system_shrunk_custom`

한 줄: 정확도(방향)= 0.5169, 오차비율(naive 대비)= 1.0044 - 위 수치는 검증 캔들 구간에서만 계산됨.

---

**해석:** 분위별로 hit_rate·mae_ratio가 들쭉날쭉하면 레인지/추세·갭 크기에 따라 시스템가 유효성이 달라짐을 시사.

## 분위별 스킬 — `mean_pairwise_per_atr`

| quintile | n | mean_pairwise_per_atr_min | mean_pairwise_per_atr_max | directional_hit_rate | mae_ratio_sys_over_naive | spearman_signed_sys_vs_fwd1 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 24 | 1.3855 | 1.9137 | 0.6957 | 0.9804 | 0.2791 |
| 1 | 24 | 1.9178 | 2.3500 | 0.5833 | 1.0024 | 0.3713 |
| 2 | 24 | 2.3686 | 2.9046 | 0.3333 | 1.0198 | -0.1391 |
| 3 | 24 | 2.9579 | 3.5611 | 0.4348 | 1.0303 | 0.0208 |
| 4 | 24 | 3.5639 | 4.2827 | 0.5417 | 0.9834 | 0.2313 |


## 분위별 스킬 — `atr_14`

| quintile | n | atr_14_min | atr_14_max | directional_hit_rate | mae_ratio_sys_over_naive | spearman_signed_sys_vs_fwd1 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 24 | 6.7147 | 8.0553 | 0.4167 | 1.0187 | -0.0261 |
| 1 | 24 | 8.1218 | 13.0469 | 0.4783 | 1.0266 | 0.0226 |
| 2 | 24 | 13.6828 | 16.2458 | 0.7391 | 0.9925 | 0.3053 |
| 3 | 24 | 16.2844 | 17.9688 | 0.4583 | 1.0036 | 0.3922 |
| 4 | 24 | 18.0230 | 20.3684 | 0.5000 | 0.9984 | 0.1348 |


## 분위별 스킬 — `vbt_rolling_return_std`

| quintile | n | vbt_rolling_return_std_min | vbt_rolling_return_std_max | directional_hit_rate | mae_ratio_sys_over_naive | spearman_signed_sys_vs_fwd1 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 24 | 0.0004 | 0.0016 | 0.6364 | 0.9995 | 0.3271 |
| 1 | 24 | 0.0016 | 0.0026 | 0.4167 | 1.0074 | -0.0452 |
| 2 | 24 | 0.0027 | 0.0033 | 0.5833 | 1.0078 | 0.0374 |
| 3 | 24 | 0.0033 | 0.0045 | 0.5000 | 0.9924 | 0.1217 |
| 4 | 24 | 0.0046 | 0.0113 | 0.4583 | 1.0110 | 0.2365 |

