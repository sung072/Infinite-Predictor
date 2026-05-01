# Strict Multi-Cycle Research Result

- symbol: `SUI`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5829 | 0.9830 | 0.3086 | 1.0679 | 12.4553 | 0.6271 | 0.6239 | 0.6239 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5829 | 0.9844 | 0.3086 | 1.0679 | 12.4553 | 0.6271 | 0.6238 | 0.6238 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5829 | 0.9835 | 0.3086 | 1.0679 | 12.4553 | 0.6271 | 0.6231 | 0.6231 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5829 | 0.9854 | 0.3086 | 1.0679 | 12.4553 | 0.6271 | 0.6218 | 0.6218 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5406 | 0.9928 | 0.3256 | 1.1573 | 5.5183 | 1.0097 | 0.5989 | 0.5989 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5406 | 0.9943 | 0.3256 | 1.1573 | 5.5183 | 1.0097 | 0.5988 | 0.5988 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5406 | 0.9931 | 0.3256 | 1.1573 | 5.5183 | 1.0097 | 0.5984 | 0.5984 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5406 | 0.9972 | 0.3256 | 1.1573 | 5.5183 | 1.0097 | 0.5982 | 0.5982 |
| `base|emb=12|sh=0.97` | 18 | 0.5199 | 1.0002 | 1.0000 | 1.0400 | 2.0863 | 0.3726 | 0.5838 | 0.5838 |
| `base|emb=12|sh=0.96` | 18 | 0.5199 | 1.0016 | 1.0000 | 1.0400 | 2.0863 | 0.3726 | 0.5833 | 0.5833 |
| `base|emb=12|sh=0.95` | 18 | 0.5199 | 1.0036 | 1.0000 | 1.0400 | 2.0863 | 0.3726 | 0.5826 | 0.5826 |
| `base|emb=12|sh=0.94` | 18 | 0.5199 | 1.0059 | 1.0000 | 1.0400 | 2.0863 | 0.3726 | 0.5818 | 0.5818 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5043 | 1.0015 | 0.3812 | 1.0706 | -1.5251 | 0.2932 | 0.5718 | 0.5718 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5043 | 1.0023 | 0.3812 | 1.0706 | -1.5251 | 0.2932 | 0.5715 | 0.5715 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5043 | 1.0032 | 0.3812 | 1.0706 | -1.5251 | 0.2932 | 0.5711 | 0.5711 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5043 | 1.0043 | 0.3812 | 1.0706 | -1.5251 | 0.2932 | 0.5708 | 0.5708 |
| `base|emb=24|sh=0.97` | 18 | 0.5194 | 1.0004 | 1.0000 | 1.0235 | 2.0718 | 0.3182 | 0.5576 | 0.5576 |
| `base|emb=24|sh=0.96` | 18 | 0.5194 | 1.0015 | 1.0000 | 1.0235 | 2.0718 | 0.3182 | 0.5572 | 0.5572 |
| `base|emb=24|sh=0.95` | 18 | 0.5194 | 1.0033 | 1.0000 | 1.0235 | 2.0718 | 0.3182 | 0.5566 | 0.5566 |
| `base|emb=24|sh=0.94` | 18 | 0.5194 | 1.0053 | 1.0000 | 1.0235 | 2.0718 | 0.3182 | 0.5559 | 0.5559 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.8042

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6281 | 0.1286 | 0.9695 | 0.0458 |
| all validations | 0.5283 | 0.1228 | 0.9984 | 0.0354 |

- improvement vs all (primary fraction): `hit +9.98pp, mae +2.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5385 | 0.9845 | 0.7500 | 1.2965 | 0.1490 | 13.9463 | 1.5013 | 0.7713 | 0.7713 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5385 | 0.9871 | 0.7500 | 1.2965 | 0.1490 | 13.9463 | 1.5013 | 0.7702 | 0.7702 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5385 | 0.9897 | 0.7500 | 1.2965 | 0.1490 | 13.9463 | 1.5013 | 0.7692 | 0.7692 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5385 | 0.9923 | 0.7500 | 1.2965 | 0.1490 | 13.9463 | 1.5013 | 0.7681 | 0.7681 |
| 5 | `base|emb=12|sh=0.97` | 0.6286 | 0.9940 | 1.0000 | 0.9476 | 0.1699 | 15.9058 | 1.2106 | 0.7623 | 0.7623 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.6000 | 1.0167 | 0.8669 | 8.6987 | 0.2960 |
| 1 | 5 | 0.2000 | 1.0236 | 3.3583 | -5.7324 | -0.1870 |
| 2 | 5 | 0.4000 | 1.0414 | 3.0725 | 20.2576 | 1.1447 |
| 3 | 5 | 0.8000 | 0.9172 | 0.2376 | -1.6523 | -0.0559 |
| 4 | 6 | 0.6667 | 0.9695 | 1.4632 | 39.2557 | 2.1956 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.4000 | 0.9954 | 2.3981 | 15.3148 | 0.8914 |
| 1 | 5 | 0.6000 | 0.9535 | 1.2379 | 22.1925 | 1.0837 |
| 2 | 5 | 0.6000 | 0.9663 | 2.2890 | 37.8977 | 3.3607 |
| 3 | 5 | 0.6000 | 0.9272 | 0.7178 | 2.4234 | 0.0713 |
| 4 | 6 | 0.5000 | 1.0569 | 1.0196 | 0.5778 | 0.0108 |

