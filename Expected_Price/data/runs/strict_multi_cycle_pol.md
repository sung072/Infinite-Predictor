# Strict Multi-Cycle Research Result

- symbol: `POL`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5888 | 0.9923 | 0.3102 | 1.1050 | 14.6184 | 1.9401 | 0.6601 | 0.6601 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5888 | 0.9931 | 0.3102 | 1.1050 | 14.6184 | 1.9401 | 0.6585 | 0.6585 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5888 | 0.9939 | 0.3102 | 1.1050 | 14.6184 | 1.9401 | 0.6570 | 0.6570 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5888 | 0.9954 | 0.3102 | 1.1050 | 14.6184 | 1.9401 | 0.6556 | 0.6556 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5475 | 1.0076 | 0.2886 | 1.3406 | 10.2835 | 4.3455 | 0.6297 | 0.6297 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5475 | 1.0102 | 0.2886 | 1.3406 | 10.2835 | 4.3455 | 0.6292 | 0.6292 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5475 | 1.0135 | 0.2886 | 1.3406 | 10.2835 | 4.3455 | 0.6286 | 0.6286 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5475 | 1.0168 | 0.2886 | 1.3406 | 10.2835 | 4.3455 | 0.6280 | 0.6280 |
| `base|emb=12|sh=0.97` | 18 | 0.5024 | 1.0040 | 1.0000 | 1.0805 | 2.4362 | 0.5994 | 0.6010 | 0.6010 |
| `base|emb=12|sh=0.96` | 18 | 0.5024 | 1.0055 | 1.0000 | 1.0805 | 2.4362 | 0.5994 | 0.6005 | 0.6005 |
| `base|emb=12|sh=0.95` | 18 | 0.5024 | 1.0078 | 1.0000 | 1.0805 | 2.4362 | 0.5994 | 0.5997 | 0.5997 |
| `base|emb=12|sh=0.94` | 18 | 0.5024 | 1.0102 | 1.0000 | 1.0805 | 2.4362 | 0.5994 | 0.5988 | 0.5988 |
| `base|emb=24|sh=0.97` | 18 | 0.4994 | 1.0066 | 1.0000 | 1.0627 | 1.2667 | 0.4420 | 0.5772 | 0.5772 |
| `base|emb=24|sh=0.96` | 18 | 0.4994 | 1.0090 | 1.0000 | 1.0627 | 1.2667 | 0.4420 | 0.5763 | 0.5763 |
| `base|emb=24|sh=0.95` | 18 | 0.4994 | 1.0121 | 1.0000 | 1.0627 | 1.2667 | 0.4420 | 0.5753 | 0.5753 |
| `base|emb=24|sh=0.94` | 18 | 0.4994 | 1.0153 | 1.0000 | 1.0627 | 1.2667 | 0.4420 | 0.5743 | 0.5743 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.3810 | 1.0195 | 0.3704 | 1.0789 | -25.2157 | 0.7535 | 0.4483 | 0.4483 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.3810 | 1.0260 | 0.3704 | 1.0789 | -25.2157 | 0.7535 | 0.4461 | 0.4461 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4066 | 1.0106 | 0.3735 | 0.9403 | -18.7698 | -0.3506 | 0.4449 | 0.4449 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.3810 | 1.0326 | 0.3704 | 1.0789 | -25.2157 | 0.7535 | 0.4439 | 0.4439 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8626

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7132 | 0.0862 | 0.9598 | 0.0492 |
| all validations | 0.4864 | 0.1477 | 1.0114 | 0.0490 |

- improvement vs all (primary fraction): `hit +22.68pp, mae +5.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.5000 | 1.0065 | 1.0000 | 1.3643 | 0.1155 | 10.8058 | 0.7340 | 0.7351 | 0.7351 |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9955 | 0.7778 | 1.1088 | 0.0384 | 3.5925 | 0.1641 | 0.6853 | 0.6853 |
| 3 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9966 | 0.7778 | 1.1088 | 0.0384 | 3.5925 | 0.1641 | 0.6848 | 0.6848 |
| 4 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9982 | 0.7778 | 1.1088 | 0.0384 | 3.5925 | 0.1641 | 0.6842 | 0.6842 |
| 5 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0045 | 0.7778 | 1.1088 | 0.0384 | 3.5925 | 0.1641 | 0.6817 | 0.6817 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 1.0119 | 2.9007 | 31.0849 | 2.7088 |
| 1 | 7 | 0.8571 | 0.9591 | 4.5183 | 90.3929 | 26.3783 |
| 2 | 7 | 0.5714 | 0.9857 | 1.3453 | 19.5297 | 1.1825 |
| 3 | 7 | 0.2857 | 1.0170 | 0.6971 | -45.3113 | -1.2940 |
| 4 | 7 | 0.2000 | 1.0701 | 1.1935 | -44.3907 | -1.1645 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 1.0119 | 2.9007 | 31.0849 | 2.7088 |
| top_20pct | 8 | 0.1667 | 1.0658 | 1.1451 | -57.4312 | -1.4255 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 0.9982 | 2.9384 | 35.1815 | 1.9425 |
| 1 | 7 | 1.0000 | 0.9574 | n/a | 143.3243 | n/a |
| 2 | 7 | 0.2857 | 1.0048 | 2.3851 | -1.6533 | -0.0575 |
| 3 | 7 | 0.4286 | 1.0041 | 0.7609 | -20.6688 | -0.4337 |
| 4 | 7 | 0.2000 | 1.0701 | 1.1935 | -44.3907 | -1.1645 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 0.9982 | 2.9384 | 35.1815 | 1.9425 |
| top_20pct | 8 | 0.1667 | 1.0658 | 1.1451 | -57.4312 | -1.4255 |

