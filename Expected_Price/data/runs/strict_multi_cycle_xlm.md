# Strict Multi-Cycle Research Result

- symbol: `XLM`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6442 | 0.9856 | 0.3688 | 1.2002 | 26.1376 | 2.6230 | 0.7921 | 0.7921 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6442 | 0.9857 | 0.3688 | 1.2002 | 26.1376 | 2.6230 | 0.7920 | 0.7920 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6442 | 0.9869 | 0.3688 | 1.2002 | 26.1376 | 2.6230 | 0.7915 | 0.7915 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6442 | 0.9899 | 0.3688 | 1.2002 | 26.1376 | 2.6230 | 0.7903 | 0.7903 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6587 | 0.9868 | 0.3503 | 1.5029 | 25.0219 | 5.5617 | 0.7654 | 0.7654 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6587 | 0.9882 | 0.3503 | 1.5029 | 25.0219 | 5.5617 | 0.7648 | 0.7648 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6587 | 0.9901 | 0.3503 | 1.5029 | 25.0219 | 5.5617 | 0.7640 | 0.7640 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6587 | 0.9925 | 0.3503 | 1.5029 | 25.0219 | 5.5617 | 0.7629 | 0.7629 |
| `base|emb=12|sh=0.97` | 18 | 0.5250 | 1.0034 | 1.0000 | 1.2067 | 7.7809 | 1.1393 | 0.6627 | 0.6627 |
| `base|emb=12|sh=0.96` | 18 | 0.5250 | 1.0051 | 1.0000 | 1.2067 | 7.7809 | 1.1393 | 0.6621 | 0.6621 |
| `base|emb=12|sh=0.95` | 18 | 0.5250 | 1.0079 | 1.0000 | 1.2067 | 7.7809 | 1.1393 | 0.6611 | 0.6611 |
| `base|emb=12|sh=0.94` | 18 | 0.5250 | 1.0114 | 1.0000 | 1.2067 | 7.7809 | 1.1393 | 0.6599 | 0.6599 |
| `base|emb=24|sh=0.97` | 18 | 0.5318 | 1.0005 | 1.0000 | 1.1199 | 6.5676 | 0.9398 | 0.6356 | 0.6356 |
| `base|emb=24|sh=0.96` | 18 | 0.5318 | 1.0011 | 1.0000 | 1.1199 | 6.5676 | 0.9398 | 0.6354 | 0.6354 |
| `base|emb=24|sh=0.95` | 18 | 0.5318 | 1.0027 | 1.0000 | 1.1199 | 6.5676 | 0.9398 | 0.6349 | 0.6349 |
| `base|emb=24|sh=0.94` | 18 | 0.5318 | 1.0049 | 1.0000 | 1.1199 | 6.5676 | 0.9398 | 0.6341 | 0.6341 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5085 | 1.0014 | 0.3827 | 1.7105 | 15.5063 | 1.5433 | 0.6107 | 0.6107 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5085 | 1.0002 | 0.3827 | 1.7105 | 15.5063 | 1.5433 | 0.6105 | 0.6105 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5085 | 1.0057 | 0.3827 | 1.7105 | 15.5063 | 1.5433 | 0.6098 | 0.6098 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5085 | 1.0116 | 0.3827 | 1.7105 | 15.5063 | 1.5433 | 0.6085 | 0.6085 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.8464

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7173 | 0.1175 | 0.9738 | 0.0371 |
| all validations | 0.5547 | 0.1453 | 1.0003 | 0.0360 |

- improvement vs all (primary fraction): `hit +16.25pp, mae +2.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.4706 | 1.0053 | 1.0000 | 1.6362 | 0.1521 | 14.2390 | 1.1253 | 0.7524 | 0.7524 |
| 2 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5000 | 1.0294 | 0.1389 | 0.6056 | -0.1966 | -18.4029 | -1.4827 | 0.3227 | 0.3227 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5000 | 1.0392 | 0.1389 | 0.6056 | -0.1966 | -18.4029 | -1.4827 | 0.3190 | 0.3190 |
| 4 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5000 | 1.0490 | 0.1389 | 0.6056 | -0.1966 | -18.4029 | -1.4827 | 0.3154 | 0.3154 |
| 5 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5000 | 1.0588 | 0.1389 | 0.6056 | -0.1966 | -18.4029 | -1.4827 | 0.3119 | 0.3119 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 1.0092 | 1.9471 | 23.9732 | 0.9464 |
| 1 | 7 | 0.6667 | 1.0032 | 0.9279 | 24.5886 | 1.3175 |
| 2 | 7 | 0.4286 | 0.9998 | 1.3326 | -0.0211 | -0.0093 |
| 3 | 7 | 0.2857 | 1.0240 | 1.1448 | -32.9395 | -0.6639 |
| 4 | 7 | 0.5000 | 0.9909 | 2.2229 | 30.3581 | 1.5521 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 1.0092 | 1.9471 | 23.9732 | 0.9464 |
| top_20pct | 8 | 0.4286 | 0.9991 | 2.0758 | 17.1101 | 0.6503 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5714 | 0.9806 | 1.8282 | 33.5088 | 1.8283 |
| 1 | 7 | 0.2857 | 1.0168 | 1.0241 | -37.2473 | -0.8894 |
| 2 | 7 | 0.3333 | 1.0273 | 2.2192 | 3.7732 | 0.1523 |
| 3 | 7 | 0.7143 | 0.9804 | 0.9337 | 32.6524 | 1.9962 |
| 4 | 7 | 0.4286 | 1.0225 | 3.0525 | 24.9652 | 2.7815 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5714 | 0.9806 | 1.8282 | 33.5088 | 1.8283 |
| top_20pct | 8 | 0.5000 | 1.0194 | 2.5188 | 27.7852 | 3.2839 |

