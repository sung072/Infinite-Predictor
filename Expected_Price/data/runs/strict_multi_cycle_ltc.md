# Strict Multi-Cycle Research Result

- symbol: `LTC`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5385 | 1.0044 | 0.2870 | 1.4658 | 19.7744 | 2.0477 | 0.6775 | 0.6775 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5385 | 1.0090 | 0.2870 | 1.4658 | 19.7744 | 2.0477 | 0.6760 | 0.6760 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5385 | 1.0139 | 0.2870 | 1.4658 | 19.7744 | 2.0477 | 0.6745 | 0.6745 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5385 | 1.0195 | 0.2870 | 1.4658 | 19.7744 | 2.0477 | 0.6727 | 0.6727 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5380 | 1.0062 | 0.2855 | 1.6184 | 21.4035 | 3.2436 | 0.6710 | 0.6710 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5380 | 1.0124 | 0.2855 | 1.6184 | 21.4035 | 3.2436 | 0.6690 | 0.6690 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5380 | 1.0186 | 0.2855 | 1.6184 | 21.4035 | 3.2436 | 0.6672 | 0.6672 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5380 | 1.0252 | 0.2855 | 1.6184 | 21.4035 | 3.2436 | 0.6653 | 0.6653 |
| `base|emb=24|sh=0.95` | 18 | 0.5377 | 0.9975 | 1.0000 | 1.0327 | 6.2051 | 0.5930 | 0.6510 | 0.6510 |
| `base|emb=24|sh=0.96` | 18 | 0.5377 | 0.9976 | 1.0000 | 1.0327 | 6.2051 | 0.5930 | 0.6509 | 0.6509 |
| `base|emb=24|sh=0.94` | 18 | 0.5377 | 0.9981 | 1.0000 | 1.0327 | 6.2051 | 0.5930 | 0.6508 | 0.6508 |
| `base|emb=24|sh=0.97` | 18 | 0.5377 | 0.9977 | 1.0000 | 1.0327 | 6.2051 | 0.5930 | 0.6508 | 0.6508 |
| `base|emb=12|sh=0.97` | 18 | 0.5235 | 0.9992 | 1.0000 | 1.0933 | 5.4158 | 0.5486 | 0.6305 | 0.6305 |
| `base|emb=12|sh=0.96` | 18 | 0.5235 | 0.9996 | 1.0000 | 1.0933 | 5.4158 | 0.5486 | 0.6304 | 0.6304 |
| `base|emb=12|sh=0.95` | 18 | 0.5235 | 1.0003 | 1.0000 | 1.0933 | 5.4158 | 0.5486 | 0.6302 | 0.6302 |
| `base|emb=12|sh=0.94` | 18 | 0.5235 | 1.0016 | 1.0000 | 1.0933 | 5.4158 | 0.5486 | 0.6297 | 0.6297 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4921 | 1.0009 | 0.5015 | 1.1542 | -1.7940 | 0.7805 | 0.5694 | 0.5694 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4921 | 1.0012 | 0.5015 | 1.1542 | -1.7940 | 0.7805 | 0.5693 | 0.5693 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4921 | 1.0017 | 0.5015 | 1.1542 | -1.7940 | 0.7805 | 0.5692 | 0.5692 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4921 | 1.0028 | 0.5015 | 1.1542 | -1.7940 | 0.7805 | 0.5688 | 0.5688 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=392, top_n=40, cutoff=0.8276

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7117 | 0.1159 | 0.9821 | 0.0212 |
| all validations | 0.5249 | 0.1173 | 1.0028 | 0.0326 |

- improvement vs all (primary fraction): `hit +18.68pp, mae +2.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.95` | 0.7714 | 0.9343 | 1.0000 | 0.4633 | 0.1498 | 14.0168 | 1.0804 | 0.7899 | 0.7899 |
| 2 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6471 | 0.9565 | 0.4722 | 0.2380 | -0.2227 | -20.8391 | -0.7109 | 0.3862 | 0.3862 |
| 3 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6471 | 0.9594 | 0.4722 | 0.2380 | -0.2227 | -20.8391 | -0.7109 | 0.3850 | 0.3850 |
| 4 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6471 | 0.9632 | 0.4722 | 0.2380 | -0.2227 | -20.8391 | -0.7109 | 0.3833 | 0.3833 |
| 5 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6471 | 0.9713 | 0.4722 | 0.2380 | -0.2227 | -20.8391 | -0.7109 | 0.3799 | 0.3799 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1.0000 | 0.8643 | n/a | 105.1329 | n/a |
| 1 | 7 | 0.7143 | 0.9255 | 0.4338 | 2.7383 | 0.0774 |
| 2 | 7 | 0.5714 | 0.9854 | 0.2263 | -25.2383 | -0.7396 |
| 3 | 7 | 0.7143 | 0.9388 | 0.4485 | 4.2402 | 0.1336 |
| 4 | 7 | 0.8571 | 0.9196 | 1.9524 | 79.2797 | 10.8190 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 1.0000 | 0.8643 | n/a | 105.1329 | n/a |
| top_20pct | 8 | 0.8750 | 0.9163 | 1.6832 | 72.0416 | 10.8890 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1.0000 | 0.8643 | n/a | 105.1329 | n/a |
| 1 | 7 | 0.8571 | 0.9033 | 9.1491 | 118.1386 | 54.3031 |
| 2 | 7 | 0.8571 | 0.8857 | 0.3288 | 23.2834 | 0.9698 |
| 3 | 7 | 0.4286 | 0.9806 | 0.4354 | -36.2223 | -0.8061 |
| 4 | 7 | 0.7143 | 0.9495 | 0.5632 | 11.3742 | 0.4591 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 1.0000 | 0.8643 | n/a | 105.1329 | n/a |
| top_20pct | 8 | 0.6250 | 0.9678 | 0.5281 | -4.4767 | -0.1827 |

