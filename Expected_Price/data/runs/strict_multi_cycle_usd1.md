# Strict Multi-Cycle Research Result

- symbol: `USD1`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7718 | 1.0027 | 0.3040 | 1.1362 | 179966.6461 | 5.3585 | 0.8096 | 0.8096 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7718 | 1.0036 | 0.3040 | 1.1362 | 179966.6461 | 5.3585 | 0.8092 | 0.8092 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7718 | 1.0045 | 0.3040 | 1.1362 | 179966.6461 | 5.3585 | 0.8089 | 0.8089 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7718 | 1.0054 | 0.3040 | 1.1362 | 179966.6461 | 5.3585 | 0.8086 | 0.8086 |
| `base|emb=12|sh=0.97` | 18 | 0.6829 | 1.0048 | 1.0000 | 1.0592 | 37.3904 | 5.4452 | 0.8058 | 0.8058 |
| `base|emb=12|sh=0.96` | 18 | 0.6829 | 1.0065 | 1.0000 | 1.0592 | 37.3904 | 5.4452 | 0.8052 | 0.8052 |
| `base|emb=12|sh=0.95` | 18 | 0.6829 | 1.0081 | 1.0000 | 1.0592 | 37.3904 | 5.4452 | 0.8046 | 0.8046 |
| `base|emb=12|sh=0.94` | 18 | 0.6829 | 1.0097 | 1.0000 | 1.0592 | 37.3904 | 5.4452 | 0.8040 | 0.8040 |
| `base|emb=24|sh=0.97` | 18 | 0.6569 | 1.0074 | 1.0000 | 1.0780 | 32.2328 | 5.4164 | 0.7751 | 0.7751 |
| `base|emb=24|sh=0.96` | 18 | 0.6569 | 1.0098 | 1.0000 | 1.0780 | 32.2328 | 5.4164 | 0.7742 | 0.7742 |
| `base|emb=24|sh=0.95` | 18 | 0.6569 | 1.0123 | 1.0000 | 1.0780 | 32.2328 | 5.4164 | 0.7733 | 0.7733 |
| `base|emb=24|sh=0.94` | 18 | 0.6569 | 1.0147 | 1.0000 | 1.0780 | 32.2328 | 5.4164 | 0.7724 | 0.7724 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6885 | 1.0046 | 0.3349 | 1.1803 | 197156.8157 | 4.2717 | 0.7596 | 0.7596 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6885 | 1.0061 | 0.3349 | 1.1803 | 197156.8157 | 4.2717 | 0.7591 | 0.7591 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6885 | 1.0076 | 0.3349 | 1.1803 | 197156.8157 | 4.2717 | 0.7585 | 0.7585 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6885 | 1.0092 | 0.3349 | 1.1803 | 197156.8157 | 4.2717 | 0.7580 | 0.7580 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6648 | 1.0045 | 0.4660 | 1.1039 | 36.6610 | 3.6729 | 0.7529 | 0.7529 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6648 | 1.0061 | 0.4660 | 1.1039 | 36.6610 | 3.6729 | 0.7524 | 0.7524 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6648 | 1.0076 | 0.4660 | 1.1039 | 36.6610 | 3.6729 | 0.7518 | 0.7518 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6648 | 1.0091 | 0.4660 | 1.1039 | 36.6610 | 3.6729 | 0.7513 | 0.7513 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=316, top_n=32, cutoff=0.8631

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.8324 | 0.0285 | 0.9949 | 0.0085 |
| all validations | 0.6731 | 0.1489 | 1.0101 | 0.0297 |

- improvement vs all (primary fraction): `hit +15.94pp, mae +1.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.7778 | 0.9895 | 1.0000 | 1.2857 | 0.6736 | 63.0457 | 21.0143 | 0.8704 | 0.8704 |
