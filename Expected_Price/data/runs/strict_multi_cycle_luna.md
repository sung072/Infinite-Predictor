# Strict Multi-Cycle Research Result

- symbol: `LUNA`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4920 | 1.0030 | 0.2469 | 1.2958 | 3.8432 | 0.7630 | 0.5807 | 0.5807 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4920 | 1.0041 | 0.2469 | 1.2958 | 3.8432 | 0.7630 | 0.5806 | 0.5806 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4920 | 1.0087 | 0.2469 | 1.2958 | 3.8432 | 0.7630 | 0.5791 | 0.5791 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4920 | 1.0155 | 0.2469 | 1.2958 | 3.8432 | 0.7630 | 0.5769 | 0.5769 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4875 | 1.0079 | 0.4228 | 1.0987 | -0.1650 | 0.8957 | 0.5503 | 0.5503 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4875 | 1.0105 | 0.4228 | 1.0987 | -0.1650 | 0.8957 | 0.5494 | 0.5494 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4875 | 1.0131 | 0.4228 | 1.0987 | -0.1650 | 0.8957 | 0.5484 | 0.5484 |
| `base|emb=12|sh=0.97` | 18 | 0.4935 | 1.0101 | 1.0000 | 1.0348 | -0.2672 | 0.2713 | 0.5483 | 0.5483 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4875 | 1.0157 | 0.4228 | 1.0987 | -0.1650 | 0.8957 | 0.5475 | 0.5475 |
| `base|emb=12|sh=0.96` | 18 | 0.4935 | 1.0135 | 1.0000 | 1.0348 | -0.2672 | 0.2713 | 0.5471 | 0.5471 |
| `base|emb=12|sh=0.95` | 18 | 0.4935 | 1.0176 | 1.0000 | 1.0348 | -0.2672 | 0.2713 | 0.5456 | 0.5456 |
| `base|emb=12|sh=0.94` | 18 | 0.4935 | 1.0222 | 1.0000 | 1.0348 | -0.2672 | 0.2713 | 0.5439 | 0.5439 |
| `base|emb=24|sh=0.97` | 18 | 0.4752 | 1.0107 | 1.0000 | 1.1323 | -0.0916 | 0.4686 | 0.5414 | 0.5414 |
| `base|emb=24|sh=0.96` | 18 | 0.4752 | 1.0143 | 1.0000 | 1.1323 | -0.0916 | 0.4686 | 0.5401 | 0.5401 |
| `base|emb=24|sh=0.95` | 18 | 0.4752 | 1.0186 | 1.0000 | 1.1323 | -0.0916 | 0.4686 | 0.5385 | 0.5385 |
| `base|emb=24|sh=0.94` | 18 | 0.4752 | 1.0233 | 1.0000 | 1.1323 | -0.0916 | 0.4686 | 0.5369 | 0.5369 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.3977 | 1.0196 | 0.2160 | 1.4484 | -10.5376 | 0.3535 | 0.4819 | 0.4819 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.3977 | 1.0262 | 0.2160 | 1.4484 | -10.5376 | 0.3535 | 0.4799 | 0.4799 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.3977 | 1.0349 | 0.2160 | 1.4484 | -10.5376 | 0.3535 | 0.4774 | 0.4774 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.3977 | 1.0446 | 0.2160 | 1.4484 | -10.5376 | 0.3535 | 0.4747 | 0.4747 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=344, top_n=35, cutoff=0.7914

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6380 | 0.0665 | 0.9809 | 0.0362 |
| all validations | 0.4761 | 0.1280 | 1.0162 | 0.0390 |

- improvement vs all (primary fraction): `hit +16.19pp, mae +3.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.5000 | 0.9976 | 1.0000 | 0.8823 | -0.0457 | -4.2740 | -0.3578 | 0.3984 | 0.3984 |
