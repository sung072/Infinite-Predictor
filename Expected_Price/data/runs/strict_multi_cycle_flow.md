# Strict Multi-Cycle Research Result

- symbol: `FLOW`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5332 | 0.9922 | 0.4352 | 0.9290 | 0.1630 | 0.3563 | 0.5537 | 0.5537 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5332 | 0.9920 | 0.4352 | 0.9290 | 0.1630 | 0.3563 | 0.5535 | 0.5535 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5332 | 0.9920 | 0.4352 | 0.9290 | 0.1630 | 0.3563 | 0.5533 | 0.5533 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5332 | 0.9933 | 0.4352 | 0.9290 | 0.1630 | 0.3563 | 0.5525 | 0.5525 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5037 | 1.0040 | 0.3997 | 0.9280 | -4.2846 | 0.8466 | 0.5400 | 0.5400 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5037 | 1.0064 | 0.3997 | 0.9280 | -4.2846 | 0.8466 | 0.5393 | 0.5393 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5037 | 1.0096 | 0.3997 | 0.9280 | -4.2846 | 0.8466 | 0.5383 | 0.5383 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5037 | 1.0129 | 0.3997 | 0.9280 | -4.2846 | 0.8466 | 0.5374 | 0.5374 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4910 | 1.0005 | 0.3148 | 0.8154 | -9.8599 | -0.0448 | 0.5101 | 0.5101 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4910 | 1.0009 | 0.3148 | 0.8154 | -9.8599 | -0.0448 | 0.5099 | 0.5099 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4910 | 1.0013 | 0.3148 | 0.8154 | -9.8599 | -0.0448 | 0.5098 | 0.5098 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4910 | 1.0017 | 0.3148 | 0.8154 | -9.8599 | -0.0448 | 0.5097 | 0.5097 |
| `base|emb=24|sh=0.94` | 18 | 0.5251 | 0.9901 | 1.0000 | 0.8762 | -2.1398 | 0.0545 | 0.5068 | 0.5068 |
| `base|emb=24|sh=0.95` | 18 | 0.5251 | 0.9911 | 1.0000 | 0.8762 | -2.1398 | 0.0545 | 0.5063 | 0.5063 |
| `base|emb=24|sh=0.96` | 18 | 0.5251 | 0.9921 | 1.0000 | 0.8762 | -2.1398 | 0.0545 | 0.5059 | 0.5059 |
| `base|emb=24|sh=0.97` | 18 | 0.5251 | 0.9937 | 1.0000 | 0.8762 | -2.1398 | 0.0545 | 0.5052 | 0.5052 |
| `base|emb=12|sh=0.96` | 18 | 0.5112 | 0.9963 | 1.0000 | 0.8631 | -4.0704 | -0.0809 | 0.4760 | 0.4760 |
| `base|emb=12|sh=0.95` | 18 | 0.5112 | 0.9964 | 1.0000 | 0.8631 | -4.0704 | -0.0809 | 0.4760 | 0.4760 |
| `base|emb=12|sh=0.94` | 18 | 0.5112 | 0.9965 | 1.0000 | 0.8631 | -4.0704 | -0.0809 | 0.4760 | 0.4760 |
| `base|emb=12|sh=0.97` | 18 | 0.5112 | 0.9967 | 1.0000 | 0.8631 | -4.0704 | -0.0809 | 0.4758 | 0.4758 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=344, top_n=35, cutoff=0.7885

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6616 | 0.0273 | 0.9757 | 0.0122 |
| all validations | 0.5110 | 0.0949 | 0.9976 | 0.0271 |

- improvement vs all (primary fraction): `hit +15.06pp, mae +2.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0127 | 0.3333 | 0.4508 | -0.2746 | -25.6979 | -0.6531 | 0.3459 | 0.3459 |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0169 | 0.3333 | 0.4508 | -0.2746 | -25.6979 | -0.6531 | 0.3443 | 0.3443 |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0212 | 0.3333 | 0.4508 | -0.2746 | -25.6979 | -0.6531 | 0.3426 | 0.3426 |
| 4 | `base|emb=24|sh=0.94` | 0.4571 | 1.0049 | 1.0000 | 0.6230 | -0.2453 | -22.9569 | -0.8909 | 0.3413 | 0.3413 |
| 5 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0254 | 0.3333 | 0.4508 | -0.2746 | -25.6979 | -0.6531 | 0.3410 | 0.3410 |
