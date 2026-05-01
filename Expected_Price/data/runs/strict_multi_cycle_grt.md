# Strict Multi-Cycle Research Result

- symbol: `GRT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5760 | 0.9875 | 0.3086 | 1.4664 | 20.6370 | 1.9665 | 0.7354 | 0.7354 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5760 | 0.9893 | 0.3086 | 1.4664 | 20.6370 | 1.9665 | 0.7347 | 0.7347 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5760 | 0.9911 | 0.3086 | 1.4664 | 20.6370 | 1.9665 | 0.7339 | 0.7339 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5760 | 0.9929 | 0.3086 | 1.4664 | 20.6370 | 1.9665 | 0.7331 | 0.7331 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5633 | 0.9999 | 0.3457 | 1.2572 | 9.1389 | 1.4590 | 0.6654 | 0.6654 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5633 | 1.0006 | 0.3457 | 1.2572 | 9.1389 | 1.4590 | 0.6652 | 0.6652 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5633 | 1.0015 | 0.3457 | 1.2572 | 9.1389 | 1.4590 | 0.6651 | 0.6651 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5633 | 1.0024 | 0.3457 | 1.2572 | 9.1389 | 1.4590 | 0.6649 | 0.6649 |
| `base|emb=12|sh=0.97` | 18 | 0.5500 | 0.9968 | 1.0000 | 1.0701 | 8.4921 | 1.2246 | 0.6649 | 0.6649 |
| `base|emb=12|sh=0.96` | 18 | 0.5500 | 0.9972 | 1.0000 | 1.0701 | 8.4921 | 1.2246 | 0.6648 | 0.6648 |
| `base|emb=12|sh=0.95` | 18 | 0.5500 | 0.9977 | 1.0000 | 1.0701 | 8.4921 | 1.2246 | 0.6647 | 0.6647 |
| `base|emb=12|sh=0.94` | 18 | 0.5500 | 0.9993 | 1.0000 | 1.0701 | 8.4921 | 1.2246 | 0.6641 | 0.6641 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5573 | 0.9945 | 0.3071 | 1.2020 | 11.4077 | 2.1300 | 0.6517 | 0.6517 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5573 | 0.9960 | 0.3071 | 1.2020 | 11.4077 | 2.1300 | 0.6517 | 0.6517 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5573 | 0.9952 | 0.3071 | 1.2020 | 11.4077 | 2.1300 | 0.6517 | 0.6517 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5573 | 0.9998 | 0.3071 | 1.2020 | 11.4077 | 2.1300 | 0.6506 | 0.6506 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5658 | 0.9888 | 0.3056 | 0.9501 | 5.2671 | 1.2411 | 0.6498 | 0.6498 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5658 | 0.9909 | 0.3056 | 0.9501 | 5.2671 | 1.2411 | 0.6493 | 0.6493 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5658 | 0.9895 | 0.3056 | 0.9501 | 5.2671 | 1.2411 | 0.6491 | 0.6491 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5658 | 0.9904 | 0.3056 | 0.9501 | 5.2671 | 1.2411 | 0.6485 | 0.6485 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.8428

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6756 | 0.0674 | 0.9618 | 0.0222 |
| all validations | 0.5604 | 0.0969 | 0.9955 | 0.0300 |

- improvement vs all (primary fraction): `hit +11.52pp, mae +3.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0833 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.4412 | 0.9954 | 1.0000 | 0.9825 | -0.1008 | -9.4388 | -0.6774 | 0.3659 | 0.3659 |
