# Strict Multi-Cycle Research Result

- symbol: `ZBT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4957 | 1.0065 | 0.3410 | 1.3218 | 5.4035 | 1.7907 | 0.5964 | 0.5964 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4957 | 1.0091 | 0.3410 | 1.3218 | 5.4035 | 1.7907 | 0.5955 | 0.5955 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4957 | 1.0121 | 0.3410 | 1.3218 | 5.4035 | 1.7907 | 0.5945 | 0.5945 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4957 | 1.0150 | 0.3410 | 1.3218 | 5.4035 | 1.7907 | 0.5936 | 0.5936 |
| `base|emb=12|sh=0.97` | 18 | 0.4992 | 1.0106 | 1.0000 | 1.0631 | 1.0368 | 0.4882 | 0.5700 | 0.5700 |
| `base|emb=24|sh=0.97` | 18 | 0.4989 | 1.0104 | 1.0000 | 1.0527 | -0.2976 | 0.3709 | 0.5685 | 0.5685 |
| `base|emb=12|sh=0.96` | 18 | 0.4992 | 1.0154 | 1.0000 | 1.0631 | 1.0368 | 0.4882 | 0.5683 | 0.5683 |
| `base|emb=24|sh=0.96` | 18 | 0.4989 | 1.0150 | 1.0000 | 1.0527 | -0.2976 | 0.3709 | 0.5668 | 0.5668 |
| `base|emb=12|sh=0.95` | 18 | 0.4992 | 1.0204 | 1.0000 | 1.0631 | 1.0368 | 0.4882 | 0.5666 | 0.5666 |
| `base|emb=24|sh=0.95` | 18 | 0.4989 | 1.0199 | 1.0000 | 1.0527 | -0.2976 | 0.3709 | 0.5652 | 0.5652 |
| `base|emb=12|sh=0.94` | 18 | 0.4992 | 1.0256 | 1.0000 | 1.0631 | 1.0368 | 0.4882 | 0.5648 | 0.5648 |
| `base|emb=24|sh=0.94` | 18 | 0.4989 | 1.0250 | 1.0000 | 1.0527 | -0.2976 | 0.3709 | 0.5635 | 0.5635 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4998 | 1.0065 | 0.3488 | 0.9822 | -3.7314 | 0.4767 | 0.5422 | 0.5422 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4998 | 1.0089 | 0.3488 | 0.9822 | -3.7314 | 0.4767 | 0.5414 | 0.5414 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4998 | 1.0114 | 0.3488 | 0.9822 | -3.7314 | 0.4767 | 0.5406 | 0.5406 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4998 | 1.0138 | 0.3488 | 0.9822 | -3.7314 | 0.4767 | 0.5398 | 0.5398 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4570 | 1.0311 | 0.3472 | 1.1582 | -4.2850 | 0.1324 | 0.5274 | 0.5274 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4570 | 1.0436 | 0.3472 | 1.1582 | -4.2850 | 0.1324 | 0.5232 | 0.5232 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5232 | 1.0204 | 0.3333 | 3.1184 | 14.4177 | -0.4159 | 0.5230 | 0.5230 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5232 | 1.0292 | 0.3333 | 3.1184 | 14.4177 | -0.4159 | 0.5200 | 0.5200 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=336, top_n=34, cutoff=0.8380

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6822 | 0.0964 | 0.9880 | 0.0178 |
| all validations | 0.4960 | 0.1499 | 1.0215 | 0.0447 |

- improvement vs all (primary fraction): `hit +18.62pp, mae +3.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.4706 | 1.0313 | 1.0000 | 2.1126 | 0.2164 | 20.2498 | 1.8800 | 0.7786 | 0.7786 |
| 2 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4500 | 1.0089 | 0.5556 | 2.0075 | 0.1696 | 15.8710 | 0.9221 | 0.7539 | 0.7539 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4500 | 1.0119 | 0.5556 | 2.0075 | 0.1696 | 15.8710 | 0.9221 | 0.7528 | 0.7528 |
| 4 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4500 | 1.0149 | 0.5556 | 2.0075 | 0.1696 | 15.8710 | 0.9221 | 0.7516 | 0.7516 |
| 5 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4500 | 1.0179 | 0.5556 | 2.0075 | 0.1696 | 15.8710 | 0.9221 | 0.7504 | 0.7504 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.2500 | 1.0238 | 5.0598 | 16.3180 | 0.7658 |
| 1 | 7 | 0.8571 | 0.9774 | 1.0273 | 50.8251 | 5.2661 |
| 2 | 7 | 0.2857 | 1.0380 | 0.9474 | -39.8849 | -0.6342 |
| 3 | 7 | 0.6000 | 1.0799 | 2.7606 | 38.7360 | 4.1755 |
| 4 | 7 | 0.4286 | 1.0898 | 2.2833 | 15.4771 | 0.7324 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.2500 | 1.0238 | 5.0598 | 16.3180 | 0.7658 |
| top_20pct | 8 | 0.3750 | 1.1356 | 2.4751 | 11.3423 | 0.5677 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.8333 | 0.9804 | 2.6005 | 75.3079 | 12.4726 |
| 1 | 7 | 0.2857 | 1.0608 | 1.6887 | -14.3017 | -0.3357 |
| 2 | 7 | 0.2857 | 1.0308 | 1.3304 | -22.6545 | -0.6311 |
| 3 | 7 | 0.5714 | 0.9841 | 2.1171 | 37.6086 | 1.8837 |
| 4 | 7 | 0.4286 | 1.1996 | 1.6643 | 6.1145 | 0.2705 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.8333 | 0.9804 | 2.6005 | 75.3079 | 12.4726 |
| top_20pct | 8 | 0.5000 | 1.1346 | 1.5409 | 12.3910 | 0.6221 |

