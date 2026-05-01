# Strict Multi-Cycle Research Result

- symbol: `U`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `base|emb=24|sh=0.94` | 18 | 0.7432 | 1.0001 | 1.0000 | 1.1378 | 59.0636 | 7.7781 | 0.8219 | 0.8219 |
| `base|emb=24|sh=0.95` | 18 | 0.7432 | 1.0001 | 1.0000 | 1.1378 | 59.0636 | 7.7781 | 0.8219 | 0.8219 |
| `base|emb=24|sh=0.96` | 18 | 0.7432 | 1.0000 | 1.0000 | 1.1378 | 59.0636 | 7.7781 | 0.8219 | 0.8219 |
| `base|emb=24|sh=0.97` | 18 | 0.7432 | 1.0000 | 1.0000 | 1.1378 | 59.0636 | 7.7781 | 0.8219 | 0.8219 |
| `base|emb=12|sh=0.97` | 18 | 0.7367 | 1.0008 | 1.0000 | 1.1015 | 55.4039 | 6.6892 | 0.8181 | 0.8181 |
| `base|emb=12|sh=0.96` | 18 | 0.7367 | 1.0011 | 1.0000 | 1.1015 | 55.4039 | 6.6892 | 0.8180 | 0.8180 |
| `base|emb=12|sh=0.95` | 18 | 0.7367 | 1.0013 | 1.0000 | 1.1015 | 55.4039 | 6.6892 | 0.8179 | 0.8179 |
| `base|emb=12|sh=0.94` | 18 | 0.7367 | 1.0016 | 1.0000 | 1.1015 | 55.4039 | 6.6892 | 0.8178 | 0.8178 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7464 | 0.9957 | 0.4259 | 1.1373 | 108106.4485 | 5.2142 | 0.8018 | 0.8018 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7464 | 0.9964 | 0.4259 | 1.1373 | 108106.4485 | 5.2142 | 0.8015 | 0.8015 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7464 | 0.9971 | 0.4259 | 1.1373 | 108106.4485 | 5.2142 | 0.8012 | 0.8012 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7464 | 0.9979 | 0.4259 | 1.1373 | 108106.4485 | 5.2142 | 0.8009 | 0.8009 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7144 | 0.9993 | 0.3843 | 1.1674 | 50.0032 | 4.7752 | 0.7722 | 0.7722 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7144 | 0.9994 | 0.3843 | 1.1674 | 50.0032 | 4.7752 | 0.7721 | 0.7721 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7144 | 0.9995 | 0.3843 | 1.1674 | 50.0032 | 4.7752 | 0.7721 | 0.7721 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.7144 | 0.9997 | 0.3843 | 1.1674 | 50.0032 | 4.7752 | 0.7720 | 0.7720 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7109 | 1.0001 | 0.1836 | 1.0483 | 58.7629 | 2.6875 | 0.7279 | 0.7279 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7109 | 1.0001 | 0.1836 | 1.0483 | 58.7629 | 2.6875 | 0.7278 | 0.7278 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7109 | 1.0001 | 0.1836 | 1.0483 | 58.7629 | 2.6875 | 0.7278 | 0.7278 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.7109 | 1.0000 | 0.1836 | 1.0483 | 58.7629 | 2.6875 | 0.7277 | 0.7277 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8825

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.8769 | 0.0293 | 0.9941 | 0.0055 |
| all validations | 0.7221 | 0.1509 | 1.0000 | 0.0138 |

- improvement vs all (primary fraction): `hit +15.47pp, mae +0.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.94` | 0.7500 | 0.9957 | 1.0000 | 1.1905 | 0.5797 | 54.2558 | 6.0046 | 0.8547 | 0.8547 |
| 2 | `base|emb=24|sh=0.95` | 0.7500 | 0.9964 | 1.0000 | 1.1905 | 0.5797 | 54.2558 | 6.0046 | 0.8545 | 0.8545 |
| 3 | `base|emb=24|sh=0.96` | 0.7500 | 0.9971 | 1.0000 | 1.1905 | 0.5797 | 54.2558 | 6.0046 | 0.8542 | 0.8542 |
| 4 | `base|emb=24|sh=0.97` | 0.7500 | 0.9978 | 1.0000 | 1.1905 | 0.5797 | 54.2558 | 6.0046 | 0.8539 | 0.8539 |
| 5 | `base|emb=12|sh=0.97` | 0.6190 | 1.0108 | 1.0000 | 1.0256 | 0.2402 | 22.4858 | 2.0002 | 0.7772 | 0.7772 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1.0000 | 1.0034 | n/a | 171.0493 | n/a |
| 1 | 7 | 0.6000 | 1.0068 | 1.9999 | 41.8562 | 3.9994 |
| 2 | 7 | 0.6667 | 0.9801 | 0.6666 | 11.7334 | 0.4996 |
| 3 | 7 | 1.0000 | 1.0163 | n/a | 1872224.9996 | n/a |
| 4 | 7 | 0.6000 | 0.9763 | 1.3332 | 27.9007 | 1.9994 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 1.0000 | 1.0034 | n/a | 171.0493 | n/a |
| top_20pct | 8 | 0.6000 | 0.9833 | 1.3332 | 27.9007 | 1.9994 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6667 | 0.9888 | 1.2500 | 38.2099 | 2.9999 |
| 1 | 7 | 0.8000 | 0.9842 | 0.5000 | 27.9046 | 0.9999 |
| 2 | 7 | 0.6667 | 0.9965 | 1.2501 | 38.2130 | 3.0001 |
| 3 | 7 | 0.8000 | 0.9860 | 2.0002 | 78.3057 | n/a |
| 4 | 7 | 1.0000 | 1.0618 | n/a | n/a | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6667 | 0.9888 | 1.2500 | 38.2099 | 2.9999 |
| top_20pct | 8 | 1.0000 | 1.0938 | n/a | n/a | n/a |

