# Strict Multi-Cycle Research Result

- symbol: `AAVE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5009 | 1.0067 | 0.2978 | 1.3307 | 6.5776 | 0.6429 | 0.5830 | 0.5830 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5009 | 1.0107 | 0.2978 | 1.3307 | 6.5776 | 0.6429 | 0.5818 | 0.5818 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5041 | 1.0023 | 0.4599 | 0.8924 | -7.7546 | 0.1785 | 0.5818 | 0.5818 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5041 | 1.0035 | 0.4599 | 0.8924 | -7.7546 | 0.1785 | 0.5814 | 0.5814 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5041 | 1.0046 | 0.4599 | 0.8924 | -7.7546 | 0.1785 | 0.5811 | 0.5811 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5041 | 1.0060 | 0.4599 | 0.8924 | -7.7546 | 0.1785 | 0.5807 | 0.5807 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5009 | 1.0187 | 0.2978 | 1.3307 | 6.5776 | 0.6429 | 0.5794 | 0.5794 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5009 | 1.0290 | 0.2978 | 1.3307 | 6.5776 | 0.6429 | 0.5763 | 0.5763 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5111 | 1.0016 | 0.4583 | 0.9197 | -4.6260 | 0.3514 | 0.5626 | 0.5626 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5111 | 1.0022 | 0.4583 | 0.9197 | -4.6260 | 0.3514 | 0.5624 | 0.5624 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5111 | 1.0030 | 0.4583 | 0.9197 | -4.6260 | 0.3514 | 0.5623 | 0.5623 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5111 | 1.0040 | 0.4583 | 0.9197 | -4.6260 | 0.3514 | 0.5621 | 0.5621 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4650 | 1.0060 | 0.3318 | 1.2371 | -2.1782 | 0.1975 | 0.5556 | 0.5556 |
| `base|emb=24|sh=0.97` | 18 | 0.5031 | 1.0034 | 1.0000 | 0.9892 | -2.0257 | 0.0901 | 0.5556 | 0.5556 |
| `base|emb=24|sh=0.96` | 18 | 0.5031 | 1.0058 | 1.0000 | 0.9892 | -2.0257 | 0.0901 | 0.5547 | 0.5547 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4650 | 1.0103 | 0.3318 | 1.2371 | -2.1782 | 0.1975 | 0.5541 | 0.5541 |
| `base|emb=24|sh=0.95` | 18 | 0.5031 | 1.0093 | 1.0000 | 0.9892 | -2.0257 | 0.0901 | 0.5535 | 0.5535 |
| `base|emb=24|sh=0.94` | 18 | 0.5031 | 1.0136 | 1.0000 | 0.9892 | -2.0257 | 0.0901 | 0.5519 | 0.5519 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4650 | 1.0167 | 0.3318 | 1.2371 | -2.1782 | 0.1975 | 0.5517 | 0.5517 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4650 | 1.0256 | 0.3318 | 1.2371 | -2.1782 | 0.1975 | 0.5485 | 0.5485 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.7853

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6080 | 0.1175 | 0.9851 | 0.0286 |
| all validations | 0.4971 | 0.1004 | 1.0094 | 0.0376 |

- improvement vs all (primary fraction): `hit +11.09pp, mae +2.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.7500 | 1.0019 | 0.3611 | 0.3583 | 0.0272 | 2.5478 | 0.0667 | 0.6729 | 0.6729 |
| 2 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.7500 | 1.0037 | 0.3611 | 0.3583 | 0.0272 | 2.5478 | 0.0667 | 0.6722 | 0.6722 |
| 3 | `base|emb=24|sh=0.97` | 0.5429 | 1.0052 | 1.0000 | 0.7505 | -0.0439 | -4.1080 | -0.1938 | 0.4050 | 0.4050 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4167 | 1.0088 | 0.3333 | 1.1475 | -0.0728 | -6.8149 | -0.3124 | 0.3774 | 0.3774 |
| 5 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4167 | 1.0117 | 0.3333 | 1.1475 | -0.0728 | -6.8149 | -0.3124 | 0.3762 | 0.3762 |
