# Strict Multi-Cycle Research Result

- symbol: `CHZ`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4629 | 1.0068 | 0.3287 | 1.6434 | 6.3163 | 0.9277 | 0.6069 | 0.6069 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4629 | 1.0090 | 0.3287 | 1.6434 | 6.3163 | 0.9277 | 0.6061 | 0.6061 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4629 | 1.0115 | 0.3287 | 1.6434 | 6.3163 | 0.9277 | 0.6053 | 0.6053 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4629 | 1.0145 | 0.3287 | 1.6434 | 6.3163 | 0.9277 | 0.6042 | 0.6042 |
| `base|emb=12|sh=0.97` | 18 | 0.5122 | 1.0029 | 1.0000 | 1.0633 | 3.3970 | 0.6533 | 0.5942 | 0.5942 |
| `base|emb=12|sh=0.96` | 18 | 0.5122 | 1.0046 | 1.0000 | 1.0633 | 3.3970 | 0.6533 | 0.5936 | 0.5936 |
| `base|emb=12|sh=0.95` | 18 | 0.5122 | 1.0070 | 1.0000 | 1.0633 | 3.3970 | 0.6533 | 0.5928 | 0.5928 |
| `base|emb=12|sh=0.94` | 18 | 0.5122 | 1.0100 | 1.0000 | 1.0633 | 3.3970 | 0.6533 | 0.5917 | 0.5917 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5097 | 1.0119 | 0.3380 | 0.9774 | -3.2954 | 0.7257 | 0.5882 | 0.5882 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5097 | 1.0195 | 0.3380 | 0.9774 | -3.2954 | 0.7257 | 0.5862 | 0.5862 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5097 | 1.0281 | 0.3380 | 0.9774 | -3.2954 | 0.7257 | 0.5840 | 0.5840 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5097 | 1.0372 | 0.3380 | 0.9774 | -3.2954 | 0.7257 | 0.5818 | 0.5818 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4847 | 0.9991 | 0.3858 | 1.3089 | 2.3389 | 0.7726 | 0.5744 | 0.5744 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4847 | 0.9991 | 0.3858 | 1.3089 | 2.3389 | 0.7726 | 0.5743 | 0.5743 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4847 | 0.9993 | 0.3858 | 1.3089 | 2.3389 | 0.7726 | 0.5742 | 0.5742 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4847 | 1.0009 | 0.3858 | 1.3089 | 2.3389 | 0.7726 | 0.5737 | 0.5737 |
| `base|emb=24|sh=0.97` | 18 | 0.5103 | 1.0016 | 1.0000 | 1.0441 | 1.7285 | 0.6677 | 0.5734 | 0.5734 |
| `base|emb=24|sh=0.96` | 18 | 0.5103 | 1.0027 | 1.0000 | 1.0441 | 1.7285 | 0.6677 | 0.5730 | 0.5730 |
| `base|emb=24|sh=0.95` | 18 | 0.5103 | 1.0045 | 1.0000 | 1.0441 | 1.7285 | 0.6677 | 0.5724 | 0.5724 |
| `base|emb=24|sh=0.94` | 18 | 0.5103 | 1.0071 | 1.0000 | 1.0441 | 1.7285 | 0.6677 | 0.5714 | 0.5714 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8244

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6883 | 0.1143 | 0.9619 | 0.0455 |
| all validations | 0.4986 | 0.1313 | 1.0105 | 0.0553 |

- improvement vs all (primary fraction): `hit +18.97pp, mae +4.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.3824 | 1.0299 | 1.0000 | 0.6876 | -0.3097 | -28.9823 | -0.6701 | 0.3267 | 0.3267 |
