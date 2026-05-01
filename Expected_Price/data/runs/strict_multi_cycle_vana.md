# Strict Multi-Cycle Research Result

- symbol: `VANA`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5132 | 1.0003 | 0.4028 | 1.0188 | -1.9058 | 0.4564 | 0.5798 | 0.5798 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5132 | 1.0013 | 0.4028 | 1.0188 | -1.9058 | 0.4564 | 0.5795 | 0.5795 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5132 | 1.0023 | 0.4028 | 1.0188 | -1.9058 | 0.4564 | 0.5791 | 0.5791 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5132 | 1.0035 | 0.4028 | 1.0188 | -1.9058 | 0.4564 | 0.5787 | 0.5787 |
| `base|emb=12|sh=0.97` | 18 | 0.4956 | 1.0138 | 1.0000 | 0.9292 | -3.6880 | 0.1007 | 0.5443 | 0.5443 |
| `base|emb=12|sh=0.96` | 18 | 0.4956 | 1.0200 | 1.0000 | 0.9292 | -3.6880 | 0.1007 | 0.5423 | 0.5423 |
| `base|emb=12|sh=0.95` | 18 | 0.4956 | 1.0273 | 1.0000 | 0.9292 | -3.6880 | 0.1007 | 0.5401 | 0.5401 |
| `base|emb=12|sh=0.94` | 18 | 0.4956 | 1.0354 | 1.0000 | 0.9292 | -3.6880 | 0.1007 | 0.5377 | 0.5377 |
| `base|emb=24|sh=0.97` | 18 | 0.4762 | 1.0123 | 1.0000 | 1.0689 | -2.2030 | 0.3652 | 0.5368 | 0.5368 |
| `base|emb=24|sh=0.96` | 18 | 0.4762 | 1.0172 | 1.0000 | 1.0689 | -2.2030 | 0.3652 | 0.5350 | 0.5350 |
| `base|emb=24|sh=0.95` | 18 | 0.4762 | 1.0231 | 1.0000 | 1.0689 | -2.2030 | 0.3652 | 0.5330 | 0.5330 |
| `base|emb=24|sh=0.94` | 18 | 0.4762 | 1.0296 | 1.0000 | 1.0689 | -2.2030 | 0.3652 | 0.5308 | 0.5308 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4975 | 1.0103 | 0.3194 | 1.2527 | 0.8435 | 1.3989 | 0.5269 | 0.5269 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4975 | 1.0139 | 0.3194 | 1.2527 | 0.8435 | 1.3989 | 0.5256 | 0.5256 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4975 | 1.0204 | 0.3194 | 1.2527 | 0.8435 | 1.3989 | 0.5234 | 0.5234 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4975 | 1.0279 | 0.3194 | 1.2527 | 0.8435 | 1.3989 | 0.5208 | 0.5208 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4894 | 1.0137 | 0.3364 | 1.0453 | -1.0684 | 0.3570 | 0.4978 | 0.4978 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4894 | 1.0185 | 0.3364 | 1.0453 | -1.0684 | 0.3570 | 0.4960 | 0.4960 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4894 | 1.0260 | 0.3364 | 1.0453 | -1.0684 | 0.3570 | 0.4934 | 0.4934 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4894 | 1.0351 | 0.3364 | 1.0453 | -1.0684 | 0.3570 | 0.4903 | 0.4903 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=320, top_n=32, cutoff=0.8045

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5930 | 0.0578 | 0.9907 | 0.0064 |
| all validations | 0.4955 | 0.0791 | 1.0163 | 0.0414 |

- improvement vs all (primary fraction): `hit +9.76pp, mae +2.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.4848 | 0.9966 | 1.0000 | 0.8339 | -0.0972 | -9.0979 | -0.4852 | 0.3736 | 0.3736 |
| 2 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3750 | 1.0212 | 0.2222 | 0.5271 | -0.4868 | -45.5596 | -1.0713 | 0.3085 | 0.3085 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3750 | 1.0283 | 0.2222 | 0.5271 | -0.4868 | -45.5596 | -1.0713 | 0.3058 | 0.3058 |
| 4 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3750 | 1.0354 | 0.2222 | 0.5271 | -0.4868 | -45.5596 | -1.0713 | 0.3032 | 0.3032 |
| 5 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.3750 | 1.0424 | 0.2222 | 0.5271 | -0.4868 | -45.5596 | -1.0713 | 0.3005 | 0.3005 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.3750 | 0.9985 | 0.6459 | -40.1358 | -1.4451 |
| 1 | 7 | 0.1667 | 1.0310 | 0.5275 | -89.4762 | -0.8983 |
| 2 | 7 | 0.5714 | 0.9912 | 1.8741 | 38.3866 | 3.7537 |
| 3 | 7 | 0.5714 | 0.9727 | 1.4161 | 20.4465 | 2.4358 |
| 4 | 7 | 0.8000 | 0.9516 | 2.2585 | 61.3873 | 8.0627 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.3750 | 0.9985 | 0.6459 | -40.1358 | -1.4451 |
| top_20pct | 8 | 0.8333 | 0.9483 | 1.9368 | 60.8623 | 8.7236 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 1.0020 | 0.7871 | -9.0183 | -0.2955 |
| 1 | 7 | 0.5000 | 0.9966 | 1.5487 | 15.0596 | 0.7879 |
| 2 | 7 | 0.6667 | 0.9732 | 0.9936 | 25.0783 | 1.9625 |
| 3 | 7 | 0.3333 | 1.0185 | 0.6522 | -40.8178 | -0.8413 |
| 4 | 7 | 0.4286 | 0.9798 | 0.4810 | -39.3352 | -0.8715 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 1.0020 | 0.7871 | -9.0183 | -0.2955 |
| top_20pct | 8 | 0.5000 | 0.9725 | 0.5052 | -26.5841 | -0.6779 |

