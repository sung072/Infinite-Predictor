# Strict Multi-Cycle Research Result

- symbol: `SAND`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6158 | 0.9717 | 0.3025 | 1.3489 | 23.1163 | 1.9352 | 0.7320 | 0.7320 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6158 | 0.9751 | 0.3025 | 1.3489 | 23.1163 | 1.9352 | 0.7298 | 0.7298 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6158 | 0.9787 | 0.3025 | 1.3489 | 23.1163 | 1.9352 | 0.7277 | 0.7277 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6158 | 0.9836 | 0.3025 | 1.3489 | 23.1163 | 1.9352 | 0.7253 | 0.7253 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5422 | 1.0010 | 0.3333 | 1.2570 | 11.5905 | 0.9801 | 0.6492 | 0.6492 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5422 | 1.0016 | 0.3333 | 1.2570 | 11.5905 | 0.9801 | 0.6492 | 0.6492 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5422 | 1.0036 | 0.3333 | 1.2570 | 11.5905 | 0.9801 | 0.6487 | 0.6487 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5422 | 1.0059 | 0.3333 | 1.2570 | 11.5905 | 0.9801 | 0.6481 | 0.6481 |
| `base|emb=24|sh=0.96` | 18 | 0.5518 | 0.9986 | 1.0000 | 0.9868 | 5.9702 | 0.5090 | 0.6175 | 0.6175 |
| `base|emb=24|sh=0.95` | 18 | 0.5518 | 0.9988 | 1.0000 | 0.9868 | 5.9702 | 0.5090 | 0.6175 | 0.6175 |
| `base|emb=24|sh=0.94` | 18 | 0.5518 | 0.9990 | 1.0000 | 0.9868 | 5.9702 | 0.5090 | 0.6175 | 0.6175 |
| `base|emb=24|sh=0.97` | 18 | 0.5518 | 0.9988 | 1.0000 | 0.9868 | 5.9702 | 0.5090 | 0.6174 | 0.6174 |
| `base|emb=12|sh=0.97` | 18 | 0.5327 | 1.0030 | 1.0000 | 1.0310 | 5.1806 | 0.4337 | 0.5910 | 0.5910 |
| `base|emb=12|sh=0.96` | 18 | 0.5327 | 1.0042 | 1.0000 | 1.0310 | 5.1806 | 0.4337 | 0.5905 | 0.5905 |
| `base|emb=12|sh=0.95` | 18 | 0.5327 | 1.0059 | 1.0000 | 1.0310 | 5.1806 | 0.4337 | 0.5899 | 0.5899 |
| `base|emb=12|sh=0.94` | 18 | 0.5327 | 1.0078 | 1.0000 | 1.0310 | 5.1806 | 0.4337 | 0.5893 | 0.5893 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4735 | 1.0083 | 0.4136 | 0.9965 | -7.7693 | 0.3856 | 0.5045 | 0.5045 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4735 | 1.0111 | 0.4136 | 0.9965 | -7.7693 | 0.3856 | 0.5036 | 0.5036 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4735 | 1.0139 | 0.4136 | 0.9965 | -7.7693 | 0.3856 | 0.5027 | 0.5027 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4735 | 1.0167 | 0.4136 | 0.9965 | -7.7693 | 0.3856 | 0.5018 | 0.5018 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=400, top_n=40, cutoff=0.8287

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6944 | 0.1078 | 0.9510 | 0.0483 |
| all validations | 0.5301 | 0.1288 | 1.0015 | 0.0351 |

- improvement vs all (primary fraction): `hit +16.44pp, mae +5.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.96` | 0.4706 | 0.9987 | 1.0000 | 0.5972 | -0.2409 | -22.5427 | -0.8382 | 0.3469 | 0.3469 |
| 2 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.2857 | 1.0323 | 0.1944 | 0.8451 | -0.3684 | -34.4845 | -0.7425 | 0.3115 | 0.3115 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.2857 | 1.0431 | 0.1944 | 0.8451 | -0.3684 | -34.4845 | -0.7425 | 0.3075 | 0.3075 |
| 4 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.2857 | 1.0538 | 0.1944 | 0.8451 | -0.3684 | -34.4845 | -0.7425 | 0.3036 | 0.3036 |
| 5 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.2857 | 1.0646 | 0.1944 | 0.8451 | -0.3684 | -34.4845 | -0.7425 | 0.2998 | 0.2998 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.4286 | 1.0170 | 0.4037 | -43.5927 | -0.7400 |
| 1 | 7 | 0.5714 | 0.9835 | 0.4627 | -16.1844 | -1.8922 |
| 2 | 7 | 0.1429 | 1.0707 | 0.3403 | -73.6397 | -2.0870 |
| 3 | 7 | 0.6667 | 0.8989 | 0.7194 | 14.5927 | 0.6067 |
| 4 | 7 | 0.5714 | 0.9643 | 1.3062 | 20.8183 | 1.3499 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.4286 | 1.0170 | 0.4037 | -43.5927 | -0.7400 |
| top_20pct | 8 | 0.5000 | 0.9881 | 1.1961 | 6.9054 | 0.2746 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5714 | 0.9678 | 0.8378 | 3.9720 | 0.2507 |
| 1 | 7 | 0.4286 | 1.0199 | 0.9699 | -12.4929 | -0.2775 |
| 2 | 7 | 0.5000 | 0.9856 | 1.1656 | 5.8034 | 0.2271 |
| 3 | 7 | 0.5714 | 0.9581 | 0.3508 | -23.6909 | -0.6120 |
| 4 | 7 | 0.2857 | 1.0524 | 0.2797 | -77.3377 | -0.8912 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5714 | 0.9678 | 0.8378 | 3.9720 | 0.2507 |
| top_20pct | 8 | 0.3750 | 1.0255 | 0.3826 | -54.1771 | -0.7763 |

