# Strict Multi-Cycle Research Result

- symbol: `OPEN`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4993 | 1.0065 | 0.3519 | 1.0475 | 0.9735 | 0.2353 | 0.6202 | 0.6202 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4993 | 1.0096 | 0.3519 | 1.0475 | 0.9735 | 0.2353 | 0.6190 | 0.6190 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4993 | 1.0127 | 0.3519 | 1.0475 | 0.9735 | 0.2353 | 0.6179 | 0.6179 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4993 | 1.0162 | 0.3519 | 1.0475 | 0.9735 | 0.2353 | 0.6167 | 0.6167 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5311 | 0.9979 | 0.3951 | 1.0133 | 4.4535 | 0.6807 | 0.6005 | 0.6005 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5311 | 0.9984 | 0.3951 | 1.0133 | 4.4535 | 0.6807 | 0.6004 | 0.6004 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5311 | 0.9988 | 0.3951 | 1.0133 | 4.4535 | 0.6807 | 0.6003 | 0.6003 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5311 | 0.9994 | 0.3951 | 1.0133 | 4.4535 | 0.6807 | 0.6001 | 0.6001 |
| `base|emb=24|sh=0.97` | 18 | 0.4542 | 1.0104 | 1.0000 | 1.2158 | -0.3382 | 0.5298 | 0.5499 | 0.5499 |
| `base|emb=24|sh=0.96` | 18 | 0.4542 | 1.0144 | 1.0000 | 1.2158 | -0.3382 | 0.5298 | 0.5484 | 0.5484 |
| `base|emb=24|sh=0.95` | 18 | 0.4542 | 1.0183 | 1.0000 | 1.2158 | -0.3382 | 0.5298 | 0.5469 | 0.5469 |
| `base|emb=24|sh=0.94` | 18 | 0.4542 | 1.0224 | 1.0000 | 1.2158 | -0.3382 | 0.5298 | 0.5455 | 0.5455 |
| `base|emb=12|sh=0.97` | 18 | 0.4622 | 1.0097 | 1.0000 | 1.1730 | -0.6799 | 0.5200 | 0.5306 | 0.5306 |
| `base|emb=12|sh=0.96` | 18 | 0.4622 | 1.0139 | 1.0000 | 1.1730 | -0.6799 | 0.5200 | 0.5290 | 0.5290 |
| `base|emb=12|sh=0.95` | 18 | 0.4622 | 1.0181 | 1.0000 | 1.1730 | -0.6799 | 0.5200 | 0.5275 | 0.5275 |
| `base|emb=12|sh=0.94` | 18 | 0.4622 | 1.0224 | 1.0000 | 1.1730 | -0.6799 | 0.5200 | 0.5260 | 0.5260 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4335 | 1.0152 | 0.3534 | 1.5765 | 1.8131 | 0.5264 | 0.5176 | 0.5176 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4335 | 1.0218 | 0.3534 | 1.5765 | 1.8131 | 0.5264 | 0.5151 | 0.5151 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4335 | 1.0287 | 0.3534 | 1.5765 | 1.8131 | 0.5264 | 0.5126 | 0.5126 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4335 | 1.0355 | 0.3534 | 1.5765 | 1.8131 | 0.5264 | 0.5101 | 0.5101 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=324, top_n=33, cutoff=0.8076

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5896 | 0.0260 | 0.9889 | 0.0170 |
| all validations | 0.4692 | 0.0995 | 1.0155 | 0.0260 |

- improvement vs all (primary fraction): `hit +12.04pp, mae +2.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6522 | 0.9835 | 0.6667 | 1.4274 | 0.3460 | 32.3867 | 3.6270 | 0.8372 | 0.8372 |
| 2 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6522 | 0.9862 | 0.6667 | 1.4274 | 0.3460 | 32.3867 | 3.6270 | 0.8361 | 0.8361 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6522 | 0.9890 | 0.6667 | 1.4274 | 0.3460 | 32.3867 | 3.6270 | 0.8350 | 0.8350 |
| 4 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6522 | 0.9917 | 0.6667 | 1.4274 | 0.3460 | 32.3867 | 3.6270 | 0.8338 | 0.8338 |
| 5 | `base|emb=24|sh=0.97` | 0.6000 | 0.9906 | 1.0000 | 1.4800 | 0.2740 | 25.6462 | 3.7400 | 0.8271 | 0.8271 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 0.4000 | 1.0011 | 2.4576 | 17.5664 | 1.7281 |
| 1 | 5 | 1.0000 | 0.9486 | n/a | 142.2212 | n/a |
| 3 | 5 | 0.4000 | 1.0456 | 0.3766 | -43.5494 | -1.7419 |
| 4 | 5 | n/a | n/a | n/a | n/a | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 0.8000 | 0.9441 | 1.0344 | 62.1713 | 3.1744 |
| 1 | 5 | n/a | n/a | n/a | n/a | n/a |
| 3 | 5 | 0.6000 | 1.0291 | 0.2329 | -35.0649 | -0.6569 |
| 4 | 5 | 0.6000 | 0.9903 | 1.8176 | 33.5893 | 1.7125 |

