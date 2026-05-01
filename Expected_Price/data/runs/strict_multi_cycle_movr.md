# Strict Multi-Cycle Research Result

- symbol: `MOVR`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5211 | 0.9911 | 0.2840 | 1.2707 | 8.2902 | 1.3485 | 0.6659 | 0.6659 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5211 | 0.9931 | 0.2840 | 1.2707 | 8.2902 | 1.3485 | 0.6654 | 0.6654 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5211 | 0.9951 | 0.2840 | 1.2707 | 8.2902 | 1.3485 | 0.6649 | 0.6649 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5211 | 0.9973 | 0.2840 | 1.2707 | 8.2902 | 1.3485 | 0.6645 | 0.6645 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5041 | 0.9990 | 0.3688 | 1.1706 | 0.6626 | 1.0093 | 0.6075 | 0.6075 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5041 | 0.9988 | 0.3688 | 1.1706 | 0.6626 | 1.0093 | 0.6073 | 0.6073 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5041 | 0.9988 | 0.3688 | 1.1706 | 0.6626 | 1.0093 | 0.6072 | 0.6072 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5056 | 0.9990 | 0.3688 | 1.1660 | 0.7008 | 1.0119 | 0.6071 | 0.6071 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5364 | 0.9980 | 0.3194 | 1.1465 | 8.8486 | 1.2177 | 0.6036 | 0.6036 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5364 | 1.0014 | 0.3194 | 1.1465 | 8.8486 | 1.2177 | 0.6026 | 0.6026 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5364 | 1.0050 | 0.3194 | 1.1465 | 8.8486 | 1.2177 | 0.6017 | 0.6017 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5364 | 1.0088 | 0.3194 | 1.1465 | 8.8486 | 1.2177 | 0.6008 | 0.6008 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5137 | 1.0120 | 0.3642 | 1.2333 | 3.4364 | 1.8074 | 0.6003 | 0.6003 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5095 | 1.0162 | 0.3642 | 1.2448 | 3.3569 | 1.8022 | 0.5975 | 0.5975 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5095 | 1.0204 | 0.3642 | 1.2448 | 3.3569 | 1.8022 | 0.5967 | 0.5967 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5095 | 1.0249 | 0.3642 | 1.2448 | 3.3569 | 1.8022 | 0.5960 | 0.5960 |
| `base|emb=24|sh=0.97` | 18 | 0.4808 | 1.0074 | 1.0000 | 1.0132 | -1.9543 | 1.0781 | 0.5836 | 0.5836 |
| `base|emb=24|sh=0.96` | 18 | 0.4789 | 1.0108 | 1.0000 | 1.0189 | -1.9976 | 1.0746 | 0.5818 | 0.5818 |
| `base|emb=24|sh=0.95` | 18 | 0.4789 | 1.0146 | 1.0000 | 1.0189 | -1.9976 | 1.0746 | 0.5806 | 0.5806 |
| `base|emb=24|sh=0.94` | 18 | 0.4789 | 1.0189 | 1.0000 | 1.0189 | -1.9976 | 1.0746 | 0.5792 | 0.5792 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.8487

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6623 | 0.0606 | 0.9670 | 0.0216 |
| all validations | 0.5052 | 0.1238 | 1.0058 | 0.0532 |

- improvement vs all (primary fraction): `hit +15.71pp, mae +3.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=24|sh=0.97` | 0.5882 | 0.9886 | 1.0000 | 0.9865 | 0.1395 | 13.0522 | 1.3467 | 0.7619 | 0.7619 |
