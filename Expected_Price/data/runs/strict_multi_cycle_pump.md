# Strict Multi-Cycle Research Result

- symbol: `PUMP`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5613 | 0.9968 | 0.4182 | 1.0061 | 5.7303 | 0.6365 | 0.6630 | 0.6630 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5613 | 0.9995 | 0.4182 | 1.0061 | 5.7303 | 0.6365 | 0.6624 | 0.6624 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5613 | 1.0026 | 0.4182 | 1.0061 | 5.7303 | 0.6365 | 0.6618 | 0.6618 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5613 | 1.0075 | 0.4182 | 1.0061 | 5.7303 | 0.6365 | 0.6606 | 0.6606 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5868 | 0.9835 | 0.3719 | 1.2252 | 12.7439 | 2.0132 | 0.6323 | 0.6323 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5868 | 0.9848 | 0.3719 | 1.2252 | 12.7439 | 2.0132 | 0.6322 | 0.6322 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5868 | 0.9833 | 0.3719 | 1.2252 | 12.7439 | 2.0132 | 0.6320 | 0.6320 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5868 | 0.9869 | 0.3719 | 1.2252 | 12.7439 | 2.0132 | 0.6319 | 0.6319 |
| `base|emb=12|sh=0.97` | 18 | 0.5355 | 0.9971 | 1.0000 | 0.8766 | 0.0564 | 0.2024 | 0.5599 | 0.5599 |
| `base|emb=12|sh=0.96` | 18 | 0.5355 | 0.9973 | 1.0000 | 0.8766 | 0.0564 | 0.2024 | 0.5599 | 0.5599 |
| `base|emb=12|sh=0.95` | 18 | 0.5355 | 0.9981 | 1.0000 | 0.8766 | 0.0564 | 0.2024 | 0.5597 | 0.5597 |
| `base|emb=12|sh=0.94` | 18 | 0.5355 | 0.9997 | 1.0000 | 0.8766 | 0.0564 | 0.2024 | 0.5592 | 0.5592 |
| `base|emb=24|sh=0.97` | 18 | 0.5371 | 0.9981 | 1.0000 | 0.9138 | 1.2309 | 0.3246 | 0.5527 | 0.5527 |
| `base|emb=24|sh=0.96` | 18 | 0.5371 | 0.9991 | 1.0000 | 0.9138 | 1.2309 | 0.3246 | 0.5524 | 0.5524 |
| `base|emb=24|sh=0.95` | 18 | 0.5371 | 1.0006 | 1.0000 | 0.9138 | 1.2309 | 0.3246 | 0.5519 | 0.5519 |
| `base|emb=24|sh=0.94` | 18 | 0.5371 | 1.0029 | 1.0000 | 0.9138 | 1.2309 | 0.3246 | 0.5511 | 0.5511 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4828 | 1.0026 | 0.3565 | 0.8502 | -12.0707 | 0.0702 | 0.5162 | 0.5162 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4828 | 1.0035 | 0.3565 | 0.8502 | -12.0707 | 0.0702 | 0.5160 | 0.5160 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4828 | 1.0043 | 0.3565 | 0.8502 | -12.0707 | 0.0702 | 0.5157 | 0.5157 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4828 | 1.0054 | 0.3565 | 0.8502 | -12.0707 | 0.0702 | 0.5154 | 0.5154 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8147

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7173 | 0.0807 | 0.9518 | 0.0536 |
| all validations | 0.5343 | 0.1198 | 0.9992 | 0.0411 |

- improvement vs all (primary fraction): `hit +18.30pp, mae +4.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.5938 | 0.9966 | 1.0000 | 1.0524 | 0.1574 | 14.7343 | 0.7615 | 0.7455 | 0.7455 |
| 2 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9818 | 0.1667 | 1.4659 | 0.1627 | 15.2235 | 0.5782 | 0.7444 | 0.7444 |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9848 | 0.1667 | 1.4659 | 0.1627 | 15.2235 | 0.5782 | 0.7432 | 0.7432 |
| 4 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9879 | 0.1667 | 1.4659 | 0.1627 | 15.2235 | 0.5782 | 0.7419 | 0.7419 |
| 5 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9909 | 0.1667 | 1.4659 | 0.1627 | 15.2235 | 0.5782 | 0.7407 | 0.7407 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.4286 | 1.0235 | 0.6119 | -23.8814 | -0.6014 |
| 1 | 7 | 0.3333 | 1.0880 | 2.6321 | 8.6438 | 0.3612 |
| 2 | 7 | 0.6667 | 1.0046 | 0.6447 | 8.4439 | 0.3140 |
| 3 | 7 | 0.6667 | 1.0141 | 2.4052 | 57.5150 | 4.5092 |
| 4 | 7 | 0.8571 | 0.9026 | 0.4031 | 27.6308 | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.4286 | 1.0235 | 0.6119 | -23.8814 | -0.6014 |
| top_20pct | 8 | 0.8750 | 0.9220 | 0.4777 | 40.0338 | 2.3570 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 0.9998 | 1.9417 | 25.3469 | 1.1740 |
| 1 | 7 | 0.8333 | 0.9407 | 0.9675 | 43.5592 | 3.8485 |
| 2 | 7 | 0.7143 | 0.9298 | 1.8341 | 51.2618 | 3.6165 |
| 3 | 7 | 0.0000 | 1.1059 | n/a | -104.0277 | -1.4054 |
| 4 | 7 | 0.8571 | 0.9641 | 2.9504 | 99.9095 | 17.0918 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 0.9998 | 1.9417 | 25.3469 | 1.1740 |
| top_20pct | 8 | 0.7500 | 0.9760 | 0.8088 | 32.8907 | 1.6520 |

