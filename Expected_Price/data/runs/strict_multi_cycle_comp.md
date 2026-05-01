# Strict Multi-Cycle Research Result

- symbol: `COMP`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5277 | 0.9822 | 0.2948 | 1.4416 | 14.0925 | 1.8254 | 0.6687 | 0.6687 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5277 | 0.9847 | 0.2948 | 1.4416 | 14.0925 | 1.8254 | 0.6675 | 0.6675 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5277 | 0.9872 | 0.2948 | 1.4416 | 14.0925 | 1.8254 | 0.6663 | 0.6663 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5277 | 0.9903 | 0.2948 | 1.4416 | 14.0925 | 1.8254 | 0.6649 | 0.6649 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4876 | 0.9927 | 0.3133 | 1.2230 | 4.6710 | 0.9167 | 0.6190 | 0.6190 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4876 | 0.9937 | 0.3133 | 1.2230 | 4.6710 | 0.9167 | 0.6184 | 0.6184 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4876 | 0.9947 | 0.3133 | 1.2230 | 4.6710 | 0.9167 | 0.6179 | 0.6179 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4876 | 0.9960 | 0.3133 | 1.2230 | 4.6710 | 0.9167 | 0.6173 | 0.6173 |
| `base|emb=24|sh=0.97` | 18 | 0.4950 | 1.0034 | 1.0000 | 1.0110 | -1.5535 | 0.5620 | 0.5336 | 0.5336 |
| `base|emb=24|sh=0.96` | 18 | 0.4950 | 1.0054 | 1.0000 | 1.0110 | -1.5535 | 0.5620 | 0.5329 | 0.5329 |
| `base|emb=24|sh=0.95` | 18 | 0.4950 | 1.0082 | 1.0000 | 1.0110 | -1.5535 | 0.5620 | 0.5319 | 0.5319 |
| `base|emb=24|sh=0.94` | 18 | 0.4950 | 1.0114 | 1.0000 | 1.0110 | -1.5535 | 0.5620 | 0.5309 | 0.5309 |
| `base|emb=12|sh=0.97` | 18 | 0.4842 | 1.0074 | 1.0000 | 0.9998 | -3.9731 | 0.3715 | 0.5047 | 0.5047 |
| `base|emb=12|sh=0.96` | 18 | 0.4842 | 1.0107 | 1.0000 | 0.9998 | -3.9731 | 0.3715 | 0.5035 | 0.5035 |
| `base|emb=12|sh=0.95` | 18 | 0.4842 | 1.0148 | 1.0000 | 0.9998 | -3.9731 | 0.3715 | 0.5020 | 0.5020 |
| `base|emb=12|sh=0.94` | 18 | 0.4842 | 1.0194 | 1.0000 | 0.9998 | -3.9731 | 0.3715 | 0.5004 | 0.5004 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4631 | 1.0266 | 0.4383 | 0.8566 | -6.5434 | -0.5134 | 0.4221 | 0.4221 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4631 | 1.0372 | 0.4383 | 0.8566 | -6.5434 | -0.5134 | 0.4195 | 0.4195 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4631 | 1.0483 | 0.4383 | 0.8566 | -6.5434 | -0.5134 | 0.4172 | 0.4172 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4631 | 1.0599 | 0.4383 | 0.8566 | -6.5434 | -0.5134 | 0.4151 | 0.4151 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=332, top_n=34, cutoff=0.8314

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6452 | 0.1278 | 0.9657 | 0.0487 |
| all validations | 0.4789 | 0.1297 | 1.0215 | 0.0960 |

- improvement vs all (primary fraction): `hit +16.62pp, mae +5.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.5714 | 0.9884 | 1.0000 | 1.4496 | 0.2149 | 20.1175 | 2.1031 | 0.7968 | 0.7968 |
| 2 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5588 | 0.9949 | 1.0000 | 1.1272 | 0.1131 | 10.5873 | 1.0413 | 0.7508 | 0.7508 |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5588 | 0.9979 | 1.0000 | 1.1272 | 0.1131 | 10.5873 | 1.0413 | 0.7496 | 0.7496 |
| 4 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5588 | 1.0029 | 1.0000 | 1.1272 | 0.1131 | 10.5873 | 1.0413 | 0.7476 | 0.7476 |
| 5 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5588 | 1.0094 | 1.0000 | 1.1272 | 0.1131 | 10.5873 | 1.0413 | 0.7450 | 0.7450 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 0.9565 | 0.2106 | -42.9118 | -0.9641 |
| 1 | 7 | 0.4286 | 1.0076 | 0.6498 | -22.4447 | -0.5207 |
| 2 | 7 | 0.5000 | 0.9870 | 1.3667 | 11.5793 | 0.5408 |
| 3 | 7 | 0.7143 | 0.9926 | 1.8953 | 60.4652 | 3.9340 |
| 4 | 7 | 0.7143 | 0.9790 | 10.2893 | 51.9550 | 99.9326 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 0.9565 | 0.2106 | -42.9118 | -0.9641 |
| top_20pct | 8 | 0.6250 | 0.9937 | 12.3883 | 47.4114 | 98.9070 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.7500 | 0.9861 | 8.8669 | 90.2372 | 104.1797 |
| 1 | 7 | 0.4286 | 0.9751 | 0.2006 | -51.1905 | -1.0368 |
| 2 | 7 | 0.5714 | 0.9975 | 0.3313 | -23.4940 | -0.5655 |
| 3 | 7 | 0.5714 | 0.9865 | 1.8617 | 32.9326 | 2.2219 |
| 4 | 7 | 0.5000 | 0.9899 | 3.0551 | 29.9598 | 2.0453 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.7500 | 0.9861 | 8.8669 | 90.2372 | 104.1797 |
| top_20pct | 8 | 0.4286 | 0.9921 | 2.9088 | 21.7688 | 1.1701 |

