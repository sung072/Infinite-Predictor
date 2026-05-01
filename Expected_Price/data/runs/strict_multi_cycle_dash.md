# Strict Multi-Cycle Research Result

- symbol: `DASH`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `base|emb=24|sh=0.97` | 18 | 0.4885 | 1.0024 | 1.0000 | 1.0125 | -2.1425 | -0.0096 | 0.5447 | 0.5447 |
| `base|emb=24|sh=0.96` | 18 | 0.4885 | 1.0052 | 1.0000 | 1.0125 | -2.1425 | -0.0096 | 0.5436 | 0.5436 |
| `base|emb=24|sh=0.95` | 18 | 0.4885 | 1.0088 | 1.0000 | 1.0125 | -2.1425 | -0.0096 | 0.5423 | 0.5423 |
| `base|emb=24|sh=0.94` | 18 | 0.4885 | 1.0130 | 1.0000 | 1.0125 | -2.1425 | -0.0096 | 0.5407 | 0.5407 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4490 | 1.0037 | 0.3302 | 1.1185 | -5.9754 | 0.2342 | 0.5301 | 0.5301 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4490 | 1.0062 | 0.3302 | 1.1185 | -5.9754 | 0.2342 | 0.5292 | 0.5292 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4490 | 1.0096 | 0.3302 | 1.1185 | -5.9754 | 0.2342 | 0.5279 | 0.5279 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4490 | 1.0135 | 0.3302 | 1.1185 | -5.9754 | 0.2342 | 0.5265 | 0.5265 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4422 | 1.0061 | 0.3503 | 1.0989 | -8.5750 | 0.0178 | 0.5188 | 0.5188 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4422 | 1.0095 | 0.3503 | 1.0989 | -8.5750 | 0.0178 | 0.5176 | 0.5176 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4422 | 1.0135 | 0.3503 | 1.0989 | -8.5750 | 0.0178 | 0.5162 | 0.5162 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4422 | 1.0177 | 0.3503 | 1.0989 | -8.5750 | 0.0178 | 0.5147 | 0.5147 |
| `base|emb=12|sh=0.97` | 18 | 0.4863 | 1.0023 | 1.0000 | 0.9590 | -4.4664 | 0.0184 | 0.4841 | 0.4841 |
| `base|emb=12|sh=0.96` | 18 | 0.4863 | 1.0050 | 1.0000 | 0.9590 | -4.4664 | 0.0184 | 0.4831 | 0.4831 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5137 | 1.0146 | 0.3349 | 0.9247 | -4.3706 | 0.0154 | 0.4828 | 0.4828 |
| `base|emb=12|sh=0.95` | 18 | 0.4863 | 1.0085 | 1.0000 | 0.9590 | -4.4664 | 0.0184 | 0.4818 | 0.4818 |
| `base|emb=12|sh=0.94` | 18 | 0.4863 | 1.0128 | 1.0000 | 0.9590 | -4.4664 | 0.0184 | 0.4802 | 0.4802 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5137 | 1.0229 | 0.3349 | 0.9247 | -4.3706 | 0.0154 | 0.4800 | 0.4800 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5137 | 1.0322 | 0.3349 | 0.9247 | -4.3706 | 0.0154 | 0.4771 | 0.4771 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5137 | 1.0418 | 0.3349 | 0.9247 | -4.3706 | 0.0154 | 0.4742 | 0.4742 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.7834

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6438 | 0.1385 | 0.9704 | 0.0327 |
| all validations | 0.4853 | 0.1185 | 1.0116 | 0.0357 |

- improvement vs all (primary fraction): `hit +15.85pp, mae +4.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `base|emb=24|sh=0.97` | 0.4545 | 1.0016 | 1.0000 | 0.8462 | -0.1388 | -12.9925 | -0.6912 | 0.3589 | 0.3589 |
| 3 | `base|emb=24|sh=0.96` | 0.4545 | 1.0021 | 1.0000 | 0.8462 | -0.1388 | -12.9925 | -0.6912 | 0.3587 | 0.3587 |
| 4 | `base|emb=24|sh=0.95` | 0.4545 | 1.0027 | 1.0000 | 0.8462 | -0.1388 | -12.9925 | -0.6912 | 0.3585 | 0.3585 |
| 5 | `base|emb=24|sh=0.94` | 0.4545 | 1.0032 | 1.0000 | 0.8462 | -0.1388 | -12.9925 | -0.6912 | 0.3583 | 0.3583 |
