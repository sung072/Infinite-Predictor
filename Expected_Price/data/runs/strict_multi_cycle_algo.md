# Strict Multi-Cycle Research Result

- symbol: `ALGO`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5306 | 0.9968 | 0.3318 | 0.9417 | 1.3215 | 0.7578 | 0.5891 | 0.5891 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5306 | 0.9971 | 0.3318 | 0.9417 | 1.3215 | 0.7578 | 0.5889 | 0.5889 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5306 | 0.9978 | 0.3318 | 0.9417 | 1.3215 | 0.7578 | 0.5886 | 0.5886 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5306 | 0.9983 | 0.3318 | 0.9417 | 1.3215 | 0.7578 | 0.5886 | 0.5886 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5177 | 1.0021 | 0.3889 | 1.0231 | 0.0609 | 0.5534 | 0.5784 | 0.5784 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5177 | 1.0011 | 0.3889 | 1.0231 | 0.0609 | 0.5534 | 0.5784 | 0.5784 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5177 | 1.0074 | 0.3889 | 1.0231 | 0.0609 | 0.5534 | 0.5769 | 0.5769 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5177 | 1.0136 | 0.3889 | 1.0231 | 0.0609 | 0.5534 | 0.5753 | 0.5753 |
| `base|emb=24|sh=0.97` | 18 | 0.4949 | 1.0069 | 1.0000 | 0.9708 | -2.7940 | 0.3735 | 0.5455 | 0.5455 |
| `base|emb=24|sh=0.96` | 18 | 0.4949 | 1.0098 | 1.0000 | 0.9708 | -2.7940 | 0.3735 | 0.5445 | 0.5445 |
| `base|emb=24|sh=0.95` | 18 | 0.4949 | 1.0146 | 1.0000 | 0.9708 | -2.7940 | 0.3735 | 0.5428 | 0.5428 |
| `base|emb=24|sh=0.94` | 18 | 0.4949 | 1.0206 | 1.0000 | 0.9708 | -2.7940 | 0.3735 | 0.5408 | 0.5408 |
| `base|emb=12|sh=0.97` | 18 | 0.5050 | 1.0049 | 1.0000 | 0.9662 | -0.9549 | 0.1954 | 0.5372 | 0.5372 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4889 | 1.0045 | 0.3426 | 0.9566 | -7.6869 | 0.7723 | 0.5368 | 0.5368 |
| `base|emb=12|sh=0.96` | 18 | 0.5050 | 1.0073 | 1.0000 | 0.9662 | -0.9549 | 0.1954 | 0.5363 | 0.5363 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4889 | 1.0060 | 0.3426 | 0.9566 | -7.6869 | 0.7723 | 0.5363 | 0.5363 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4889 | 1.0081 | 0.3426 | 0.9566 | -7.6869 | 0.7723 | 0.5356 | 0.5356 |
| `base|emb=12|sh=0.95` | 18 | 0.5050 | 1.0113 | 1.0000 | 0.9662 | -0.9549 | 0.1954 | 0.5349 | 0.5349 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4889 | 1.0113 | 0.3426 | 0.9566 | -7.6869 | 0.7723 | 0.5345 | 0.5345 |
| `base|emb=12|sh=0.94` | 18 | 0.5050 | 1.0165 | 1.0000 | 0.9662 | -0.9549 | 0.1954 | 0.5330 | 0.5330 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=344, top_n=35, cutoff=0.8044

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6798 | 0.0811 | 0.9765 | 0.0236 |
| all validations | 0.5041 | 0.1214 | 1.0100 | 0.0363 |

- improvement vs all (primary fraction): `hit +17.58pp, mae +3.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.8000 | 0.9917 | 0.2778 | 1.8224 | 0.9552 | 89.4012 | 7.6784 | 0.8935 | 0.8935 |
| 2 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.8000 | 0.9931 | 0.2778 | 1.8224 | 0.9552 | 89.4012 | 7.6784 | 0.8929 | 0.8929 |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.8000 | 0.9945 | 0.2778 | 1.8224 | 0.9552 | 89.4012 | 7.6784 | 0.8924 | 0.8924 |
| 4 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.8000 | 0.9959 | 0.2778 | 1.8224 | 0.9552 | 89.4012 | 7.6784 | 0.8918 | 0.8918 |
| 5 | `base|emb=24|sh=0.97` | 0.5625 | 1.0002 | 1.0000 | 0.9869 | 0.0922 | 8.6324 | 0.5023 | 0.7257 | 0.7257 |
