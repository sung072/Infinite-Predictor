# Strict Multi-Cycle Research Result

- symbol: `EDU`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4491 | 1.0238 | 0.3133 | 1.2515 | -3.2824 | 0.1313 | 0.5622 | 0.5622 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4491 | 1.0395 | 0.3133 | 1.2515 | -3.2824 | 0.1313 | 0.5580 | 0.5580 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4491 | 1.0557 | 0.3133 | 1.2515 | -3.2824 | 0.1313 | 0.5543 | 0.5543 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4491 | 1.0722 | 0.3133 | 1.2515 | -3.2824 | 0.1313 | 0.5511 | 0.5511 |
| `base|emb=12|sh=0.97` | 18 | 0.4659 | 1.0092 | 1.0000 | 1.0802 | -2.6318 | -0.0214 | 0.5313 | 0.5313 |
| `base|emb=12|sh=0.96` | 18 | 0.4659 | 1.0139 | 1.0000 | 1.0802 | -2.6318 | -0.0214 | 0.5296 | 0.5296 |
| `base|emb=12|sh=0.95` | 18 | 0.4659 | 1.0190 | 1.0000 | 1.0802 | -2.6318 | -0.0214 | 0.5278 | 0.5278 |
| `base|emb=12|sh=0.94` | 18 | 0.4659 | 1.0245 | 1.0000 | 1.0802 | -2.6318 | -0.0214 | 0.5259 | 0.5259 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4419 | 1.0102 | 0.4136 | 1.1382 | -5.5543 | 0.2557 | 0.5149 | 0.5149 |
| `base|emb=24|sh=0.97` | 18 | 0.4632 | 1.0102 | 1.0000 | 1.0634 | -3.8101 | 0.0593 | 0.5137 | 0.5137 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4419 | 1.0136 | 0.4136 | 1.1382 | -5.5543 | 0.2557 | 0.5137 | 0.5137 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4419 | 1.0169 | 0.4136 | 1.1382 | -5.5543 | 0.2557 | 0.5125 | 0.5125 |
| `base|emb=24|sh=0.96` | 18 | 0.4632 | 1.0152 | 1.0000 | 1.0634 | -3.8101 | 0.0593 | 0.5118 | 0.5118 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4419 | 1.0203 | 0.4136 | 1.1382 | -5.5543 | 0.2557 | 0.5114 | 0.5114 |
| `base|emb=24|sh=0.95` | 18 | 0.4632 | 1.0210 | 1.0000 | 1.0634 | -3.8101 | 0.0593 | 0.5098 | 0.5098 |
| `base|emb=24|sh=0.94` | 18 | 0.4632 | 1.0273 | 1.0000 | 1.0634 | -3.8101 | 0.0593 | 0.5076 | 0.5076 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4410 | 1.0215 | 0.2485 | 1.1660 | -7.8778 | 0.0087 | 0.5009 | 0.5009 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4410 | 1.0323 | 0.2485 | 1.1660 | -7.8778 | 0.0087 | 0.4973 | 0.4973 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4410 | 1.0444 | 0.2485 | 1.1660 | -7.8778 | 0.0087 | 0.4935 | 0.4935 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4284 | 1.0130 | 0.4506 | 1.0045 | -11.9645 | 0.1783 | 0.4913 | 0.4913 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.7728

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5764 | 0.0523 | 0.9945 | 0.0102 |
| all validations | 0.4499 | 0.0903 | 1.0248 | 0.0637 |

- improvement vs all (primary fraction): `hit +12.65pp, mae +3.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3636 | 1.0065 | 0.3611 | 1.1969 | -0.1636 | -15.3155 | -0.5213 | 0.3598 | 0.3598 |
| 2 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3636 | 1.0087 | 0.3611 | 1.1969 | -0.1636 | -15.3155 | -0.5213 | 0.3590 | 0.3590 |
| 3 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3636 | 1.0108 | 0.3611 | 1.1969 | -0.1636 | -15.3155 | -0.5213 | 0.3581 | 0.3581 |
| 4 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3636 | 1.0130 | 0.3611 | 1.1969 | -0.1636 | -15.3155 | -0.5213 | 0.3573 | 0.3573 |
| 5 | `base|emb=12|sh=0.97` | 0.4194 | 1.0045 | 1.0000 | 0.9388 | -0.1643 | -15.3776 | -0.9650 | 0.3464 | 0.3464 |
