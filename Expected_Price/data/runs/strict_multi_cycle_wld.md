# Strict Multi-Cycle Research Result

- symbol: `WLD`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5538 | 0.9987 | 0.2377 | 1.2413 | 8.0531 | 1.2836 | 0.6041 | 0.6041 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5538 | 1.0001 | 0.2377 | 1.2413 | 8.0531 | 1.2836 | 0.6039 | 0.6039 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5310 | 0.9998 | 0.2052 | 1.3012 | 9.0802 | 1.3438 | 0.6033 | 0.6033 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5310 | 0.9993 | 0.2052 | 1.3012 | 9.0802 | 1.3438 | 0.6033 | 0.6033 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5538 | 1.0031 | 0.2377 | 1.2413 | 8.0531 | 1.2836 | 0.6030 | 0.6030 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5310 | 1.0014 | 0.2052 | 1.3012 | 9.0802 | 1.3438 | 0.6029 | 0.6029 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5310 | 1.0050 | 0.2052 | 1.3012 | 9.0802 | 1.3438 | 0.6017 | 0.6017 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5538 | 1.0076 | 0.2377 | 1.2413 | 8.0531 | 1.2836 | 0.6016 | 0.6016 |
| `base|emb=12|sh=0.97` | 18 | 0.5033 | 0.9992 | 1.0000 | 1.0130 | 0.1808 | 0.2038 | 0.5483 | 0.5483 |
| `base|emb=12|sh=0.96` | 18 | 0.5033 | 0.9999 | 1.0000 | 1.0130 | 0.1808 | 0.2038 | 0.5482 | 0.5482 |
| `base|emb=12|sh=0.95` | 18 | 0.5033 | 1.0012 | 1.0000 | 1.0130 | 0.1808 | 0.2038 | 0.5478 | 0.5478 |
| `base|emb=12|sh=0.94` | 18 | 0.5033 | 1.0040 | 1.0000 | 1.0130 | 0.1808 | 0.2038 | 0.5469 | 0.5469 |
| `base|emb=24|sh=0.97` | 18 | 0.4781 | 1.0033 | 1.0000 | 0.9720 | -5.5581 | -0.1312 | 0.4866 | 0.4866 |
| `base|emb=24|sh=0.96` | 18 | 0.4781 | 1.0052 | 1.0000 | 0.9720 | -5.5581 | -0.1312 | 0.4859 | 0.4859 |
| `base|emb=24|sh=0.95` | 18 | 0.4781 | 1.0078 | 1.0000 | 0.9720 | -5.5581 | -0.1312 | 0.4850 | 0.4850 |
| `base|emb=24|sh=0.94` | 18 | 0.4781 | 1.0117 | 1.0000 | 0.9720 | -5.5581 | -0.1312 | 0.4837 | 0.4837 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4881 | 0.9981 | 0.4105 | 0.8139 | -11.3056 | 0.3074 | 0.4669 | 0.4669 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4881 | 0.9984 | 0.4105 | 0.8139 | -11.3056 | 0.3074 | 0.4668 | 0.4668 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4881 | 0.9989 | 0.4105 | 0.8139 | -11.3056 | 0.3074 | 0.4667 | 0.4667 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4881 | 0.9996 | 0.4105 | 0.8139 | -11.3056 | 0.3074 | 0.4665 | 0.4665 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8061

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7126 | 0.1091 | 0.9703 | 0.0184 |
| all validations | 0.5021 | 0.1198 | 1.0015 | 0.0319 |

- improvement vs all (primary fraction): `hit +21.05pp, mae +3.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5455 | 0.9962 | 0.9722 | 1.1505 | 0.1219 | 11.4051 | 1.0712 | 0.7496 | 0.7496 |
| 2 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5455 | 0.9971 | 0.9722 | 1.1505 | 0.1219 | 11.4051 | 1.0712 | 0.7492 | 0.7492 |
| 3 | `base|emb=12|sh=0.97` | 0.5882 | 1.0001 | 1.0000 | 0.9667 | 0.1299 | 12.1543 | 0.8286 | 0.7412 | 0.7412 |
| 4 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5217 | 1.0031 | 0.6944 | 1.1559 | 0.0916 | 8.5773 | 0.6288 | 0.7279 | 0.7279 |
| 5 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5217 | 1.0041 | 0.6944 | 1.1559 | 0.0916 | 8.5773 | 0.6288 | 0.7275 | 0.7275 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.3333 | 1.0089 | 2.2725 | 3.9872 | 0.1325 |
| 1 | 7 | 0.7143 | 0.9821 | 0.3184 | -7.1581 | -0.9864 |
| 2 | 7 | 0.7143 | 0.9797 | 1.2135 | 39.1314 | 2.0414 |
| 3 | 7 | 0.5000 | 1.0335 | 1.6419 | 16.6441 | 1.2334 |
| 4 | 7 | 0.4286 | 0.9936 | 1.4711 | 3.9692 | 0.0978 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.3333 | 1.0089 | 2.2725 | 3.9872 | 0.1325 |
| top_20pct | 7 | 0.4286 | 0.9936 | 1.4711 | 3.9692 | 0.0978 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.8333 | 0.9521 | 1.3696 | 64.5446 | n/a |
| 1 | 7 | 0.2857 | 1.0526 | 0.5929 | -47.9899 | -2.2287 |
| 2 | 7 | 0.2857 | 1.0596 | 0.6257 | -56.3043 | -0.8201 |
| 3 | 7 | 0.7143 | 0.9507 | 0.9269 | 31.8342 | 1.3757 |
| 4 | 7 | 0.6667 | 1.0017 | 0.8429 | 20.7405 | 0.6774 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.8333 | 0.9521 | 1.3696 | 64.5446 | n/a |
| top_20pct | 7 | 0.6667 | 1.0017 | 0.8429 | 20.7405 | 0.6774 |

