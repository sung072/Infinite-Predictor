# Strict Multi-Cycle Research Result

- symbol: `TRX`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5450 | 1.0030 | 0.3719 | 1.3384 | 14.7326 | 1.7736 | 0.7011 | 0.7011 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5450 | 1.0040 | 0.3719 | 1.3384 | 14.7326 | 1.7736 | 0.7009 | 0.7009 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5450 | 1.0052 | 0.3719 | 1.3384 | 14.7326 | 1.7736 | 0.7007 | 0.7007 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5450 | 1.0071 | 0.3719 | 1.3384 | 14.7326 | 1.7736 | 0.7003 | 0.7003 |
| `base|emb=12|sh=0.97` | 18 | 0.5278 | 1.0044 | 1.0000 | 1.0596 | 5.1785 | 0.7676 | 0.6197 | 0.6197 |
| `base|emb=12|sh=0.96` | 18 | 0.5278 | 1.0059 | 1.0000 | 1.0596 | 5.1785 | 0.7676 | 0.6191 | 0.6191 |
| `base|emb=12|sh=0.95` | 18 | 0.5278 | 1.0077 | 1.0000 | 1.0596 | 5.1785 | 0.7676 | 0.6185 | 0.6185 |
| `base|emb=12|sh=0.94` | 18 | 0.5278 | 1.0102 | 1.0000 | 1.0596 | 5.1785 | 0.7676 | 0.6175 | 0.6175 |
| `base|emb=24|sh=0.97` | 18 | 0.5211 | 1.0059 | 1.0000 | 1.1641 | 7.0089 | 0.8768 | 0.6054 | 0.6054 |
| `base|emb=24|sh=0.96` | 18 | 0.5211 | 1.0079 | 1.0000 | 1.1641 | 7.0089 | 0.8768 | 0.6046 | 0.6046 |
| `base|emb=24|sh=0.95` | 18 | 0.5211 | 1.0100 | 1.0000 | 1.1641 | 7.0089 | 0.8768 | 0.6038 | 0.6038 |
| `base|emb=24|sh=0.94` | 18 | 0.5211 | 1.0127 | 1.0000 | 1.1641 | 7.0089 | 0.8768 | 0.6028 | 0.6028 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5097 | 1.0202 | 0.3688 | 1.2618 | 7.3351 | 1.5045 | 0.5956 | 0.5956 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5097 | 1.0269 | 0.3688 | 1.2618 | 7.3351 | 1.5045 | 0.5934 | 0.5934 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5097 | 1.0338 | 0.3688 | 1.2618 | 7.3351 | 1.5045 | 0.5914 | 0.5914 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5097 | 1.0425 | 0.3688 | 1.2618 | 7.3351 | 1.5045 | 0.5887 | 0.5887 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4889 | 1.0097 | 0.3472 | 1.0400 | -3.0298 | 0.3276 | 0.5758 | 0.5758 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4889 | 1.0129 | 0.3472 | 1.0400 | -3.0298 | 0.3276 | 0.5746 | 0.5746 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4889 | 1.0163 | 0.3472 | 1.0400 | -3.0298 | 0.3276 | 0.5735 | 0.5735 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4889 | 1.0197 | 0.3472 | 1.0400 | -3.0298 | 0.3276 | 0.5724 | 0.5724 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=368, top_n=37, cutoff=0.8360

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6828 | 0.0492 | 0.9733 | 0.0158 |
| all validations | 0.5156 | 0.1113 | 1.0133 | 0.0363 |

- improvement vs all (primary fraction): `hit +16.72pp, mae +3.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.5000 | 1.0059 | 1.0000 | 1.1678 | 0.0630 | 5.8988 | 0.5318 | 0.7150 | 0.7150 |
| 2 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3636 | 1.0183 | 0.3333 | 0.8063 | -0.3270 | -30.6024 | -1.2737 | 0.3148 | 0.3148 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3636 | 1.0245 | 0.3333 | 0.8063 | -0.3270 | -30.6024 | -1.2737 | 0.3125 | 0.3125 |
| 4 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3636 | 1.0306 | 0.3333 | 0.8063 | -0.3270 | -30.6024 | -1.2737 | 0.3102 | 0.3102 |
| 5 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.3636 | 1.0367 | 0.3333 | 0.8063 | -0.3270 | -30.6024 | -1.2737 | 0.3079 | 0.3079 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5714 | 0.9906 | 1.3112 | 20.3575 | 1.1950 |
| 1 | 7 | 0.6667 | 0.9881 | 1.3005 | 35.0650 | 1.6012 |
| 2 | 7 | 0.1667 | 1.0172 | 2.5071 | -23.8317 | -1.1015 |
| 3 | 7 | 0.6000 | 0.9857 | 0.8567 | 10.2473 | 0.4955 |
| 4 | 7 | 0.5000 | 1.0464 | 1.5075 | 16.0577 | 0.7600 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5714 | 0.9906 | 1.3112 | 20.3575 | 1.1950 |
| top_20pct | 8 | 0.6000 | 1.0143 | 1.2286 | 24.3788 | 1.2641 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6667 | 0.9816 | 1.7536 | 43.7377 | 3.0112 |
| 1 | 7 | 0.5714 | 0.9876 | 3.1880 | 48.5648 | 6.5062 |
| 2 | 7 | 0.3333 | 1.0165 | 0.3992 | -67.9639 | -1.3344 |
| 3 | 7 | 0.6000 | 1.0135 | 0.9536 | 14.6559 | 0.4295 |
| 4 | 7 | 0.2500 | 1.0403 | 0.9391 | -39.2180 | -0.6881 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6667 | 0.9816 | 1.7536 | 43.7377 | 3.0112 |
| top_20pct | 8 | 0.4000 | 1.0216 | 0.8430 | -20.4091 | -0.5405 |

