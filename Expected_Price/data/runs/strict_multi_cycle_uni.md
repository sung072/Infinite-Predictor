# Strict Multi-Cycle Research Result

- symbol: `UNI`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5995 | 0.9847 | 0.2917 | 0.9686 | 7.1151 | -0.1281 | 0.6443 | 0.6443 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5995 | 0.9867 | 0.2917 | 0.9686 | 7.1151 | -0.1281 | 0.6431 | 0.6431 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5995 | 0.9889 | 0.2917 | 0.9686 | 7.1151 | -0.1281 | 0.6419 | 0.6419 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5995 | 0.9913 | 0.2917 | 0.9686 | 7.1151 | -0.1281 | 0.6408 | 0.6408 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4926 | 1.0097 | 0.3981 | 1.1356 | -0.6600 | 0.7640 | 0.5497 | 0.5497 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4926 | 1.0140 | 0.3981 | 1.1356 | -0.6600 | 0.7640 | 0.5483 | 0.5483 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4926 | 1.0190 | 0.3981 | 1.1356 | -0.6600 | 0.7640 | 0.5467 | 0.5467 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4926 | 1.0243 | 0.3981 | 1.1356 | -0.6600 | 0.7640 | 0.5451 | 0.5451 |
| `base|emb=12|sh=0.97` | 18 | 0.5117 | 1.0005 | 1.0000 | 0.9848 | -0.1191 | 0.2040 | 0.5359 | 0.5359 |
| `base|emb=12|sh=0.96` | 18 | 0.5117 | 1.0014 | 1.0000 | 0.9848 | -0.1191 | 0.2040 | 0.5355 | 0.5355 |
| `base|emb=12|sh=0.95` | 18 | 0.5117 | 1.0033 | 1.0000 | 0.9848 | -0.1191 | 0.2040 | 0.5348 | 0.5348 |
| `base|emb=12|sh=0.94` | 18 | 0.5117 | 1.0055 | 1.0000 | 0.9848 | -0.1191 | 0.2040 | 0.5340 | 0.5340 |
| `base|emb=24|sh=0.97` | 18 | 0.5115 | 1.0001 | 1.0000 | 0.9778 | -0.2095 | 0.2160 | 0.5288 | 0.5288 |
| `base|emb=24|sh=0.96` | 18 | 0.5115 | 1.0006 | 1.0000 | 0.9778 | -0.2095 | 0.2160 | 0.5287 | 0.5287 |
| `base|emb=24|sh=0.95` | 18 | 0.5115 | 1.0018 | 1.0000 | 0.9778 | -0.2095 | 0.2160 | 0.5282 | 0.5282 |
| `base|emb=24|sh=0.94` | 18 | 0.5115 | 1.0036 | 1.0000 | 0.9778 | -0.2095 | 0.2160 | 0.5275 | 0.5275 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4701 | 1.0301 | 0.3904 | 0.9059 | -9.7580 | 0.0661 | 0.5202 | 0.5202 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4701 | 1.0429 | 0.3904 | 0.9059 | -9.7580 | 0.0661 | 0.5174 | 0.5174 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4701 | 1.0565 | 0.3904 | 0.9059 | -9.7580 | 0.0661 | 0.5146 | 0.5146 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4701 | 1.0704 | 0.3904 | 0.9059 | -9.7580 | 0.0661 | 0.5119 | 0.5119 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=336, top_n=34, cutoff=0.7890

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6044 | 0.1029 | 0.9764 | 0.0325 |
| all validations | 0.5147 | 0.1140 | 1.0095 | 0.0684 |

- improvement vs all (primary fraction): `hit +8.97pp, mae +3.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.6364 | 0.9857 | 1.0000 | 0.6823 | 0.0673 | 6.2985 | 0.5572 | 0.7305 | 0.7305 |
