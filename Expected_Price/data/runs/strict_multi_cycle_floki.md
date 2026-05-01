# Strict Multi-Cycle Research Result

- symbol: `FLOKI`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5437 | 1.0064 | 0.2423 | 1.7923 | 18.8855 | 5.2392 | 0.6752 | 0.6752 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5437 | 1.0088 | 0.2423 | 1.7923 | 18.8855 | 5.2392 | 0.6745 | 0.6745 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5437 | 1.0116 | 0.2423 | 1.7923 | 18.8855 | 5.2392 | 0.6737 | 0.6737 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5319 | 1.0166 | 0.2423 | 1.6939 | 14.4636 | 2.1457 | 0.6650 | 0.6650 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5524 | 1.0080 | 0.2454 | 1.4633 | 17.5769 | 4.2601 | 0.6615 | 0.6615 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5524 | 1.0106 | 0.2454 | 1.4633 | 17.5769 | 4.2601 | 0.6611 | 0.6611 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5524 | 1.0133 | 0.2454 | 1.4633 | 17.5769 | 4.2601 | 0.6608 | 0.6608 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5409 | 1.0198 | 0.2454 | 1.4508 | 14.1162 | 2.2483 | 0.6543 | 0.6543 |
| `base|emb=12|sh=0.94` | 18 | 0.5196 | 1.0044 | 1.0000 | 1.1029 | 4.9648 | 0.6962 | 0.6163 | 0.6163 |
| `base|emb=12|sh=0.97` | 18 | 0.5226 | 1.0013 | 1.0000 | 1.0679 | 4.2855 | 0.5925 | 0.6126 | 0.6126 |
| `base|emb=12|sh=0.96` | 18 | 0.5208 | 1.0020 | 1.0000 | 1.0738 | 4.2018 | 0.5877 | 0.6121 | 0.6121 |
| `base|emb=12|sh=0.95` | 18 | 0.5175 | 1.0029 | 1.0000 | 1.0884 | 4.1591 | 0.5919 | 0.6106 | 0.6106 |
| `base|emb=24|sh=0.97` | 18 | 0.5060 | 1.0024 | 1.0000 | 1.0676 | 1.5166 | 0.4377 | 0.5693 | 0.5693 |
| `base|emb=24|sh=0.96` | 18 | 0.5037 | 1.0034 | 1.0000 | 1.0708 | 1.3553 | 0.4255 | 0.5616 | 0.5616 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4892 | 1.0061 | 0.4275 | 0.9843 | -4.8285 | 0.6490 | 0.5565 | 0.5565 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4868 | 1.0046 | 0.4275 | 0.9838 | -5.3667 | 0.5611 | 0.5559 | 0.5559 |
| `base|emb=24|sh=0.95` | 18 | 0.4992 | 1.0049 | 1.0000 | 1.0782 | 0.8910 | 0.3892 | 0.5519 | 0.5519 |
| `base|emb=24|sh=0.94` | 18 | 0.5000 | 1.0073 | 1.0000 | 1.0873 | 1.3820 | 0.4326 | 0.5489 | 0.5489 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4910 | 1.0025 | 0.4275 | 1.0449 | -4.5155 | 0.9540 | 0.5414 | 0.5414 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4910 | 1.0034 | 0.4275 | 1.0449 | -4.5155 | 0.9540 | 0.5411 | 0.5411 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.8368

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7117 | 0.1524 | 0.9631 | 0.0303 |
| all validations | 0.5126 | 0.1203 | 1.0062 | 0.0372 |

- improvement vs all (primary fraction): `hit +19.92pp, mae +4.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7308 | 0.9364 | 0.7500 | 0.7992 | 0.3113 | 29.1351 | 2.2969 | 0.8268 | 0.8268 |
| 2 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7600 | 0.9462 | 0.7500 | 0.6990 | 0.3240 | 30.3237 | 2.3383 | 0.8243 | 0.8243 |
| 3 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7600 | 0.9569 | 0.7500 | 0.6990 | 0.3240 | 30.3237 | 2.3383 | 0.8196 | 0.8196 |
| 4 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7917 | 0.9677 | 0.7500 | 0.6041 | 0.3425 | 32.0538 | 2.4109 | 0.8181 | 0.8181 |
| 5 | `base|emb=12|sh=0.94` | 0.6970 | 0.9531 | 1.0000 | 0.5062 | 0.0525 | 4.9109 | 0.3360 | 0.7344 | 0.7344 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.3333 | 0.9830 | 0.6104 | -42.2531 | -1.3015 |
| 1 | 5 | 0.6000 | 0.9596 | 2.6435 | 53.9304 | 3.5910 |
| 2 | 5 | 0.8000 | 0.8965 | 0.2196 | -4.1225 | -0.1297 |
| 3 | 5 | 1.0000 | 0.8812 | n/a | 121.3011 | n/a |
| 4 | 6 | 1.0000 | 0.9442 | n/a | 131.0184 | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.6667 | 0.8799 | 4.9321 | 87.7382 | 8.9619 |
| 1 | 5 | 1.0000 | 0.8609 | n/a | 89.1732 | n/a |
| 2 | 5 | 0.5000 | 1.0301 | 0.3638 | -34.8438 | -0.9185 |
| 3 | 5 | 0.8000 | 0.9444 | 0.4793 | 22.6297 | 0.9045 |
| 4 | 6 | 0.6667 | 0.9380 | 0.9475 | 25.1074 | 0.8887 |

