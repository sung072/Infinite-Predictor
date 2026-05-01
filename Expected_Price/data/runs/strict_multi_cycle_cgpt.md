# Strict Multi-Cycle Research Result

- symbol: `CGPT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5507 | 0.9822 | 0.4151 | 1.0171 | 7.3843 | 0.8795 | 0.6025 | 0.6025 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5507 | 0.9845 | 0.4151 | 1.0171 | 7.3843 | 0.8795 | 0.6015 | 0.6015 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5507 | 0.9873 | 0.4151 | 1.0171 | 7.3843 | 0.8795 | 0.6003 | 0.6003 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5507 | 0.9902 | 0.4151 | 1.0171 | 7.3843 | 0.8795 | 0.5990 | 0.5990 |
| `base|emb=12|sh=0.97` | 18 | 0.4837 | 1.0006 | 1.0000 | 0.9867 | -3.5618 | -0.0252 | 0.5166 | 0.5166 |
| `base|emb=12|sh=0.96` | 18 | 0.4837 | 1.0018 | 1.0000 | 0.9867 | -3.5618 | -0.0252 | 0.5162 | 0.5162 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4750 | 0.9993 | 0.4105 | 0.9517 | -7.1068 | 0.3167 | 0.5156 | 0.5156 |
| `base|emb=12|sh=0.95` | 18 | 0.4837 | 1.0033 | 1.0000 | 0.9867 | -3.5618 | -0.0252 | 0.5156 | 0.5156 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4750 | 0.9990 | 0.4105 | 0.9517 | -7.1068 | 0.3167 | 0.5156 | 0.5156 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4750 | 1.0000 | 0.4105 | 0.9517 | -7.1068 | 0.3167 | 0.5156 | 0.5156 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4750 | 0.9990 | 0.4105 | 0.9517 | -7.1068 | 0.3167 | 0.5154 | 0.5154 |
| `base|emb=24|sh=0.97` | 18 | 0.4845 | 1.0019 | 1.0000 | 1.0298 | -2.1776 | -0.0375 | 0.5154 | 0.5154 |
| `base|emb=12|sh=0.94` | 18 | 0.4837 | 1.0050 | 1.0000 | 0.9867 | -3.5618 | -0.0252 | 0.5150 | 0.5150 |
| `base|emb=24|sh=0.96` | 18 | 0.4845 | 1.0034 | 1.0000 | 1.0298 | -2.1776 | -0.0375 | 0.5148 | 0.5148 |
| `base|emb=24|sh=0.95` | 18 | 0.4845 | 1.0053 | 1.0000 | 1.0298 | -2.1776 | -0.0375 | 0.5141 | 0.5141 |
| `base|emb=24|sh=0.94` | 18 | 0.4845 | 1.0074 | 1.0000 | 1.0298 | -2.1776 | -0.0375 | 0.5133 | 0.5133 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4696 | 1.0168 | 0.3164 | 0.8705 | -12.6545 | -0.3741 | 0.4482 | 0.4482 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4696 | 1.0253 | 0.3164 | 0.8705 | -12.6545 | -0.3741 | 0.4455 | 0.4455 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4696 | 1.0341 | 0.3164 | 0.8705 | -12.6545 | -0.3741 | 0.4428 | 0.4428 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4696 | 1.0429 | 0.3164 | 0.8705 | -12.6545 | -0.3741 | 0.4403 | 0.4403 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=332, top_n=34, cutoff=0.7899

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6171 | 0.0603 | 0.9725 | 0.0140 |
| all validations | 0.4861 | 0.0950 | 1.0064 | 0.0362 |

- improvement vs all (primary fraction): `hit +13.10pp, mae +3.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5714 | 1.0006 | 0.8333 | 1.1581 | 0.1787 | 16.7270 | 0.7219 | 0.7428 | 0.7428 |
| 2 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5714 | 1.0008 | 0.8333 | 1.1581 | 0.1787 | 16.7270 | 0.7219 | 0.7428 | 0.7428 |
| 3 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5714 | 1.0010 | 0.8333 | 1.1581 | 0.1787 | 16.7270 | 0.7219 | 0.7427 | 0.7427 |
| 4 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5714 | 1.0012 | 0.8333 | 1.1581 | 0.1787 | 16.7270 | 0.7219 | 0.7426 | 0.7426 |
| 5 | `base|emb=12|sh=0.97` | 0.5143 | 0.9954 | 1.0000 | 1.0509 | 0.0381 | 3.5647 | 0.1717 | 0.6854 | 0.6854 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.5000 | 1.0117 | 1.7411 | 21.2755 | 0.7360 |
| 1 | 6 | 0.4000 | 1.0276 | 0.5118 | -34.2894 | -0.6674 |
| 2 | 6 | 0.6667 | 0.9790 | 1.9822 | 54.6012 | 35.2085 |
| 3 | 6 | 0.5000 | 1.0091 | 0.7986 | -7.9949 | -0.2633 |
| 4 | 6 | 0.8000 | 0.9915 | 0.9267 | 50.5189 | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 6 | 0.5000 | 1.0117 | 1.7411 | 21.2755 | 0.7360 |
| top_20pct | 6 | 0.8000 | 0.9915 | 0.9267 | 50.5189 | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.5000 | 1.0117 | 1.7411 | 21.2755 | 0.7360 |
| 1 | 6 | 0.3333 | 1.0277 | 0.4021 | -59.0705 | -0.8065 |
| 2 | 6 | 0.6667 | 0.9659 | 1.7661 | 48.3456 | 4.2020 |
| 3 | 6 | 0.8000 | 1.0040 | 0.4129 | 18.1423 | n/a |
| 4 | 6 | 0.6000 | 0.9945 | 4.4911 | 66.5196 | 36.6041 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 6 | 0.5000 | 1.0117 | 1.7411 | 21.2755 | 0.7360 |
| top_20pct | 6 | 0.6000 | 0.9945 | 4.4911 | 66.5196 | 36.6041 |

