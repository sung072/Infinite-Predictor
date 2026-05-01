# Strict Multi-Cycle Research Result

- symbol: `DOT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `base|emb=12|sh=0.96` | 18 | 0.5274 | 0.9979 | 1.0000 | 0.9473 | 1.4675 | 0.2232 | 0.5982 | 0.5982 |
| `base|emb=12|sh=0.97` | 18 | 0.5274 | 0.9981 | 1.0000 | 0.9473 | 1.4675 | 0.2232 | 0.5981 | 0.5981 |
| `base|emb=12|sh=0.95` | 18 | 0.5274 | 0.9990 | 1.0000 | 0.9473 | 1.4675 | 0.2232 | 0.5978 | 0.5978 |
| `base|emb=12|sh=0.94` | 18 | 0.5274 | 1.0009 | 1.0000 | 0.9473 | 1.4675 | 0.2232 | 0.5971 | 0.5971 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5055 | 1.0060 | 0.3102 | 1.0864 | -0.2445 | 0.8813 | 0.5778 | 0.5778 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5055 | 1.0040 | 0.3102 | 1.0864 | -0.2445 | 0.8813 | 0.5777 | 0.5777 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5055 | 1.0028 | 0.3102 | 1.0864 | -0.2445 | 0.8813 | 0.5774 | 0.5774 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5055 | 1.0119 | 0.3102 | 1.0864 | -0.2445 | 0.8813 | 0.5767 | 0.5767 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5111 | 1.0052 | 0.3133 | 1.1204 | 1.3303 | 1.9495 | 0.5687 | 0.5687 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5111 | 1.0079 | 0.3133 | 1.1204 | 1.3303 | 1.9495 | 0.5682 | 0.5682 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5111 | 1.0137 | 0.3133 | 1.1204 | 1.3303 | 1.9495 | 0.5667 | 0.5667 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5111 | 1.0227 | 0.3133 | 1.1204 | 1.3303 | 1.9495 | 0.5639 | 0.5639 |
| `base|emb=24|sh=0.96` | 18 | 0.5262 | 0.9982 | 1.0000 | 0.9333 | 0.3875 | 0.2425 | 0.5603 | 0.5603 |
| `base|emb=24|sh=0.95` | 18 | 0.5262 | 0.9986 | 1.0000 | 0.9333 | 0.3875 | 0.2425 | 0.5602 | 0.5602 |
| `base|emb=24|sh=0.97` | 18 | 0.5262 | 0.9986 | 1.0000 | 0.9333 | 0.3875 | 0.2425 | 0.5601 | 0.5601 |
| `base|emb=24|sh=0.94` | 18 | 0.5262 | 0.9997 | 1.0000 | 0.9333 | 0.3875 | 0.2425 | 0.5599 | 0.5599 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5022 | 1.0079 | 0.4645 | 0.8688 | -6.8298 | 0.1693 | 0.5235 | 0.5235 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5022 | 1.0105 | 0.4645 | 0.8688 | -6.8298 | 0.1693 | 0.5227 | 0.5227 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5022 | 1.0131 | 0.4645 | 0.8688 | -6.8298 | 0.1693 | 0.5218 | 0.5218 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5022 | 1.0158 | 0.4645 | 0.8688 | -6.8298 | 0.1693 | 0.5210 | 0.5210 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8184

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6671 | 0.0840 | 0.9640 | 0.0412 |
| all validations | 0.5131 | 0.1177 | 1.0053 | 0.0457 |

- improvement vs all (primary fraction): `hit +15.40pp, mae +4.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.8077 | 0.9554 | 0.7500 | 0.6767 | 0.3863 | 36.1548 | 3.1669 | 0.8419 | 0.8419 |
| 2 | `base|emb=12|sh=0.94` | 0.6250 | 0.9724 | 1.0000 | 0.6915 | 0.0534 | 4.9963 | 0.3337 | 0.7211 | 0.7211 |
| 3 | `base|emb=12|sh=0.95` | 0.6250 | 0.9770 | 1.0000 | 0.6915 | 0.0534 | 4.9963 | 0.3337 | 0.7191 | 0.7191 |
| 4 | `base|emb=12|sh=0.96` | 0.6250 | 0.9816 | 1.0000 | 0.6915 | 0.0534 | 4.9963 | 0.3337 | 0.7172 | 0.7172 |
| 5 | `base|emb=12|sh=0.97` | 0.6250 | 0.9862 | 1.0000 | 0.6915 | 0.0534 | 4.9963 | 0.3337 | 0.7153 | 0.7153 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 1.0000 | 0.9545 | n/a | 212.7171 | n/a |
| 1 | 5 | 0.8000 | 0.9519 | 0.2159 | -4.5682 | -0.1471 |
| 2 | 5 | 0.8000 | 0.9166 | 3.9849 | 88.4846 | n/a |
| 3 | 5 | 0.4000 | 1.0312 | 0.7992 | -18.7937 | -0.5056 |
| 4 | 6 | 1.0000 | 0.9310 | n/a | 130.9808 | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 1.0000 | 0.9734 | n/a | 189.6162 | n/a |
| 1 | 5 | 1.0000 | 0.8518 | n/a | 177.1313 | n/a |
| 2 | 5 | 0.6000 | 0.9735 | 6.9881 | 61.7969 | 18.9502 |
| 3 | 5 | 0.8000 | 0.9566 | 0.5010 | 26.5226 | 0.9973 |
| 4 | 6 | 0.6667 | 0.9717 | 0.5863 | 5.3111 | 0.1613 |

