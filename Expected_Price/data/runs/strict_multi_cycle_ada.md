# Strict Multi-Cycle Research Result

- symbol: `ADA`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5444 | 0.9933 | 0.3009 | 1.5034 | 16.5978 | 2.1782 | 0.6899 | 0.6899 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5444 | 0.9984 | 0.3009 | 1.5034 | 16.5978 | 2.1782 | 0.6881 | 0.6881 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5444 | 1.0039 | 0.3009 | 1.5034 | 16.5978 | 2.1782 | 0.6863 | 0.6863 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5444 | 1.0101 | 0.3009 | 1.5034 | 16.5978 | 2.1782 | 0.6843 | 0.6843 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5207 | 1.0012 | 0.4830 | 1.1214 | 5.9341 | 1.7712 | 0.6033 | 0.6033 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5207 | 1.0021 | 0.4830 | 1.1214 | 5.9341 | 1.7712 | 0.6030 | 0.6030 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5207 | 1.0033 | 0.4830 | 1.1214 | 5.9341 | 1.7712 | 0.6027 | 0.6027 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5207 | 1.0046 | 0.4830 | 1.1214 | 5.9341 | 1.7712 | 0.6023 | 0.6023 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4838 | 1.0072 | 0.4846 | 1.0530 | -2.0800 | 1.3604 | 0.5639 | 0.5639 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4838 | 1.0099 | 0.4846 | 1.0530 | -2.0800 | 1.3604 | 0.5629 | 0.5629 |
| `base|emb=12|sh=0.97` | 18 | 0.5000 | 1.0048 | 1.0000 | 1.0461 | 0.5374 | 0.3042 | 0.5620 | 0.5620 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4838 | 1.0133 | 0.4846 | 1.0530 | -2.0800 | 1.3604 | 0.5617 | 0.5617 |
| `base|emb=12|sh=0.96` | 18 | 0.5000 | 1.0073 | 1.0000 | 1.0461 | 0.5374 | 0.3042 | 0.5610 | 0.5610 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4838 | 1.0167 | 0.4846 | 1.0530 | -2.0800 | 1.3604 | 0.5605 | 0.5605 |
| `base|emb=12|sh=0.95` | 18 | 0.5000 | 1.0104 | 1.0000 | 1.0461 | 0.5374 | 0.3042 | 0.5599 | 0.5599 |
| `base|emb=12|sh=0.94` | 18 | 0.5000 | 1.0141 | 1.0000 | 1.0461 | 0.5374 | 0.3042 | 0.5586 | 0.5586 |
| `base|emb=24|sh=0.97` | 18 | 0.5048 | 1.0046 | 1.0000 | 1.0388 | 1.1495 | 0.4459 | 0.5550 | 0.5550 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4561 | 1.0248 | 0.2994 | 1.2233 | -5.4022 | 0.8803 | 0.5542 | 0.5542 |
| `base|emb=24|sh=0.96` | 18 | 0.5048 | 1.0073 | 1.0000 | 1.0388 | 1.1495 | 0.4459 | 0.5539 | 0.5539 |
| `base|emb=24|sh=0.95` | 18 | 0.5048 | 1.0106 | 1.0000 | 1.0388 | 1.1495 | 0.4459 | 0.5527 | 0.5527 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=332, top_n=34, cutoff=0.8397

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6533 | 0.0735 | 0.9782 | 0.0168 |
| all validations | 0.5016 | 0.1131 | 1.0116 | 0.0360 |

- improvement vs all (primary fraction): `hit +15.17pp, mae +3.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6061 | 0.9795 | 0.9444 | 0.7758 | 0.0651 | 6.0896 | 0.3864 | 0.7252 | 0.7252 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6061 | 0.9829 | 0.9444 | 0.7758 | 0.0651 | 6.0896 | 0.3864 | 0.7238 | 0.7238 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6061 | 0.9864 | 0.9444 | 0.7758 | 0.0651 | 6.0896 | 0.3864 | 0.7224 | 0.7224 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6061 | 0.9898 | 0.9444 | 0.7758 | 0.0651 | 6.0896 | 0.3864 | 0.7210 | 0.7210 |
| 5 | `base|emb=12|sh=0.97` | 0.5758 | 0.9915 | 1.0000 | 0.7527 | 0.0078 | 0.7266 | 0.0242 | 0.5919 | 0.5919 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.2857 | 1.0489 | 0.4282 | -54.8204 | -1.4897 |
| 1 | 7 | 0.4286 | 0.9660 | 0.4124 | -37.1057 | -0.8984 |
| 2 | 6 | 0.8000 | 0.9725 | 12.0041 | 103.5492 | 47.3199 |
| 3 | 7 | 0.7143 | 0.9262 | 3.5448 | 62.7522 | 13.1601 |
| 4 | 7 | 0.8571 | 0.9452 | 1.8419 | 78.6924 | 10.1216 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.2857 | 1.0489 | 0.4282 | -54.8204 | -1.4897 |
| top_20pct | 7 | 0.8571 | 0.9452 | 1.8419 | 78.6924 | 10.1216 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.5714 | 0.9541 | 0.7909 | 1.5964 | 0.0502 |
| 1 | 7 | 0.7143 | 0.9175 | 7.2695 | 79.2574 | 26.0312 |
| 2 | 6 | 0.8000 | 1.0328 | 1.9232 | 70.1975 | 6.7068 |
| 3 | 7 | 0.5714 | 0.9910 | 0.5063 | -14.1130 | -0.7067 |
| 4 | 7 | 0.4286 | 0.9972 | 0.8645 | -16.8039 | -0.3586 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.5714 | 0.9541 | 0.7909 | 1.5964 | 0.0502 |
| top_20pct | 7 | 0.4286 | 0.9972 | 0.8645 | -16.8039 | -0.3586 |

