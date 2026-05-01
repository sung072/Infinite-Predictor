# Strict Multi-Cycle Research Result

- symbol: `TRB`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5758 | 0.9571 | 0.3519 | 1.2278 | 16.0559 | 1.2985 | 0.7189 | 0.7189 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5758 | 0.9611 | 0.3519 | 1.2278 | 16.0559 | 1.2985 | 0.7170 | 0.7170 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5758 | 0.9678 | 0.3519 | 1.2278 | 16.0559 | 1.2985 | 0.7140 | 0.7140 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5758 | 0.9758 | 0.3519 | 1.2278 | 16.0559 | 1.2985 | 0.7105 | 0.7105 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5362 | 0.9708 | 0.3580 | 1.1801 | 9.7343 | 0.9259 | 0.6337 | 0.6337 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5362 | 0.9715 | 0.3580 | 1.1801 | 9.7343 | 0.9259 | 0.6331 | 0.6331 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5362 | 0.9758 | 0.3580 | 1.1801 | 9.7343 | 0.9259 | 0.6310 | 0.6310 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5362 | 0.9816 | 0.3580 | 1.1801 | 9.7343 | 0.9259 | 0.6284 | 0.6284 |
| `base|emb=12|sh=0.94` | 18 | 0.5491 | 0.9886 | 1.0000 | 0.8401 | 0.3140 | 0.3243 | 0.5380 | 0.5380 |
| `base|emb=12|sh=0.95` | 18 | 0.5491 | 0.9887 | 1.0000 | 0.8401 | 0.3140 | 0.3243 | 0.5379 | 0.5379 |
| `base|emb=12|sh=0.96` | 18 | 0.5491 | 0.9898 | 1.0000 | 0.8401 | 0.3140 | 0.3243 | 0.5374 | 0.5374 |
| `base|emb=12|sh=0.97` | 18 | 0.5491 | 0.9918 | 1.0000 | 0.8401 | 0.3140 | 0.3243 | 0.5366 | 0.5366 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5116 | 1.0049 | 0.3657 | 0.8647 | -3.9242 | 0.0680 | 0.5266 | 0.5266 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5116 | 1.0078 | 0.3657 | 0.8647 | -3.9242 | 0.0680 | 0.5256 | 0.5256 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5116 | 1.0113 | 0.3657 | 0.8647 | -3.9242 | 0.0680 | 0.5243 | 0.5243 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5116 | 1.0151 | 0.3657 | 0.8647 | -3.9242 | 0.0680 | 0.5230 | 0.5230 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5332 | 0.9977 | 0.3565 | 0.8347 | -6.0575 | 0.3300 | 0.5017 | 0.5017 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5332 | 0.9980 | 0.3565 | 0.8347 | -6.0575 | 0.3300 | 0.5016 | 0.5016 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5332 | 0.9995 | 0.3565 | 0.8347 | -6.0575 | 0.3300 | 0.5011 | 0.5011 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5332 | 1.0015 | 0.3565 | 0.8347 | -6.0575 | 0.3300 | 0.5005 | 0.5005 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8198

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6558 | 0.0439 | 0.9504 | 0.0281 |
| all validations | 0.5376 | 0.0939 | 0.9896 | 0.0299 |

- improvement vs all (primary fraction): `hit +11.82pp, mae +4.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5517 | 0.9901 | 0.8611 | 0.8360 | 0.0123 | 1.1556 | 0.0405 | 0.6115 | 0.6115 |
| 2 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5517 | 0.9918 | 0.8611 | 0.8360 | 0.0123 | 1.1556 | 0.0405 | 0.6108 | 0.6108 |
| 3 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5517 | 0.9934 | 0.8611 | 0.8360 | 0.0123 | 1.1556 | 0.0405 | 0.6102 | 0.6102 |
| 4 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5517 | 0.9951 | 0.8611 | 0.8360 | 0.0123 | 1.1556 | 0.0405 | 0.6095 | 0.6095 |
| 5 | `base|emb=12|sh=0.94` | 0.5294 | 0.9873 | 1.0000 | 0.7351 | -0.0799 | -7.4741 | -0.4965 | 0.3827 | 0.3827 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.4286 | 1.0092 | 1.3813 | 1.4605 | 0.0707 |
| 1 | 6 | 0.6667 | 0.9492 | 0.7125 | 11.8938 | 0.5076 |
| 2 | 6 | 1.0000 | 0.9583 | n/a | 106.1520 | n/a |
| 3 | 6 | 0.3333 | 0.9838 | 0.8517 | -33.0478 | -0.7844 |
| 4 | 6 | 0.4000 | 1.0326 | 0.8600 | -23.0107 | -0.4341 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.4286 | 1.0092 | 1.3813 | 1.4605 | 0.0707 |
| top_20pct | 7 | 0.3333 | 1.0254 | 0.7806 | -40.1800 | -0.6172 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.7143 | 0.9419 | 0.9468 | 34.1507 | 1.6937 |
| 1 | 6 | 0.6667 | 0.9641 | 1.1305 | 27.4145 | 1.2561 |
| 2 | 6 | 0.1667 | 1.0758 | 0.9501 | -75.5931 | -0.9323 |
| 3 | 6 | 0.6000 | 0.9912 | 0.5110 | -9.7006 | -0.3651 |
| 4 | 6 | 0.6000 | 0.9509 | 1.2716 | 22.9956 | 0.9008 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.7143 | 0.9419 | 0.9468 | 34.1507 | 1.6937 |
| top_20pct | 7 | 0.6667 | 0.9256 | 1.3567 | 37.7421 | 1.7164 |

