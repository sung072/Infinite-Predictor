# Strict Multi-Cycle Research Result

- symbol: `LINK`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5558 | 0.9933 | 0.2685 | 1.0437 | 7.7148 | 0.6324 | 0.6500 | 0.6500 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5558 | 0.9945 | 0.2685 | 1.0437 | 7.7148 | 0.6324 | 0.6494 | 0.6494 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5558 | 0.9961 | 0.2685 | 1.0437 | 7.7148 | 0.6324 | 0.6492 | 0.6492 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5558 | 0.9959 | 0.2685 | 1.0437 | 7.7148 | 0.6324 | 0.6487 | 0.6487 |
| `base|emb=12|sh=0.97` | 18 | 0.5273 | 1.0037 | 1.0000 | 0.9621 | 1.9655 | 0.3213 | 0.5979 | 0.5979 |
| `base|emb=12|sh=0.96` | 18 | 0.5273 | 1.0049 | 1.0000 | 0.9621 | 1.9655 | 0.3213 | 0.5975 | 0.5975 |
| `base|emb=12|sh=0.95` | 18 | 0.5273 | 1.0065 | 1.0000 | 0.9621 | 1.9655 | 0.3213 | 0.5969 | 0.5969 |
| `base|emb=12|sh=0.94` | 18 | 0.5273 | 1.0096 | 1.0000 | 0.9621 | 1.9655 | 0.3213 | 0.5958 | 0.5958 |
| `base|emb=24|sh=0.97` | 18 | 0.5352 | 1.0005 | 1.0000 | 0.9804 | 3.4293 | 0.3678 | 0.5832 | 0.5832 |
| `base|emb=24|sh=0.96` | 18 | 0.5352 | 1.0007 | 1.0000 | 0.9804 | 3.4293 | 0.3678 | 0.5832 | 0.5832 |
| `base|emb=24|sh=0.95` | 18 | 0.5352 | 1.0010 | 1.0000 | 0.9804 | 3.4293 | 0.3678 | 0.5831 | 0.5831 |
| `base|emb=24|sh=0.94` | 18 | 0.5352 | 1.0022 | 1.0000 | 0.9804 | 3.4293 | 0.3678 | 0.5826 | 0.5826 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5087 | 1.0047 | 0.3457 | 1.0652 | 1.5692 | 0.6226 | 0.5815 | 0.5815 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5087 | 1.0063 | 0.3457 | 1.0652 | 1.5692 | 0.6226 | 0.5809 | 0.5809 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5087 | 1.0078 | 0.3457 | 1.0652 | 1.5692 | 0.6226 | 0.5803 | 0.5803 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5087 | 1.0094 | 0.3457 | 1.0652 | 1.5692 | 0.6226 | 0.5798 | 0.5798 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5092 | 1.0194 | 0.3117 | 1.1311 | 2.8750 | 0.6880 | 0.5669 | 0.5669 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5092 | 1.0258 | 0.3117 | 1.1311 | 2.8750 | 0.6880 | 0.5647 | 0.5647 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5092 | 1.0327 | 0.3117 | 1.1311 | 2.8750 | 0.6880 | 0.5624 | 0.5624 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5092 | 1.0470 | 0.3117 | 1.1311 | 2.8750 | 0.6880 | 0.5576 | 0.5576 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=324, top_n=33, cutoff=0.7874

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6164 | 0.0475 | 0.9850 | 0.0151 |
| all validations | 0.5238 | 0.0896 | 1.0073 | 0.0281 |

- improvement vs all (primary fraction): `hit +9.26pp, mae +2.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6000 | 0.9781 | 0.8056 | 1.1333 | 0.2014 | 18.8520 | 1.7049 | 0.7845 | 0.7845 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6000 | 0.9818 | 0.8056 | 1.1333 | 0.2014 | 18.8520 | 1.7049 | 0.7829 | 0.7829 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6000 | 0.9854 | 0.8056 | 1.1333 | 0.2014 | 18.8520 | 1.7049 | 0.7814 | 0.7814 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6000 | 0.9891 | 0.8056 | 1.1333 | 0.2014 | 18.8520 | 1.7049 | 0.7799 | 0.7799 |
| 5 | `base|emb=12|sh=0.97` | 0.6429 | 0.9962 | 1.0000 | 0.7192 | 0.1035 | 9.6885 | 0.6053 | 0.7348 | 0.7348 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.5000 | 0.9731 | 3.9100 | 43.7517 | 2.9196 |
| 1 | 6 | 0.6000 | 1.0506 | 0.4781 | -10.5092 | -0.2907 |
| 2 | 5 | 0.7500 | 0.8566 | 3.3772 | 84.3430 | 9.1552 |
| 3 | 6 | 0.5000 | 0.9703 | 0.5415 | -22.3845 | -0.5010 |
| 4 | 6 | 0.7500 | 0.9682 | 3.6751 | 75.3242 | 10.0507 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.5000 | 0.9838 | 1.1974 | 7.2135 | 0.1953 |
| 1 | 6 | 0.7500 | 0.9212 | 2.0081 | 56.8166 | 5.0276 |
| 2 | 5 | 0.5000 | 1.0026 | 1.2880 | 9.0749 | 0.3288 |
| 3 | 6 | 0.5000 | 0.9461 | 1.1213 | 4.2728 | 0.1504 |
| 4 | 6 | 0.8000 | 0.9923 | 0.5564 | 31.1193 | 1.2190 |

