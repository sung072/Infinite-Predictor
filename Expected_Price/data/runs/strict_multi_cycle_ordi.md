# Strict Multi-Cycle Research Result

- symbol: `ORDI`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4805 | 1.0049 | 0.4151 | 1.3312 | -7.9522 | 1.1007 | 0.6184 | 0.6184 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4805 | 1.0088 | 0.4151 | 1.3312 | -7.9522 | 1.1007 | 0.6170 | 0.6170 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4805 | 1.0134 | 0.4151 | 1.3312 | -7.9522 | 1.1007 | 0.6154 | 0.6154 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4805 | 1.0188 | 0.4151 | 1.3312 | -7.9522 | 1.1007 | 0.6136 | 0.6136 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5157 | 0.9989 | 0.4136 | 1.0135 | 0.0550 | 0.8809 | 0.5765 | 0.5765 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5157 | 1.0008 | 0.4136 | 1.0135 | 0.0550 | 0.8809 | 0.5759 | 0.5759 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5157 | 1.0037 | 0.4136 | 1.0135 | 0.0550 | 0.8809 | 0.5749 | 0.5749 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5157 | 1.0071 | 0.4136 | 1.0135 | 0.0550 | 0.8809 | 0.5737 | 0.5737 |
| `base|emb=24|sh=0.97` | 18 | 0.4841 | 1.0027 | 1.0000 | 1.0004 | -4.7544 | 0.1766 | 0.5365 | 0.5365 |
| `base|emb=24|sh=0.96` | 18 | 0.4841 | 1.0064 | 1.0000 | 1.0004 | -4.7544 | 0.1766 | 0.5351 | 0.5351 |
| `base|emb=24|sh=0.95` | 18 | 0.4841 | 1.0113 | 1.0000 | 1.0004 | -4.7544 | 0.1766 | 0.5332 | 0.5332 |
| `base|emb=24|sh=0.94` | 18 | 0.4841 | 1.0175 | 1.0000 | 1.0004 | -4.7544 | 0.1766 | 0.5309 | 0.5309 |
| `base|emb=12|sh=0.97` | 18 | 0.4925 | 1.0014 | 1.0000 | 0.9306 | -6.5791 | 0.2919 | 0.5191 | 0.5191 |
| `base|emb=12|sh=0.96` | 18 | 0.4925 | 1.0048 | 1.0000 | 0.9306 | -6.5791 | 0.2919 | 0.5178 | 0.5178 |
| `base|emb=12|sh=0.95` | 18 | 0.4925 | 1.0093 | 1.0000 | 0.9306 | -6.5791 | 0.2919 | 0.5161 | 0.5161 |
| `base|emb=12|sh=0.94` | 18 | 0.4925 | 1.0150 | 1.0000 | 0.9306 | -6.5791 | 0.2919 | 0.5140 | 0.5140 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5336 | 0.9986 | 0.3349 | 0.8526 | -6.6161 | 2.0130 | 0.5105 | 0.5105 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5336 | 1.0032 | 0.3349 | 0.8526 | -6.6161 | 2.0130 | 0.5088 | 0.5088 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5336 | 1.0094 | 0.3349 | 0.8526 | -6.6161 | 2.0130 | 0.5065 | 0.5065 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5336 | 1.0171 | 0.3349 | 0.8526 | -6.6161 | 2.0130 | 0.5037 | 0.5037 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=312, top_n=32, cutoff=0.8243

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6442 | 0.0618 | 0.9790 | 0.0182 |
| all validations | 0.4991 | 0.1065 | 1.0083 | 0.0286 |

- improvement vs all (primary fraction): `hit +14.52pp, mae +2.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.5294 | 0.9918 | 1.0000 | 0.8219 | -0.0296 | -2.7683 | -0.3411 | 0.4289 | 0.4289 |
| 2 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4444 | 1.0070 | 0.2778 | 0.7057 | -0.2240 | -20.9655 | -0.5396 | 0.3530 | 0.3530 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4444 | 1.0093 | 0.2778 | 0.7057 | -0.2240 | -20.9655 | -0.5396 | 0.3521 | 0.3521 |
| 4 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4444 | 1.0116 | 0.2778 | 0.7057 | -0.2240 | -20.9655 | -0.5396 | 0.3512 | 0.3512 |
| 5 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4444 | 1.0139 | 0.2778 | 0.7057 | -0.2240 | -20.9655 | -0.5396 | 0.3503 | 0.3503 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.2857 | 1.0221 | 0.7332 | -43.8132 | -0.8580 |
| 1 | 7 | 0.8333 | 0.9677 | 0.1849 | -2.4090 | -0.0890 |
| 2 | 7 | 0.7143 | 0.9476 | 1.7382 | 61.5199 | 6.3834 |
| 3 | 7 | 0.2857 | 1.0217 | 0.5095 | -54.6081 | -0.9220 |
| 4 | 7 | 0.5714 | 0.9885 | 1.8136 | 33.4510 | 1.8511 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.2857 | 1.0221 | 0.7332 | -43.8132 | -0.8580 |
| top_20pct | 8 | 0.5000 | 0.9935 | 1.8676 | 23.7468 | 1.0551 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6250 | 0.9971 | 1.1435 | 21.2419 | 1.1012 |
| 1 | 7 | 0.4286 | 0.9733 | 0.6457 | -25.9952 | -1.0406 |
| 2 | 7 | 0.6667 | 0.9861 | 0.9200 | 26.1087 | 1.6220 |
| 3 | 7 | 0.4286 | 0.9938 | 1.4411 | 2.6188 | 0.1065 |
| 4 | 7 | 0.5000 | 1.0074 | 0.3117 | -32.1784 | -0.8736 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6250 | 0.9971 | 1.1435 | 21.2419 | 1.1012 |
| top_20pct | 8 | 0.5714 | 1.0058 | 0.2746 | -27.2297 | -0.8458 |

