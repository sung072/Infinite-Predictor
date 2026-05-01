# Strict Multi-Cycle Research Result

- symbol: `GIGGLE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5200 | 0.9910 | 0.4630 | 1.0621 | 1.3595 | 0.4207 | 0.5658 | 0.5658 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5200 | 0.9913 | 0.4630 | 1.0621 | 1.3595 | 0.4207 | 0.5657 | 0.5657 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5200 | 0.9918 | 0.4630 | 1.0621 | 1.3595 | 0.4207 | 0.5653 | 0.5653 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5200 | 0.9935 | 0.4630 | 1.0621 | 1.3595 | 0.4207 | 0.5645 | 0.5645 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5234 | 0.9953 | 0.2531 | 0.8899 | -5.7836 | -0.0249 | 0.5495 | 0.5495 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5234 | 0.9951 | 0.2531 | 0.8899 | -5.7836 | -0.0249 | 0.5482 | 0.5482 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5234 | 0.9949 | 0.2531 | 0.8899 | -5.7836 | -0.0249 | 0.5472 | 0.5472 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5234 | 0.9948 | 0.2531 | 0.8899 | -5.7836 | -0.0249 | 0.5464 | 0.5464 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5124 | 0.9788 | 0.2454 | 0.8928 | -4.8711 | -0.0487 | 0.5340 | 0.5340 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4608 | 1.0007 | 0.4676 | 1.0485 | -9.6029 | 0.2117 | 0.5315 | 0.5315 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4608 | 1.0014 | 0.4676 | 1.0485 | -9.6029 | 0.2117 | 0.5314 | 0.5314 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4608 | 1.0024 | 0.4676 | 1.0485 | -9.6029 | 0.2117 | 0.5312 | 0.5312 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5124 | 0.9818 | 0.2454 | 0.8928 | -4.8711 | -0.0487 | 0.5307 | 0.5307 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4608 | 1.0042 | 0.4676 | 1.0485 | -9.6029 | 0.2117 | 0.5307 | 0.5307 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5124 | 0.9848 | 0.2454 | 0.8928 | -4.8711 | -0.0487 | 0.5279 | 0.5279 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5124 | 0.9878 | 0.2454 | 0.8928 | -4.8711 | -0.0487 | 0.5256 | 0.5256 |
| `base|emb=12|sh=0.96` | 18 | 0.5080 | 0.9949 | 1.0000 | 0.9049 | -3.8491 | -0.1035 | 0.4951 | 0.4951 |
| `base|emb=12|sh=0.97` | 18 | 0.5080 | 0.9952 | 1.0000 | 0.9049 | -3.8491 | -0.1035 | 0.4949 | 0.4949 |
| `base|emb=12|sh=0.95` | 18 | 0.5080 | 0.9962 | 1.0000 | 0.9049 | -3.8491 | -0.1035 | 0.4946 | 0.4946 |
| `base|emb=12|sh=0.94` | 18 | 0.5080 | 0.9992 | 1.0000 | 0.9049 | -3.8491 | -0.1035 | 0.4935 | 0.4935 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.7646

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6355 | 0.1039 | 0.9282 | 0.0826 |
| all validations | 0.4997 | 0.0945 | 0.9958 | 0.0441 |

- improvement vs all (primary fraction): `hit +13.59pp, mae +6.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.96` | 0.4848 | 1.0030 | 1.0000 | 0.5861 | -0.2297 | -21.4964 | -0.7028 | 0.3517 | 0.3517 |
| 2 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4545 | 1.0144 | 0.3333 | 0.6058 | -0.2874 | -26.8963 | -0.5028 | 0.3485 | 0.3485 |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4545 | 1.0192 | 0.3333 | 0.6058 | -0.2874 | -26.8963 | -0.5028 | 0.3466 | 0.3466 |
| 4 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4545 | 1.0240 | 0.3333 | 0.6058 | -0.2874 | -26.8963 | -0.5028 | 0.3448 | 0.3448 |
| 5 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4545 | 1.0288 | 0.3333 | 0.6058 | -0.2874 | -26.8963 | -0.5028 | 0.3430 | 0.3430 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.3750 | 1.0265 | 0.7355 | -31.8194 | -0.5648 |
| 1 | 7 | 0.4000 | 1.0710 | 0.2796 | -57.5396 | -0.8176 |
| 2 | 7 | 0.5714 | 0.9712 | 0.5157 | -13.7297 | -0.3757 |
| 3 | 7 | 0.6667 | 0.9517 | 0.2354 | -25.6127 | -1.1003 |
| 4 | 7 | 0.4286 | 1.0145 | 1.3964 | 1.5146 | 0.0386 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.3750 | 1.0265 | 0.7355 | -31.8194 | -0.5648 |
| top_20pct | 8 | 0.5000 | 0.9849 | 1.2530 | 7.5358 | 0.2585 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 1.0195 | 1.3037 | 9.7767 | 0.5656 |
| 1 | 7 | 0.6667 | 0.9374 | 0.1727 | -30.3917 | -2.3986 |
| 2 | 7 | 0.5714 | 0.9649 | 0.7395 | -0.4595 | -0.0561 |
| 3 | 7 | 0.1429 | 1.0599 | 1.0390 | -73.2082 | -1.0878 |
| 4 | 7 | 0.5714 | 0.9880 | 0.7750 | 1.2284 | 0.0280 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 1.0195 | 1.3037 | 9.7767 | 0.5656 |
| top_20pct | 8 | 0.5000 | 1.0056 | 0.7814 | -9.5337 | -0.2241 |

