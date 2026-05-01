# Strict Multi-Cycle Research Result

- symbol: `HBAR`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5058 | 0.9992 | 0.4985 | 1.4376 | 11.2050 | 1.7581 | 0.6583 | 0.6583 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5058 | 0.9991 | 0.4985 | 1.4376 | 11.2050 | 1.7581 | 0.6583 | 0.6583 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5058 | 0.9992 | 0.4985 | 1.4376 | 11.2050 | 1.7581 | 0.6582 | 0.6582 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5058 | 0.9999 | 0.4985 | 1.4376 | 11.2050 | 1.7581 | 0.6580 | 0.6580 |
| `base|emb=12|sh=0.95` | 18 | 0.5290 | 0.9959 | 1.0000 | 1.0811 | 5.8959 | 0.8295 | 0.6397 | 0.6397 |
| `base|emb=12|sh=0.96` | 18 | 0.5290 | 0.9959 | 1.0000 | 1.0811 | 5.8959 | 0.8295 | 0.6397 | 0.6397 |
| `base|emb=12|sh=0.97` | 18 | 0.5290 | 0.9964 | 1.0000 | 1.0811 | 5.8959 | 0.8295 | 0.6394 | 0.6394 |
| `base|emb=12|sh=0.94` | 18 | 0.5290 | 0.9968 | 1.0000 | 1.0811 | 5.8959 | 0.8295 | 0.6394 | 0.6394 |
| `base|emb=24|sh=0.97` | 18 | 0.5204 | 0.9991 | 1.0000 | 1.0857 | 4.8998 | 0.7915 | 0.6016 | 0.6016 |
| `base|emb=24|sh=0.96` | 18 | 0.5204 | 0.9992 | 1.0000 | 1.0857 | 4.8998 | 0.7915 | 0.6016 | 0.6016 |
| `base|emb=24|sh=0.95` | 18 | 0.5204 | 0.9997 | 1.0000 | 1.0857 | 4.8998 | 0.7915 | 0.6014 | 0.6014 |
| `base|emb=24|sh=0.94` | 18 | 0.5204 | 1.0011 | 1.0000 | 1.0857 | 4.8998 | 0.7915 | 0.6010 | 0.6010 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4634 | 1.0059 | 0.5185 | 1.2335 | -3.0733 | 0.8341 | 0.5850 | 0.5850 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4634 | 1.0082 | 0.5185 | 1.2335 | -3.0733 | 0.8341 | 0.5843 | 0.5843 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4634 | 1.0106 | 0.5185 | 1.2335 | -3.0733 | 0.8341 | 0.5835 | 0.5835 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4634 | 1.0135 | 0.5185 | 1.2335 | -3.0733 | 0.8341 | 0.5826 | 0.5826 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4749 | 1.0134 | 0.2932 | 1.1855 | -1.9141 | 1.5963 | 0.5338 | 0.5338 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4749 | 1.0192 | 0.2932 | 1.1855 | -1.9141 | 1.5963 | 0.5324 | 0.5324 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4749 | 1.0256 | 0.2932 | 1.1855 | -1.9141 | 1.5963 | 0.5310 | 0.5310 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4749 | 1.0360 | 0.2932 | 1.1855 | -1.9141 | 1.5963 | 0.5287 | 0.5287 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8439

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6847 | 0.0871 | 0.9650 | 0.0390 |
| all validations | 0.4977 | 0.1388 | 1.0068 | 0.0452 |

- improvement vs all (primary fraction): `hit +18.70pp, mae +4.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.95` | 0.5000 | 0.9983 | 1.0000 | 1.0450 | 0.0171 | 1.6006 | 0.0964 | 0.6273 | 0.6273 |
| 2 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4000 | 1.0075 | 0.1389 | 0.5791 | -0.2780 | -26.0212 | -0.6247 | 0.3351 | 0.3351 |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4000 | 1.0100 | 0.1389 | 0.5791 | -0.2780 | -26.0212 | -0.6247 | 0.3341 | 0.3341 |
| 4 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4000 | 1.0125 | 0.1389 | 0.5791 | -0.2780 | -26.0212 | -0.6247 | 0.3331 | 0.3331 |
| 5 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4000 | 1.0150 | 0.1389 | 0.5791 | -0.2780 | -26.0212 | -0.6247 | 0.3322 | 0.3322 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.2500 | 1.0631 | 0.6411 | -46.3256 | -0.8113 |
| 1 | 7 | 0.5714 | 0.9886 | 0.2973 | -26.0963 | -0.6425 |
| 2 | 7 | 0.4286 | 0.9950 | 1.3801 | 1.4357 | 0.0485 |
| 3 | 7 | 0.8333 | 0.9460 | 14.9750 | 92.6760 | 74.3029 |
| 4 | 7 | 0.5000 | 0.9967 | 1.8169 | 21.4255 | 0.8664 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.2500 | 1.0631 | 0.6411 | -46.3256 | -0.8113 |
| top_20pct | 8 | 0.5714 | 0.9966 | 2.0952 | 38.1218 | 1.9140 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5714 | 0.9794 | 1.8019 | 32.9621 | 1.4945 |
| 1 | 7 | 0.6667 | 1.0018 | 1.6377 | 37.1416 | 38.7734 |
| 2 | 7 | 0.2857 | 1.0428 | 0.6676 | -37.3714 | -0.7622 |
| 3 | 7 | 0.5714 | 0.9772 | 0.5666 | -9.2481 | -0.4462 |
| 4 | 7 | 0.4286 | 1.0093 | 1.0601 | -9.0854 | -0.2102 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5714 | 0.9794 | 1.8019 | 32.9621 | 1.4945 |
| top_20pct | 8 | 0.3750 | 1.0116 | 0.8310 | -27.2390 | -0.8063 |

