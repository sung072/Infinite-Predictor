# Strict Multi-Cycle Research Result

- symbol: `ETH`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4627 | 1.0075 | 0.3488 | 1.4632 | 4.7535 | 0.6382 | 0.6141 | 0.6141 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4627 | 1.0144 | 0.3488 | 1.4632 | 4.7535 | 0.6382 | 0.6115 | 0.6115 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4627 | 1.0228 | 0.3488 | 1.4632 | 4.7535 | 0.6382 | 0.6085 | 0.6085 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4627 | 1.0324 | 0.3488 | 1.4632 | 4.7535 | 0.6382 | 0.6051 | 0.6051 |
| `base|emb=24|sh=0.97` | 18 | 0.4968 | 1.0012 | 1.0000 | 1.0747 | 0.5873 | 0.5252 | 0.5526 | 0.5526 |
| `base|emb=24|sh=0.96` | 18 | 0.4968 | 1.0035 | 1.0000 | 1.0747 | 0.5873 | 0.5252 | 0.5518 | 0.5518 |
| `base|emb=24|sh=0.95` | 18 | 0.4968 | 1.0065 | 1.0000 | 1.0747 | 0.5873 | 0.5252 | 0.5507 | 0.5507 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4785 | 1.0155 | 0.3272 | 1.2765 | 0.7100 | 0.5435 | 0.5505 | 0.5505 |
| `base|emb=24|sh=0.94` | 18 | 0.4968 | 1.0101 | 1.0000 | 1.0747 | 0.5873 | 0.5252 | 0.5494 | 0.5494 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4785 | 1.0312 | 0.3272 | 1.2765 | 0.7100 | 0.5435 | 0.5448 | 0.5448 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5136 | 0.9965 | 0.4151 | 1.0262 | -0.1619 | 0.6168 | 0.5440 | 0.5440 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5136 | 0.9968 | 0.4151 | 1.0262 | -0.1619 | 0.6168 | 0.5438 | 0.5438 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5136 | 0.9971 | 0.4151 | 1.0262 | -0.1619 | 0.6168 | 0.5436 | 0.5436 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5136 | 0.9976 | 0.4151 | 1.0262 | -0.1619 | 0.6168 | 0.5434 | 0.5434 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4785 | 1.0522 | 0.3272 | 1.2765 | 0.7100 | 0.5435 | 0.5378 | 0.5378 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4785 | 1.0765 | 0.3272 | 1.2765 | 0.7100 | 0.5435 | 0.5302 | 0.5302 |
| `base|emb=12|sh=0.97` | 18 | 0.4759 | 1.0072 | 1.0000 | 1.0454 | -2.6613 | 0.3025 | 0.5133 | 0.5133 |
| `base|emb=12|sh=0.96` | 18 | 0.4759 | 1.0121 | 1.0000 | 1.0454 | -2.6613 | 0.3025 | 0.5115 | 0.5115 |
| `base|emb=12|sh=0.95` | 18 | 0.4759 | 1.0181 | 1.0000 | 1.0454 | -2.6613 | 0.3025 | 0.5093 | 0.5093 |
| `base|emb=12|sh=0.94` | 18 | 0.4759 | 1.0251 | 1.0000 | 1.0454 | -2.6613 | 0.3025 | 0.5068 | 0.5068 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8135

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5940 | 0.0511 | 0.9810 | 0.0095 |
| all validations | 0.4829 | 0.0872 | 1.0130 | 0.0353 |

- improvement vs all (primary fraction): `hit +11.10pp, mae +3.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6154 | 0.9368 | 0.7222 | 0.9988 | 0.1805 | 16.8962 | 1.3754 | 0.7911 | 0.7911 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6154 | 0.9457 | 0.7222 | 0.9988 | 0.1805 | 16.8962 | 1.3754 | 0.7871 | 0.7871 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6154 | 0.9548 | 0.7222 | 0.9988 | 0.1805 | 16.8962 | 1.3754 | 0.7831 | 0.7831 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6154 | 0.9657 | 0.7222 | 0.9988 | 0.1805 | 16.8962 | 1.3754 | 0.7783 | 0.7783 |
| 5 | `base|emb=24|sh=0.97` | 0.5429 | 0.9809 | 1.0000 | 0.7820 | -0.0258 | -2.4129 | -0.1837 | 0.4485 | 0.4485 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.5000 | 1.0057 | 0.9063 | -2.9117 | -0.1082 |
| 1 | 5 | 0.8000 | 0.8706 | 1.4068 | 67.0096 | 4.6406 |
| 2 | 5 | 0.6000 | 0.9475 | 0.9814 | 15.2312 | 0.6265 |
| 3 | 5 | 0.6000 | 0.9161 | 0.7045 | 1.8118 | 0.0485 |
| 4 | 5 | 0.6000 | 0.9736 | 1.5774 | 28.0156 | 2.6666 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.6667 | 0.8687 | 2.8057 | 65.2376 | 6.4943 |
| 1 | 5 | 0.6000 | 0.9542 | 0.4503 | -12.7634 | -0.4116 |
| 2 | 5 | 0.4000 | 0.9857 | 1.1349 | -9.2039 | -0.2952 |
| 3 | 5 | 0.6000 | 0.9294 | 1.8625 | 33.7195 | 1.7925 |
| 4 | 5 | 0.8000 | 0.9239 | 0.6368 | 35.1300 | n/a |

