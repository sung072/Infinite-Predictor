# Strict Multi-Cycle Research Result

- symbol: `PEPE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5867 | 0.9899 | 0.4784 | 1.2761 | 16.9569 | 2.7076 | 0.6697 | 0.6697 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6263 | 0.9949 | 0.4784 | 1.2525 | 29.5888 | 2.3719 | 0.6694 | 0.6694 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5985 | 0.9916 | 0.4784 | 1.2032 | 21.4880 | 2.8262 | 0.6603 | 0.6603 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6172 | 0.9933 | 0.4784 | 1.2912 | 27.8703 | 2.5465 | 0.6522 | 0.6522 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5880 | 0.9967 | 0.4815 | 1.1084 | 12.9833 | 1.7643 | 0.6501 | 0.6501 |
| `base|emb=12|sh=0.94` | 18 | 0.5459 | 0.9992 | 1.0000 | 1.0791 | 7.2734 | 0.7442 | 0.6419 | 0.6419 |
| `base|emb=12|sh=0.95` | 18 | 0.5492 | 0.9991 | 1.0000 | 1.0622 | 7.0769 | 0.7289 | 0.6256 | 0.6256 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5633 | 0.9945 | 0.4815 | 1.1894 | 13.2966 | 2.1551 | 0.6131 | 0.6131 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5683 | 0.9956 | 0.4815 | 1.1563 | 9.9698 | 1.8757 | 0.6097 | 0.6097 |
| `base|emb=12|sh=0.96` | 18 | 0.5510 | 0.9991 | 1.0000 | 1.0470 | 6.4158 | 0.6113 | 0.6094 | 0.6094 |
| `base|emb=12|sh=0.97` | 18 | 0.5449 | 0.9993 | 1.0000 | 1.0670 | 6.3049 | 0.5237 | 0.6091 | 0.6091 |
| `base|emb=24|sh=0.94` | 18 | 0.5263 | 1.0062 | 1.0000 | 1.0518 | 4.0457 | 0.4091 | 0.6087 | 0.6087 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5481 | 0.9933 | 0.4815 | 1.2000 | 10.6212 | 2.0707 | 0.6083 | 0.6083 |
| `base|emb=24|sh=0.97` | 18 | 0.5313 | 1.0030 | 1.0000 | 1.0092 | 2.9821 | 0.2811 | 0.6012 | 0.6012 |
| `base|emb=24|sh=0.96` | 18 | 0.5375 | 1.0039 | 1.0000 | 1.0096 | 3.7510 | 0.3842 | 0.5889 | 0.5889 |
| `base|emb=24|sh=0.95` | 18 | 0.5314 | 1.0050 | 1.0000 | 1.0304 | 3.9501 | 0.4100 | 0.5681 | 0.5681 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5368 | 1.0494 | 0.2685 | 0.9813 | 10.1043 | 0.0774 | 0.5678 | 0.5678 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5381 | 1.0408 | 0.2685 | 0.9437 | 6.5972 | 0.0101 | 0.5511 | 0.5511 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5421 | 1.0325 | 0.2685 | 0.9483 | 12.1485 | 0.0831 | 0.5477 | 0.5477 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5332 | 1.0244 | 0.2685 | 0.9727 | -3.4630 | 0.1072 | 0.5379 | 0.5379 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8426

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6842 | 0.0722 | 0.9813 | 0.0110 |
| all validations | 0.5495 | 0.1440 | 1.0084 | 0.0521 |

- improvement vs all (primary fraction): `hit +13.47pp, mae +2.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.94` | 0.5833 | 0.9899 | 1.0000 | 0.7762 | 0.0312 | 2.9217 | 0.1602 | 0.6766 | 0.6766 |
