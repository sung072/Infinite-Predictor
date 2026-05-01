# Strict Multi-Cycle Research Result

- symbol: `ACH`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6303 | 0.9682 | 0.3488 | 1.0352 | 19.5749 | 2.0235 | 0.6847 | 0.6847 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6303 | 0.9728 | 0.3488 | 1.0352 | 19.5749 | 2.0235 | 0.6826 | 0.6826 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6303 | 0.9778 | 0.3488 | 1.0352 | 19.5749 | 2.0235 | 0.6803 | 0.6803 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6303 | 0.9834 | 0.3488 | 1.0352 | 19.5749 | 2.0235 | 0.6779 | 0.6779 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5838 | 0.9777 | 0.3349 | 0.9160 | 8.0472 | 0.9732 | 0.6403 | 0.6403 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5838 | 0.9811 | 0.3349 | 0.9160 | 8.0472 | 0.9732 | 0.6387 | 0.6387 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5838 | 0.9846 | 0.3349 | 0.9160 | 8.0472 | 0.9732 | 0.6370 | 0.6370 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5838 | 0.9885 | 0.3349 | 0.9160 | 8.0472 | 0.9732 | 0.6353 | 0.6353 |
| `base|emb=12|sh=0.96` | 18 | 0.5424 | 1.0001 | 1.0000 | 1.0469 | 5.8693 | 1.3018 | 0.6019 | 0.6019 |
| `base|emb=12|sh=0.97` | 18 | 0.5424 | 1.0001 | 1.0000 | 1.0469 | 5.8693 | 1.3018 | 0.6018 | 0.6018 |
| `base|emb=12|sh=0.95` | 18 | 0.5424 | 1.0003 | 1.0000 | 1.0469 | 5.8693 | 1.3018 | 0.6018 | 0.6018 |
| `base|emb=12|sh=0.94` | 18 | 0.5424 | 1.0006 | 1.0000 | 1.0469 | 5.8693 | 1.3018 | 0.6017 | 0.6017 |
| `base|emb=24|sh=0.97` | 18 | 0.5322 | 1.0010 | 1.0000 | 1.0292 | 4.0259 | 1.1157 | 0.5933 | 0.5933 |
| `base|emb=24|sh=0.96` | 18 | 0.5322 | 1.0013 | 1.0000 | 1.0292 | 4.0259 | 1.1157 | 0.5932 | 0.5932 |
| `base|emb=24|sh=0.95` | 18 | 0.5322 | 1.0017 | 1.0000 | 1.0292 | 4.0259 | 1.1157 | 0.5931 | 0.5931 |
| `base|emb=24|sh=0.94` | 18 | 0.5322 | 1.0022 | 1.0000 | 1.0292 | 4.0259 | 1.1157 | 0.5929 | 0.5929 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4476 | 1.0109 | 0.3627 | 1.2121 | -5.8847 | 1.0435 | 0.5277 | 0.5277 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4476 | 1.0146 | 0.3627 | 1.2121 | -5.8847 | 1.0435 | 0.5264 | 0.5264 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4476 | 1.0182 | 0.3627 | 1.2121 | -5.8847 | 1.0435 | 0.5251 | 0.5251 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4476 | 1.0218 | 0.3627 | 1.2121 | -5.8847 | 1.0435 | 0.5238 | 0.5238 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=388, top_n=39, cutoff=0.8514

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6887 | 0.0737 | 0.9761 | 0.0117 |
| all validations | 0.5243 | 0.1437 | 1.0001 | 0.0290 |

- improvement vs all (primary fraction): `hit +16.44pp, mae +2.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.96` | 0.4857 | 0.9862 | 1.0000 | 0.9012 | -0.0584 | -5.4662 | -0.4539 | 0.3891 | 0.3891 |
| 2 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 0.9925 | 0.6389 | 0.9767 | -0.0825 | -7.7203 | -0.3894 | 0.3800 | 0.3800 |
| 3 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 0.9931 | 0.6389 | 0.9767 | -0.0825 | -7.7203 | -0.3894 | 0.3797 | 0.3797 |
| 4 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 0.9935 | 0.6389 | 0.9767 | -0.0825 | -7.7203 | -0.3894 | 0.3795 | 0.3795 |
| 5 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4545 | 0.9945 | 0.6389 | 0.9767 | -0.0825 | -7.7203 | -0.3894 | 0.3791 | 0.3791 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.3750 | 1.0078 | 0.3374 | -46.2815 | -1.0203 |
| 1 | 7 | 0.5000 | 0.9943 | 1.1042 | 3.8073 | 0.1639 |
| 2 | 7 | 0.4286 | 0.9772 | 0.9069 | -13.1846 | -0.6596 |
| 3 | 7 | 0.5714 | 0.9703 | 2.5270 | 36.6203 | 5.3921 |
| 4 | 7 | 0.5714 | 0.9556 | 1.0042 | 10.1584 | 0.5000 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.3750 | 1.0078 | 0.3374 | -46.2815 | -1.0203 |
| top_20pct | 8 | 0.6250 | 0.9174 | 1.0727 | 21.1108 | 1.1792 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 0.9780 | 0.9949 | -0.1529 | -0.0460 |
| 1 | 7 | 0.5714 | 0.9740 | 0.4672 | -17.7224 | -0.7350 |
| 2 | 7 | 0.2857 | 1.0313 | 0.4538 | -65.6898 | -1.2654 |
| 3 | 7 | 0.4286 | 0.9902 | 0.3403 | -46.4150 | -1.7830 |
| 4 | 7 | 0.6667 | 0.9707 | 1.3290 | 40.8756 | 2.2288 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 0.9780 | 0.9949 | -0.1529 | -0.0460 |
| top_20pct | 8 | 0.5714 | 0.9808 | 1.3098 | 23.3084 | 1.4928 |

