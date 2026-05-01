# Strict Multi-Cycle Research Result

- symbol: `RLUSD`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `base|emb=24|sh=0.97` | 18 | 0.7544 | 1.0033 | 1.0000 | 1.2507 | 61.0906 | 10.1908 | 0.8533 | 0.8533 |
| `base|emb=24|sh=0.96` | 18 | 0.7544 | 1.0045 | 1.0000 | 1.2507 | 61.0906 | 10.1908 | 0.8529 | 0.8529 |
| `base|emb=24|sh=0.95` | 18 | 0.7544 | 1.0056 | 1.0000 | 1.2507 | 61.0906 | 10.1908 | 0.8524 | 0.8524 |
| `base|emb=24|sh=0.94` | 18 | 0.7544 | 1.0067 | 1.0000 | 1.2507 | 61.0906 | 10.1908 | 0.8520 | 0.8520 |
| `base|emb=12|sh=0.97` | 18 | 0.7465 | 1.0035 | 1.0000 | 1.2301 | 59.2631 | 9.1250 | 0.8484 | 0.8484 |
| `base|emb=12|sh=0.96` | 18 | 0.7465 | 1.0047 | 1.0000 | 1.2301 | 59.2631 | 9.1250 | 0.8479 | 0.8479 |
| `base|emb=12|sh=0.95` | 18 | 0.7465 | 1.0059 | 1.0000 | 1.2301 | 59.2631 | 9.1250 | 0.8475 | 0.8475 |
| `base|emb=12|sh=0.94` | 18 | 0.7465 | 1.0071 | 1.0000 | 1.2301 | 59.2631 | 9.1250 | 0.8470 | 0.8470 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7242 | 1.0020 | 0.3812 | 1.2225 | 49.5930 | 6.2062 | 0.8441 | 0.8441 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7242 | 1.0026 | 0.3812 | 1.2225 | 49.5930 | 6.2062 | 0.8439 | 0.8439 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7242 | 1.0033 | 0.3812 | 1.2225 | 49.5930 | 6.2062 | 0.8436 | 0.8436 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7242 | 1.0040 | 0.3812 | 1.2225 | 49.5930 | 6.2062 | 0.8434 | 0.8434 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7074 | 1.0025 | 0.3580 | 1.1765 | 47.4881 | 6.0437 | 0.8319 | 0.8319 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7074 | 1.0033 | 0.3580 | 1.1765 | 47.4881 | 6.0437 | 0.8316 | 0.8316 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7074 | 1.0041 | 0.3580 | 1.1765 | 47.4881 | 6.0437 | 0.8313 | 0.8313 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7074 | 1.0050 | 0.3580 | 1.1765 | 47.4881 | 6.0437 | 0.8311 | 0.8311 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7560 | 1.0044 | 0.3256 | 1.7411 | 75.1424 | 7.3544 | 0.8207 | 0.8207 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7560 | 1.0059 | 0.3256 | 1.7411 | 75.1424 | 7.3544 | 0.8202 | 0.8202 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7560 | 1.0074 | 0.3256 | 1.7411 | 75.1424 | 7.3544 | 0.8196 | 0.8196 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7560 | 1.0089 | 0.3256 | 1.7411 | 75.1424 | 7.3544 | 0.8190 | 0.8190 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=308, top_n=31, cutoff=0.8782

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7825 | 0.1689 | 1.0032 | 0.0076 |
| all validations | 0.7466 | 0.1161 | 1.0046 | 0.0120 |

- improvement vs all (primary fraction): `hit +3.60pp, mae +0.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.5333 | 1.0246 | 1.0000 | 0.9999 | 0.0645 | 6.0379 | 0.4992 | 0.7065 | 0.7065 |
| 2 | `base|emb=24|sh=0.96` | 0.5333 | 1.0328 | 1.0000 | 0.9999 | 0.0645 | 6.0379 | 0.4992 | 0.7034 | 0.7034 |
| 3 | `base|emb=24|sh=0.95` | 0.5333 | 1.0410 | 1.0000 | 0.9999 | 0.0645 | 6.0379 | 0.4992 | 0.7003 | 0.7003 |
| 4 | `base|emb=24|sh=0.94` | 0.5333 | 1.0492 | 1.0000 | 0.9999 | 0.0645 | 6.0379 | 0.4992 | 0.6973 | 0.6973 |
| 5 | `base|emb=12|sh=0.97` | 0.5000 | 1.0276 | 1.0000 | 1.0000 | -0.0000 | -0.0022 | -0.0003 | 0.5374 | 0.5374 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.7500 | 1.0072 | 1.0000 | 46.7974 | n/a |
| 1 | 7 | 0.5000 | 0.9908 | 0.9999 | -0.0041 | -0.0004 |
| 2 | 7 | 0.5000 | 1.0006 | 0.9999 | -0.0041 | -0.0004 |
| 3 | 7 | 0.0000 | 1.2284 | n/a | n/a | n/a |
| 4 | 7 | 0.5000 | 1.0733 | n/a | n/a | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.7500 | 1.0072 | 1.0000 | 46.7974 | n/a |
| top_20pct | 8 | 0.5000 | 1.0857 | n/a | n/a | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 1.0164 | 0.9999 | -0.0041 | -0.0004 |
| 1 | 7 | 0.0000 | 1.2212 | n/a | n/a | n/a |
| 2 | 7 | 0.5000 | 1.0734 | n/a | n/a | n/a |
| 3 | 7 | 0.5000 | 0.9984 | 1.0000 | 0.0000 | -0.0002 |
| 4 | 7 | 0.7500 | 0.9855 | 0.9999 | 46.7943 | 1.9998 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 1.0164 | 0.9999 | -0.0041 | -0.0004 |
| top_20pct | 8 | 0.7500 | 0.9871 | 0.9999 | 46.7943 | 1.9998 |

