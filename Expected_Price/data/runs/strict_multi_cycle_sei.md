# Strict Multi-Cycle Research Result

- symbol: `SEI`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5207 | 0.9991 | 0.3441 | 1.2366 | 6.0297 | 0.5175 | 0.5907 | 0.5907 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5207 | 0.9998 | 0.3441 | 1.2366 | 6.0297 | 0.5175 | 0.5905 | 0.5905 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5207 | 1.0030 | 0.3441 | 1.2366 | 6.0297 | 0.5175 | 0.5895 | 0.5895 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5207 | 1.0095 | 0.3441 | 1.2366 | 6.0297 | 0.5175 | 0.5873 | 0.5873 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5381 | 1.0071 | 0.3580 | 1.0312 | 2.2328 | 0.5923 | 0.5644 | 0.5644 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5381 | 1.0112 | 0.3580 | 1.0312 | 2.2328 | 0.5923 | 0.5633 | 0.5633 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5381 | 1.0181 | 0.3580 | 1.0312 | 2.2328 | 0.5923 | 0.5613 | 0.5613 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5381 | 1.0283 | 0.3580 | 1.0312 | 2.2328 | 0.5923 | 0.5583 | 0.5583 |
| `base|emb=24|sh=0.97` | 18 | 0.5093 | 1.0003 | 1.0000 | 0.9746 | -1.8691 | 0.1129 | 0.5479 | 0.5479 |
| `base|emb=24|sh=0.96` | 18 | 0.5093 | 1.0011 | 1.0000 | 0.9746 | -1.8691 | 0.1129 | 0.5477 | 0.5477 |
| `base|emb=24|sh=0.95` | 18 | 0.5093 | 1.0026 | 1.0000 | 0.9746 | -1.8691 | 0.1129 | 0.5471 | 0.5471 |
| `base|emb=24|sh=0.94` | 18 | 0.5093 | 1.0053 | 1.0000 | 0.9746 | -1.8691 | 0.1129 | 0.5461 | 0.5461 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4148 | 1.0168 | 0.3951 | 1.1248 | -14.7531 | 0.1447 | 0.4820 | 0.4820 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4148 | 1.0225 | 0.3951 | 1.1248 | -14.7531 | 0.1447 | 0.4799 | 0.4799 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4148 | 1.0281 | 0.3951 | 1.1248 | -14.7531 | 0.1447 | 0.4779 | 0.4779 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4148 | 1.0337 | 0.3951 | 1.1248 | -14.7531 | 0.1447 | 0.4760 | 0.4760 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4363 | 1.0153 | 0.3796 | 1.0048 | -19.4618 | -0.0328 | 0.4647 | 0.4647 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4363 | 1.0204 | 0.3796 | 1.0048 | -19.4618 | -0.0328 | 0.4629 | 0.4629 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4363 | 1.0255 | 0.3796 | 1.0048 | -19.4618 | -0.0328 | 0.4612 | 0.4612 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4363 | 1.0306 | 0.3796 | 1.0048 | -19.4618 | -0.0328 | 0.4595 | 0.4595 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.7839

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6151 | 0.0857 | 0.9939 | 0.0397 |
| all validations | 0.4875 | 0.1258 | 1.0118 | 0.0385 |

- improvement vs all (primary fraction): `hit +12.76pp, mae +1.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5625 | 0.9704 | 0.4722 | 0.9743 | 0.0910 | 8.5148 | 0.4204 | 0.7347 | 0.7347 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5625 | 0.9754 | 0.4722 | 0.9743 | 0.0910 | 8.5148 | 0.4204 | 0.7326 | 0.7326 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5625 | 0.9803 | 0.4722 | 0.9743 | 0.0910 | 8.5148 | 0.4204 | 0.7305 | 0.7305 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5625 | 0.9852 | 0.4722 | 0.9743 | 0.0910 | 8.5148 | 0.4204 | 0.7285 | 0.7285 |
| 5 | `base|emb=24|sh=0.97` | 0.4412 | 1.0085 | 1.0000 | 0.8685 | -0.1560 | -14.5972 | -0.6416 | 0.3561 | 0.3561 |
