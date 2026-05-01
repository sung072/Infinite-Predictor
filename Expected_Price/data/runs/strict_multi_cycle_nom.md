# Strict Multi-Cycle Research Result

- symbol: `NOM`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4524 | 1.0270 | 0.5185 | 1.2217 | -2.4650 | 0.3360 | 0.5419 | 0.5419 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4524 | 1.0379 | 0.5185 | 1.2217 | -2.4650 | 0.3360 | 0.5388 | 0.5388 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4524 | 1.0491 | 0.5185 | 1.2217 | -2.4650 | 0.3360 | 0.5360 | 0.5360 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4524 | 1.0606 | 0.5185 | 1.2217 | -2.4650 | 0.3360 | 0.5333 | 0.5333 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5200 | 1.0335 | 0.2407 | 1.5552 | -3.6315 | 5.2058 | 0.5330 | 0.5330 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5200 | 1.0463 | 0.2407 | 1.5552 | -3.6315 | 5.2058 | 0.5293 | 0.5293 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5200 | 1.0599 | 0.2407 | 1.5552 | -3.6315 | 5.2058 | 0.5256 | 0.5256 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5200 | 1.0734 | 0.2407 | 1.5552 | -3.6315 | 5.2058 | 0.5223 | 0.5223 |
| `base|emb=12|sh=0.97` | 18 | 0.4897 | 1.0096 | 1.0000 | 0.9882 | -2.8723 | -0.0441 | 0.5066 | 0.5066 |
| `base|emb=12|sh=0.96` | 18 | 0.4897 | 1.0147 | 1.0000 | 0.9882 | -2.8723 | -0.0441 | 0.5047 | 0.5047 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4349 | 1.0224 | 0.5247 | 1.2426 | -4.3166 | 0.1822 | 0.5047 | 0.5047 |
| `base|emb=12|sh=0.95` | 18 | 0.4897 | 1.0210 | 1.0000 | 0.9882 | -2.8723 | -0.0441 | 0.5025 | 0.5025 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4349 | 1.0304 | 0.5247 | 1.2426 | -4.3166 | 0.1822 | 0.5019 | 0.5019 |
| `base|emb=12|sh=0.94` | 18 | 0.4897 | 1.0276 | 1.0000 | 0.9882 | -2.8723 | -0.0441 | 0.5003 | 0.5003 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4349 | 1.0386 | 0.5247 | 1.2426 | -4.3166 | 0.1822 | 0.4992 | 0.4992 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4349 | 1.0469 | 0.5247 | 1.2426 | -4.3166 | 0.1822 | 0.4966 | 0.4966 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5013 | 1.0241 | 0.2546 | 1.0538 | -4.5067 | 1.2686 | 0.4939 | 0.4939 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5013 | 1.0348 | 0.2546 | 1.0538 | -4.5067 | 1.2686 | 0.4902 | 0.4902 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5013 | 1.0461 | 0.2546 | 1.0538 | -4.5067 | 1.2686 | 0.4865 | 0.4865 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5013 | 1.0574 | 0.2546 | 1.0538 | -4.5067 | 1.2686 | 0.4829 | 0.4829 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.7968

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6479 | 0.0899 | 0.9698 | 0.0164 |
| all validations | 0.4751 | 0.1061 | 1.0335 | 0.0706 |

- improvement vs all (primary fraction): `hit +17.28pp, mae +6.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.5161 | 1.0212 | 1.0000 | 0.8559 | -0.0371 | -3.4760 | -0.2790 | 0.4042 | 0.4042 |
