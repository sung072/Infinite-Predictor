# Strict Multi-Cycle Research Result

- symbol: `INJ`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4951 | 1.0117 | 0.3380 | 1.1470 | 1.6906 | 0.8461 | 0.5793 | 0.5793 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4951 | 1.0165 | 0.3380 | 1.1470 | 1.6906 | 0.8461 | 0.5779 | 0.5779 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4951 | 1.0237 | 0.3380 | 1.1470 | 1.6906 | 0.8461 | 0.5759 | 0.5759 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4951 | 1.0314 | 0.3380 | 1.1470 | 1.6906 | 0.8461 | 0.5740 | 0.5740 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5075 | 0.9984 | 0.4336 | 0.9998 | -2.8193 | 0.1997 | 0.5523 | 0.5523 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5075 | 0.9983 | 0.4336 | 0.9998 | -2.8193 | 0.1997 | 0.5522 | 0.5522 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5075 | 1.0000 | 0.4336 | 0.9998 | -2.8193 | 0.1997 | 0.5518 | 0.5518 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5075 | 1.0019 | 0.4336 | 0.9998 | -2.8193 | 0.1997 | 0.5513 | 0.5513 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5258 | 0.9993 | 0.4182 | 0.9098 | -0.4176 | -0.1870 | 0.5427 | 0.5427 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5258 | 0.9995 | 0.4182 | 0.9098 | -0.4176 | -0.1870 | 0.5427 | 0.5427 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5258 | 1.0008 | 0.4182 | 0.9098 | -0.4176 | -0.1870 | 0.5422 | 0.5422 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5258 | 1.0023 | 0.4182 | 0.9098 | -0.4176 | -0.1870 | 0.5417 | 0.5417 |
| `base|emb=12|sh=0.97` | 18 | 0.5028 | 1.0012 | 1.0000 | 1.0036 | -0.8090 | 0.2518 | 0.5405 | 0.5405 |
| `base|emb=12|sh=0.96` | 18 | 0.5028 | 1.0025 | 1.0000 | 1.0036 | -0.8090 | 0.2518 | 0.5401 | 0.5401 |
| `base|emb=12|sh=0.95` | 18 | 0.5028 | 1.0050 | 1.0000 | 1.0036 | -0.8090 | 0.2518 | 0.5391 | 0.5391 |
| `base|emb=12|sh=0.94` | 18 | 0.5028 | 1.0079 | 1.0000 | 1.0036 | -0.8090 | 0.2518 | 0.5381 | 0.5381 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4836 | 1.0139 | 0.2994 | 1.0454 | -6.2954 | 0.5066 | 0.5036 | 0.5036 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4836 | 1.0191 | 0.2994 | 1.0454 | -6.2954 | 0.5066 | 0.5019 | 0.5019 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4836 | 1.0283 | 0.2994 | 1.0454 | -6.2954 | 0.5066 | 0.4990 | 0.4990 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4836 | 1.0382 | 0.2994 | 1.0454 | -6.2954 | 0.5066 | 0.4962 | 0.4962 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.7887

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6295 | 0.0686 | 0.9750 | 0.0299 |
| all validations | 0.5023 | 0.1003 | 1.0080 | 0.0408 |

- improvement vs all (primary fraction): `hit +12.72pp, mae +3.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.5294 | 0.9872 | 1.0000 | 0.9376 | 0.0208 | 1.9431 | 0.1007 | 0.6454 | 0.6454 |
| 2 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9725 | 0.3056 | 0.8708 | -0.0567 | -5.3079 | -0.1722 | 0.4064 | 0.4064 |
| 3 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9771 | 0.3056 | 0.8708 | -0.0567 | -5.3079 | -0.1722 | 0.4045 | 0.4045 |
| 4 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9817 | 0.3056 | 0.8708 | -0.0567 | -5.3079 | -0.1722 | 0.4026 | 0.4026 |
| 5 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9862 | 0.3056 | 0.8708 | -0.0567 | -5.3079 | -0.1722 | 0.4007 | 0.4007 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.3750 | 1.0136 | 1.2501 | -10.8831 | -0.2869 |
| 1 | 7 | 0.5000 | 0.9917 | 4.5162 | 35.2244 | 3.5157 |
| 2 | 7 | 0.5714 | 0.9812 | 0.4573 | -17.9993 | -0.7691 |
| 3 | 7 | 0.7143 | 0.9214 | 1.7436 | 56.6289 | 3.3713 |
| 4 | 7 | 0.5000 | 0.9815 | 0.7214 | -13.1850 | -0.9479 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.3750 | 1.0136 | 1.2501 | -10.8831 | -0.2869 |
| top_20pct | 8 | 0.4286 | 0.9944 | 0.9284 | -13.9772 | -0.9535 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5714 | 0.9795 | 1.1918 | 18.3527 | 0.9967 |
| 1 | 7 | 0.5714 | 0.9666 | 0.4860 | -14.3062 | -0.4173 |
| 2 | 7 | 0.2857 | 1.0085 | 0.4703 | -60.2632 | -1.4912 |
| 3 | 7 | 0.6667 | 0.9898 | 1.2432 | 32.1666 | 1.4845 |
| 4 | 7 | 0.5714 | 0.9747 | 2.8211 | 43.0025 | 3.9317 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5714 | 0.9795 | 1.1918 | 18.3527 | 0.9967 |
| top_20pct | 8 | 0.6250 | 0.9745 | 2.4349 | 44.9663 | 4.3589 |

