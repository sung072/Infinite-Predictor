# Strict Multi-Cycle Research Result

- symbol: `TAO`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5081 | 0.9883 | 0.5849 | 1.5610 | 6.3956 | 1.8497 | 0.6317 | 0.6317 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5081 | 0.9899 | 0.5849 | 1.5610 | 6.3956 | 1.8497 | 0.6310 | 0.6310 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5081 | 0.9919 | 0.5849 | 1.5610 | 6.3956 | 1.8497 | 0.6301 | 0.6301 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5081 | 0.9938 | 0.5849 | 1.5610 | 6.3956 | 1.8497 | 0.6293 | 0.6293 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4982 | 0.9893 | 0.5494 | 1.2264 | 2.3526 | 0.8987 | 0.5905 | 0.5905 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4982 | 0.9908 | 0.5494 | 1.2264 | 2.3526 | 0.8987 | 0.5897 | 0.5897 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4982 | 0.9926 | 0.5494 | 1.2264 | 2.3526 | 0.8987 | 0.5888 | 0.5888 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4982 | 0.9943 | 0.5494 | 1.2264 | 2.3526 | 0.8987 | 0.5880 | 0.5880 |
| `base|emb=12|sh=0.97` | 18 | 0.5179 | 0.9971 | 1.0000 | 1.0191 | 1.9735 | 0.5182 | 0.5661 | 0.5661 |
| `base|emb=12|sh=0.96` | 18 | 0.5179 | 0.9978 | 1.0000 | 1.0191 | 1.9735 | 0.5182 | 0.5659 | 0.5659 |
| `base|emb=12|sh=0.95` | 18 | 0.5179 | 1.0000 | 1.0000 | 1.0191 | 1.9735 | 0.5182 | 0.5651 | 0.5651 |
| `base|emb=12|sh=0.94` | 18 | 0.5179 | 1.0037 | 1.0000 | 1.0191 | 1.9735 | 0.5182 | 0.5637 | 0.5637 |
| `base|emb=24|sh=0.97` | 18 | 0.5210 | 0.9955 | 1.0000 | 1.0298 | 2.7323 | 0.5907 | 0.5619 | 0.5619 |
| `base|emb=24|sh=0.96` | 18 | 0.5210 | 0.9961 | 1.0000 | 1.0298 | 2.7323 | 0.5907 | 0.5618 | 0.5618 |
| `base|emb=24|sh=0.95` | 18 | 0.5210 | 0.9980 | 1.0000 | 1.0298 | 2.7323 | 0.5907 | 0.5610 | 0.5610 |
| `base|emb=24|sh=0.94` | 18 | 0.5210 | 1.0013 | 1.0000 | 1.0298 | 2.7323 | 0.5907 | 0.5599 | 0.5599 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5457 | 1.0044 | 0.2978 | 1.0435 | 2.0737 | 0.6277 | 0.5438 | 0.5438 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5457 | 1.0089 | 0.2978 | 1.0435 | 2.0737 | 0.6277 | 0.5425 | 0.5425 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5457 | 1.0154 | 0.2978 | 1.0435 | 2.0737 | 0.6277 | 0.5404 | 0.5404 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5457 | 1.0261 | 0.2978 | 1.0435 | 2.0737 | 0.6277 | 0.5368 | 0.5368 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.8192

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5760 | 0.0644 | 0.9808 | 0.0259 |
| all validations | 0.5177 | 0.0898 | 0.9985 | 0.0301 |

- improvement vs all (primary fraction): `hit +5.84pp, mae +1.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.5294 | 0.9870 | 1.0000 | 0.9379 | 0.0228 | 2.1329 | 0.1427 | 0.6530 | 0.6530 |
