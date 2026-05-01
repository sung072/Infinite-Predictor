# Strict Multi-Cycle Research Result

- symbol: `APE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5402 | 0.9901 | 0.3256 | 1.1523 | 9.1575 | 1.6245 | 0.6422 | 0.6422 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5402 | 0.9913 | 0.3256 | 1.1523 | 9.1575 | 1.6245 | 0.6414 | 0.6414 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5402 | 0.9930 | 0.3256 | 1.1523 | 9.1575 | 1.6245 | 0.6405 | 0.6405 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5402 | 0.9948 | 0.3256 | 1.1523 | 9.1575 | 1.6245 | 0.6397 | 0.6397 |
| `base|emb=12|sh=0.95` | 18 | 0.5051 | 0.9979 | 1.0000 | 1.0427 | 0.4118 | 0.4640 | 0.5778 | 0.5778 |
| `base|emb=12|sh=0.94` | 18 | 0.5051 | 0.9984 | 1.0000 | 1.0427 | 0.4118 | 0.4640 | 0.5776 | 0.5776 |
| `base|emb=12|sh=0.96` | 18 | 0.5051 | 0.9982 | 1.0000 | 1.0427 | 0.4118 | 0.4640 | 0.5776 | 0.5776 |
| `base|emb=12|sh=0.97` | 18 | 0.5051 | 0.9985 | 1.0000 | 1.0427 | 0.4118 | 0.4640 | 0.5774 | 0.5774 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4873 | 0.9971 | 0.4028 | 1.1594 | -2.2793 | 0.9169 | 0.5625 | 0.5625 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4873 | 0.9970 | 0.4028 | 1.1594 | -2.2793 | 0.9169 | 0.5625 | 0.5625 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4873 | 0.9970 | 0.4028 | 1.1594 | -2.2793 | 0.9169 | 0.5624 | 0.5624 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4873 | 0.9973 | 0.4028 | 1.1594 | -2.2793 | 0.9169 | 0.5623 | 0.5623 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5200 | 1.0034 | 0.3241 | 2.1498 | 5.4160 | 0.6028 | 0.5504 | 0.5504 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5200 | 1.0063 | 0.3241 | 2.1498 | 5.4160 | 0.6028 | 0.5495 | 0.5495 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5200 | 1.0092 | 0.3241 | 2.1498 | 5.4160 | 0.6028 | 0.5486 | 0.5486 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5200 | 1.0124 | 0.3241 | 2.1498 | 5.4160 | 0.6028 | 0.5478 | 0.5478 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4810 | 0.9957 | 0.4213 | 0.9184 | -8.3785 | 0.3639 | 0.5411 | 0.5411 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4810 | 0.9957 | 0.4213 | 0.9184 | -8.3785 | 0.3639 | 0.5410 | 0.5410 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4810 | 0.9961 | 0.4213 | 0.9184 | -8.3785 | 0.3639 | 0.5408 | 0.5408 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4810 | 0.9969 | 0.4213 | 0.9184 | -8.3785 | 0.3639 | 0.5404 | 0.5404 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8114

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6156 | 0.0579 | 0.9811 | 0.0251 |
| all validations | 0.5045 | 0.0995 | 0.9981 | 0.0252 |

- improvement vs all (primary fraction): `hit +11.11pp, mae +1.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.95` | 0.4706 | 1.0463 | 1.0000 | 0.8337 | -0.1131 | -10.5835 | -0.6596 | 0.3457 | 0.3457 |
| 2 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3333 | 1.0803 | 0.5278 | 0.8836 | -0.3139 | -29.3813 | -0.6849 | 0.3075 | 0.3075 |
| 3 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3333 | 1.1097 | 0.5278 | 0.8836 | -0.3139 | -29.3813 | -0.6849 | 0.2976 | 0.2976 |
| 4 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3333 | 1.1432 | 0.5278 | 0.8836 | -0.3139 | -29.3813 | -0.6849 | 0.2871 | 0.2871 |
| 5 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3333 | 1.1767 | 0.5278 | 0.8836 | -0.3139 | -29.3813 | -0.6849 | 0.2771 | 0.2771 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 1.0116 | 0.5891 | -16.9927 | -0.5039 |
| 1 | 7 | 0.6667 | 0.9378 | 0.7193 | 14.9077 | 1.0369 |
| 2 | 7 | 0.4286 | 1.1079 | 2.6328 | 25.3387 | 1.2774 |
| 3 | 7 | 0.5000 | 1.1789 | 0.9033 | -3.5834 | -0.1131 |
| 4 | 7 | 0.2857 | 1.0863 | 0.5254 | -58.9802 | -1.9321 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 1.0116 | 0.5891 | -16.9927 | -0.5039 |
| top_20pct | 8 | 0.3750 | 1.0711 | 0.3945 | -51.6344 | -1.9979 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.7500 | 0.9730 | 0.4080 | 6.8893 | 0.2345 |
| 1 | 7 | 0.5714 | 0.9428 | 0.8547 | 5.1438 | 0.2041 |
| 2 | 7 | 0.5000 | 1.0130 | 0.6451 | -16.4981 | -1.1568 |
| 3 | 7 | 0.2857 | 1.2471 | 0.7073 | -49.0873 | -1.0000 |
| 4 | 7 | 0.1667 | 1.2520 | 0.8179 | -50.7416 | -0.8646 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.7500 | 0.9730 | 0.4080 | 6.8893 | 0.2345 |
| top_20pct | 8 | 0.2857 | 1.2224 | 0.5136 | -43.4473 | -0.8585 |

