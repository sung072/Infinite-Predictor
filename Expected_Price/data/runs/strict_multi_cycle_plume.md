# Strict Multi-Cycle Research Result

- symbol: `PLUME`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6201 | 0.9656 | 0.3704 | 2.0437 | 28.5749 | 4.3392 | 0.7555 | 0.7555 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6201 | 0.9697 | 0.3704 | 2.0437 | 28.5749 | 4.3392 | 0.7536 | 0.7536 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6201 | 0.9749 | 0.3704 | 2.0437 | 28.5749 | 4.3392 | 0.7513 | 0.7513 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6201 | 0.9808 | 0.3704 | 2.0437 | 28.5749 | 4.3392 | 0.7488 | 0.7488 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6163 | 0.9633 | 0.3827 | 1.3893 | 27.2241 | 2.5829 | 0.7420 | 0.7420 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6163 | 0.9681 | 0.3827 | 1.3893 | 27.2241 | 2.5829 | 0.7397 | 0.7397 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6163 | 0.9736 | 0.3827 | 1.3893 | 27.2241 | 2.5829 | 0.7372 | 0.7372 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6163 | 0.9799 | 0.3827 | 1.3893 | 27.2241 | 2.5829 | 0.7344 | 0.7344 |
| `base|emb=24|sh=0.95` | 18 | 0.5068 | 0.9966 | 1.0000 | 1.1527 | 4.1154 | 0.9068 | 0.6067 | 0.6067 |
| `base|emb=24|sh=0.96` | 18 | 0.5068 | 0.9967 | 1.0000 | 1.1527 | 4.1154 | 0.9068 | 0.6067 | 0.6067 |
| `base|emb=24|sh=0.94` | 18 | 0.5068 | 0.9971 | 1.0000 | 1.1527 | 4.1154 | 0.9068 | 0.6066 | 0.6066 |
| `base|emb=24|sh=0.97` | 18 | 0.5068 | 0.9972 | 1.0000 | 1.1527 | 4.1154 | 0.9068 | 0.6065 | 0.6065 |
| `base|emb=12|sh=0.95` | 18 | 0.5140 | 0.9971 | 1.0000 | 1.1351 | 4.4602 | 0.6924 | 0.5812 | 0.5812 |
| `base|emb=12|sh=0.96` | 18 | 0.5140 | 0.9971 | 1.0000 | 1.1351 | 4.4602 | 0.6924 | 0.5811 | 0.5811 |
| `base|emb=12|sh=0.94` | 18 | 0.5140 | 0.9977 | 1.0000 | 1.1351 | 4.4602 | 0.6924 | 0.5809 | 0.5809 |
| `base|emb=12|sh=0.97` | 18 | 0.5140 | 0.9976 | 1.0000 | 1.1351 | 4.4602 | 0.6924 | 0.5809 | 0.5809 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4524 | 1.0103 | 0.4336 | 1.0881 | -11.1069 | 0.5291 | 0.5375 | 0.5375 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4524 | 1.0142 | 0.4336 | 1.0881 | -11.1069 | 0.5291 | 0.5361 | 0.5361 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4524 | 1.0184 | 0.4336 | 1.0881 | -11.1069 | 0.5291 | 0.5346 | 0.5346 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4524 | 1.0231 | 0.4336 | 1.0881 | -11.1069 | 0.5291 | 0.5330 | 0.5330 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=388, top_n=39, cutoff=0.8580

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7023 | 0.0702 | 0.9609 | 0.0361 |
| all validations | 0.5259 | 0.1435 | 0.9947 | 0.0302 |

- improvement vs all (primary fraction): `hit +17.64pp, mae +3.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.95` | 0.5152 | 0.9917 | 1.0000 | 2.1301 | 0.2302 | 21.5447 | 4.1160 | 0.8359 | 0.8359 |
| 2 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5714 | 1.0107 | 0.2500 | 1.2711 | 0.1973 | 18.4692 | 0.8485 | 0.7476 | 0.7476 |
| 3 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5714 | 1.0143 | 0.2500 | 1.2711 | 0.1973 | 18.4692 | 0.8485 | 0.7462 | 0.7462 |
| 4 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5714 | 1.0178 | 0.2500 | 1.2711 | 0.1973 | 18.4692 | 0.8485 | 0.7448 | 0.7448 |
| 5 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5714 | 1.0214 | 0.2500 | 1.2711 | 0.1973 | 18.4692 | 0.8485 | 0.7435 | 0.7435 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.7500 | 0.9676 | 3.0207 | 57.1651 | 8.4184 |
| 1 | 7 | 0.4286 | 0.9805 | 0.8083 | -15.8131 | -0.5533 |
| 2 | 7 | 0.2857 | 1.0640 | 1.3777 | -19.8161 | -0.5277 |
| 3 | 7 | 0.7143 | 0.9209 | 1.8033 | 39.6566 | 8.7087 |
| 4 | 7 | 0.2500 | 1.1113 | 1.1719 | -38.4828 | -0.6174 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.7500 | 0.9676 | 3.0207 | 57.1651 | 8.4184 |
| top_20pct | 8 | 0.4000 | 1.0768 | 0.7514 | -27.3398 | -0.5080 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.4286 | 1.0241 | 0.4820 | -36.7924 | -0.8904 |
| 1 | 7 | 0.5714 | 0.9525 | 1.2362 | 16.1579 | 0.9860 |
| 2 | 7 | 0.5714 | 0.9345 | 3.3457 | 43.3066 | 4.5137 |
| 3 | 7 | 0.6000 | 1.0235 | 5.7280 | 51.2800 | 19.4720 |
| 4 | 7 | 0.4286 | 1.0069 | 1.0357 | -9.4979 | -0.3953 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.4286 | 1.0241 | 0.4820 | -36.7924 | -0.8904 |
| top_20pct | 8 | 0.4286 | 1.0346 | 1.0357 | -9.4979 | -0.3953 |

