# Strict Multi-Cycle Research Result

- symbol: `XPL`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `base|emb=12|sh=0.97` | 18 | 0.4732 | 1.0100 | 1.0000 | 1.1465 | -0.1290 | 0.5331 | 0.5738 | 0.5738 |
| `base|emb=12|sh=0.96` | 18 | 0.4732 | 1.0138 | 1.0000 | 1.1465 | -0.1290 | 0.5331 | 0.5727 | 0.5727 |
| `base|emb=12|sh=0.95` | 18 | 0.4732 | 1.0180 | 1.0000 | 1.1465 | -0.1290 | 0.5331 | 0.5714 | 0.5714 |
| `base|emb=12|sh=0.94` | 18 | 0.4732 | 1.0225 | 1.0000 | 1.1465 | -0.1290 | 0.5331 | 0.5701 | 0.5701 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4453 | 1.0067 | 0.3627 | 1.2816 | -5.8626 | 0.5162 | 0.5609 | 0.5609 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4453 | 1.0090 | 0.3627 | 1.2816 | -5.8626 | 0.5162 | 0.5601 | 0.5601 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4453 | 1.0113 | 0.3627 | 1.2816 | -5.8626 | 0.5162 | 0.5592 | 0.5592 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4453 | 1.0144 | 0.3627 | 1.2816 | -5.8626 | 0.5162 | 0.5582 | 0.5582 |
| `base|emb=24|sh=0.97` | 18 | 0.4669 | 1.0131 | 1.0000 | 1.1084 | -2.5336 | 0.0931 | 0.5467 | 0.5467 |
| `base|emb=24|sh=0.96` | 18 | 0.4669 | 1.0181 | 1.0000 | 1.1084 | -2.5336 | 0.0931 | 0.5451 | 0.5451 |
| `base|emb=24|sh=0.95` | 18 | 0.4669 | 1.0239 | 1.0000 | 1.1084 | -2.5336 | 0.0931 | 0.5433 | 0.5433 |
| `base|emb=24|sh=0.94` | 18 | 0.4669 | 1.0299 | 1.0000 | 1.1084 | -2.5336 | 0.0931 | 0.5415 | 0.5415 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4774 | 1.0095 | 0.3102 | 0.9572 | -8.3981 | 0.1391 | 0.5341 | 0.5341 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4774 | 1.0139 | 0.3102 | 0.9572 | -8.3981 | 0.1391 | 0.5327 | 0.5327 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4774 | 1.0191 | 0.3102 | 0.9572 | -8.3981 | 0.1391 | 0.5312 | 0.5312 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4774 | 1.0245 | 0.3102 | 0.9572 | -8.3981 | 0.1391 | 0.5296 | 0.5296 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4234 | 1.0073 | 0.3750 | 1.2528 | -7.8277 | 0.5364 | 0.5131 | 0.5131 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4234 | 1.0097 | 0.3750 | 1.2528 | -7.8277 | 0.5364 | 0.5122 | 0.5122 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4234 | 1.0122 | 0.3750 | 1.2528 | -7.8277 | 0.5364 | 0.5113 | 0.5113 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4234 | 1.0152 | 0.3750 | 1.2528 | -7.8277 | 0.5364 | 0.5102 | 0.5102 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.7785

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5980 | 0.0645 | 0.9877 | 0.0153 |
| all validations | 0.4563 | 0.1145 | 1.0167 | 0.0513 |

- improvement vs all (primary fraction): `hit +14.17pp, mae +2.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `base|emb=12|sh=0.94` | 0.5882 | 0.9980 | 1.0000 | 0.7380 | 0.0202 | 1.8868 | 0.0774 | 0.6408 | 0.6408 |
| 3 | `base|emb=12|sh=0.95` | 0.5882 | 0.9984 | 1.0000 | 0.7380 | 0.0202 | 1.8868 | 0.0774 | 0.6407 | 0.6407 |
| 4 | `base|emb=12|sh=0.96` | 0.5882 | 0.9987 | 1.0000 | 0.7380 | 0.0202 | 1.8868 | 0.0774 | 0.6405 | 0.6405 |
| 5 | `base|emb=12|sh=0.97` | 0.5882 | 0.9990 | 1.0000 | 0.7380 | 0.0202 | 1.8868 | 0.0774 | 0.6404 | 0.6404 |
