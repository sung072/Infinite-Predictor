# Strict Multi-Cycle Research Result

- symbol: `AIXBT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5023 | 1.0083 | 0.2238 | 1.1745 | 3.5998 | 0.6643 | 0.5686 | 0.5686 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5023 | 1.0110 | 0.2238 | 1.1745 | 3.5998 | 0.6643 | 0.5678 | 0.5678 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5023 | 1.0138 | 0.2238 | 1.1745 | 3.5998 | 0.6643 | 0.5671 | 0.5671 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5023 | 1.0168 | 0.2238 | 1.1745 | 3.5998 | 0.6643 | 0.5663 | 0.5663 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4409 | 1.0218 | 0.4244 | 1.1653 | -5.4577 | 0.1426 | 0.5185 | 0.5185 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4409 | 1.0291 | 0.4244 | 1.1653 | -5.4577 | 0.1426 | 0.5158 | 0.5158 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4409 | 1.0363 | 0.4244 | 1.1653 | -5.4577 | 0.1426 | 0.5133 | 0.5133 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4409 | 1.0436 | 0.4244 | 1.1653 | -5.4577 | 0.1426 | 0.5107 | 0.5107 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4856 | 1.0189 | 0.4460 | 1.1060 | 1.0912 | 0.5160 | 0.5084 | 0.5084 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4856 | 1.0252 | 0.4460 | 1.1060 | 1.0912 | 0.5160 | 0.5061 | 0.5061 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5089 | 1.0087 | 0.2299 | 0.9229 | -3.1151 | 0.0121 | 0.5052 | 0.5052 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5089 | 1.0116 | 0.2299 | 0.9229 | -3.1151 | 0.0121 | 0.5042 | 0.5042 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4856 | 1.0315 | 0.4460 | 1.1060 | 1.0912 | 0.5160 | 0.5038 | 0.5038 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5089 | 1.0145 | 0.2299 | 0.9229 | -3.1151 | 0.0121 | 0.5032 | 0.5032 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5089 | 1.0177 | 0.2299 | 0.9229 | -3.1151 | 0.0121 | 0.5023 | 0.5023 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4856 | 1.0379 | 0.4460 | 1.1060 | 1.0912 | 0.5160 | 0.5016 | 0.5016 |
| `base|emb=24|sh=0.97` | 18 | 0.4817 | 1.0116 | 1.0000 | 1.0044 | -3.3228 | 0.0319 | 0.5005 | 0.5005 |
| `base|emb=24|sh=0.96` | 18 | 0.4817 | 1.0155 | 1.0000 | 1.0044 | -3.3228 | 0.0319 | 0.4991 | 0.4991 |
| `base|emb=24|sh=0.95` | 18 | 0.4817 | 1.0194 | 1.0000 | 1.0044 | -3.3228 | 0.0319 | 0.4976 | 0.4976 |
| `base|emb=24|sh=0.94` | 18 | 0.4817 | 1.0239 | 1.0000 | 1.0044 | -3.3228 | 0.0319 | 0.4959 | 0.4959 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=344, top_n=35, cutoff=0.7909

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6389 | 0.0357 | 0.9944 | 0.0178 |
| all validations | 0.4828 | 0.0962 | 1.0205 | 0.0304 |

- improvement vs all (primary fraction): `hit +15.61pp, mae +2.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0085 | 0.8056 | 0.7600 | -0.1132 | -10.5917 | -0.6495 | 0.3628 | 0.3628 |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0113 | 0.8056 | 0.7600 | -0.1132 | -10.5917 | -0.6495 | 0.3617 | 0.3617 |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0141 | 0.8056 | 0.7600 | -0.1132 | -10.5917 | -0.6495 | 0.3606 | 0.3606 |
| 4 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0169 | 0.8056 | 0.7600 | -0.1132 | -10.5917 | -0.6495 | 0.3595 | 0.3595 |
| 5 | `base|emb=24|sh=0.97` | 0.4545 | 1.0120 | 1.0000 | 0.7896 | -0.1734 | -16.2324 | -0.7043 | 0.3517 | 0.3517 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.5000 | 1.0100 | 1.1075 | 3.8728 | 0.2432 |
| 1 | 6 | 0.4000 | 1.0864 | 0.7481 | -27.5137 | -0.5097 |
| 2 | 5 | 0.5000 | 0.9956 | 0.3477 | -36.6152 | -1.0246 |
| 3 | 6 | 0.2000 | 1.0527 | 1.1354 | -45.7623 | -1.4397 |
| 4 | 6 | 0.8333 | 0.9199 | 0.9855 | 63.3027 | 3.9802 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.6667 | 0.9867 | 0.5766 | 5.7058 | 0.2517 |
| 1 | 6 | 0.6000 | 1.0039 | 0.7553 | 4.7279 | 0.1048 |
| 2 | 5 | 0.6000 | 0.9765 | 0.5960 | -4.1769 | -0.1906 |
| 3 | 6 | 0.2000 | 1.0572 | 1.8399 | -29.7730 | -0.8240 |
| 4 | 6 | 0.4000 | 1.0122 | 0.5600 | -31.6978 | -0.6402 |

