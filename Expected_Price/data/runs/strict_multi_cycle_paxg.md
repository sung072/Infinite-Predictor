# Strict Multi-Cycle Research Result

- symbol: `PAXG`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5460 | 0.9769 | 0.4306 | 1.7611 | 15.9906 | 3.4200 | 0.6530 | 0.6530 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5460 | 0.9781 | 0.4306 | 1.7611 | 15.9906 | 3.4200 | 0.6506 | 0.6506 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5460 | 0.9804 | 0.4306 | 1.7611 | 15.9906 | 3.4200 | 0.6483 | 0.6483 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5460 | 0.9839 | 0.4306 | 1.7611 | 15.9906 | 3.4200 | 0.6459 | 0.6459 |
| `base|emb=24|sh=0.95` | 18 | 0.5397 | 0.9922 | 1.0000 | 1.0206 | 5.0981 | 1.1169 | 0.6223 | 0.6223 |
| `base|emb=24|sh=0.94` | 18 | 0.5397 | 0.9927 | 1.0000 | 1.0206 | 5.0981 | 1.1169 | 0.6221 | 0.6221 |
| `base|emb=24|sh=0.96` | 18 | 0.5397 | 0.9925 | 1.0000 | 1.0206 | 5.0981 | 1.1169 | 0.6221 | 0.6221 |
| `base|emb=24|sh=0.97` | 18 | 0.5397 | 0.9935 | 1.0000 | 1.0206 | 5.0981 | 1.1169 | 0.6216 | 0.6216 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5328 | 0.9959 | 0.4198 | 1.1234 | 5.3488 | 0.7647 | 0.6123 | 0.6123 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5328 | 0.9946 | 0.4198 | 1.1234 | 5.3488 | 0.7647 | 0.6122 | 0.6122 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5328 | 0.9942 | 0.4198 | 1.1234 | 5.3488 | 0.7647 | 0.6120 | 0.6120 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5328 | 0.9944 | 0.4198 | 1.1234 | 5.3488 | 0.7647 | 0.6116 | 0.6116 |
| `base|emb=12|sh=0.94` | 18 | 0.5350 | 0.9922 | 1.0000 | 1.0531 | 4.6410 | 1.0534 | 0.6045 | 0.6045 |
| `base|emb=12|sh=0.95` | 18 | 0.5350 | 0.9921 | 1.0000 | 1.0531 | 4.6410 | 1.0534 | 0.6044 | 0.6044 |
| `base|emb=12|sh=0.96` | 18 | 0.5350 | 0.9926 | 1.0000 | 1.0531 | 4.6410 | 1.0534 | 0.6042 | 0.6042 |
| `base|emb=12|sh=0.97` | 18 | 0.5350 | 0.9937 | 1.0000 | 1.0531 | 4.6410 | 1.0534 | 0.6037 | 0.6037 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5503 | 0.9836 | 0.3920 | 0.9373 | 5.8860 | 0.6805 | 0.5988 | 0.5988 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5503 | 0.9853 | 0.3920 | 0.9373 | 5.8860 | 0.6805 | 0.5980 | 0.5980 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5503 | 0.9871 | 0.3920 | 0.9373 | 5.8860 | 0.6805 | 0.5971 | 0.5971 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5503 | 0.9889 | 0.3920 | 0.9373 | 5.8860 | 0.6805 | 0.5963 | 0.5963 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8414

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6607 | 0.0733 | 0.9366 | 0.0739 |
| all validations | 0.5385 | 0.1093 | 0.9904 | 0.0398 |

- improvement vs all (primary fraction): `hit +12.22pp, mae +5.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6316 | 0.9371 | 0.5556 | 1.0695 | 0.2308 | 21.6018 | 1.9363 | 0.8113 | 0.8113 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6316 | 0.9457 | 0.5556 | 1.0695 | 0.2308 | 21.6018 | 1.9363 | 0.8075 | 0.8075 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6316 | 0.9566 | 0.5556 | 1.0695 | 0.2308 | 21.6018 | 1.9363 | 0.8027 | 0.8027 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6316 | 0.9674 | 0.5556 | 1.0695 | 0.2308 | 21.6018 | 1.9363 | 0.7980 | 0.7980 |
| 5 | `base|emb=24|sh=0.95` | 0.5429 | 0.9879 | 1.0000 | 0.9885 | 0.0631 | 5.9013 | 0.4756 | 0.7212 | 0.7212 |
