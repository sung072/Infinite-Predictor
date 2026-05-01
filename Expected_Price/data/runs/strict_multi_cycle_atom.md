# Strict Multi-Cycle Research Result

- symbol: `ATOM`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5961 | 0.9590 | 0.2840 | 0.7101 | 1.8177 | 0.0636 | 0.6060 | 0.6060 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5961 | 0.9627 | 0.2840 | 0.7101 | 1.8177 | 0.0636 | 0.6040 | 0.6040 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5961 | 0.9670 | 0.2840 | 0.7101 | 1.8177 | 0.0636 | 0.6019 | 0.6019 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5961 | 0.9732 | 0.2840 | 0.7101 | 1.8177 | 0.0636 | 0.5991 | 0.5991 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5535 | 0.9830 | 0.3009 | 0.7595 | -4.6549 | 0.0270 | 0.5450 | 0.5450 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5535 | 0.9842 | 0.3009 | 0.7595 | -4.6549 | 0.0270 | 0.5449 | 0.5449 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5535 | 0.9827 | 0.3009 | 0.7595 | -4.6549 | 0.0270 | 0.5448 | 0.5448 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5535 | 0.9848 | 0.3009 | 0.7595 | -4.6549 | 0.0270 | 0.5437 | 0.5437 |
| `base|emb=12|sh=0.96` | 18 | 0.5024 | 0.9966 | 1.0000 | 1.0999 | -0.0493 | 0.8960 | 0.5350 | 0.5350 |
| `base|emb=12|sh=0.97` | 18 | 0.5024 | 0.9968 | 1.0000 | 1.0999 | -0.0493 | 0.8960 | 0.5349 | 0.5349 |
| `base|emb=12|sh=0.95` | 18 | 0.5024 | 0.9973 | 1.0000 | 1.0999 | -0.0493 | 0.8960 | 0.5348 | 0.5348 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4797 | 1.0059 | 0.4738 | 1.3647 | -1.2102 | 1.6116 | 0.5348 | 0.5348 |
| `base|emb=12|sh=0.94` | 18 | 0.5024 | 0.9985 | 1.0000 | 1.0999 | -0.0493 | 0.8960 | 0.5344 | 0.5344 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4797 | 1.0078 | 0.4738 | 1.3647 | -1.2102 | 1.6116 | 0.5341 | 0.5341 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4797 | 1.0098 | 0.4738 | 1.3647 | -1.2102 | 1.6116 | 0.5334 | 0.5334 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4797 | 1.0120 | 0.4738 | 1.3647 | -1.2102 | 1.6116 | 0.5327 | 0.5327 |
| `base|emb=24|sh=0.96` | 18 | 0.5126 | 0.9966 | 1.0000 | 1.0213 | -0.6294 | 0.9628 | 0.5270 | 0.5270 |
| `base|emb=24|sh=0.97` | 18 | 0.5126 | 0.9969 | 1.0000 | 1.0213 | -0.6294 | 0.9628 | 0.5268 | 0.5268 |
| `base|emb=24|sh=0.95` | 18 | 0.5126 | 0.9974 | 1.0000 | 1.0213 | -0.6294 | 0.9628 | 0.5267 | 0.5267 |
| `base|emb=24|sh=0.94` | 18 | 0.5126 | 0.9986 | 1.0000 | 1.0213 | -0.6294 | 0.9628 | 0.5262 | 0.5262 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=384, top_n=39, cutoff=0.8201

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6720 | 0.0737 | 0.9789 | 0.0337 |
| all validations | 0.5119 | 0.1243 | 0.9950 | 0.0312 |

- improvement vs all (primary fraction): `hit +16.01pp, mae +1.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5263 | 0.9664 | 0.5278 | 0.8133 | -0.0390 | -3.6481 | -0.1906 | 0.4268 | 0.4268 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5263 | 0.9720 | 0.5278 | 0.8133 | -0.0390 | -3.6481 | -0.1906 | 0.4244 | 0.4244 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5263 | 0.9776 | 0.5278 | 0.8133 | -0.0390 | -3.6481 | -0.1906 | 0.4220 | 0.4220 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5263 | 0.9832 | 0.5278 | 0.8133 | -0.0390 | -3.6481 | -0.1906 | 0.4197 | 0.4197 |
| 5 | `base|emb=12|sh=0.96` | 0.4848 | 1.0011 | 1.0000 | 0.7650 | -0.1346 | -12.5993 | -0.6287 | 0.3634 | 0.3634 |
