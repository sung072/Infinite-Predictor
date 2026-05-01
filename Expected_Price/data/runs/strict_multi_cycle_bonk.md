# Strict Multi-Cycle Research Result

- symbol: `BONK`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6662 | 0.9929 | 0.3040 | 1.0409 | 35.5935 | 1.2418 | 0.6985 | 0.6985 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6079 | 0.9857 | 0.3040 | 1.2298 | 12.7848 | 2.4093 | 0.6548 | 0.6548 |
| `base|emb=12|sh=0.97` | 18 | 0.5875 | 0.9990 | 1.0000 | 0.9836 | 12.3832 | 1.1116 | 0.6474 | 0.6474 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5944 | 0.9881 | 0.3040 | 1.2376 | 10.3852 | 1.9697 | 0.6391 | 0.6391 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5490 | 1.0311 | 0.3133 | 1.2857 | 12.6109 | 2.7217 | 0.6389 | 0.6389 |
| `base|emb=24|sh=0.97` | 18 | 0.5617 | 1.0013 | 1.0000 | 0.9426 | 6.8788 | 0.7544 | 0.6365 | 0.6365 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5869 | 0.9905 | 0.3040 | 1.1563 | 7.1955 | 1.3682 | 0.6235 | 0.6235 |
| `base|emb=24|sh=0.94` | 18 | 0.5549 | 1.0039 | 1.0000 | 0.9338 | 5.3765 | 0.7837 | 0.6218 | 0.6218 |
| `base|emb=12|sh=0.94` | 18 | 0.5769 | 0.9995 | 1.0000 | 0.9924 | 9.5937 | 1.1402 | 0.6197 | 0.6197 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5453 | 1.0218 | 0.3133 | 1.2859 | 12.0340 | 2.7039 | 0.6194 | 0.6194 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5507 | 1.0166 | 0.3133 | 1.2822 | 12.6499 | 2.7304 | 0.6186 | 0.6186 |
| `base|emb=24|sh=0.95` | 18 | 0.5472 | 1.0023 | 1.0000 | 0.9508 | 4.8359 | 0.6653 | 0.6130 | 0.6130 |
| `base|emb=12|sh=0.95` | 18 | 0.5677 | 0.9986 | 1.0000 | 1.0049 | 8.7512 | 1.0125 | 0.6114 | 0.6114 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5336 | 1.0124 | 0.3133 | 1.2317 | 8.2493 | 2.2080 | 0.6058 | 0.6058 |
| `base|emb=24|sh=0.96` | 18 | 0.5450 | 1.0017 | 1.0000 | 0.9163 | 2.9910 | 0.4172 | 0.6040 | 0.6040 |
| `base|emb=12|sh=0.96` | 18 | 0.5680 | 0.9987 | 1.0000 | 0.9531 | 6.9966 | 0.7787 | 0.5942 | 0.5942 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5697 | 0.9985 | 0.2886 | 0.9626 | 11.6277 | 0.5967 | 0.5842 | 0.5842 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5081 | 1.0278 | 0.3503 | 1.3424 | 5.0621 | 2.0152 | 0.5626 | 0.5626 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5024 | 1.0159 | 0.3503 | 1.3349 | 3.9488 | 1.9862 | 0.5625 | 0.5625 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5014 | 1.0202 | 0.3503 | 1.3373 | 3.9528 | 1.9834 | 0.5621 | 0.5621 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8592

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7050 | 0.0850 | 0.9675 | 0.0226 |
| all validations | 0.5544 | 0.1429 | 1.0040 | 0.0440 |

- improvement vs all (primary fraction): `hit +15.06pp, mae +3.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6818 | 0.9759 | 0.7222 | 0.7623 | 0.1975 | 18.4843 | 1.0376 | 0.7668 | 0.7668 |
| 5 | `base|emb=12|sh=0.97` | 0.6538 | 0.9880 | 1.0000 | 0.6815 | 0.0965 | 9.0356 | 0.6109 | 0.7385 | 0.7385 |
