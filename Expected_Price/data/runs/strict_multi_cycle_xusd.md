# Strict Multi-Cycle Research Result

- symbol: `XUSD`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7254 | 1.0224 | 0.2855 | 1.2618 | 51.4270 | 4.0844 | 0.8254 | 0.8254 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7254 | 1.0299 | 0.2855 | 1.2618 | 51.4270 | 4.0844 | 0.8227 | 0.8227 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7254 | 1.0373 | 0.2855 | 1.2618 | 51.4270 | 4.0844 | 0.8201 | 0.8201 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7254 | 1.0448 | 0.2855 | 1.2618 | 51.4270 | 4.0844 | 0.8175 | 0.8175 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6843 | 1.0196 | 0.2994 | 1.2959 | 45.0167 | 3.9872 | 0.7853 | 0.7853 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6843 | 1.0261 | 0.2994 | 1.2959 | 45.0167 | 3.9872 | 0.7829 | 0.7829 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6843 | 1.0327 | 0.2994 | 1.2959 | 45.0167 | 3.9872 | 0.7806 | 0.7806 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6843 | 1.0392 | 0.2994 | 1.2959 | 45.0167 | 3.9872 | 0.7783 | 0.7783 |
| `base|emb=24|sh=0.97` | 18 | 0.6414 | 1.0314 | 1.0000 | 1.0712 | 29.3017 | 3.8082 | 0.7353 | 0.7353 |
| `base|emb=12|sh=0.97` | 18 | 0.6267 | 1.0284 | 1.0000 | 1.0703 | 25.8769 | 3.5456 | 0.7350 | 0.7350 |
| `base|emb=12|sh=0.96` | 18 | 0.6267 | 1.0379 | 1.0000 | 1.0703 | 25.8769 | 3.5456 | 0.7318 | 0.7318 |
| `base|emb=24|sh=0.96` | 18 | 0.6414 | 1.0418 | 1.0000 | 1.0712 | 29.3017 | 3.8082 | 0.7317 | 0.7317 |
| `base|emb=12|sh=0.95` | 18 | 0.6267 | 1.0474 | 1.0000 | 1.0703 | 25.8769 | 3.5456 | 0.7287 | 0.7287 |
| `base|emb=24|sh=0.95` | 18 | 0.6414 | 1.0523 | 1.0000 | 1.0712 | 29.3017 | 3.8082 | 0.7283 | 0.7283 |
| `base|emb=12|sh=0.94` | 18 | 0.6267 | 1.0569 | 1.0000 | 1.0703 | 25.8769 | 3.5456 | 0.7257 | 0.7257 |
| `base|emb=24|sh=0.94` | 18 | 0.6414 | 1.0628 | 1.0000 | 1.0712 | 29.3017 | 3.8082 | 0.7250 | 0.7250 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5746 | 1.0271 | 0.4599 | 1.4635 | 17.6754 | 1.9929 | 0.6637 | 0.6637 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5746 | 1.0361 | 0.4599 | 1.4635 | 17.6754 | 1.9929 | 0.6605 | 0.6605 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5746 | 1.0451 | 0.4599 | 1.4635 | 17.6754 | 1.9929 | 0.6574 | 0.6574 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5746 | 1.0542 | 0.4599 | 1.4635 | 17.6754 | 1.9929 | 0.6543 | 0.6543 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.8555

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7171 | 0.1727 | 1.0151 | 0.0180 |
| all validations | 0.6280 | 0.1340 | 1.0409 | 0.0501 |

- improvement vs all (primary fraction): `hit +8.91pp, mae +2.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 1.0076 | 0.9444 | 0.8124 | 0.2160 | 20.2146 | 0.9998 | 0.7521 | 0.7521 |
| 2 | `base|emb=24|sh=0.97` | 0.6667 | 1.0085 | 1.0000 | 0.8124 | 0.2160 | 20.2146 | 0.9998 | 0.7517 | 0.7517 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 1.0101 | 0.9444 | 0.8124 | 0.2160 | 20.2146 | 0.9998 | 0.7511 | 0.7511 |
| 4 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 1.0127 | 0.9444 | 0.8124 | 0.2160 | 20.2146 | 0.9998 | 0.7501 | 0.7501 |
| 5 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 1.0152 | 0.9444 | 0.8124 | 0.2160 | 20.2146 | 0.9998 | 0.7491 | 0.7491 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 1.0000 | 1.0019 | n/a | 135.1230 | n/a |
| 1 | 7 | 0.7500 | 0.9879 | 0.4999 | 15.5908 | 0.4995 |
| 2 | 6 | 0.3333 | 1.0146 | 0.6666 | -40.8517 | -1.0001 |
| 3 | 7 | 0.6667 | 1.0331 | 0.5001 | 0.0072 | n/a |
| 4 | 7 | 0.5000 | 1.0066 | n/a | n/a | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 1.0000 | 1.0019 | n/a | 135.1230 | n/a |
| top_20pct | 7 | 0.5000 | 1.0066 | n/a | n/a | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 0.0000 | 1.0250 | n/a | n/a | n/a |
| 1 | 7 | 0.2500 | 1.0419 | 0.6000 | -66.1788 | -0.8001 |
| 2 | 6 | 0.7500 | 1.0011 | 0.5000 | 15.6019 | 0.4999 |
| 3 | 7 | 1.0000 | 0.9761 | n/a | 216.2292 | n/a |
| 4 | 7 | 1.0000 | 0.9947 | n/a | 135.1230 | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 7 | 0.0000 | 1.0250 | n/a | n/a | n/a |
| top_20pct | 7 | 1.0000 | 0.9947 | n/a | 135.1230 | n/a |

