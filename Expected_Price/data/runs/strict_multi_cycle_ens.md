# Strict Multi-Cycle Research Result

- symbol: `ENS`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5918 | 0.9939 | 0.3889 | 1.2369 | 21.4567 | 2.0579 | 0.7015 | 0.7015 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5918 | 0.9941 | 0.3889 | 1.2369 | 21.4567 | 2.0579 | 0.7007 | 0.7007 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5918 | 0.9953 | 0.3889 | 1.2369 | 21.4567 | 2.0579 | 0.6998 | 0.6998 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5918 | 0.9965 | 0.3889 | 1.2369 | 21.4567 | 2.0579 | 0.6989 | 0.6989 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5350 | 0.9957 | 0.2901 | 1.0971 | 7.5112 | 1.2281 | 0.6322 | 0.6322 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5350 | 0.9964 | 0.2901 | 1.0971 | 7.5112 | 1.2281 | 0.6318 | 0.6318 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5350 | 0.9971 | 0.2901 | 1.0971 | 7.5112 | 1.2281 | 0.6315 | 0.6315 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5350 | 0.9978 | 0.2901 | 1.0971 | 7.5112 | 1.2281 | 0.6312 | 0.6312 |
| `base|emb=12|sh=0.97` | 18 | 0.5332 | 1.0050 | 1.0000 | 1.0288 | 5.1997 | 0.7410 | 0.6060 | 0.6060 |
| `base|emb=12|sh=0.96` | 18 | 0.5332 | 1.0066 | 1.0000 | 1.0288 | 5.1997 | 0.7410 | 0.6054 | 0.6054 |
| `base|emb=12|sh=0.95` | 18 | 0.5332 | 1.0083 | 1.0000 | 1.0288 | 5.1997 | 0.7410 | 0.6048 | 0.6048 |
| `base|emb=12|sh=0.94` | 18 | 0.5332 | 1.0102 | 1.0000 | 1.0288 | 5.1997 | 0.7410 | 0.6042 | 0.6042 |
| `base|emb=24|sh=0.97` | 18 | 0.5346 | 1.0030 | 1.0000 | 0.9687 | 3.5538 | 0.4533 | 0.5899 | 0.5899 |
| `base|emb=24|sh=0.96` | 18 | 0.5346 | 1.0040 | 1.0000 | 0.9687 | 3.5538 | 0.4533 | 0.5896 | 0.5896 |
| `base|emb=24|sh=0.95` | 18 | 0.5346 | 1.0050 | 1.0000 | 0.9687 | 3.5538 | 0.4533 | 0.5893 | 0.5893 |
| `base|emb=24|sh=0.94` | 18 | 0.5346 | 1.0063 | 1.0000 | 0.9687 | 3.5538 | 0.4533 | 0.5888 | 0.5888 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5189 | 1.0170 | 0.3935 | 1.2388 | 9.5168 | 1.3755 | 0.5859 | 0.5859 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5189 | 1.0227 | 0.3935 | 1.2388 | 9.5168 | 1.3755 | 0.5842 | 0.5842 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5189 | 1.0284 | 0.3935 | 1.2388 | 9.5168 | 1.3755 | 0.5825 | 0.5825 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5189 | 1.0350 | 0.3935 | 1.2388 | 9.5168 | 1.3755 | 0.5807 | 0.5807 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=332, top_n=34, cutoff=0.8198

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6654 | 0.0451 | 0.9675 | 0.0209 |
| all validations | 0.5344 | 0.1046 | 1.0066 | 0.0391 |

- improvement vs all (primary fraction): `hit +13.11pp, mae +3.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7273 | 0.9568 | 0.7222 | 1.1214 | 0.4313 | 40.3715 | 4.0735 | 0.8547 | 0.8547 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7273 | 0.9640 | 0.7222 | 1.1214 | 0.4313 | 40.3715 | 4.0735 | 0.8516 | 0.8516 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7273 | 0.9712 | 0.7222 | 1.1214 | 0.4313 | 40.3715 | 4.0735 | 0.8485 | 0.8485 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7273 | 0.9784 | 0.7222 | 1.1214 | 0.4313 | 40.3715 | 4.0735 | 0.8455 | 0.8455 |
| 5 | `base|emb=12|sh=0.97` | 0.6667 | 0.9888 | 1.0000 | 0.6014 | 0.0733 | 6.8636 | 0.4218 | 0.7284 | 0.7284 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.6000 | 0.9788 | 0.6714 | 0.2309 | -0.0032 |
| 1 | 5 | 0.8000 | 0.9604 | 3.1555 | 93.3698 | 11.6948 |
| 2 | 5 | 1.0000 | 0.8735 | n/a | 158.8750 | n/a |
| 3 | 5 | 0.8000 | 0.9623 | 0.7893 | 43.8318 | 2.1586 |
| 4 | 5 | 0.5000 | 0.9847 | 2.0075 | 24.5500 | 1.0050 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.7500 | 0.9791 | 1.3306 | 55.7339 | 2.9933 |
| 1 | 5 | 0.7500 | 0.8869 | 2.3479 | 81.3563 | 6.0588 |
| 2 | 5 | 0.7500 | 0.9053 | 3.0325 | 72.4897 | 8.1214 |
| 3 | 5 | 0.6000 | 1.0052 | 1.0429 | 15.5593 | 0.6486 |
| 4 | 5 | 0.8000 | 0.9598 | 0.7114 | 43.8399 | 1.8469 |

