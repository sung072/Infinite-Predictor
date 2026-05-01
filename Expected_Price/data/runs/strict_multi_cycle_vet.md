# Strict Multi-Cycle Research Result

- symbol: `VET`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5241 | 1.0061 | 0.2284 | 1.7900 | 16.9389 | 2.4900 | 0.6347 | 0.6347 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5241 | 1.0097 | 0.2284 | 1.7900 | 16.9389 | 2.4900 | 0.6344 | 0.6344 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5241 | 1.0142 | 0.2284 | 1.7900 | 16.9389 | 2.4900 | 0.6341 | 0.6341 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5241 | 1.0201 | 0.2284 | 1.7900 | 16.9389 | 2.4900 | 0.6336 | 0.6336 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5176 | 0.9995 | 0.3704 | 1.3531 | 5.6157 | 1.6271 | 0.6227 | 0.6227 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5176 | 0.9998 | 0.3704 | 1.3531 | 5.6157 | 1.6271 | 0.6227 | 0.6227 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5176 | 1.0003 | 0.3704 | 1.3531 | 5.6157 | 1.6271 | 0.6225 | 0.6225 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5176 | 1.0018 | 0.3704 | 1.3531 | 5.6157 | 1.6271 | 0.6221 | 0.6221 |
| `base|emb=24|sh=0.97` | 18 | 0.5254 | 1.0005 | 1.0000 | 1.0312 | 3.9819 | 0.6197 | 0.6076 | 0.6076 |
| `base|emb=24|sh=0.96` | 18 | 0.5254 | 1.0018 | 1.0000 | 1.0312 | 3.9819 | 0.6197 | 0.6071 | 0.6071 |
| `base|emb=24|sh=0.95` | 18 | 0.5254 | 1.0037 | 1.0000 | 1.0312 | 3.9819 | 0.6197 | 0.6065 | 0.6065 |
| `base|emb=24|sh=0.94` | 18 | 0.5254 | 1.0061 | 1.0000 | 1.0312 | 3.9819 | 0.6197 | 0.6056 | 0.6056 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5114 | 0.9978 | 0.2500 | 1.1382 | 4.1061 | 0.6753 | 0.5940 | 0.5940 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5114 | 1.0013 | 0.2500 | 1.1382 | 4.1061 | 0.6753 | 0.5936 | 0.5936 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5114 | 1.0066 | 0.2500 | 1.1382 | 4.1061 | 0.6753 | 0.5929 | 0.5929 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5114 | 1.0144 | 0.2500 | 1.1382 | 4.1061 | 0.6753 | 0.5916 | 0.5916 |
| `base|emb=12|sh=0.97` | 18 | 0.5258 | 0.9989 | 1.0000 | 0.9950 | 2.2027 | 0.4009 | 0.5834 | 0.5834 |
| `base|emb=12|sh=0.96` | 18 | 0.5258 | 1.0001 | 1.0000 | 0.9950 | 2.2027 | 0.4009 | 0.5830 | 0.5830 |
| `base|emb=12|sh=0.95` | 18 | 0.5258 | 1.0019 | 1.0000 | 0.9950 | 2.2027 | 0.4009 | 0.5824 | 0.5824 |
| `base|emb=12|sh=0.94` | 18 | 0.5258 | 1.0046 | 1.0000 | 0.9950 | 2.2027 | 0.4009 | 0.5814 | 0.5814 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8343

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6415 | 0.1500 | 0.9475 | 0.0748 |
| all validations | 0.5186 | 0.1163 | 1.0032 | 0.0543 |

- improvement vs all (primary fraction): `hit +12.29pp, mae +5.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9584 | 0.5833 | 0.6998 | 0.1291 | 12.0867 | 0.8031 | 0.7611 | 0.7611 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9622 | 0.5833 | 0.6998 | 0.1291 | 12.0867 | 0.8031 | 0.7595 | 0.7595 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9664 | 0.5833 | 0.6998 | 0.1291 | 12.0867 | 0.8031 | 0.7577 | 0.7577 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9748 | 0.5833 | 0.6998 | 0.1291 | 12.0867 | 0.8031 | 0.7541 | 0.7541 |
| 5 | `base|emb=24|sh=0.97` | 0.6000 | 0.9867 | 1.0000 | 0.7614 | 0.0517 | 4.8362 | 0.2930 | 0.7109 | 0.7109 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 0.8000 | 0.9572 | 0.2169 | -4.1789 | -0.1396 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 1.0000 | 0.8533 | n/a | 109.6621 | n/a |

