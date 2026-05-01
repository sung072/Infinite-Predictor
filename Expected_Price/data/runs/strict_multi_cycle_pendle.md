# Strict Multi-Cycle Research Result

- symbol: `PENDLE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5600 | 0.9966 | 0.4907 | 0.9960 | 6.7573 | 0.6387 | 0.6059 | 0.6059 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5600 | 0.9970 | 0.4907 | 0.9960 | 6.7573 | 0.6387 | 0.6056 | 0.6056 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5600 | 0.9976 | 0.4907 | 0.9960 | 6.7573 | 0.6387 | 0.6053 | 0.6053 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5600 | 0.9982 | 0.4907 | 0.9960 | 6.7573 | 0.6387 | 0.6050 | 0.6050 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5080 | 1.0046 | 0.2593 | 1.0881 | 3.7464 | 0.8236 | 0.5645 | 0.5645 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5080 | 1.0030 | 0.2593 | 1.0881 | 3.7464 | 0.8236 | 0.5644 | 0.5644 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5080 | 1.0016 | 0.2593 | 1.0881 | 3.7464 | 0.8236 | 0.5644 | 0.5644 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5080 | 1.0005 | 0.2593 | 1.0881 | 3.7464 | 0.8236 | 0.5644 | 0.5644 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4930 | 1.0067 | 0.2840 | 1.2599 | 1.5031 | 1.2915 | 0.5629 | 0.5629 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4930 | 1.0098 | 0.2840 | 1.2599 | 1.5031 | 1.2915 | 0.5619 | 0.5619 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4930 | 1.0134 | 0.2840 | 1.2599 | 1.5031 | 1.2915 | 0.5608 | 0.5608 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4930 | 1.0170 | 0.2840 | 1.2599 | 1.5031 | 1.2915 | 0.5597 | 0.5597 |
| `base|emb=24|sh=0.97` | 18 | 0.5017 | 1.0043 | 1.0000 | 0.9964 | -1.5316 | 0.2182 | 0.5482 | 0.5482 |
| `base|emb=12|sh=0.97` | 18 | 0.5126 | 1.0019 | 1.0000 | 1.0113 | 0.8640 | 0.2253 | 0.5476 | 0.5476 |
| `base|emb=24|sh=0.96` | 18 | 0.5017 | 1.0061 | 1.0000 | 0.9964 | -1.5316 | 0.2182 | 0.5476 | 0.5476 |
| `base|emb=12|sh=0.96` | 18 | 0.5126 | 1.0030 | 1.0000 | 1.0113 | 0.8640 | 0.2253 | 0.5472 | 0.5472 |
| `base|emb=24|sh=0.95` | 18 | 0.5017 | 1.0080 | 1.0000 | 0.9964 | -1.5316 | 0.2182 | 0.5469 | 0.5469 |
| `base|emb=12|sh=0.95` | 18 | 0.5126 | 1.0044 | 1.0000 | 1.0113 | 0.8640 | 0.2253 | 0.5467 | 0.5467 |
| `base|emb=12|sh=0.94` | 18 | 0.5126 | 1.0060 | 1.0000 | 1.0113 | 0.8640 | 0.2253 | 0.5462 | 0.5462 |
| `base|emb=24|sh=0.94` | 18 | 0.5017 | 1.0103 | 1.0000 | 0.9964 | -1.5316 | 0.2182 | 0.5461 | 0.5461 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=332, top_n=34, cutoff=0.8147

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6704 | 0.0814 | 0.9646 | 0.0348 |
| all validations | 0.5118 | 0.1270 | 1.0045 | 0.0314 |

- improvement vs all (primary fraction): `hit +15.86pp, mae +4.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=24|sh=0.97` | 0.4286 | 1.0111 | 1.0000 | 0.7825 | -0.1944 | -18.1968 | -0.7294 | 0.3457 | 0.3457 |
