# Strict Multi-Cycle Research Result

- symbol: `XRP`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5301 | 0.9891 | 0.3796 | 1.2865 | 7.5938 | 1.2774 | 0.6516 | 0.6516 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5301 | 0.9894 | 0.3796 | 1.2865 | 7.5938 | 1.2774 | 0.6513 | 0.6513 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5301 | 0.9908 | 0.3796 | 1.2865 | 7.5938 | 1.2774 | 0.6511 | 0.6511 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5301 | 0.9907 | 0.3796 | 1.2865 | 7.5938 | 1.2774 | 0.6507 | 0.6507 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5466 | 0.9920 | 0.3812 | 1.0891 | 8.0476 | 0.5943 | 0.6443 | 0.6443 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5466 | 0.9925 | 0.3812 | 1.0891 | 8.0476 | 0.5943 | 0.6442 | 0.6442 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5466 | 0.9920 | 0.3812 | 1.0891 | 8.0476 | 0.5943 | 0.6442 | 0.6442 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5466 | 0.9940 | 0.3812 | 1.0891 | 8.0476 | 0.5943 | 0.6438 | 0.6438 |
| `base|emb=24|sh=0.97` | 18 | 0.4913 | 0.9981 | 1.0000 | 1.1252 | 0.9818 | 0.3228 | 0.5726 | 0.5726 |
| `base|emb=24|sh=0.96` | 18 | 0.4913 | 0.9985 | 1.0000 | 1.1252 | 0.9818 | 0.3228 | 0.5725 | 0.5725 |
| `base|emb=24|sh=0.95` | 18 | 0.4913 | 0.9991 | 1.0000 | 1.1252 | 0.9818 | 0.3228 | 0.5723 | 0.5723 |
| `base|emb=24|sh=0.94` | 18 | 0.4913 | 1.0004 | 1.0000 | 1.1252 | 0.9818 | 0.3228 | 0.5718 | 0.5718 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4553 | 1.0073 | 0.3904 | 1.0619 | -9.5250 | 0.3013 | 0.5594 | 0.5594 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4553 | 1.0098 | 0.3904 | 1.0619 | -9.5250 | 0.3013 | 0.5586 | 0.5586 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4553 | 1.0122 | 0.3904 | 1.0619 | -9.5250 | 0.3013 | 0.5578 | 0.5578 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4553 | 1.0147 | 0.3904 | 1.0619 | -9.5250 | 0.3013 | 0.5570 | 0.5570 |
| `base|emb=12|sh=0.97` | 18 | 0.4920 | 1.0003 | 1.0000 | 1.0710 | -0.1132 | 0.2606 | 0.5486 | 0.5486 |
| `base|emb=12|sh=0.96` | 18 | 0.4920 | 1.0015 | 1.0000 | 1.0710 | -0.1132 | 0.2606 | 0.5481 | 0.5481 |
| `base|emb=12|sh=0.95` | 18 | 0.4920 | 1.0032 | 1.0000 | 1.0710 | -0.1132 | 0.2606 | 0.5476 | 0.5476 |
| `base|emb=12|sh=0.94` | 18 | 0.4920 | 1.0053 | 1.0000 | 1.0710 | -0.1132 | 0.2606 | 0.5468 | 0.5468 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=344, top_n=35, cutoff=0.7860

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6036 | 0.1011 | 0.9665 | 0.0269 |
| all validations | 0.4968 | 0.0936 | 1.0009 | 0.0271 |

- improvement vs all (primary fraction): `hit +10.68pp, mae +3.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.6857 | 0.9847 | 1.0000 | 0.6491 | 0.1307 | 12.2320 | 0.9134 | 0.7548 | 0.7548 |
| 2 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6562 | 0.9702 | 0.8889 | 0.6842 | 0.1008 | 9.4384 | 0.6662 | 0.7485 | 0.7485 |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6562 | 0.9745 | 0.8889 | 0.6842 | 0.1008 | 9.4384 | 0.6662 | 0.7466 | 0.7466 |
| 4 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6562 | 0.9793 | 0.8889 | 0.6842 | 0.1008 | 9.4384 | 0.6662 | 0.7446 | 0.7446 |
| 5 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6562 | 0.9844 | 0.8889 | 0.6842 | 0.1008 | 9.4384 | 0.6662 | 0.7425 | 0.7425 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1.0000 | 0.9860 | n/a | 169.2664 | n/a |
| 1 | 7 | 0.4286 | 1.0086 | 0.7981 | -20.4357 | -0.6351 |
| 2 | 7 | 0.7143 | 0.9532 | 0.4463 | 3.2770 | 0.1175 |
| 3 | 7 | 0.7143 | 0.9640 | 0.5300 | 9.8680 | 0.3876 |
| 4 | 7 | 0.5714 | 0.9862 | 2.8352 | 43.9974 | 7.2378 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 1.0000 | 0.9860 | n/a | 169.2664 | n/a |
| top_20pct | 8 | 0.6250 | 0.9812 | 2.3355 | 42.9052 | 7.5339 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1.0000 | 0.9860 | n/a | 169.2664 | n/a |
| 1 | 7 | 0.8571 | 0.9585 | 7.4700 | 81.5629 | 44.1621 |
| 2 | 7 | 0.5714 | 0.9491 | 1.8971 | 29.5308 | 2.0727 |
| 3 | 7 | 0.5714 | 0.9924 | 0.3861 | -23.8631 | -0.6594 |
| 4 | 7 | 0.4286 | 1.0086 | 0.7981 | -20.4357 | -0.6351 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 1.0000 | 0.9860 | n/a | 169.2664 | n/a |
| top_20pct | 8 | 0.5000 | 0.9964 | 0.6588 | -16.1817 | -0.5415 |

