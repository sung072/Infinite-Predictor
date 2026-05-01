# Strict Multi-Cycle Research Result

- symbol: `NIGHT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5645 | 0.9647 | 0.2423 | 1.5302 | 21.7760 | 1.9751 | 0.7553 | 0.7553 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5645 | 0.9695 | 0.2423 | 1.5302 | 21.7760 | 1.9751 | 0.7531 | 0.7531 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5645 | 0.9750 | 0.2423 | 1.5302 | 21.7760 | 1.9751 | 0.7507 | 0.7507 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5645 | 0.9808 | 0.2423 | 1.5302 | 21.7760 | 1.9751 | 0.7482 | 0.7482 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5606 | 0.9862 | 0.2330 | 1.3121 | 14.3409 | 1.4216 | 0.7151 | 0.7151 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5606 | 0.9871 | 0.2330 | 1.3121 | 14.3409 | 1.4216 | 0.7147 | 0.7147 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5606 | 0.9885 | 0.2330 | 1.3121 | 14.3409 | 1.4216 | 0.7142 | 0.7142 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5606 | 0.9900 | 0.2330 | 1.3121 | 14.3409 | 1.4216 | 0.7135 | 0.7135 |
| `base|emb=24|sh=0.94` | 18 | 0.5738 | 0.9895 | 1.0000 | 1.1867 | 15.9571 | 2.6394 | 0.7031 | 0.7031 |
| `base|emb=24|sh=0.95` | 18 | 0.5738 | 0.9901 | 1.0000 | 1.1867 | 15.9571 | 2.6394 | 0.7028 | 0.7028 |
| `base|emb=24|sh=0.96` | 18 | 0.5738 | 0.9912 | 1.0000 | 1.1867 | 15.9571 | 2.6394 | 0.7023 | 0.7023 |
| `base|emb=24|sh=0.97` | 18 | 0.5738 | 0.9931 | 1.0000 | 1.1867 | 15.9571 | 2.6394 | 0.7015 | 0.7015 |
| `base|emb=12|sh=0.95` | 18 | 0.5719 | 0.9943 | 1.0000 | 1.1729 | 14.4605 | 2.9638 | 0.6970 | 0.6970 |
| `base|emb=12|sh=0.94` | 18 | 0.5719 | 0.9945 | 1.0000 | 1.1729 | 14.4605 | 2.9638 | 0.6969 | 0.6969 |
| `base|emb=12|sh=0.96` | 18 | 0.5719 | 0.9945 | 1.0000 | 1.1729 | 14.4605 | 2.9638 | 0.6969 | 0.6969 |
| `base|emb=12|sh=0.97` | 18 | 0.5719 | 0.9955 | 1.0000 | 1.1729 | 14.4605 | 2.9638 | 0.6965 | 0.6965 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5538 | 0.9985 | 0.3287 | 1.1750 | 10.8262 | 1.9387 | 0.6175 | 0.6175 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5538 | 0.9988 | 0.3287 | 1.1750 | 10.8262 | 1.9387 | 0.6174 | 0.6174 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5538 | 0.9986 | 0.3287 | 1.1750 | 10.8262 | 1.9387 | 0.6174 | 0.6174 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5538 | 0.9989 | 0.3287 | 1.1750 | 10.8262 | 1.9387 | 0.6173 | 0.6173 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=292, top_n=30, cutoff=0.8612

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6570 | 0.0532 | 0.9725 | 0.0217 |
| all validations | 0.5548 | 0.0933 | 0.9943 | 0.0246 |

- improvement vs all (primary fraction): `hit +10.22pp, mae +2.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.94` | 0.5588 | 1.0304 | 1.0000 | 0.8415 | 0.0227 | 2.1246 | 0.0982 | 0.6357 | 0.6357 |
| 2 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4167 | 1.0517 | 0.3889 | 0.7264 | -0.2538 | -23.7528 | -1.0011 | 0.3171 | 0.3171 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4167 | 1.0689 | 0.3889 | 0.7264 | -0.2538 | -23.7528 | -1.0011 | 0.3110 | 0.3110 |
| 4 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4167 | 1.0861 | 0.3889 | 0.7264 | -0.2538 | -23.7528 | -1.0011 | 0.3051 | 0.3051 |
| 5 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4167 | 1.1034 | 0.3889 | 0.7264 | -0.2538 | -23.7528 | -1.0011 | 0.2993 | 0.2993 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.7500 | 0.9593 | 0.9964 | 41.8907 | 3.3828 |
| 1 | 7 | 0.5714 | 0.9704 | 0.5425 | -9.5326 | -0.3296 |
| 2 | 7 | 0.4000 | 1.1127 | 0.2326 | -51.9200 | -1.1154 |
| 3 | 7 | 0.4286 | 1.0325 | 1.5482 | 5.9130 | 0.2101 |
| 4 | 7 | 0.5714 | 1.0817 | 1.1571 | 13.7765 | 0.5470 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.7500 | 0.9593 | 0.9964 | 41.8907 | 3.3828 |
| top_20pct | 8 | 0.6250 | 1.0396 | 1.0988 | 19.7106 | 0.8490 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6667 | 0.9771 | 1.4509 | 34.9735 | 1.9021 |
| 1 | 7 | 0.7143 | 0.9247 | 3.8502 | 61.2222 | 12.5763 |
| 2 | 7 | 0.5714 | 1.0269 | 1.0164 | 11.1757 | 0.4849 |
| 3 | 7 | 0.5714 | 1.0891 | 0.4556 | -15.7301 | -0.4121 |
| 4 | 7 | 0.2857 | 1.0983 | 0.4516 | -52.8806 | -0.9158 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6667 | 0.9771 | 1.4509 | 34.9735 | 1.9021 |
| top_20pct | 8 | 0.3750 | 1.0505 | 0.5543 | -36.4730 | -0.7501 |

