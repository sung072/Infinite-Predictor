# Strict Multi-Cycle Research Result

- symbol: `DEXE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5134 | 1.0002 | 0.4552 | 1.6103 | 6.9936 | 3.0687 | 0.6635 | 0.6635 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5134 | 1.0015 | 0.4552 | 1.6103 | 6.9936 | 3.0687 | 0.6631 | 0.6631 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5134 | 1.0034 | 0.4552 | 1.6103 | 6.9936 | 3.0687 | 0.6625 | 0.6625 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5134 | 1.0064 | 0.4552 | 1.6103 | 6.9936 | 3.0687 | 0.6615 | 0.6615 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4746 | 1.0032 | 0.4537 | 1.3980 | 2.1614 | 0.8557 | 0.6218 | 0.6218 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4746 | 1.0054 | 0.4537 | 1.3980 | 2.1614 | 0.8557 | 0.6209 | 0.6209 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4746 | 1.0083 | 0.4537 | 1.3980 | 2.1614 | 0.8557 | 0.6199 | 0.6199 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4746 | 1.0127 | 0.4537 | 1.3980 | 2.1614 | 0.8557 | 0.6182 | 0.6182 |
| `base|emb=12|sh=0.97` | 18 | 0.4810 | 0.9993 | 1.0000 | 1.2112 | 1.0766 | 0.5796 | 0.5902 | 0.5902 |
| `base|emb=12|sh=0.96` | 18 | 0.4810 | 1.0004 | 1.0000 | 1.2112 | 1.0766 | 0.5796 | 0.5898 | 0.5898 |
| `base|emb=12|sh=0.95` | 18 | 0.4810 | 1.0023 | 1.0000 | 1.2112 | 1.0766 | 0.5796 | 0.5891 | 0.5891 |
| `base|emb=12|sh=0.94` | 18 | 0.4810 | 1.0049 | 1.0000 | 1.2112 | 1.0766 | 0.5796 | 0.5881 | 0.5881 |
| `base|emb=24|sh=0.97` | 18 | 0.4857 | 0.9977 | 1.0000 | 1.2492 | 1.5542 | 0.7833 | 0.5868 | 0.5868 |
| `base|emb=24|sh=0.96` | 18 | 0.4857 | 0.9983 | 1.0000 | 1.2492 | 1.5542 | 0.7833 | 0.5866 | 0.5866 |
| `base|emb=24|sh=0.95` | 18 | 0.4857 | 0.9997 | 1.0000 | 1.2492 | 1.5542 | 0.7833 | 0.5861 | 0.5861 |
| `base|emb=24|sh=0.94` | 18 | 0.4857 | 1.0019 | 1.0000 | 1.2492 | 1.5542 | 0.7833 | 0.5853 | 0.5853 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4930 | 0.9976 | 0.3673 | 1.9223 | -4.1657 | 0.5322 | 0.5603 | 0.5603 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4930 | 0.9982 | 0.3673 | 1.9223 | -4.1657 | 0.5322 | 0.5601 | 0.5601 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4930 | 0.9989 | 0.3673 | 1.9223 | -4.1657 | 0.5322 | 0.5598 | 0.5598 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4930 | 0.9998 | 0.3673 | 1.9223 | -4.1657 | 0.5322 | 0.5596 | 0.5596 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8280

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5811 | 0.1171 | 0.9780 | 0.0175 |
| all validations | 0.4804 | 0.1030 | 1.0029 | 0.0237 |

- improvement vs all (primary fraction): `hit +10.07pp, mae +2.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6400 | 0.9497 | 0.7222 | 0.8225 | 0.1547 | 14.4802 | 2.0851 | 0.7994 | 0.7994 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6400 | 0.9573 | 0.7222 | 0.8225 | 0.1547 | 14.4802 | 2.0851 | 0.7961 | 0.7961 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6400 | 0.9650 | 0.7222 | 0.8225 | 0.1547 | 14.4802 | 2.0851 | 0.7927 | 0.7927 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6400 | 0.9727 | 0.7222 | 0.8225 | 0.1547 | 14.4802 | 2.0851 | 0.7895 | 0.7895 |
| 5 | `base|emb=12|sh=0.97` | 0.5143 | 0.9997 | 1.0000 | 0.6159 | -0.1666 | -15.5928 | -0.7132 | 0.3600 | 0.3600 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.6667 | 0.9922 | 0.4250 | -6.0579 | -0.1605 |
| 1 | 5 | 0.6000 | 0.9486 | 0.7992 | 7.4102 | 0.3576 |
| 2 | 5 | 0.6000 | 0.9607 | 1.6202 | 33.9759 | 1.5385 |
| 3 | 5 | 0.6000 | 0.9527 | 0.3786 | -19.5984 | -0.5006 |
| 4 | 5 | n/a | n/a | n/a | n/a | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.8000 | 0.9137 | 0.5780 | 29.8784 | 1.2997 |
| 1 | 5 | 0.4000 | 0.9916 | 1.0694 | -12.3085 | -0.3358 |
| 2 | 5 | 0.6000 | 0.9034 | 0.8263 | 7.6106 | 0.2671 |
| 3 | 5 | 0.6000 | 1.0235 | 1.0013 | 15.1185 | 0.4928 |
| 4 | 5 | 0.8000 | 0.9199 | 1.0005 | 46.4967 | 3.0069 |

