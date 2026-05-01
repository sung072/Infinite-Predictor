# Strict Multi-Cycle Research Result

- symbol: `AXS`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5685 | 0.9891 | 0.2917 | 1.3244 | 18.4383 | 2.4296 | 0.7238 | 0.7238 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5685 | 0.9897 | 0.2917 | 1.3244 | 18.4383 | 2.4296 | 0.7237 | 0.7237 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5685 | 0.9898 | 0.2917 | 1.3244 | 18.4383 | 2.4296 | 0.7234 | 0.7234 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5685 | 0.9918 | 0.2917 | 1.3244 | 18.4383 | 2.4296 | 0.7224 | 0.7224 |
| `base|emb=24|sh=0.95` | 18 | 0.5347 | 0.9978 | 1.0000 | 1.1362 | 8.3077 | 0.9768 | 0.6875 | 0.6875 |
| `base|emb=24|sh=0.96` | 18 | 0.5347 | 0.9978 | 1.0000 | 1.1362 | 8.3077 | 0.9768 | 0.6874 | 0.6874 |
| `base|emb=24|sh=0.94` | 18 | 0.5347 | 0.9986 | 1.0000 | 1.1362 | 8.3077 | 0.9768 | 0.6872 | 0.6872 |
| `base|emb=24|sh=0.97` | 18 | 0.5347 | 0.9983 | 1.0000 | 1.1362 | 8.3077 | 0.9768 | 0.6871 | 0.6871 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5919 | 0.9851 | 0.2809 | 1.2170 | 16.6199 | 2.9805 | 0.6499 | 0.6499 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5919 | 0.9858 | 0.2809 | 1.2170 | 16.6199 | 2.9805 | 0.6495 | 0.6495 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5919 | 0.9873 | 0.2809 | 1.2170 | 16.6199 | 2.9805 | 0.6493 | 0.6493 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5919 | 0.9891 | 0.2809 | 1.2170 | 16.6199 | 2.9805 | 0.6480 | 0.6480 |
| `base|emb=12|sh=0.96` | 18 | 0.5314 | 0.9991 | 1.0000 | 1.0740 | 6.1813 | 0.7513 | 0.6361 | 0.6361 |
| `base|emb=12|sh=0.95` | 18 | 0.5314 | 0.9992 | 1.0000 | 1.0740 | 6.1813 | 0.7513 | 0.6361 | 0.6361 |
| `base|emb=12|sh=0.97` | 18 | 0.5314 | 0.9992 | 1.0000 | 1.0740 | 6.1813 | 0.7513 | 0.6360 | 0.6360 |
| `base|emb=12|sh=0.94` | 18 | 0.5314 | 1.0001 | 1.0000 | 1.0740 | 6.1813 | 0.7513 | 0.6358 | 0.6358 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4780 | 1.0003 | 0.3611 | 1.1441 | -11.1778 | 1.1025 | 0.5649 | 0.5649 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4780 | 1.0002 | 0.3611 | 1.1441 | -11.1778 | 1.1025 | 0.5647 | 0.5647 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4780 | 1.0002 | 0.3611 | 1.1441 | -11.1778 | 1.1025 | 0.5645 | 0.5645 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4780 | 1.0001 | 0.3611 | 1.1441 | -11.1778 | 1.1025 | 0.5644 | 0.5644 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8579

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7127 | 0.0639 | 0.9771 | 0.0254 |
| all validations | 0.5229 | 0.1420 | 0.9977 | 0.0290 |

- improvement vs all (primary fraction): `hit +18.99pp, mae +2.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5625 | 0.9719 | 0.5000 | 0.6199 | -0.0872 | -8.1595 | -0.5743 | 0.3870 | 0.3870 |
| 2 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5625 | 0.9721 | 0.5000 | 0.6199 | -0.0872 | -8.1595 | -0.5743 | 0.3869 | 0.3869 |
| 3 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5625 | 0.9791 | 0.5000 | 0.6199 | -0.0872 | -8.1595 | -0.5743 | 0.3840 | 0.3840 |
| 4 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5625 | 0.9809 | 0.5000 | 0.6199 | -0.0872 | -8.1595 | -0.5743 | 0.3832 | 0.3832 |
| 5 | `base|emb=24|sh=0.95` | 0.4706 | 1.0152 | 1.0000 | 0.5151 | -0.2965 | -27.7482 | -1.1967 | 0.3257 | 0.3257 |
