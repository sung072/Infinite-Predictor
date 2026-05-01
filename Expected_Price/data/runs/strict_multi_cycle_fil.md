# Strict Multi-Cycle Research Result

- symbol: `FIL`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5308 | 1.0045 | 0.3086 | 1.2923 | 5.9017 | 1.7470 | 0.6132 | 0.6132 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5308 | 1.0063 | 0.3086 | 1.2923 | 5.9017 | 1.7470 | 0.6132 | 0.6132 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5308 | 1.0095 | 0.3086 | 1.2923 | 5.9017 | 1.7470 | 0.6128 | 0.6128 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5308 | 1.0143 | 0.3086 | 1.2923 | 5.9017 | 1.7470 | 0.6123 | 0.6123 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4380 | 1.0253 | 0.3194 | 1.2702 | -4.7730 | 0.5132 | 0.5752 | 0.5752 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4380 | 1.0344 | 0.3194 | 1.2702 | -4.7730 | 0.5132 | 0.5724 | 0.5724 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4380 | 1.0444 | 0.3194 | 1.2702 | -4.7730 | 0.5132 | 0.5696 | 0.5696 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4380 | 1.0553 | 0.3194 | 1.2702 | -4.7730 | 0.5132 | 0.5666 | 0.5666 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5542 | 0.9989 | 0.4259 | 0.8958 | 5.8014 | 0.7874 | 0.5472 | 0.5472 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5542 | 0.9991 | 0.4259 | 0.8958 | 5.8014 | 0.7874 | 0.5470 | 0.5470 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5542 | 0.9993 | 0.4259 | 0.8958 | 5.8014 | 0.7874 | 0.5469 | 0.5469 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5542 | 0.9994 | 0.4259 | 0.8958 | 5.8014 | 0.7874 | 0.5467 | 0.5467 |
| `base|emb=24|sh=0.97` | 18 | 0.5127 | 1.0030 | 1.0000 | 0.9566 | -0.5890 | 0.6040 | 0.5354 | 0.5354 |
| `base|emb=24|sh=0.96` | 18 | 0.5127 | 1.0042 | 1.0000 | 0.9566 | -0.5890 | 0.6040 | 0.5350 | 0.5350 |
| `base|emb=24|sh=0.95` | 18 | 0.5127 | 1.0056 | 1.0000 | 0.9566 | -0.5890 | 0.6040 | 0.5346 | 0.5346 |
| `base|emb=24|sh=0.94` | 18 | 0.5127 | 1.0076 | 1.0000 | 0.9566 | -0.5890 | 0.6040 | 0.5339 | 0.5339 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5038 | 1.0020 | 0.4012 | 0.8802 | -4.6077 | 0.1836 | 0.5252 | 0.5252 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5038 | 1.0027 | 0.4012 | 0.8802 | -4.6077 | 0.1836 | 0.5250 | 0.5250 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5038 | 1.0034 | 0.4012 | 0.8802 | -4.6077 | 0.1836 | 0.5248 | 0.5248 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5038 | 1.0041 | 0.4012 | 0.8802 | -4.6077 | 0.1836 | 0.5247 | 0.5247 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=372, top_n=38, cutoff=0.8351

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7605 | 0.0795 | 0.9832 | 0.0387 |
| all validations | 0.5106 | 0.1425 | 1.0088 | 0.0459 |

- improvement vs all (primary fraction): `hit +24.99pp, mae +2.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.6562 | 0.9859 | 1.0000 | 0.6261 | 0.0675 | 6.3192 | 0.4168 | 0.7273 | 0.7273 |
| 2 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6538 | 0.9771 | 0.8056 | 0.5020 | -0.0203 | -1.9004 | -0.1460 | 0.4761 | 0.4761 |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6538 | 0.9798 | 0.8056 | 0.5020 | -0.0203 | -1.9004 | -0.1460 | 0.4749 | 0.4749 |
| 4 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6538 | 0.9839 | 0.8056 | 0.5020 | -0.0203 | -1.9004 | -0.1460 | 0.4733 | 0.4733 |
| 5 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6538 | 0.9879 | 0.8056 | 0.5020 | -0.0203 | -1.9004 | -0.1460 | 0.4716 | 0.4716 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.1667 | 1.0525 | 0.4120 | -66.7496 | -2.4480 |
| 1 | 7 | 0.5714 | 0.9893 | 0.2830 | -33.0155 | -1.0976 |
| 2 | 7 | 0.7143 | 0.9770 | 0.7130 | 21.9350 | 1.2047 |
| 3 | 7 | 0.8333 | 0.9646 | 1.0324 | 68.1795 | 4.1886 |
| 4 | 7 | 1.0000 | 0.9672 | n/a | 152.0216 | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.1667 | 1.0525 | 0.4120 | -66.7496 | -2.4480 |
| top_20pct | 8 | 1.0000 | 0.9624 | n/a | 140.3698 | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.4286 | 1.0067 | 1.2074 | -3.7443 | -0.1205 |
| 1 | 7 | 1.0000 | 0.9446 | n/a | 159.4779 | n/a |
| 2 | 7 | 0.8333 | 0.9165 | 0.8098 | 58.7022 | 3.0611 |
| 3 | 7 | 0.7143 | 0.9873 | 0.4275 | 2.4314 | 0.0831 |
| 4 | 7 | 0.4286 | 1.0133 | 0.6695 | -26.1141 | -0.7398 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.4286 | 1.0067 | 1.2074 | -3.7443 | -0.1205 |
| top_20pct | 8 | 0.5000 | 1.0013 | 0.7088 | -13.3288 | -0.4471 |

