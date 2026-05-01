# Strict Multi-Cycle Research Result

- symbol: `AVAX`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6461 | 0.9802 | 0.2701 | 1.3114 | 28.8392 | 1.9756 | 0.7303 | 0.7303 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6461 | 0.9808 | 0.2701 | 1.3114 | 28.8392 | 1.9756 | 0.7294 | 0.7294 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6461 | 0.9842 | 0.2701 | 1.3114 | 28.8392 | 1.9756 | 0.7271 | 0.7271 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6461 | 0.9882 | 0.2701 | 1.3114 | 28.8392 | 1.9756 | 0.7249 | 0.7249 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5583 | 1.0000 | 0.3117 | 1.2532 | 15.5394 | 1.5496 | 0.6647 | 0.6647 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5583 | 1.0000 | 0.3117 | 1.2532 | 15.5394 | 1.5496 | 0.6643 | 0.6643 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5583 | 1.0021 | 0.3117 | 1.2532 | 15.5394 | 1.5496 | 0.6643 | 0.6643 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5583 | 1.0061 | 0.3117 | 1.2532 | 15.5394 | 1.5496 | 0.6633 | 0.6633 |
| `base|emb=12|sh=0.97` | 18 | 0.5209 | 1.0033 | 1.0000 | 1.0705 | 4.9690 | 0.5813 | 0.6459 | 0.6459 |
| `base|emb=12|sh=0.96` | 18 | 0.5209 | 1.0044 | 1.0000 | 1.0705 | 4.9690 | 0.5813 | 0.6455 | 0.6455 |
| `base|emb=12|sh=0.95` | 18 | 0.5209 | 1.0065 | 1.0000 | 1.0705 | 4.9690 | 0.5813 | 0.6448 | 0.6448 |
| `base|emb=12|sh=0.94` | 18 | 0.5209 | 1.0092 | 1.0000 | 1.0705 | 4.9690 | 0.5813 | 0.6439 | 0.6439 |
| `base|emb=24|sh=0.97` | 18 | 0.5285 | 1.0029 | 1.0000 | 1.0740 | 6.0793 | 0.7042 | 0.6321 | 0.6321 |
| `base|emb=24|sh=0.96` | 18 | 0.5285 | 1.0039 | 1.0000 | 1.0740 | 6.0793 | 0.7042 | 0.6318 | 0.6318 |
| `base|emb=24|sh=0.95` | 18 | 0.5285 | 1.0053 | 1.0000 | 1.0740 | 6.0793 | 0.7042 | 0.6314 | 0.6314 |
| `base|emb=24|sh=0.94` | 18 | 0.5285 | 1.0071 | 1.0000 | 1.0740 | 6.0793 | 0.7042 | 0.6308 | 0.6308 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4674 | 1.0034 | 0.4120 | 1.0338 | -5.8471 | 0.5997 | 0.5341 | 0.5341 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4674 | 1.0045 | 0.4120 | 1.0338 | -5.8471 | 0.5997 | 0.5337 | 0.5337 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4674 | 1.0056 | 0.4120 | 1.0338 | -5.8471 | 0.5997 | 0.5333 | 0.5333 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4674 | 1.0067 | 0.4120 | 1.0338 | -5.8471 | 0.5997 | 0.5329 | 0.5329 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.8298

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6727 | 0.0814 | 0.9600 | 0.0399 |
| all validations | 0.5184 | 0.1275 | 1.0042 | 0.0377 |

- improvement vs all (primary fraction): `hit +15.43pp, mae +4.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6818 | 0.9854 | 0.8056 | 1.0145 | 0.3137 | 29.3607 | 2.6569 | 0.8121 | 0.8121 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6818 | 0.9878 | 0.8056 | 1.0145 | 0.3137 | 29.3607 | 2.6569 | 0.8111 | 0.8111 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6818 | 0.9903 | 0.8056 | 1.0145 | 0.3137 | 29.3607 | 2.6569 | 0.8101 | 0.8101 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6818 | 0.9927 | 0.8056 | 1.0145 | 0.3137 | 29.3607 | 2.6569 | 0.8091 | 0.8091 |
| 5 | `base|emb=12|sh=0.97` | 0.6429 | 0.9934 | 1.0000 | 0.6796 | 0.0807 | 7.5539 | 0.5747 | 0.7316 | 0.7316 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.5000 | 1.0388 | 0.5423 | -19.4443 | -0.5469 |
| 1 | 6 | 0.5000 | 0.9919 | 2.1387 | 27.5446 | 1.1337 |
| 2 | 5 | 0.6000 | 0.9563 | 3.6696 | 65.1019 | 9.0595 |
| 3 | 6 | 0.7500 | 0.9912 | 0.4156 | 7.4104 | 0.2391 |
| 4 | 6 | 1.0000 | 0.9436 | n/a | 152.2109 | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.6667 | 0.9698 | 2.5071 | 49.6284 | 4.0132 |
| 1 | 6 | 1.0000 | 0.9235 | n/a | 114.1080 | n/a |
| 2 | 5 | 0.5000 | 0.9956 | 0.7816 | -8.4314 | -0.2516 |
| 3 | 6 | 0.6667 | 0.9811 | 0.7941 | 16.6373 | 0.5807 |
| 4 | 6 | 0.5000 | 1.0473 | 1.8346 | 22.8509 | 0.8296 |

