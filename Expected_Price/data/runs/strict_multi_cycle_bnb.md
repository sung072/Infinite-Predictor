# Strict Multi-Cycle Research Result

- symbol: `BNB`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5261 | 0.9998 | 0.3735 | 1.1682 | 5.6897 | 2.3488 | 0.5726 | 0.5726 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5261 | 1.0018 | 0.3735 | 1.1682 | 5.6897 | 2.3488 | 0.5721 | 0.5721 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5261 | 1.0058 | 0.3735 | 1.1682 | 5.6897 | 2.3488 | 0.5710 | 0.5710 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5261 | 1.0111 | 0.3735 | 1.1682 | 5.6897 | 2.3488 | 0.5694 | 0.5694 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5026 | 1.0014 | 0.3580 | 1.0255 | -2.8061 | 1.9245 | 0.5171 | 0.5171 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5026 | 1.0039 | 0.3580 | 1.0255 | -2.8061 | 1.9245 | 0.5164 | 0.5164 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5026 | 1.0091 | 0.3580 | 1.0255 | -2.8061 | 1.9245 | 0.5147 | 0.5147 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5026 | 1.0158 | 0.3580 | 1.0255 | -2.8061 | 1.9245 | 0.5127 | 0.5127 |
| `base|emb=12|sh=0.97` | 18 | 0.4919 | 1.0003 | 1.0000 | 1.0169 | -1.2318 | 0.1840 | 0.5096 | 0.5096 |
| `base|emb=12|sh=0.96` | 18 | 0.4919 | 1.0014 | 1.0000 | 1.0169 | -1.2318 | 0.1840 | 0.5092 | 0.5092 |
| `base|emb=24|sh=0.97` | 18 | 0.5014 | 0.9994 | 1.0000 | 0.9683 | -1.8040 | 0.2818 | 0.5086 | 0.5086 |
| `base|emb=12|sh=0.95` | 18 | 0.4919 | 1.0033 | 1.0000 | 1.0169 | -1.2318 | 0.1840 | 0.5085 | 0.5085 |
| `base|emb=24|sh=0.96` | 18 | 0.5014 | 1.0000 | 1.0000 | 0.9683 | -1.8040 | 0.2818 | 0.5084 | 0.5084 |
| `base|emb=24|sh=0.95` | 18 | 0.5014 | 1.0014 | 1.0000 | 0.9683 | -1.8040 | 0.2818 | 0.5079 | 0.5079 |
| `base|emb=12|sh=0.94` | 18 | 0.4919 | 1.0056 | 1.0000 | 1.0169 | -1.2318 | 0.1840 | 0.5076 | 0.5076 |
| `base|emb=24|sh=0.94` | 18 | 0.5014 | 1.0032 | 1.0000 | 0.9683 | -1.8040 | 0.2818 | 0.5073 | 0.5073 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4934 | 1.0032 | 0.4367 | 0.9846 | -3.1618 | 0.1753 | 0.4962 | 0.4962 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4934 | 1.0043 | 0.4367 | 0.9846 | -3.1618 | 0.1753 | 0.4958 | 0.4958 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4934 | 1.0055 | 0.4367 | 0.9846 | -3.1618 | 0.1753 | 0.4954 | 0.4954 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4934 | 1.0066 | 0.4367 | 0.9846 | -3.1618 | 0.1753 | 0.4950 | 0.4950 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=392, top_n=40, cutoff=0.8158

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6128 | 0.0521 | 0.9839 | 0.0169 |
| all validations | 0.5025 | 0.0901 | 1.0045 | 0.0330 |

- improvement vs all (primary fraction): `hit +11.03pp, mae +2.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5652 | 0.9647 | 0.6389 | 0.8727 | 0.0458 | 4.2871 | 0.3058 | 0.7140 | 0.7140 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5652 | 0.9706 | 0.6389 | 0.8727 | 0.0458 | 4.2871 | 0.3058 | 0.7115 | 0.7115 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5652 | 0.9765 | 0.6389 | 0.8727 | 0.0458 | 4.2871 | 0.3058 | 0.7090 | 0.7090 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5652 | 0.9824 | 0.6389 | 0.8727 | 0.0458 | 4.2871 | 0.3058 | 0.7066 | 0.7066 |
| 5 | `base|emb=12|sh=0.97` | 0.5429 | 0.9860 | 1.0000 | 0.7845 | -0.0272 | -2.5467 | -0.1957 | 0.4425 | 0.4425 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 0.8000 | 0.9264 | 0.1860 | -8.8433 | -0.2616 |
| 2 | 5 | 0.6000 | 0.9714 | 1.6294 | 33.6468 | 2.7405 |
| 4 | 5 | 0.4000 | 1.0119 | 1.4961 | -0.0885 | -0.0054 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 0.4000 | 1.0883 | 1.0665 | -12.2748 | -0.8378 |
| 2 | 5 | 0.6000 | 0.9583 | 0.8708 | 9.4417 | 0.3617 |
| 4 | 5 | 0.6000 | 0.9553 | 0.5571 | -5.8364 | -0.1704 |

