# Strict Multi-Cycle Research Result

- symbol: `JST`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4133 | 1.0148 | 0.4182 | 1.3693 | -6.2908 | 0.3053 | 0.5278 | 0.5278 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4133 | 1.0205 | 0.4182 | 1.3693 | -6.2908 | 0.3053 | 0.5259 | 0.5259 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4133 | 1.0266 | 0.4182 | 1.3693 | -6.2908 | 0.3053 | 0.5239 | 0.5239 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4133 | 1.0331 | 0.4182 | 1.3693 | -6.2908 | 0.3053 | 0.5219 | 0.5219 |
| `base|emb=24|sh=0.97` | 18 | 0.4448 | 1.0095 | 1.0000 | 1.1752 | -4.1270 | 0.2853 | 0.4931 | 0.4931 |
| `base|emb=24|sh=0.96` | 18 | 0.4448 | 1.0135 | 1.0000 | 1.1752 | -4.1270 | 0.2853 | 0.4916 | 0.4916 |
| `base|emb=24|sh=0.95` | 18 | 0.4448 | 1.0177 | 1.0000 | 1.1752 | -4.1270 | 0.2853 | 0.4901 | 0.4901 |
| `base|emb=12|sh=0.97` | 18 | 0.4413 | 1.0108 | 1.0000 | 1.0567 | -8.1552 | -0.1073 | 0.4895 | 0.4895 |
| `base|emb=24|sh=0.94` | 18 | 0.4448 | 1.0227 | 1.0000 | 1.1752 | -4.1270 | 0.2853 | 0.4884 | 0.4884 |
| `base|emb=12|sh=0.96` | 18 | 0.4413 | 1.0153 | 1.0000 | 1.0567 | -8.1552 | -0.1073 | 0.4879 | 0.4879 |
| `base|emb=12|sh=0.95` | 18 | 0.4413 | 1.0202 | 1.0000 | 1.0567 | -8.1552 | -0.1073 | 0.4861 | 0.4861 |
| `base|emb=12|sh=0.94` | 18 | 0.4413 | 1.0261 | 1.0000 | 1.0567 | -8.1552 | -0.1073 | 0.4840 | 0.4840 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4230 | 1.0148 | 0.3704 | 1.1234 | -10.2082 | -0.0743 | 0.4772 | 0.4772 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4230 | 1.0207 | 0.3704 | 1.1234 | -10.2082 | -0.0743 | 0.4751 | 0.4751 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4230 | 1.0271 | 0.3704 | 1.1234 | -10.2082 | -0.0743 | 0.4730 | 0.4730 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4230 | 1.0344 | 0.3704 | 1.1234 | -10.2082 | -0.0743 | 0.4707 | 0.4707 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4127 | 1.0079 | 0.3426 | 0.9847 | -20.6010 | -0.1695 | 0.4558 | 0.4558 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4127 | 1.0105 | 0.3426 | 0.9847 | -20.6010 | -0.1695 | 0.4549 | 0.4549 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4127 | 1.0132 | 0.3426 | 0.9847 | -20.6010 | -0.1695 | 0.4540 | 0.4540 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4127 | 1.0169 | 0.3426 | 0.9847 | -20.6010 | -0.1695 | 0.4527 | 0.4527 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=384, top_n=39, cutoff=0.7989

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5861 | 0.0307 | 0.9813 | 0.0111 |
| all validations | 0.4242 | 0.1032 | 1.0185 | 0.0375 |

- improvement vs all (primary fraction): `hit +16.19pp, mae +3.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4800 | 0.9964 | 0.7222 | 1.3134 | 0.0735 | 6.8814 | 0.6286 | 0.7269 | 0.7269 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4800 | 0.9970 | 0.7222 | 1.3134 | 0.0735 | 6.8814 | 0.6286 | 0.7266 | 0.7266 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4800 | 0.9976 | 0.7222 | 1.3134 | 0.0735 | 6.8814 | 0.6286 | 0.7264 | 0.7264 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4800 | 0.9982 | 0.7222 | 1.3134 | 0.0735 | 6.8814 | 0.6286 | 0.7261 | 0.7261 |
| 5 | `base|emb=24|sh=0.97` | 0.3714 | 1.0153 | 1.0000 | 1.2698 | -0.1094 | -10.2351 | -0.7916 | 0.3528 | 0.3528 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.3333 | 1.1756 | 1.0717 | -23.0611 | -0.6188 |
| 1 | 5 | 0.2000 | 1.0780 | 0.7190 | -58.1167 | -2.5256 |
| 2 | 5 | 0.6000 | 0.9719 | 1.8675 | 37.9685 | 2.4024 |
| 3 | 5 | 0.6000 | 0.9036 | 0.9527 | 14.1070 | 0.4250 |
| 4 | 5 | n/a | n/a | n/a | n/a | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0.3333 | 1.0619 | 0.5931 | -37.1538 | -0.8191 |
| 1 | 5 | 0.8000 | 0.9278 | 1.6855 | 65.2629 | 5.7841 |
| 2 | 5 | 0.2000 | 1.0389 | 0.4952 | -89.0078 | -1.4437 |
| 3 | 5 | 0.4000 | 1.0783 | 4.6703 | 33.2994 | 2.1111 |
| 4 | 5 | n/a | n/a | n/a | n/a | n/a |

