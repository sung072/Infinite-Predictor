# Strict Multi-Cycle Research Result

- symbol: `ENA`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5275 | 0.9850 | 0.2377 | 1.1069 | -8.5362 | 1.0335 | 0.6370 | 0.6370 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5275 | 0.9873 | 0.2377 | 1.1069 | -8.5362 | 1.0335 | 0.6352 | 0.6352 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5275 | 0.9895 | 0.2377 | 1.1069 | -8.5362 | 1.0335 | 0.6336 | 0.6336 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5275 | 0.9919 | 0.2377 | 1.1069 | -8.5362 | 1.0335 | 0.6322 | 0.6322 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5814 | 0.9690 | 0.2160 | 1.0982 | 8.7422 | 1.7312 | 0.6052 | 0.6052 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5814 | 0.9736 | 0.2160 | 1.0982 | 8.7422 | 1.7312 | 0.6027 | 0.6027 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5814 | 0.9782 | 0.2160 | 1.0982 | 8.7422 | 1.7312 | 0.6004 | 0.6004 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5814 | 0.9829 | 0.2160 | 1.0982 | 8.7422 | 1.7312 | 0.5982 | 0.5982 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4933 | 1.0020 | 0.4336 | 1.0025 | -7.4277 | 0.5946 | 0.5637 | 0.5637 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4933 | 1.0032 | 0.4336 | 1.0025 | -7.4277 | 0.5946 | 0.5632 | 0.5632 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4933 | 1.0059 | 0.4336 | 1.0025 | -7.4277 | 0.5946 | 0.5623 | 0.5623 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4933 | 1.0095 | 0.4336 | 1.0025 | -7.4277 | 0.5946 | 0.5610 | 0.5610 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5436 | 0.9975 | 0.4321 | 0.8939 | -2.4297 | 0.7297 | 0.5568 | 0.5568 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5436 | 0.9983 | 0.4321 | 0.8939 | -2.4297 | 0.7297 | 0.5568 | 0.5568 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5436 | 0.9971 | 0.4321 | 0.8939 | -2.4297 | 0.7297 | 0.5568 | 0.5568 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5436 | 0.9975 | 0.4321 | 0.8939 | -2.4297 | 0.7297 | 0.5565 | 0.5565 |
| `base|emb=24|sh=0.96` | 18 | 0.5374 | 0.9972 | 1.0000 | 0.9035 | -0.3971 | 0.6340 | 0.5491 | 0.5491 |
| `base|emb=24|sh=0.97` | 18 | 0.5374 | 0.9973 | 1.0000 | 0.9035 | -0.3971 | 0.6340 | 0.5490 | 0.5490 |
| `base|emb=24|sh=0.95` | 18 | 0.5374 | 0.9976 | 1.0000 | 0.9035 | -0.3971 | 0.6340 | 0.5490 | 0.5490 |
| `base|emb=24|sh=0.94` | 18 | 0.5374 | 0.9983 | 1.0000 | 0.9035 | -0.3971 | 0.6340 | 0.5488 | 0.5488 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=344, top_n=35, cutoff=0.8469

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7320 | 0.0792 | 0.9451 | 0.0429 |
| all validations | 0.5354 | 0.1369 | 0.9952 | 0.0351 |

- improvement vs all (primary fraction): `hit +19.66pp, mae +5.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.96` | 0.5588 | 0.9600 | 1.0000 | 0.9517 | 0.0725 | 6.7878 | 0.5516 | 0.7395 | 0.7395 |
| 2 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 0.9684 | 0.3056 | 1.2858 | 0.0271 | 2.5385 | 0.1344 | 0.6724 | 0.6724 |
| 3 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 0.9737 | 0.3056 | 1.2858 | 0.0271 | 2.5385 | 0.1344 | 0.6702 | 0.6702 |
| 4 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 0.9789 | 0.3056 | 1.2858 | 0.0271 | 2.5385 | 0.1344 | 0.6680 | 0.6680 |
| 5 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 0.9842 | 0.3056 | 1.2858 | 0.0271 | 2.5385 | 0.1344 | 0.6658 | 0.6658 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 0.9791 | 0.8819 | -4.3486 | -0.1936 |
| 1 | 7 | 0.4286 | 1.0013 | 3.0505 | 28.4769 | 1.8031 |
| 2 | 7 | 0.5714 | 0.9446 | 0.9895 | 10.3804 | 0.5913 |
| 3 | 7 | 0.7143 | 0.9246 | 0.6377 | 18.1959 | 0.7395 |
| 4 | 7 | 0.5714 | 0.9695 | 0.6028 | -8.1666 | -0.8424 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 0.9791 | 0.8819 | -4.3486 | -0.1936 |
| top_20pct | 8 | 0.6250 | 0.9684 | 0.5857 | -0.9089 | -0.0532 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6250 | 0.9500 | 2.6480 | 51.5052 | 3.4325 |
| 1 | 7 | 0.2000 | 1.0969 | 0.4017 | -77.3744 | -1.1249 |
| 2 | 7 | 0.5714 | 0.9566 | 1.0202 | 12.5298 | 0.4638 |
| 3 | 7 | 0.7143 | 0.9236 | 0.4290 | 2.7068 | 0.0788 |
| 4 | 7 | 0.5714 | 0.9592 | 0.7629 | 0.6241 | 0.0088 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6250 | 0.9500 | 2.6480 | 51.5052 | 3.4325 |
| top_20pct | 8 | 0.6250 | 0.9516 | 0.6884 | 5.0182 | 0.2345 |

