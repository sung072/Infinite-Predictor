# Strict Multi-Cycle Research Result

- symbol: `STX`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5545 | 0.9917 | 0.3488 | 1.2708 | 7.2778 | 1.3016 | 0.6390 | 0.6390 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5545 | 0.9924 | 0.3488 | 1.2708 | 7.2778 | 1.3016 | 0.6388 | 0.6388 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5545 | 0.9935 | 0.3488 | 1.2708 | 7.2778 | 1.3016 | 0.6386 | 0.6386 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5545 | 0.9927 | 0.3488 | 1.2708 | 7.2778 | 1.3016 | 0.6385 | 0.6385 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4969 | 1.0058 | 0.4167 | 1.1630 | -2.0973 | 0.9182 | 0.5774 | 0.5774 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4969 | 1.0077 | 0.4167 | 1.1630 | -2.0973 | 0.9182 | 0.5768 | 0.5768 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4969 | 1.0097 | 0.4167 | 1.1630 | -2.0973 | 0.9182 | 0.5762 | 0.5762 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4969 | 1.0119 | 0.4167 | 1.1630 | -2.0973 | 0.9182 | 0.5755 | 0.5755 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5313 | 0.9982 | 0.3194 | 0.9162 | -2.3245 | 0.1632 | 0.5506 | 0.5506 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5313 | 1.0002 | 0.3194 | 0.9162 | -2.3245 | 0.1632 | 0.5499 | 0.5499 |
| `base|emb=12|sh=0.97` | 18 | 0.4942 | 1.0017 | 1.0000 | 1.1005 | -1.2260 | 0.5795 | 0.5486 | 0.5486 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5313 | 1.0040 | 0.3194 | 0.9162 | -2.3245 | 0.1632 | 0.5484 | 0.5484 |
| `base|emb=12|sh=0.96` | 18 | 0.4942 | 1.0039 | 1.0000 | 1.1005 | -1.2260 | 0.5795 | 0.5478 | 0.5478 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5313 | 1.0081 | 0.3194 | 0.9162 | -2.3245 | 0.1632 | 0.5469 | 0.5469 |
| `base|emb=12|sh=0.95` | 18 | 0.4942 | 1.0067 | 1.0000 | 1.1005 | -1.2260 | 0.5795 | 0.5467 | 0.5467 |
| `base|emb=12|sh=0.94` | 18 | 0.4942 | 1.0099 | 1.0000 | 1.1005 | -1.2260 | 0.5795 | 0.5455 | 0.5455 |
| `base|emb=24|sh=0.97` | 18 | 0.4941 | 1.0015 | 1.0000 | 1.0868 | -1.9509 | 0.3678 | 0.5423 | 0.5423 |
| `base|emb=24|sh=0.96` | 18 | 0.4941 | 1.0032 | 1.0000 | 1.0868 | -1.9509 | 0.3678 | 0.5417 | 0.5417 |
| `base|emb=24|sh=0.95` | 18 | 0.4941 | 1.0053 | 1.0000 | 1.0868 | -1.9509 | 0.3678 | 0.5409 | 0.5409 |
| `base|emb=24|sh=0.94` | 18 | 0.4941 | 1.0078 | 1.0000 | 1.0868 | -1.9509 | 0.3678 | 0.5399 | 0.5399 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8254

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5653 | 0.0833 | 0.9870 | 0.0261 |
| all validations | 0.5002 | 0.0972 | 1.0044 | 0.0262 |

- improvement vs all (primary fraction): `hit +6.51pp, mae +1.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5806 | 0.9811 | 0.9167 | 1.2477 | 0.1961 | 18.3584 | 1.8134 | 0.7869 | 0.7869 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5806 | 0.9842 | 0.9167 | 1.2477 | 0.1961 | 18.3584 | 1.8134 | 0.7856 | 0.7856 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5806 | 0.9874 | 0.9167 | 1.2477 | 0.1961 | 18.3584 | 1.8134 | 0.7843 | 0.7843 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5806 | 0.9905 | 0.9167 | 1.2477 | 0.1961 | 18.3584 | 1.8134 | 0.7830 | 0.7830 |
| 5 | `base|emb=12|sh=0.97` | 0.5882 | 0.9914 | 1.0000 | 0.7416 | 0.0214 | 1.9986 | 0.1106 | 0.6485 | 0.6485 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.4286 | 1.0365 | 0.8360 | -17.5281 | -0.4377 |
| 1 | 6 | 0.6000 | 0.9944 | 0.5655 | -5.4937 | -0.1611 |
| 2 | 7 | 0.5714 | 0.9441 | 2.0810 | 31.9999 | 2.5733 |
| 3 | 6 | 0.4000 | 1.0069 | 3.0001 | 23.1205 | 1.0796 |
| 4 | 7 | 0.8571 | 0.9090 | 4.0178 | 70.8736 | 23.2620 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.4286 | 1.0365 | 0.8360 | -17.5281 | -0.4377 |
| top_20pct | 7 | 0.8571 | 0.9090 | 4.0178 | 70.8736 | 23.2620 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.5000 | 0.9982 | 1.7297 | 21.1143 | 1.5986 |
| 1 | 6 | 0.8333 | 0.8732 | 0.7483 | 41.5083 | 2.7432 |
| 2 | 7 | 0.6667 | 0.9565 | 9.5389 | 76.9466 | 18.2228 |
| 3 | 6 | 0.3333 | 1.0448 | 0.9897 | -22.7189 | -1.4574 |
| 4 | 7 | 0.5714 | 0.9651 | 1.5285 | 26.9518 | 1.0374 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.5000 | 0.9982 | 1.7297 | 21.1143 | 1.5986 |
| top_20pct | 7 | 0.5714 | 0.9651 | 1.5285 | 26.9518 | 1.0374 |

