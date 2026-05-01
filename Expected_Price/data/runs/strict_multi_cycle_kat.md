# Strict Multi-Cycle Research Result

- symbol: `KAT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `base|emb=12|sh=0.94` | 18 | 0.5578 | 0.9886 | 1.0000 | 0.9854 | 8.7248 | 1.3628 | 0.6732 | 0.6732 |
| `base|emb=12|sh=0.95` | 18 | 0.5578 | 0.9901 | 1.0000 | 0.9854 | 8.7248 | 1.3628 | 0.6725 | 0.6725 |
| `base|emb=12|sh=0.96` | 18 | 0.5578 | 0.9915 | 1.0000 | 0.9854 | 8.7248 | 1.3628 | 0.6719 | 0.6719 |
| `base|emb=12|sh=0.97` | 18 | 0.5578 | 0.9935 | 1.0000 | 0.9854 | 8.7248 | 1.3628 | 0.6711 | 0.6711 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5630 | 0.9836 | 0.3580 | 1.4396 | 16.1830 | 3.4816 | 0.6696 | 0.6696 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5630 | 0.9853 | 0.3580 | 1.4396 | 16.1830 | 3.4816 | 0.6685 | 0.6685 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5630 | 0.9870 | 0.3580 | 1.4396 | 16.1830 | 3.4816 | 0.6674 | 0.6674 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5630 | 0.9902 | 0.3580 | 1.4396 | 16.1830 | 3.4816 | 0.6659 | 0.6659 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5261 | 0.9897 | 0.3920 | 1.3555 | 9.0069 | 1.8612 | 0.6110 | 0.6110 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5261 | 0.9907 | 0.3920 | 1.3555 | 9.0069 | 1.8612 | 0.6104 | 0.6104 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5261 | 0.9917 | 0.3920 | 1.3555 | 9.0069 | 1.8612 | 0.6098 | 0.6098 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5261 | 0.9938 | 0.3920 | 1.3555 | 9.0069 | 1.8612 | 0.6088 | 0.6088 |
| `base|emb=24|sh=0.94` | 18 | 0.5258 | 0.9958 | 1.0000 | 1.0235 | 4.4799 | 0.7855 | 0.6004 | 0.6004 |
| `base|emb=24|sh=0.95` | 18 | 0.5258 | 0.9960 | 1.0000 | 1.0235 | 4.4799 | 0.7855 | 0.6003 | 0.6003 |
| `base|emb=24|sh=0.96` | 18 | 0.5258 | 0.9963 | 1.0000 | 1.0235 | 4.4799 | 0.7855 | 0.6001 | 0.6001 |
| `base|emb=24|sh=0.97` | 18 | 0.5258 | 0.9970 | 1.0000 | 1.0235 | 4.4799 | 0.7855 | 0.5998 | 0.5998 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5025 | 1.0004 | 0.4321 | 0.9149 | -1.7146 | 1.0205 | 0.5711 | 0.5711 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5025 | 1.0006 | 0.4321 | 0.9149 | -1.7146 | 1.0205 | 0.5710 | 0.5710 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5025 | 1.0007 | 0.4321 | 0.9149 | -1.7146 | 1.0205 | 0.5710 | 0.5710 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5025 | 1.0008 | 0.4321 | 0.9149 | -1.7146 | 1.0205 | 0.5710 | 0.5710 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8406

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7328 | 0.1168 | 0.9593 | 0.0394 |
| all validations | 0.5270 | 0.1368 | 0.9953 | 0.0236 |

- improvement vs all (primary fraction): `hit +20.58pp, mae +3.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `base|emb=12|sh=0.97` | 0.3824 | 1.0092 | 1.0000 | 1.4019 | -0.0537 | -5.0281 | -0.4376 | 0.3839 | 0.3839 |
| 3 | `base|emb=12|sh=0.96` | 0.3824 | 1.0163 | 1.0000 | 1.4019 | -0.0537 | -5.0281 | -0.4376 | 0.3811 | 0.3811 |
| 4 | `base|emb=12|sh=0.95` | 0.3824 | 1.0266 | 1.0000 | 1.4019 | -0.0537 | -5.0281 | -0.4376 | 0.3772 | 0.3772 |
| 5 | `base|emb=12|sh=0.94` | 0.3824 | 1.0368 | 1.0000 | 1.4019 | -0.0537 | -5.0281 | -0.4376 | 0.3733 | 0.3733 |
