# Strict Multi-Cycle Research Result

- symbol: `STO`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5365 | 0.9947 | 0.4429 | 1.2996 | 12.5878 | 1.8936 | 0.6889 | 0.6889 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5365 | 0.9953 | 0.4429 | 1.2996 | 12.5878 | 1.8936 | 0.6885 | 0.6885 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5365 | 0.9960 | 0.4429 | 1.2996 | 12.5878 | 1.8936 | 0.6882 | 0.6882 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5365 | 0.9968 | 0.4429 | 1.2996 | 12.5878 | 1.8936 | 0.6878 | 0.6878 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5633 | 0.9806 | 0.1867 | 1.3235 | 13.7761 | 2.1327 | 0.6465 | 0.6465 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5633 | 0.9817 | 0.1867 | 1.3235 | 13.7761 | 2.1327 | 0.6459 | 0.6459 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5633 | 0.9847 | 0.1867 | 1.3235 | 13.7761 | 2.1327 | 0.6446 | 0.6446 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5633 | 0.9880 | 0.1867 | 1.3235 | 13.7761 | 2.1327 | 0.6432 | 0.6432 |
| `base|emb=12|sh=0.97` | 18 | 0.5056 | 1.0015 | 1.0000 | 1.1243 | 4.0880 | 0.9141 | 0.6219 | 0.6219 |
| `base|emb=12|sh=0.96` | 18 | 0.5056 | 1.0025 | 1.0000 | 1.1243 | 4.0880 | 0.9141 | 0.6215 | 0.6215 |
| `base|emb=12|sh=0.95` | 18 | 0.5056 | 1.0038 | 1.0000 | 1.1243 | 4.0880 | 0.9141 | 0.6211 | 0.6211 |
| `base|emb=12|sh=0.94` | 18 | 0.5056 | 1.0058 | 1.0000 | 1.1243 | 4.0880 | 0.9141 | 0.6204 | 0.6204 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4892 | 0.9987 | 0.4491 | 1.2769 | -0.1712 | 0.9061 | 0.5723 | 0.5723 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4892 | 0.9987 | 0.4491 | 1.2769 | -0.1712 | 0.9061 | 0.5722 | 0.5722 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4892 | 0.9989 | 0.4491 | 1.2769 | -0.1712 | 0.9061 | 0.5720 | 0.5720 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4892 | 0.9992 | 0.4491 | 1.2769 | -0.1712 | 0.9061 | 0.5719 | 0.5719 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5278 | 0.9979 | 0.2330 | 1.0673 | 3.0873 | 0.6589 | 0.5516 | 0.5516 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5278 | 0.9972 | 0.2330 | 1.0673 | 3.0873 | 0.6589 | 0.5515 | 0.5515 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5278 | 0.9974 | 0.2330 | 1.0673 | 3.0873 | 0.6589 | 0.5512 | 0.5512 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5278 | 1.0011 | 0.2330 | 1.0673 | 3.0873 | 0.6589 | 0.5507 | 0.5507 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=328, top_n=33, cutoff=0.8319

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6428 | 0.0602 | 0.9880 | 0.0070 |
| all validations | 0.5104 | 0.1143 | 0.9996 | 0.0281 |

- improvement vs all (primary fraction): `hit +13.24pp, mae +1.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.4062 | 1.0114 | 1.0000 | 1.3598 | -0.0281 | -2.6298 | -0.1925 | 0.4283 | 0.4283 |
| 2 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3636 | 1.0153 | 0.6667 | 1.1455 | -0.1651 | -15.4529 | -0.9652 | 0.3402 | 0.3402 |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3636 | 1.0205 | 0.6667 | 1.1455 | -0.1651 | -15.4529 | -0.9652 | 0.3383 | 0.3383 |
| 4 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3636 | 1.0256 | 0.6667 | 1.1455 | -0.1651 | -15.4529 | -0.9652 | 0.3363 | 0.3363 |
| 5 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3636 | 1.0307 | 0.6667 | 1.1455 | -0.1651 | -15.4529 | -0.9652 | 0.3344 | 0.3344 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.2500 | 1.0294 | 0.9363 | -41.8523 | -0.8027 |
| 1 | 7 | 0.5000 | 1.0062 | 0.6167 | -16.6095 | -0.6670 |
| 2 | 7 | 0.5000 | 0.9968 | 1.2884 | 8.7077 | 0.3850 |
| 3 | 7 | 0.2857 | 1.0233 | 1.6520 | -14.2174 | -0.6210 |
| 4 | 7 | 0.6000 | 1.0059 | 1.6943 | 33.9883 | 4.1460 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.2500 | 1.0294 | 0.9363 | -41.8523 | -0.8027 |
| top_20pct | 8 | 0.6667 | 0.9990 | 1.7668 | 48.8517 | 6.9018 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.4286 | 1.0220 | 0.9240 | -11.6017 | -0.3490 |
| 1 | 7 | 0.3333 | 1.0209 | 0.6417 | -41.4702 | -1.0574 |
| 2 | 7 | 0.4286 | 0.9837 | 2.0958 | 15.9307 | 1.4079 |
| 3 | 7 | 0.2000 | 1.0588 | 0.3270 | -96.2210 | -1.5299 |
| 4 | 7 | 0.5714 | 0.9973 | 2.3539 | 41.5459 | 3.4851 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.4286 | 1.0220 | 0.9240 | -11.6017 | -0.3490 |
| top_20pct | 8 | 0.5000 | 1.0019 | 2.5580 | 33.6601 | 2.2744 |

