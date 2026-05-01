# Strict Multi-Cycle Research Result

- symbol: `BIO`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4994 | 1.0078 | 0.2731 | 1.2131 | 5.5412 | 0.8612 | 0.6359 | 0.6359 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5511 | 1.0060 | 0.3488 | 0.9784 | 5.5355 | 1.3132 | 0.6351 | 0.6351 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4994 | 1.0103 | 0.2731 | 1.2131 | 5.5412 | 0.8612 | 0.6349 | 0.6349 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5511 | 1.0080 | 0.3488 | 0.9784 | 5.5355 | 1.3132 | 0.6345 | 0.6345 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5511 | 1.0100 | 0.3488 | 0.9784 | 5.5355 | 1.3132 | 0.6340 | 0.6340 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4994 | 1.0129 | 0.2731 | 1.2131 | 5.5412 | 0.8612 | 0.6340 | 0.6340 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5511 | 1.0120 | 0.3488 | 0.9784 | 5.5355 | 1.3132 | 0.6335 | 0.6335 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4994 | 1.0155 | 0.2731 | 1.2131 | 5.5412 | 0.8612 | 0.6330 | 0.6330 |
| `base|emb=24|sh=0.97` | 18 | 0.5282 | 1.0055 | 1.0000 | 1.0599 | 5.9355 | 1.1561 | 0.6326 | 0.6326 |
| `base|emb=24|sh=0.96` | 18 | 0.5282 | 1.0075 | 1.0000 | 1.0599 | 5.9355 | 1.1561 | 0.6319 | 0.6319 |
| `base|emb=24|sh=0.95` | 18 | 0.5282 | 1.0096 | 1.0000 | 1.0599 | 5.9355 | 1.1561 | 0.6312 | 0.6312 |
| `base|emb=24|sh=0.94` | 18 | 0.5282 | 1.0119 | 1.0000 | 1.0599 | 5.9355 | 1.1561 | 0.6304 | 0.6304 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4774 | 1.0151 | 0.3040 | 1.3065 | 2.4291 | 1.6255 | 0.6090 | 0.6090 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4774 | 1.0202 | 0.3040 | 1.3065 | 2.4291 | 1.6255 | 0.6071 | 0.6071 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4774 | 1.0252 | 0.3040 | 1.3065 | 2.4291 | 1.6255 | 0.6053 | 0.6053 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4774 | 1.0302 | 0.3040 | 1.3065 | 2.4291 | 1.6255 | 0.6034 | 0.6034 |
| `base|emb=12|sh=0.97` | 18 | 0.5151 | 1.0069 | 1.0000 | 1.0433 | 3.2096 | 0.4959 | 0.5967 | 0.5967 |
| `base|emb=12|sh=0.96` | 18 | 0.5151 | 1.0095 | 1.0000 | 1.0433 | 3.2096 | 0.4959 | 0.5958 | 0.5958 |
| `base|emb=12|sh=0.95` | 18 | 0.5151 | 1.0123 | 1.0000 | 1.0433 | 3.2096 | 0.4959 | 0.5948 | 0.5948 |
| `base|emb=12|sh=0.94` | 18 | 0.5151 | 1.0153 | 1.0000 | 1.0433 | 3.2096 | 0.4959 | 0.5937 | 0.5937 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=336, top_n=34, cutoff=0.8176

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6664 | 0.0667 | 0.9986 | 0.0095 |
| all validations | 0.5128 | 0.1238 | 1.0136 | 0.0299 |

- improvement vs all (primary fraction): `hit +15.36pp, mae +1.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6250 | 0.9715 | 0.6667 | 0.4927 | -0.0728 | -6.8167 | -0.4582 | 0.3991 | 0.3991 |
| 4 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6250 | 0.9726 | 0.6667 | 0.4927 | -0.0728 | -6.8167 | -0.4582 | 0.3987 | 0.3987 |
| 5 | `base|emb=24|sh=0.97` | 0.6176 | 0.9814 | 1.0000 | 0.4975 | -0.0800 | -7.4867 | -0.4095 | 0.3942 | 0.3942 |
