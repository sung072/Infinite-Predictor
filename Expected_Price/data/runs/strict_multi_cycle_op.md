# Strict Multi-Cycle Research Result

- symbol: `OP`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5508 | 0.9979 | 0.4383 | 1.0204 | 6.9081 | 1.5084 | 0.6351 | 0.6351 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5508 | 0.9988 | 0.4383 | 1.0204 | 6.9081 | 1.5084 | 0.6348 | 0.6348 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5508 | 0.9997 | 0.4383 | 1.0204 | 6.9081 | 1.5084 | 0.6346 | 0.6346 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5508 | 1.0006 | 0.4383 | 1.0204 | 6.9081 | 1.5084 | 0.6344 | 0.6344 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5452 | 0.9975 | 0.4090 | 0.9676 | -0.0578 | 1.3820 | 0.6310 | 0.6310 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5452 | 0.9980 | 0.4090 | 0.9676 | -0.0578 | 1.3820 | 0.6309 | 0.6309 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5452 | 0.9985 | 0.4090 | 0.9676 | -0.0578 | 1.3820 | 0.6309 | 0.6309 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5452 | 0.9991 | 0.4090 | 0.9676 | -0.0578 | 1.3820 | 0.6309 | 0.6309 |
| `base|emb=24|sh=0.97` | 18 | 0.5114 | 1.0052 | 1.0000 | 1.0465 | 2.8142 | 0.7378 | 0.5736 | 0.5736 |
| `base|emb=24|sh=0.96` | 18 | 0.5114 | 1.0090 | 1.0000 | 1.0465 | 2.8142 | 0.7378 | 0.5722 | 0.5722 |
| `base|emb=24|sh=0.95` | 18 | 0.5114 | 1.0135 | 1.0000 | 1.0465 | 2.8142 | 0.7378 | 0.5706 | 0.5706 |
| `base|emb=24|sh=0.94` | 18 | 0.5114 | 1.0183 | 1.0000 | 1.0465 | 2.8142 | 0.7378 | 0.5688 | 0.5688 |
| `base|emb=12|sh=0.97` | 18 | 0.5074 | 1.0078 | 1.0000 | 1.0508 | 2.3424 | 0.8734 | 0.5656 | 0.5656 |
| `base|emb=12|sh=0.96` | 18 | 0.5074 | 1.0126 | 1.0000 | 1.0508 | 2.3424 | 0.8734 | 0.5638 | 0.5638 |
| `base|emb=12|sh=0.95` | 18 | 0.5074 | 1.0181 | 1.0000 | 1.0508 | 2.3424 | 0.8734 | 0.5617 | 0.5617 |
| `base|emb=12|sh=0.94` | 18 | 0.5074 | 1.0241 | 1.0000 | 1.0508 | 2.3424 | 0.8734 | 0.5596 | 0.5596 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4654 | 1.0571 | 0.3241 | 1.6768 | 5.3369 | 1.3890 | 0.5333 | 0.5333 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4654 | 1.0807 | 0.3241 | 1.6768 | 5.3369 | 1.3890 | 0.5275 | 0.5275 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4654 | 1.1071 | 0.3241 | 1.6768 | 5.3369 | 1.3890 | 0.5213 | 0.5213 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4654 | 1.1343 | 0.3241 | 1.6768 | 5.3369 | 1.3890 | 0.5153 | 0.5153 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8396

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6956 | 0.1163 | 0.9766 | 0.0256 |
| all validations | 0.5080 | 0.1347 | 1.0255 | 0.0879 |

- improvement vs all (primary fraction): `hit +18.76pp, mae +4.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.6452 | 0.9828 | 1.0000 | 0.8527 | 0.1732 | 16.2084 | 1.1820 | 0.7650 | 0.7650 |
| 2 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3333 | 1.0104 | 0.1667 | 0.3293 | -0.5671 | -53.0816 | -0.8391 | 0.3017 | 0.3017 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3333 | 1.0138 | 0.1667 | 0.3293 | -0.5671 | -53.0816 | -0.8391 | 0.3004 | 0.3004 |
| 4 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3333 | 1.0173 | 0.1667 | 0.3293 | -0.5671 | -53.0816 | -0.8391 | 0.2990 | 0.2990 |
| 5 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3333 | 1.0207 | 0.1667 | 0.3293 | -0.5671 | -53.0816 | -0.8391 | 0.2977 | 0.2977 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.4286 | 1.0049 | 0.6550 | -23.8673 | -0.5186 |
| 1 | 7 | 0.6667 | 0.9715 | 1.2700 | 39.1663 | 2.0529 |
| 2 | 7 | 0.8333 | 0.9699 | 0.2254 | 3.6809 | 0.1117 |
| 3 | 7 | 0.6667 | 0.9659 | 0.7784 | 16.6050 | 0.6929 |
| 4 | 7 | 0.6667 | 0.9940 | 6.1634 | 81.8836 | 15.2805 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.4286 | 1.0049 | 0.6550 | -23.8673 | -0.5186 |
| top_20pct | 8 | 0.6667 | 0.9993 | 6.1634 | 81.8836 | 15.2805 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5714 | 0.9723 | 1.1906 | 18.5644 | 0.9699 |
| 1 | 7 | 1.0000 | 0.9508 | n/a | 125.1606 | n/a |
| 2 | 7 | 0.8000 | 1.0105 | 1.7099 | 83.8374 | 5.8734 |
| 3 | 7 | 0.3333 | 0.9970 | 1.4554 | -11.3444 | -0.4466 |
| 4 | 7 | 0.5714 | 0.9821 | 0.5462 | -11.0692 | -0.2835 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5714 | 0.9723 | 1.1906 | 18.5644 | 0.9699 |
| top_20pct | 8 | 0.6250 | 0.9736 | 0.6572 | 3.3171 | 0.0833 |

