# Strict Multi-Cycle Research Result

- symbol: `ZEC`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5698 | 0.9762 | 0.2608 | 1.3521 | 20.2211 | 2.4516 | 0.7189 | 0.7189 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5698 | 0.9792 | 0.2608 | 1.3521 | 20.2211 | 2.4516 | 0.7174 | 0.7174 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5698 | 0.9823 | 0.2608 | 1.3521 | 20.2211 | 2.4516 | 0.7160 | 0.7160 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5698 | 0.9855 | 0.2608 | 1.3521 | 20.2211 | 2.4516 | 0.7145 | 0.7145 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5256 | 0.9917 | 0.2932 | 1.4301 | 13.4768 | 2.2118 | 0.6767 | 0.6767 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5256 | 0.9925 | 0.2932 | 1.4301 | 13.4768 | 2.2118 | 0.6766 | 0.6766 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5256 | 0.9938 | 0.2932 | 1.4301 | 13.4768 | 2.2118 | 0.6764 | 0.6764 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5256 | 0.9952 | 0.2932 | 1.4301 | 13.4768 | 2.2118 | 0.6762 | 0.6762 |
| `base|emb=24|sh=0.97` | 18 | 0.5494 | 0.9987 | 1.0000 | 1.0505 | 7.8981 | 1.8126 | 0.6304 | 0.6304 |
| `base|emb=24|sh=0.96` | 18 | 0.5494 | 1.0000 | 1.0000 | 1.0505 | 7.8981 | 1.8126 | 0.6300 | 0.6300 |
| `base|emb=24|sh=0.95` | 18 | 0.5494 | 1.0015 | 1.0000 | 1.0505 | 7.8981 | 1.8126 | 0.6295 | 0.6295 |
| `base|emb=24|sh=0.94` | 18 | 0.5494 | 1.0030 | 1.0000 | 1.0505 | 7.8981 | 1.8126 | 0.6291 | 0.6291 |
| `base|emb=12|sh=0.97` | 18 | 0.5432 | 1.0006 | 1.0000 | 1.0516 | 7.0785 | 1.9620 | 0.6248 | 0.6248 |
| `base|emb=12|sh=0.96` | 18 | 0.5432 | 1.0025 | 1.0000 | 1.0516 | 7.0785 | 1.9620 | 0.6242 | 0.6242 |
| `base|emb=12|sh=0.95` | 18 | 0.5432 | 1.0045 | 1.0000 | 1.0516 | 7.0785 | 1.9620 | 0.6235 | 0.6235 |
| `base|emb=12|sh=0.94` | 18 | 0.5432 | 1.0066 | 1.0000 | 1.0516 | 7.0785 | 1.9620 | 0.6229 | 0.6229 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5582 | 0.9959 | 0.3812 | 0.8986 | 2.5749 | 1.9954 | 0.5753 | 0.5753 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5582 | 0.9962 | 0.3812 | 0.8986 | 2.5749 | 1.9954 | 0.5751 | 0.5751 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5582 | 0.9965 | 0.3812 | 0.8986 | 2.5749 | 1.9954 | 0.5749 | 0.5749 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5582 | 0.9970 | 0.3812 | 0.8986 | 2.5749 | 1.9954 | 0.5747 | 0.5747 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.8646

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7029 | 0.0503 | 0.9760 | 0.0182 |
| all validations | 0.5477 | 0.1086 | 0.9972 | 0.0303 |

- improvement vs all (primary fraction): `hit +15.52pp, mae +2.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5333 | 0.9854 | 0.8611 | 0.9651 | 0.0374 | 3.4988 | 0.1336 | 0.6872 | 0.6872 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5333 | 0.9871 | 0.8611 | 0.9651 | 0.0374 | 3.4988 | 0.1336 | 0.6865 | 0.6865 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5333 | 0.9889 | 0.8611 | 0.9651 | 0.0374 | 3.4988 | 0.1336 | 0.6857 | 0.6857 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5333 | 0.9906 | 0.8611 | 0.9651 | 0.0374 | 3.4988 | 0.1336 | 0.6850 | 0.6850 |
| 5 | `base|emb=24|sh=0.97` | 0.5143 | 0.9873 | 1.0000 | 1.0106 | 0.0262 | 2.4510 | 0.0972 | 0.6610 | 0.6610 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.2857 | 1.1312 | 1.1793 | -27.9819 | -0.5451 |
| 1 | 6 | 0.5000 | 1.0269 | 1.2054 | 6.6745 | 0.1990 |
| 2 | 6 | 0.5000 | 1.0305 | 0.2809 | -32.1993 | -0.8535 |
| 3 | 6 | 0.6667 | 0.8854 | 0.6310 | 8.7360 | 0.4370 |
| 4 | 6 | 0.8000 | 0.9009 | 1.3799 | 65.0334 | 4.5471 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.2857 | 1.1312 | 1.1793 | -27.9819 | -0.5451 |
| top_20pct | 7 | 0.8333 | 0.8695 | 1.1764 | 64.2999 | 4.9190 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 1.0000 | 0.8885 | n/a | 127.1043 | n/a |
| 1 | 6 | 0.3333 | 0.9881 | 1.1978 | -17.5813 | -0.6518 |
| 2 | 6 | 0.3333 | 1.0679 | 1.8788 | -1.9772 | -0.0697 |
| 3 | 6 | 0.1667 | 1.0821 | 0.3070 | -81.0379 | -0.9405 |
| 4 | 6 | 0.8000 | 0.8719 | 0.8564 | 46.7361 | 2.4282 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 1.0000 | 0.8885 | n/a | 127.1043 | n/a |
| top_20pct | 7 | 0.6667 | 0.9662 | 0.3851 | -8.7312 | -1.0674 |

