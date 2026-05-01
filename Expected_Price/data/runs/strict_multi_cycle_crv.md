# Strict Multi-Cycle Research Result

- symbol: `CRV`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4940 | 1.0044 | 0.4213 | 1.1891 | 2.7890 | 0.7198 | 0.6208 | 0.6208 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4940 | 1.0069 | 0.4213 | 1.1891 | 2.7890 | 0.7198 | 0.6200 | 0.6200 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4940 | 1.0098 | 0.4213 | 1.1891 | 2.7890 | 0.7198 | 0.6191 | 0.6191 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4940 | 1.0130 | 0.4213 | 1.1891 | 2.7890 | 0.7198 | 0.6181 | 0.6181 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5170 | 1.0059 | 0.4198 | 1.2761 | 6.4056 | 1.0079 | 0.5924 | 0.5924 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5170 | 1.0097 | 0.4198 | 1.2761 | 6.4056 | 1.0079 | 0.5912 | 0.5912 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5170 | 1.0145 | 0.4198 | 1.2761 | 6.4056 | 1.0079 | 0.5897 | 0.5897 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5170 | 1.0193 | 0.4198 | 1.2761 | 6.4056 | 1.0079 | 0.5882 | 0.5882 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4810 | 1.0054 | 0.2901 | 1.0700 | -1.6106 | -0.0241 | 0.5395 | 0.5395 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4810 | 1.0073 | 0.2901 | 1.0700 | -1.6106 | -0.0241 | 0.5389 | 0.5389 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4810 | 1.0095 | 0.2901 | 1.0700 | -1.6106 | -0.0241 | 0.5383 | 0.5383 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4810 | 1.0122 | 0.2901 | 1.0700 | -1.6106 | -0.0241 | 0.5375 | 0.5375 |
| `base|emb=12|sh=0.97` | 18 | 0.4851 | 1.0022 | 1.0000 | 1.0435 | -1.8779 | 0.1059 | 0.5191 | 0.5191 |
| `base|emb=12|sh=0.96` | 18 | 0.4851 | 1.0038 | 1.0000 | 1.0435 | -1.8779 | 0.1059 | 0.5185 | 0.5185 |
| `base|emb=12|sh=0.95` | 18 | 0.4851 | 1.0061 | 1.0000 | 1.0435 | -1.8779 | 0.1059 | 0.5177 | 0.5177 |
| `base|emb=12|sh=0.94` | 18 | 0.4851 | 1.0087 | 1.0000 | 1.0435 | -1.8779 | 0.1059 | 0.5167 | 0.5167 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4723 | 1.0021 | 0.3086 | 1.0757 | -6.5724 | 0.2056 | 0.5054 | 0.5054 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4723 | 1.0055 | 0.3086 | 1.0757 | -6.5724 | 0.2056 | 0.5044 | 0.5044 |
| `base|emb=24|sh=0.97` | 18 | 0.4943 | 1.0012 | 1.0000 | 1.0234 | -1.6500 | 0.2318 | 0.5031 | 0.5031 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4723 | 1.0106 | 0.3086 | 1.0757 | -6.5724 | 0.2056 | 0.5029 | 0.5029 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=332, top_n=34, cutoff=0.7867

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6314 | 0.0395 | 0.9904 | 0.0133 |
| all validations | 0.4912 | 0.1068 | 1.0075 | 0.0370 |

- improvement vs all (primary fraction): `hit +14.02pp, mae +1.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.5294 | 0.9963 | 1.0000 | 0.8440 | -0.0210 | -1.9682 | -0.2653 | 0.4533 | 0.4533 |
| 2 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5455 | 0.9879 | 0.3056 | 0.4197 | -0.2421 | -22.6570 | -0.5311 | 0.3673 | 0.3673 |
| 3 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5455 | 0.9889 | 0.3056 | 0.4197 | -0.2421 | -22.6570 | -0.5311 | 0.3669 | 0.3669 |
| 4 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5455 | 0.9909 | 0.3056 | 0.4197 | -0.2421 | -22.6570 | -0.5311 | 0.3661 | 0.3661 |
| 5 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5455 | 0.9937 | 0.3056 | 0.4197 | -0.2421 | -22.6570 | -0.5311 | 0.3650 | 0.3650 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.3750 | 1.0292 | 0.4185 | -45.2472 | -0.7636 |
| 1 | 7 | 0.7143 | 0.9661 | 0.4378 | 2.6755 | 0.0897 |
| 2 | 7 | 0.7143 | 0.9561 | 0.6895 | 20.6920 | 1.0012 |
| 3 | 7 | 0.5000 | 1.0073 | 1.0365 | 1.4513 | 0.0419 |
| 4 | 7 | 0.3333 | 1.0197 | 2.4337 | 7.2881 | 0.2320 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.3750 | 1.0292 | 0.4185 | -45.2472 | -0.7636 |
| top_20pct | 8 | 0.2857 | 1.0249 | 2.4363 | -0.9725 | -0.0386 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.4286 | 1.0075 | 1.3176 | -0.4677 | -0.0279 |
| 1 | 7 | 0.5714 | 0.9882 | 0.9039 | 7.3149 | 0.3269 |
| 2 | 7 | 0.3333 | 1.0824 | 0.5271 | -46.1870 | -0.7636 |
| 3 | 7 | 0.5714 | 0.9707 | 0.2698 | -30.8550 | -0.8998 |
| 4 | 7 | 0.7143 | 0.9823 | 0.9175 | 31.9000 | 1.2957 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.4286 | 1.0075 | 1.3176 | -0.4677 | -0.0279 |
| top_20pct | 8 | 0.6250 | 0.9891 | 0.7396 | 8.1266 | 0.4164 |

