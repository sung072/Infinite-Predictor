# Strict Multi-Cycle Research Result

- symbol: `KAITO`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4649 | 1.0130 | 0.2577 | 1.2208 | -1.2866 | 1.2373 | 0.5453 | 0.5453 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4649 | 1.0176 | 0.2577 | 1.2208 | -1.2866 | 1.2373 | 0.5437 | 0.5437 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4649 | 1.0225 | 0.2577 | 1.2208 | -1.2866 | 1.2373 | 0.5421 | 0.5421 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4649 | 1.0279 | 0.2577 | 1.2208 | -1.2866 | 1.2373 | 0.5402 | 0.5402 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4465 | 1.0145 | 0.2407 | 1.1347 | 4.6542 | 0.3181 | 0.5183 | 0.5183 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4465 | 1.0195 | 0.2407 | 1.1347 | 4.6542 | 0.3181 | 0.5165 | 0.5165 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4465 | 1.0248 | 0.2407 | 1.1347 | 4.6542 | 0.3181 | 0.5147 | 0.5147 |
| `base|emb=24|sh=0.97` | 18 | 0.4698 | 1.0105 | 1.0000 | 1.0948 | -2.1447 | 0.2957 | 0.5137 | 0.5137 |
| `base|emb=12|sh=0.97` | 18 | 0.4603 | 1.0127 | 1.0000 | 1.0721 | -4.3631 | 0.0284 | 0.5128 | 0.5128 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4465 | 1.0307 | 0.2407 | 1.1347 | 4.6542 | 0.3181 | 0.5127 | 0.5127 |
| `base|emb=24|sh=0.96` | 18 | 0.4698 | 1.0159 | 1.0000 | 1.0948 | -2.1447 | 0.2957 | 0.5117 | 0.5117 |
| `base|emb=12|sh=0.96` | 18 | 0.4603 | 1.0185 | 1.0000 | 1.0721 | -4.3631 | 0.0284 | 0.5106 | 0.5106 |
| `base|emb=24|sh=0.95` | 18 | 0.4698 | 1.0219 | 1.0000 | 1.0948 | -2.1447 | 0.2957 | 0.5094 | 0.5094 |
| `base|emb=12|sh=0.95` | 18 | 0.4603 | 1.0249 | 1.0000 | 1.0721 | -4.3631 | 0.0284 | 0.5083 | 0.5083 |
| `base|emb=24|sh=0.94` | 18 | 0.4698 | 1.0292 | 1.0000 | 1.0948 | -2.1447 | 0.2957 | 0.5068 | 0.5068 |
| `base|emb=12|sh=0.94` | 18 | 0.4603 | 1.0323 | 1.0000 | 1.0721 | -4.3631 | 0.0284 | 0.5056 | 0.5056 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.3576 | 1.0322 | 0.3256 | 1.4847 | -12.1496 | -0.0281 | 0.4489 | 0.4489 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.3576 | 1.0445 | 0.3256 | 1.4847 | -12.1496 | -0.0281 | 0.4447 | 0.4447 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.3576 | 1.0570 | 0.3256 | 1.4847 | -12.1496 | -0.0281 | 0.4405 | 0.4405 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.3576 | 1.0698 | 0.3256 | 1.4847 | -12.1496 | -0.0281 | 0.4364 | 0.4364 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=328, top_n=33, cutoff=0.7950

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6370 | 0.0851 | 0.9887 | 0.0163 |
| all validations | 0.4295 | 0.1590 | 1.0301 | 0.0421 |

- improvement vs all (primary fraction): `hit +20.75pp, mae +4.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.5714 | 0.9936 | 1.0000 | 0.8771 | 0.0628 | 5.8803 | 0.2489 | 0.7120 | 0.7120 |
| 2 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5455 | 0.9716 | 0.3056 | 0.4877 | -0.2035 | -19.0482 | -0.4531 | 0.3800 | 0.3800 |
| 3 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5455 | 0.9763 | 0.3056 | 0.4877 | -0.2035 | -19.0482 | -0.4531 | 0.3780 | 0.3780 |
| 4 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5455 | 0.9811 | 0.3056 | 0.4877 | -0.2035 | -19.0482 | -0.4531 | 0.3760 | 0.3760 |
| 5 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5455 | 0.9858 | 0.3056 | 0.4877 | -0.2035 | -19.0482 | -0.4531 | 0.3740 | 0.3740 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 0.9992 | 0.3345 | -38.3165 | -0.7475 |
| 1 | 7 | 0.4286 | 1.0126 | 0.4687 | -41.2822 | -0.7180 |
| 2 | 7 | 0.5000 | 1.0038 | 2.1750 | 28.3820 | 4.1889 |
| 3 | 7 | 0.8571 | 0.9780 | 0.7918 | 65.1543 | n/a |
| 4 | 7 | 0.5714 | 0.9800 | 0.8650 | 5.0872 | 0.2983 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 0.9992 | 0.3345 | -38.3165 | -0.7475 |
| top_20pct | 8 | 0.6250 | 0.9812 | 0.9091 | 15.3778 | 1.0845 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6250 | 0.9697 | 0.5210 | -4.7793 | -0.1442 |
| 1 | 7 | 0.2857 | 1.0359 | 0.2967 | -79.2673 | -1.1709 |
| 2 | 7 | 0.5714 | 0.9868 | 0.4415 | -20.4906 | -0.9242 |
| 3 | 7 | 0.5714 | 0.9908 | 1.8053 | 33.0603 | 2.2763 |
| 4 | 7 | 0.8333 | 0.9824 | 1.9388 | 74.8237 | 8.8106 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6250 | 0.9697 | 0.5210 | -4.7793 | -0.1442 |
| top_20pct | 8 | 0.7143 | 0.9883 | 2.1129 | 56.3035 | 7.9387 |

