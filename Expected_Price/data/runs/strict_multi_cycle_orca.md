# Strict Multi-Cycle Research Result

- symbol: `ORCA`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5747 | 0.9963 | 0.3596 | 0.9379 | 9.0658 | 1.8457 | 0.5898 | 0.5898 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5747 | 0.9978 | 0.3596 | 0.9379 | 9.0658 | 1.8457 | 0.5897 | 0.5897 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5747 | 0.9998 | 0.3596 | 0.9379 | 9.0658 | 1.8457 | 0.5895 | 0.5895 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5747 | 0.9970 | 0.3596 | 0.9379 | 9.0658 | 1.8457 | 0.5889 | 0.5889 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5097 | 1.0067 | 0.4367 | 1.1336 | 3.9817 | 0.9255 | 0.5842 | 0.5842 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5097 | 1.0090 | 0.4367 | 1.1336 | 3.9817 | 0.9255 | 0.5833 | 0.5833 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5097 | 1.0112 | 0.4367 | 1.1336 | 3.9817 | 0.9255 | 0.5825 | 0.5825 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5097 | 1.0134 | 0.4367 | 1.1336 | 3.9817 | 0.9255 | 0.5817 | 0.5817 |
| `base|emb=12|sh=0.97` | 18 | 0.5005 | 1.0078 | 1.0000 | 1.1284 | 2.7952 | 1.5335 | 0.5506 | 0.5506 |
| `base|emb=12|sh=0.96` | 18 | 0.5005 | 1.0105 | 1.0000 | 1.1284 | 2.7952 | 1.5335 | 0.5496 | 0.5496 |
| `base|emb=12|sh=0.95` | 18 | 0.5005 | 1.0134 | 1.0000 | 1.1284 | 2.7952 | 1.5335 | 0.5485 | 0.5485 |
| `base|emb=12|sh=0.94` | 18 | 0.5005 | 1.0165 | 1.0000 | 1.1284 | 2.7952 | 1.5335 | 0.5474 | 0.5474 |
| `base|emb=24|sh=0.97` | 18 | 0.4911 | 1.0081 | 1.0000 | 1.0471 | -0.4987 | 0.5807 | 0.5292 | 0.5292 |
| `base|emb=24|sh=0.96` | 18 | 0.4911 | 1.0109 | 1.0000 | 1.0471 | -0.4987 | 0.5807 | 0.5282 | 0.5282 |
| `base|emb=24|sh=0.95` | 18 | 0.4911 | 1.0139 | 1.0000 | 1.0471 | -0.4987 | 0.5807 | 0.5271 | 0.5271 |
| `base|emb=24|sh=0.94` | 18 | 0.4911 | 1.0171 | 1.0000 | 1.0471 | -0.4987 | 0.5807 | 0.5259 | 0.5259 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4466 | 1.0129 | 0.4398 | 0.9775 | -17.1675 | 0.5521 | 0.5201 | 0.5201 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4466 | 1.0172 | 0.4398 | 0.9775 | -17.1675 | 0.5521 | 0.5185 | 0.5185 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4466 | 1.0214 | 0.4398 | 0.9775 | -17.1675 | 0.5521 | 0.5171 | 0.5171 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4466 | 1.0257 | 0.4398 | 0.9775 | -17.1675 | 0.5521 | 0.5156 | 0.5156 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8384

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7162 | 0.0961 | 0.9726 | 0.0450 |
| all validations | 0.5062 | 0.1399 | 1.0123 | 0.0369 |

- improvement vs all (primary fraction): `hit +21.00pp, mae +3.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.5588 | 1.0040 | 1.0000 | 1.9182 | 0.2800 | 26.2059 | 3.7719 | 0.8299 | 0.8299 |
