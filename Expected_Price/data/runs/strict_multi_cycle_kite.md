# Strict Multi-Cycle Research Result

- symbol: `KITE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5343 | 1.0004 | 0.3395 | 1.5849 | 18.5325 | 2.4876 | 0.7147 | 0.7147 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5343 | 1.0026 | 0.3395 | 1.5849 | 18.5325 | 2.4876 | 0.7140 | 0.7140 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5343 | 1.0048 | 0.3395 | 1.5849 | 18.5325 | 2.4876 | 0.7134 | 0.7134 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5343 | 1.0070 | 0.3395 | 1.5849 | 18.5325 | 2.4876 | 0.7128 | 0.7128 |
| `base|emb=24|sh=0.97` | 18 | 0.4707 | 1.0022 | 1.0000 | 1.2342 | 2.2069 | 0.4170 | 0.5959 | 0.5959 |
| `base|emb=24|sh=0.96` | 18 | 0.4707 | 1.0035 | 1.0000 | 1.2342 | 2.2069 | 0.4170 | 0.5955 | 0.5955 |
| `base|emb=24|sh=0.95` | 18 | 0.4707 | 1.0048 | 1.0000 | 1.2342 | 2.2069 | 0.4170 | 0.5950 | 0.5950 |
| `base|emb=24|sh=0.94` | 18 | 0.4707 | 1.0063 | 1.0000 | 1.2342 | 2.2069 | 0.4170 | 0.5945 | 0.5945 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4349 | 1.0033 | 0.3287 | 1.2229 | -6.2931 | 0.3145 | 0.5446 | 0.5446 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4349 | 1.0044 | 0.3287 | 1.2229 | -6.2931 | 0.3145 | 0.5443 | 0.5443 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4349 | 1.0057 | 0.3287 | 1.2229 | -6.2931 | 0.3145 | 0.5440 | 0.5440 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4349 | 1.0076 | 0.3287 | 1.2229 | -6.2931 | 0.3145 | 0.5434 | 0.5434 |
| `base|emb=12|sh=0.97` | 18 | 0.4579 | 1.0065 | 1.0000 | 1.2380 | 0.3055 | 0.1693 | 0.5424 | 0.5424 |
| `base|emb=12|sh=0.96` | 18 | 0.4579 | 1.0095 | 1.0000 | 1.2380 | 0.3055 | 0.1693 | 0.5413 | 0.5413 |
| `base|emb=12|sh=0.95` | 18 | 0.4579 | 1.0127 | 1.0000 | 1.2380 | 0.3055 | 0.1693 | 0.5402 | 0.5402 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4191 | 1.0101 | 0.3765 | 1.2693 | -13.4457 | 0.2680 | 0.5400 | 0.5400 |
| `base|emb=12|sh=0.94` | 18 | 0.4579 | 1.0163 | 1.0000 | 1.2380 | 0.3055 | 0.1693 | 0.5389 | 0.5389 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4191 | 1.0140 | 0.3765 | 1.2693 | -13.4457 | 0.2680 | 0.5387 | 0.5387 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4191 | 1.0180 | 0.3765 | 1.2693 | -13.4457 | 0.2680 | 0.5375 | 0.5375 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4191 | 1.0223 | 0.3765 | 1.2693 | -13.4457 | 0.2680 | 0.5362 | 0.5362 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=332, top_n=34, cutoff=0.8127

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6098 | 0.0868 | 0.9857 | 0.0169 |
| all validations | 0.4600 | 0.1169 | 1.0132 | 0.0488 |

- improvement vs all (primary fraction): `hit +14.98pp, mae +2.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=24|sh=0.97` | 0.5000 | 0.9993 | 1.0000 | 2.2313 | 0.2899 | 27.1294 | 6.2501 | 0.8419 | 0.8419 |
