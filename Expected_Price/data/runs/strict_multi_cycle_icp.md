# Strict Multi-Cycle Research Result

- symbol: `ICP`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5001 | 0.9999 | 0.4028 | 0.9433 | -3.7275 | 0.5945 | 0.5450 | 0.5450 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5001 | 1.0002 | 0.4028 | 0.9433 | -3.7275 | 0.5945 | 0.5450 | 0.5450 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5001 | 1.0012 | 0.4028 | 0.9433 | -3.7275 | 0.5945 | 0.5446 | 0.5446 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5001 | 1.0022 | 0.4028 | 0.9433 | -3.7275 | 0.5945 | 0.5443 | 0.5443 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4915 | 1.0139 | 0.3457 | 0.9910 | -2.0821 | 1.3599 | 0.5316 | 0.5316 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4915 | 1.0209 | 0.3457 | 0.9910 | -2.0821 | 1.3599 | 0.5296 | 0.5296 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4915 | 1.0285 | 0.3457 | 0.9910 | -2.0821 | 1.3599 | 0.5276 | 0.5276 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4915 | 1.0379 | 0.3457 | 0.9910 | -2.0821 | 1.3599 | 0.5250 | 0.5250 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5040 | 1.0138 | 0.3750 | 1.0004 | -0.3201 | 0.9907 | 0.5216 | 0.5216 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5040 | 1.0207 | 0.3750 | 1.0004 | -0.3201 | 0.9907 | 0.5195 | 0.5195 |
| `base|emb=12|sh=0.97` | 18 | 0.4830 | 1.0067 | 1.0000 | 0.9823 | -4.0006 | 0.0241 | 0.5186 | 0.5186 |
| `base|emb=12|sh=0.96` | 18 | 0.4830 | 1.0102 | 1.0000 | 0.9823 | -4.0006 | 0.0241 | 0.5173 | 0.5173 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5040 | 1.0282 | 0.3750 | 1.0004 | -0.3201 | 0.9907 | 0.5173 | 0.5173 |
| `base|emb=12|sh=0.95` | 18 | 0.4830 | 1.0144 | 1.0000 | 0.9823 | -4.0006 | 0.0241 | 0.5158 | 0.5158 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5040 | 1.0372 | 0.3750 | 1.0004 | -0.3201 | 0.9907 | 0.5147 | 0.5147 |
| `base|emb=12|sh=0.94` | 18 | 0.4830 | 1.0190 | 1.0000 | 0.9823 | -4.0006 | 0.0241 | 0.5142 | 0.5142 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4511 | 1.0068 | 0.4120 | 0.8576 | -13.5686 | 0.2628 | 0.5020 | 0.5020 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4511 | 1.0093 | 0.4120 | 0.8576 | -13.5686 | 0.2628 | 0.5012 | 0.5012 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4511 | 1.0129 | 0.4120 | 0.8576 | -13.5686 | 0.2628 | 0.5000 | 0.5000 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4511 | 1.0166 | 0.4120 | 0.8576 | -13.5686 | 0.2628 | 0.4988 | 0.4988 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8251

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6804 | 0.0647 | 0.9728 | 0.0094 |
| all validations | 0.4861 | 0.1294 | 1.0135 | 0.0483 |

- improvement vs all (primary fraction): `hit +19.42pp, mae +4.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.6471 | 0.9880 | 1.0000 | 0.7369 | 0.1189 | 11.1265 | 0.9499 | 0.7509 | 0.7509 |
