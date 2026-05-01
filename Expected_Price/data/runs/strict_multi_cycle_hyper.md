# Strict Multi-Cycle Research Result

- symbol: `HYPER`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5399 | 0.9941 | 0.2963 | 1.1212 | 8.8286 | 0.7987 | 0.6524 | 0.6524 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5399 | 0.9946 | 0.2963 | 1.1212 | 8.8286 | 0.7987 | 0.6521 | 0.6521 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5399 | 0.9952 | 0.2963 | 1.1212 | 8.8286 | 0.7987 | 0.6518 | 0.6518 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5399 | 0.9960 | 0.2963 | 1.1212 | 8.8286 | 0.7987 | 0.6514 | 0.6514 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5201 | 0.9917 | 0.3117 | 1.1808 | 6.7469 | 1.1297 | 0.6130 | 0.6130 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5201 | 0.9929 | 0.3117 | 1.1808 | 6.7469 | 1.1297 | 0.6124 | 0.6124 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5201 | 0.9942 | 0.3117 | 1.1808 | 6.7469 | 1.1297 | 0.6117 | 0.6117 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5201 | 0.9955 | 0.3117 | 1.1808 | 6.7469 | 1.1297 | 0.6111 | 0.6111 |
| `base|emb=12|sh=0.94` | 18 | 0.5323 | 0.9962 | 1.0000 | 0.9906 | 4.0654 | 0.5217 | 0.6105 | 0.6105 |
| `base|emb=12|sh=0.95` | 18 | 0.5323 | 0.9964 | 1.0000 | 0.9906 | 4.0654 | 0.5217 | 0.6104 | 0.6104 |
| `base|emb=12|sh=0.96` | 18 | 0.5323 | 0.9968 | 1.0000 | 0.9906 | 4.0654 | 0.5217 | 0.6102 | 0.6102 |
| `base|emb=12|sh=0.97` | 18 | 0.5323 | 0.9972 | 1.0000 | 0.9906 | 4.0654 | 0.5217 | 0.6100 | 0.6100 |
| `base|emb=24|sh=0.97` | 18 | 0.5199 | 0.9996 | 1.0000 | 1.0273 | 2.9743 | 0.4842 | 0.6082 | 0.6082 |
| `base|emb=24|sh=0.96` | 18 | 0.5199 | 0.9999 | 1.0000 | 1.0273 | 2.9743 | 0.4842 | 0.6080 | 0.6080 |
| `base|emb=24|sh=0.95` | 18 | 0.5199 | 1.0004 | 1.0000 | 1.0273 | 2.9743 | 0.4842 | 0.6079 | 0.6079 |
| `base|emb=24|sh=0.94` | 18 | 0.5199 | 1.0011 | 1.0000 | 1.0273 | 2.9743 | 0.4842 | 0.6076 | 0.6076 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5300 | 1.0002 | 0.4012 | 1.0405 | 3.8883 | 0.8463 | 0.5864 | 0.5864 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5300 | 0.9998 | 0.4012 | 1.0405 | 3.8883 | 0.8463 | 0.5863 | 0.5863 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5300 | 0.9996 | 0.4012 | 1.0405 | 3.8883 | 0.8463 | 0.5862 | 0.5862 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5300 | 0.9993 | 0.4012 | 1.0405 | 3.8883 | 0.8463 | 0.5862 | 0.5862 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.7981

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6372 | 0.0570 | 0.9804 | 0.0301 |
| all validations | 0.5269 | 0.1042 | 0.9982 | 0.0223 |

- improvement vs all (primary fraction): `hit +11.03pp, mae +1.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 0.9795 | 0.4722 | 0.5307 | 0.0228 | 2.1380 | 0.0939 | 0.6630 | 0.6630 |
| 2 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 0.9829 | 0.4722 | 0.5307 | 0.0228 | 2.1380 | 0.0939 | 0.6615 | 0.6615 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 0.9863 | 0.4722 | 0.5307 | 0.0228 | 2.1380 | 0.0939 | 0.6601 | 0.6601 |
| 4 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 0.9897 | 0.4722 | 0.5307 | 0.0228 | 2.1380 | 0.0939 | 0.6587 | 0.6587 |
| 5 | `base|emb=12|sh=0.94` | 0.5588 | 0.9910 | 1.0000 | 0.7494 | -0.0187 | -1.7492 | -0.1632 | 0.4679 | 0.4679 |
