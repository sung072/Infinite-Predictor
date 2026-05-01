# Strict Multi-Cycle Research Result

- symbol: `EGLD`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5190 | 1.0099 | 0.2623 | 1.3560 | 9.3264 | 1.8482 | 0.6270 | 0.6270 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5190 | 1.0132 | 0.2623 | 1.3560 | 9.3264 | 1.8482 | 0.6260 | 0.6260 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5190 | 1.0164 | 0.2623 | 1.3560 | 9.3264 | 1.8482 | 0.6251 | 0.6251 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5190 | 1.0197 | 0.2623 | 1.3560 | 9.3264 | 1.8482 | 0.6243 | 0.6243 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5207 | 1.0094 | 0.2932 | 1.1061 | 4.9609 | 1.2827 | 0.5885 | 0.5885 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5207 | 1.0126 | 0.2932 | 1.1061 | 4.9609 | 1.2827 | 0.5874 | 0.5874 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5207 | 1.0157 | 0.2932 | 1.1061 | 4.9609 | 1.2827 | 0.5865 | 0.5865 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5207 | 1.0189 | 0.2932 | 1.1061 | 4.9609 | 1.2827 | 0.5856 | 0.5856 |
| `base|emb=24|sh=0.97` | 18 | 0.5147 | 1.0094 | 1.0000 | 0.9870 | 0.9974 | 0.4295 | 0.5754 | 0.5754 |
| `base|emb=24|sh=0.96` | 18 | 0.5147 | 1.0125 | 1.0000 | 0.9870 | 0.9974 | 0.4295 | 0.5742 | 0.5742 |
| `base|emb=24|sh=0.95` | 18 | 0.5147 | 1.0157 | 1.0000 | 0.9870 | 0.9974 | 0.4295 | 0.5731 | 0.5731 |
| `base|emb=24|sh=0.94` | 18 | 0.5147 | 1.0188 | 1.0000 | 0.9870 | 0.9974 | 0.4295 | 0.5719 | 0.5719 |
| `base|emb=12|sh=0.97` | 18 | 0.5091 | 1.0112 | 1.0000 | 1.0071 | 1.0109 | 0.6343 | 0.5328 | 0.5328 |
| `base|emb=12|sh=0.96` | 18 | 0.5091 | 1.0150 | 1.0000 | 1.0071 | 1.0109 | 0.6343 | 0.5314 | 0.5314 |
| `base|emb=12|sh=0.95` | 18 | 0.5091 | 1.0187 | 1.0000 | 1.0071 | 1.0109 | 0.6343 | 0.5300 | 0.5300 |
| `base|emb=12|sh=0.94` | 18 | 0.5091 | 1.0224 | 1.0000 | 1.0071 | 1.0109 | 0.6343 | 0.5286 | 0.5286 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4870 | 1.0119 | 0.3765 | 1.0472 | -2.9820 | 0.3266 | 0.5178 | 0.5178 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4870 | 1.0159 | 0.3765 | 1.0472 | -2.9820 | 0.3266 | 0.5164 | 0.5164 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4870 | 1.0198 | 0.3765 | 1.0472 | -2.9820 | 0.3266 | 0.5150 | 0.5150 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4870 | 1.0238 | 0.3765 | 1.0472 | -2.9820 | 0.3266 | 0.5137 | 0.5137 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.8232

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6581 | 0.0774 | 0.9931 | 0.0104 |
| all validations | 0.5001 | 0.1339 | 1.0172 | 0.0338 |

- improvement vs all (primary fraction): `hit +15.80pp, mae +2.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.3810 | 1.0594 | 1.0000 | 1.0602 | -0.1822 | -17.0556 | -0.6150 | 0.3345 | 0.3345 |
| 2 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.2857 | 1.0613 | 0.5833 | 1.6367 | -0.1727 | -16.1614 | -0.7816 | 0.3332 | 0.3332 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.2857 | 1.0817 | 0.5833 | 1.6367 | -0.1727 | -16.1614 | -0.7816 | 0.3260 | 0.3260 |
| 4 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.2857 | 1.1021 | 0.5833 | 1.6367 | -0.1727 | -16.1614 | -0.7816 | 0.3192 | 0.3192 |
| 5 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.2857 | 1.1226 | 0.5833 | 1.6367 | -0.1727 | -16.1614 | -0.7816 | 0.3126 | 0.3126 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1.0000 | 1.0169 | n/a | 267.8128 | n/a |
| 1 | 7 | 0.2500 | 1.0709 | 0.5382 | -73.9637 | -0.8237 |
| 2 | 7 | 0.3333 | 1.0312 | 1.0053 | -25.3490 | -0.7182 |
| 3 | 7 | 0.5000 | 1.0264 | 4.0160 | 46.9422 | 6.0247 |
| 4 | 7 | 0.0000 | 1.1613 | n/a | -131.5492 | -1.1401 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 1.0000 | 1.0169 | n/a | 267.8128 | n/a |
| top_20pct | 8 | 0.2000 | 1.0914 | 1.5199 | -36.1461 | -0.7126 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1.0000 | 1.0182 | n/a | 267.8128 | n/a |
| 1 | 7 | 0.2500 | 1.1666 | 0.7509 | -55.7094 | -1.0000 |
| 2 | 7 | 0.2000 | 1.0804 | 1.5199 | -36.1461 | -0.7126 |
| 3 | 7 | 0.5000 | 1.0151 | 1.5157 | 15.5045 | 0.5049 |
| 4 | 7 | 0.2000 | 1.0662 | 0.6055 | -83.6661 | -0.8516 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 1.0000 | 1.0182 | n/a | 267.8128 | n/a |
| top_20pct | 8 | 0.3333 | 1.0367 | 0.9304 | -32.0348 | -0.5424 |

