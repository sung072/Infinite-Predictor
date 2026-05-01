# Strict Multi-Cycle Research Result

- symbol: `TIA`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5303 | 0.9871 | 0.2762 | 1.1548 | 7.7016 | 1.5640 | 0.6146 | 0.6146 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5303 | 0.9860 | 0.2762 | 1.1548 | 7.7016 | 1.5640 | 0.6146 | 0.6146 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5303 | 0.9896 | 0.2762 | 1.1548 | 7.7016 | 1.5640 | 0.6143 | 0.6143 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5303 | 0.9938 | 0.2762 | 1.1548 | 7.7016 | 1.5640 | 0.6135 | 0.6135 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5300 | 0.9937 | 0.2778 | 1.1805 | 4.2835 | 1.3147 | 0.5784 | 0.5784 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5300 | 0.9968 | 0.2778 | 1.1805 | 4.2835 | 1.3147 | 0.5773 | 0.5773 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5300 | 1.0021 | 0.2778 | 1.1805 | 4.2835 | 1.3147 | 0.5755 | 0.5755 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5300 | 1.0102 | 0.2778 | 1.1805 | 4.2835 | 1.3147 | 0.5729 | 0.5729 |
| `base|emb=12|sh=0.97` | 18 | 0.5165 | 0.9981 | 1.0000 | 0.9223 | -0.9538 | 0.3643 | 0.5680 | 0.5680 |
| `base|emb=12|sh=0.96` | 18 | 0.5165 | 0.9992 | 1.0000 | 0.9223 | -0.9538 | 0.3643 | 0.5676 | 0.5676 |
| `base|emb=12|sh=0.95` | 18 | 0.5165 | 1.0007 | 1.0000 | 0.9223 | -0.9538 | 0.3643 | 0.5671 | 0.5671 |
| `base|emb=12|sh=0.94` | 18 | 0.5165 | 1.0035 | 1.0000 | 0.9223 | -0.9538 | 0.3643 | 0.5661 | 0.5661 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4825 | 0.9997 | 0.4182 | 0.9709 | -6.8573 | 0.1862 | 0.5344 | 0.5344 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4825 | 1.0002 | 0.4182 | 0.9709 | -6.8573 | 0.1862 | 0.5342 | 0.5342 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4825 | 1.0009 | 0.4182 | 0.9709 | -6.8573 | 0.1862 | 0.5341 | 0.5341 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4825 | 1.0028 | 0.4182 | 0.9709 | -6.8573 | 0.1862 | 0.5334 | 0.5334 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4858 | 1.0005 | 0.4074 | 0.9621 | -6.0266 | -0.1023 | 0.5283 | 0.5283 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4858 | 1.0009 | 0.4074 | 0.9621 | -6.0266 | -0.1023 | 0.5282 | 0.5282 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4858 | 1.0014 | 0.4074 | 0.9621 | -6.0266 | -0.1023 | 0.5281 | 0.5281 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4858 | 1.0027 | 0.4074 | 0.9621 | -6.0266 | -0.1023 | 0.5276 | 0.5276 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=332, top_n=34, cutoff=0.8262

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6879 | 0.0708 | 0.9460 | 0.0316 |
| all validations | 0.5081 | 0.1145 | 0.9993 | 0.0322 |

- improvement vs all (primary fraction): `hit +17.98pp, mae +5.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.5143 | 0.9919 | 1.0000 | 0.7603 | -0.0865 | -8.0998 | -0.5268 | 0.3773 | 0.3773 |
| 2 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 1.0008 | 0.6389 | 0.7134 | -0.2062 | -19.2971 | -0.8731 | 0.3473 | 0.3473 |
| 3 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 1.0011 | 0.6389 | 0.7134 | -0.2062 | -19.2971 | -0.8731 | 0.3472 | 0.3472 |
| 4 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 1.0013 | 0.6389 | 0.7134 | -0.2062 | -19.2971 | -0.8731 | 0.3471 | 0.3471 |
| 5 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 1.0016 | 0.6389 | 0.7134 | -0.2062 | -19.2971 | -0.8731 | 0.3470 | 0.3470 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.0000 | 1.0526 | n/a | -119.4904 | -1.0072 |
| 1 | 7 | 0.8571 | 0.9377 | 1.5762 | 95.4952 | 8.5886 |
| 2 | 7 | 0.5714 | 0.9909 | 0.4419 | -17.2966 | -0.6048 |
| 3 | 7 | 0.6667 | 0.9607 | 0.4965 | -0.2526 | -0.0215 |
| 4 | 7 | 0.5714 | 0.9828 | 1.4559 | 22.7881 | 2.1237 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.0000 | 1.0526 | n/a | -119.4904 | -1.0072 |
| top_20pct | 8 | 0.6250 | 0.9637 | 1.2548 | 24.9716 | 2.4714 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.7500 | 0.9655 | 0.7761 | 31.3123 | 2.0013 |
| 1 | 7 | 0.5000 | 0.9785 | 0.3844 | -35.3087 | -0.9228 |
| 2 | 7 | 0.2857 | 1.0106 | 0.6097 | -51.2763 | -0.8584 |
| 3 | 7 | 0.2857 | 1.0223 | 1.0537 | -29.2437 | -0.9840 |
| 4 | 7 | 0.7143 | 0.9811 | 0.5459 | 11.5440 | 0.3527 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.7500 | 0.9655 | 0.7761 | 31.3123 | 2.0013 |
| top_20pct | 8 | 0.7500 | 0.9778 | 0.4713 | 12.3870 | 0.4028 |

