# Strict Multi-Cycle Research Result

- symbol: `BROCCOLI714`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5680 | 1.0113 | 0.3056 | 1.5444 | 10.3481 | 2.0441 | 0.6695 | 0.6695 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5680 | 1.0187 | 0.3056 | 1.5444 | 10.3481 | 2.0441 | 0.6677 | 0.6677 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5680 | 1.0277 | 0.3056 | 1.5444 | 10.3481 | 2.0441 | 0.6658 | 0.6658 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5680 | 1.0375 | 0.3056 | 1.5444 | 10.3481 | 2.0441 | 0.6641 | 0.6641 |
| `base|emb=24|sh=0.97` | 18 | 0.5055 | 1.0032 | 1.0000 | 0.9852 | -0.5711 | 0.2444 | 0.5728 | 0.5728 |
| `base|emb=24|sh=0.96` | 18 | 0.5055 | 1.0052 | 1.0000 | 0.9852 | -0.5711 | 0.2444 | 0.5721 | 0.5721 |
| `base|emb=24|sh=0.95` | 18 | 0.5055 | 1.0080 | 1.0000 | 0.9852 | -0.5711 | 0.2444 | 0.5712 | 0.5712 |
| `base|emb=24|sh=0.94` | 18 | 0.5055 | 1.0114 | 1.0000 | 0.9852 | -0.5711 | 0.2444 | 0.5701 | 0.5701 |
| `base|emb=12|sh=0.97` | 18 | 0.5103 | 1.0026 | 1.0000 | 0.9501 | -1.1319 | 0.3519 | 0.5524 | 0.5524 |
| `base|emb=12|sh=0.96` | 18 | 0.5103 | 1.0042 | 1.0000 | 0.9501 | -1.1319 | 0.3519 | 0.5519 | 0.5519 |
| `base|emb=12|sh=0.95` | 18 | 0.5103 | 1.0069 | 1.0000 | 0.9501 | -1.1319 | 0.3519 | 0.5511 | 0.5511 |
| `base|emb=12|sh=0.94` | 18 | 0.5103 | 1.0101 | 1.0000 | 0.9501 | -1.1319 | 0.3519 | 0.5502 | 0.5502 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4969 | 1.0015 | 0.4198 | 1.0100 | -1.9888 | 0.1994 | 0.5310 | 0.5310 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4969 | 1.0020 | 0.4198 | 1.0100 | -1.9888 | 0.1994 | 0.5308 | 0.5308 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4969 | 1.0029 | 0.4198 | 1.0100 | -1.9888 | 0.1994 | 0.5305 | 0.5305 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4969 | 1.0040 | 0.4198 | 1.0100 | -1.9888 | 0.1994 | 0.5301 | 0.5301 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5253 | 1.0234 | 0.3040 | 0.9658 | -2.8309 | 0.1508 | 0.5080 | 0.5080 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5253 | 1.0340 | 0.3040 | 0.9658 | -2.8309 | 0.1508 | 0.5052 | 0.5052 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5253 | 1.0489 | 0.3040 | 0.9658 | -2.8309 | 0.1508 | 0.5017 | 0.5017 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5253 | 1.0659 | 0.3040 | 0.9658 | -2.8309 | 0.1508 | 0.4983 | 0.4983 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=336, top_n=34, cutoff=0.7831

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6114 | 0.1306 | 0.9822 | 0.0239 |
| all validations | 0.5138 | 0.1025 | 1.0134 | 0.0645 |

- improvement vs all (primary fraction): `hit +9.76pp, mae +3.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.6471 | 0.9751 | 1.0000 | 1.0906 | 0.2403 | 22.4921 | 3.5634 | 0.8249 | 0.8249 |
| 2 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.8886 | 0.1667 | 0.5973 | 0.0650 | 6.0802 | 0.2256 | 0.7654 | 0.7654 |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.8942 | 0.1667 | 0.5973 | 0.0650 | 6.0802 | 0.2256 | 0.7625 | 0.7625 |
| 4 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9154 | 0.1667 | 0.5973 | 0.0650 | 6.0802 | 0.2256 | 0.7522 | 0.7522 |
| 5 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9365 | 0.1667 | 0.5973 | 0.0650 | 6.0802 | 0.2256 | 0.7423 | 0.7423 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6250 | 0.9870 | 1.4732 | 30.6455 | 3.2658 |
| 1 | 7 | 0.4000 | 0.9954 | 2.0881 | 12.0044 | 1.3401 |
| 2 | 7 | 0.8571 | 0.9547 | 8.2750 | 86.1173 | 49.5886 |
| 3 | 7 | 0.7143 | 0.9764 | 0.7485 | 19.9935 | 1.6442 |
| 4 | 7 | 0.5714 | 0.9654 | 0.6679 | -4.2498 | -0.2750 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6250 | 0.9870 | 1.4732 | 30.6455 | 3.2658 |
| top_20pct | 8 | 0.6250 | 0.9460 | 0.5756 | -1.4838 | -0.1003 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.7500 | 0.9822 | 2.3312 | 49.2531 | 7.7925 |
| 1 | 7 | 0.4286 | 0.9953 | 2.9680 | 27.3074 | 1.2239 |
| 2 | 7 | 0.6667 | 0.9691 | 0.2753 | -16.2769 | -5.4467 |
| 3 | 7 | 0.8333 | 0.9603 | 0.5439 | 41.3924 | 1.7233 |
| 4 | 7 | 0.5714 | 0.9646 | 0.3511 | -26.3911 | -0.7400 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.7500 | 0.9822 | 2.3312 | 49.2531 | 7.7925 |
| top_20pct | 8 | 0.6250 | 0.9460 | 0.5756 | -1.4838 | -0.1003 |

