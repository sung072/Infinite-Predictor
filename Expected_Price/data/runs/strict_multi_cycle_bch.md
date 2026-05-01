# Strict Multi-Cycle Research Result

- symbol: `BCH`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6069 | 0.9738 | 0.2593 | 0.8524 | 8.1560 | 0.4587 | 0.6993 | 0.6993 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6069 | 0.9730 | 0.2593 | 0.8524 | 8.1560 | 0.4587 | 0.6992 | 0.6992 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6069 | 0.9741 | 0.2593 | 0.8524 | 8.1560 | 0.4587 | 0.6984 | 0.6984 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6069 | 0.9790 | 0.2593 | 0.8524 | 8.1560 | 0.4587 | 0.6958 | 0.6958 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5619 | 0.9988 | 0.2654 | 1.1875 | 5.8100 | 1.1542 | 0.5823 | 0.5823 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5619 | 1.0028 | 0.2654 | 1.1875 | 5.8100 | 1.1542 | 0.5809 | 0.5809 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5619 | 1.0099 | 0.2654 | 1.1875 | 5.8100 | 1.1542 | 0.5784 | 0.5784 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5619 | 1.0189 | 0.2654 | 1.1875 | 5.8100 | 1.1542 | 0.5753 | 0.5753 |
| `base|emb=24|sh=0.97` | 18 | 0.5015 | 1.0009 | 1.0000 | 0.8654 | -5.1696 | -0.1768 | 0.4738 | 0.4738 |
| `base|emb=12|sh=0.97` | 18 | 0.5057 | 0.9999 | 1.0000 | 0.8410 | -5.6179 | -0.1126 | 0.4737 | 0.4737 |
| `base|emb=24|sh=0.96` | 18 | 0.5015 | 1.0027 | 1.0000 | 0.8654 | -5.1696 | -0.1768 | 0.4731 | 0.4731 |
| `base|emb=12|sh=0.96` | 18 | 0.5057 | 1.0015 | 1.0000 | 0.8410 | -5.6179 | -0.1126 | 0.4731 | 0.4731 |
| `base|emb=12|sh=0.95` | 18 | 0.5057 | 1.0045 | 1.0000 | 0.8410 | -5.6179 | -0.1126 | 0.4720 | 0.4720 |
| `base|emb=24|sh=0.95` | 18 | 0.5015 | 1.0060 | 1.0000 | 0.8654 | -5.1696 | -0.1768 | 0.4719 | 0.4719 |
| `base|emb=12|sh=0.94` | 18 | 0.5057 | 1.0084 | 1.0000 | 0.8410 | -5.6179 | -0.1126 | 0.4705 | 0.4705 |
| `base|emb=24|sh=0.94` | 18 | 0.5015 | 1.0105 | 1.0000 | 0.8654 | -5.1696 | -0.1768 | 0.4702 | 0.4702 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4006 | 1.0107 | 0.3642 | 0.7052 | -29.2126 | -0.6883 | 0.3589 | 0.3589 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4006 | 1.0163 | 0.3642 | 0.7052 | -29.2126 | -0.6883 | 0.3567 | 0.3567 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4006 | 1.0232 | 0.3642 | 0.7052 | -29.2126 | -0.6883 | 0.3542 | 0.3542 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4006 | 1.0300 | 0.3642 | 0.7052 | -29.2126 | -0.6883 | 0.3518 | 0.3518 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.7645

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6481 | 0.0830 | 0.9737 | 0.0615 |
| all validations | 0.4952 | 0.1172 | 1.0057 | 0.0326 |

- improvement vs all (primary fraction): `hit +15.29pp, mae +3.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9523 | 0.8333 | 0.5501 | 0.0382 | 3.5762 | 0.2755 | 0.7144 | 0.7144 |
| 2 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9532 | 0.8333 | 0.5501 | 0.0382 | 3.5762 | 0.2755 | 0.7140 | 0.7140 |
| 3 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9588 | 0.8333 | 0.5501 | 0.0382 | 3.5762 | 0.2755 | 0.7115 | 0.7115 |
| 4 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9668 | 0.8333 | 0.5501 | 0.0382 | 3.5762 | 0.2755 | 0.7081 | 0.7081 |
| 5 | `base|emb=24|sh=0.97` | 0.5714 | 0.9800 | 1.0000 | 0.6471 | -0.0557 | -5.2095 | -0.3901 | 0.4004 | 0.4004 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.6667 | 0.9395 | 0.9336 | 24.1619 | 0.8662 |
| 1 | 6 | 0.5000 | 1.0093 | 0.7905 | -8.9890 | -0.2780 |
| 2 | 6 | 0.8333 | 0.8580 | 1.3731 | 64.6372 | 5.8803 |
| 3 | 6 | 0.5000 | 0.9805 | 0.2688 | -46.7979 | -0.8477 |
| 4 | 6 | 0.8333 | 0.9308 | 0.4819 | 29.2754 | 1.4071 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 6 | 0.6667 | 0.9395 | 0.9336 | 24.1619 | 0.8662 |
| top_20pct | 6 | 0.8333 | 0.9308 | 0.4819 | 29.2754 | 1.4071 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.5000 | 0.9760 | 1.1464 | 5.1631 | 0.1786 |
| 1 | 6 | 0.5000 | 0.9941 | 0.6001 | -18.0067 | -0.4586 |
| 2 | 6 | 0.6667 | 0.9358 | 0.6053 | 7.3079 | 0.2732 |
| 3 | 6 | 0.8333 | 0.8630 | 0.1145 | -14.2030 | -0.4301 |
| 4 | 6 | 0.8333 | 0.9468 | 0.6238 | 42.7509 | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 6 | 0.5000 | 0.9760 | 1.1464 | 5.1631 | 0.1786 |
| top_20pct | 6 | 0.8333 | 0.9468 | 0.6238 | 42.7509 | n/a |

