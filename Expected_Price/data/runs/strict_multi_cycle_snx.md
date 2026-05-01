# Strict Multi-Cycle Research Result

- symbol: `SNX`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5070 | 1.0167 | 0.3272 | 1.4550 | 9.2673 | 1.3327 | 0.6578 | 0.6578 |
| `base|emb=12|sh=0.97` | 18 | 0.5248 | 1.0134 | 1.0000 | 1.1118 | 6.8113 | 0.8709 | 0.6573 | 0.6573 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5070 | 1.0222 | 0.3272 | 1.4550 | 9.2673 | 1.3327 | 0.6558 | 0.6558 |
| `base|emb=12|sh=0.96` | 18 | 0.5248 | 1.0178 | 1.0000 | 1.1118 | 6.8113 | 0.8709 | 0.6556 | 0.6556 |
| `base|emb=12|sh=0.95` | 18 | 0.5248 | 1.0223 | 1.0000 | 1.1118 | 6.8113 | 0.8709 | 0.6540 | 0.6540 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5070 | 1.0278 | 0.3272 | 1.4550 | 9.2673 | 1.3327 | 0.6538 | 0.6538 |
| `base|emb=12|sh=0.94` | 18 | 0.5248 | 1.0267 | 1.0000 | 1.1118 | 6.8113 | 0.8709 | 0.6524 | 0.6524 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5070 | 1.0333 | 0.3272 | 1.4550 | 9.2673 | 1.3327 | 0.6519 | 0.6519 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4881 | 1.0187 | 0.3457 | 1.6555 | 9.8826 | 1.7955 | 0.6457 | 0.6457 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4881 | 1.0249 | 0.3457 | 1.6555 | 9.8826 | 1.7955 | 0.6435 | 0.6435 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4881 | 1.0311 | 0.3457 | 1.6555 | 9.8826 | 1.7955 | 0.6413 | 0.6413 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4881 | 1.0373 | 0.3457 | 1.6555 | 9.8826 | 1.7955 | 0.6392 | 0.6392 |
| `base|emb=24|sh=0.97` | 18 | 0.5111 | 1.0152 | 1.0000 | 1.0714 | 3.2097 | 0.5948 | 0.6004 | 0.6004 |
| `base|emb=24|sh=0.96` | 18 | 0.5111 | 1.0203 | 1.0000 | 1.0714 | 3.2097 | 0.5948 | 0.5985 | 0.5985 |
| `base|emb=24|sh=0.95` | 18 | 0.5111 | 1.0253 | 1.0000 | 1.0714 | 3.2097 | 0.5948 | 0.5967 | 0.5967 |
| `base|emb=24|sh=0.94` | 18 | 0.5111 | 1.0304 | 1.0000 | 1.0714 | 3.2097 | 0.5948 | 0.5950 | 0.5950 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5313 | 1.0092 | 0.3627 | 1.3371 | 11.3533 | 0.9527 | 0.5793 | 0.5793 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5313 | 1.0123 | 0.3627 | 1.3371 | 11.3533 | 0.9527 | 0.5781 | 0.5781 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5313 | 1.0154 | 0.3627 | 1.3371 | 11.3533 | 0.9527 | 0.5771 | 0.5771 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5313 | 1.0185 | 0.3627 | 1.3371 | 11.3533 | 0.9527 | 0.5760 | 0.5760 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=360, top_n=36, cutoff=0.8324

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6307 | 0.0931 | 0.9983 | 0.0149 |
| all validations | 0.5065 | 0.1419 | 1.0224 | 0.0335 |

- improvement vs all (primary fraction): `hit +12.43pp, mae +2.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.8000 | 0.9545 | 0.1667 | 0.6639 | 0.4258 | 39.8541 | 1.6544 | 0.8119 | 0.8119 |
| 2 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.8000 | 0.9659 | 0.1667 | 0.6639 | 0.4258 | 39.8541 | 1.6544 | 0.8069 | 0.8069 |
| 3 | `base|emb=12|sh=0.97` | 0.4615 | 1.0077 | 1.0000 | 1.0237 | -0.0562 | -5.2613 | -0.3764 | 0.3848 | 0.3848 |
| 4 | `base|emb=12|sh=0.96` | 0.4615 | 1.0103 | 1.0000 | 1.0237 | -0.0562 | -5.2613 | -0.3764 | 0.3838 | 0.3838 |
| 5 | `base|emb=12|sh=0.95` | 0.4615 | 1.0129 | 1.0000 | 1.0237 | -0.0562 | -5.2613 | -0.3764 | 0.3828 | 0.3828 |
