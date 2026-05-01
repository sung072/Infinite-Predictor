# Strict Multi-Cycle Research Result

- symbol: `ZAMA`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5023 | 1.0087 | 0.3843 | 1.3076 | 2.0284 | 2.2595 | 0.6179 | 0.6179 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5023 | 1.0127 | 0.3843 | 1.3076 | 2.0284 | 2.2595 | 0.6165 | 0.6165 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5023 | 1.0169 | 0.3843 | 1.3076 | 2.0284 | 2.2595 | 0.6151 | 0.6151 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5023 | 1.0212 | 0.3843 | 1.3076 | 2.0284 | 2.2595 | 0.6138 | 0.6138 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4672 | 1.0076 | 0.3272 | 1.7052 | 7.4740 | 0.6246 | 0.6080 | 0.6080 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4672 | 1.0114 | 0.3272 | 1.7052 | 7.4740 | 0.6246 | 0.6066 | 0.6066 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4672 | 1.0171 | 0.3272 | 1.7052 | 7.4740 | 0.6246 | 0.6045 | 0.6045 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4672 | 1.0239 | 0.3272 | 1.7052 | 7.4740 | 0.6246 | 0.6020 | 0.6020 |
| `base|emb=24|sh=0.97` | 18 | 0.5086 | 1.0035 | 1.0000 | 1.1131 | 3.7092 | 0.8235 | 0.5976 | 0.5976 |
| `base|emb=24|sh=0.96` | 18 | 0.5086 | 1.0059 | 1.0000 | 1.1131 | 3.7092 | 0.8235 | 0.5967 | 0.5967 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5004 | 1.0065 | 0.4012 | 1.4732 | -2.9339 | 3.7562 | 0.5958 | 0.5958 |
| `base|emb=24|sh=0.95` | 18 | 0.5086 | 1.0091 | 1.0000 | 1.1131 | 3.7092 | 0.8235 | 0.5956 | 0.5956 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5004 | 1.0092 | 0.4012 | 1.4732 | -2.9339 | 3.7562 | 0.5950 | 0.5950 |
| `base|emb=24|sh=0.94` | 18 | 0.5086 | 1.0128 | 1.0000 | 1.1131 | 3.7092 | 0.8235 | 0.5943 | 0.5943 |
| `base|emb=12|sh=0.97` | 18 | 0.5023 | 1.0035 | 1.0000 | 1.1087 | 2.9882 | 0.4610 | 0.5943 | 0.5943 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5004 | 1.0122 | 0.4012 | 1.4732 | -2.9339 | 3.7562 | 0.5941 | 0.5941 |
| `base|emb=12|sh=0.96` | 18 | 0.5023 | 1.0061 | 1.0000 | 1.1087 | 2.9882 | 0.4610 | 0.5933 | 0.5933 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5004 | 1.0152 | 0.4012 | 1.4732 | -2.9339 | 3.7562 | 0.5932 | 0.5932 |
| `base|emb=12|sh=0.95` | 18 | 0.5023 | 1.0098 | 1.0000 | 1.1087 | 2.9882 | 0.4610 | 0.5920 | 0.5920 |
| `base|emb=12|sh=0.94` | 18 | 0.5023 | 1.0141 | 1.0000 | 1.1087 | 2.9882 | 0.4610 | 0.5905 | 0.5905 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.8481

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6974 | 0.0438 | 0.9827 | 0.0106 |
| all validations | 0.4993 | 0.1407 | 1.0106 | 0.0309 |

- improvement vs all (primary fraction): `hit +19.81pp, mae +2.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.7143 | 0.9631 | 0.1944 | 2.2328 | 0.6309 | 59.0457 | 7.9758 | 0.9020 | 0.9020 |
| 2 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.7143 | 0.9692 | 0.1944 | 2.2328 | 0.6309 | 59.0457 | 7.9758 | 0.8993 | 0.8993 |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.7143 | 0.9754 | 0.1944 | 2.2328 | 0.6309 | 59.0457 | 7.9758 | 0.8967 | 0.8967 |
| 4 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.7143 | 0.9815 | 0.1944 | 2.2328 | 0.6309 | 59.0457 | 7.9758 | 0.8942 | 0.8942 |
| 5 | `base|emb=24|sh=0.97` | 0.6000 | 0.9835 | 1.0000 | 1.1818 | 0.2294 | 21.4668 | 2.4782 | 0.8008 | 0.8008 |
