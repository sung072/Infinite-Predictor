# Strict Multi-Cycle Research Result

- symbol: `MKR`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5566 | 0.9986 | 0.2731 | 1.3753 | 13.5763 | 3.0382 | 0.6612 | 0.6612 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5566 | 0.9993 | 0.2731 | 1.3753 | 13.5763 | 3.0382 | 0.6611 | 0.6611 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5566 | 1.0000 | 0.2731 | 1.3753 | 13.5763 | 3.0382 | 0.6610 | 0.6610 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5566 | 1.0010 | 0.2731 | 1.3753 | 13.5763 | 3.0382 | 0.6610 | 0.6610 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5211 | 0.9959 | 0.4552 | 1.1239 | 2.8319 | 0.8052 | 0.5842 | 0.5842 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5211 | 0.9955 | 0.4552 | 1.1239 | 2.8319 | 0.8052 | 0.5842 | 0.5842 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5211 | 0.9968 | 0.4552 | 1.1239 | 2.8319 | 0.8052 | 0.5841 | 0.5841 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5211 | 0.9995 | 0.4552 | 1.1239 | 2.8319 | 0.8052 | 0.5833 | 0.5833 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4666 | 1.0081 | 0.3395 | 1.0974 | -8.5100 | 1.0273 | 0.5744 | 0.5744 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4666 | 1.0120 | 0.3395 | 1.0974 | -8.5100 | 1.0273 | 0.5730 | 0.5730 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4666 | 1.0160 | 0.3395 | 1.0974 | -8.5100 | 1.0273 | 0.5717 | 0.5717 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4666 | 1.0204 | 0.3395 | 1.0974 | -8.5100 | 1.0273 | 0.5703 | 0.5703 |
| `base|emb=12|sh=0.97` | 18 | 0.5080 | 1.0006 | 1.0000 | 1.0729 | 1.0928 | 0.5128 | 0.5522 | 0.5522 |
| `base|emb=12|sh=0.96` | 18 | 0.5080 | 1.0020 | 1.0000 | 1.0729 | 1.0928 | 0.5128 | 0.5517 | 0.5517 |
| `base|emb=12|sh=0.95` | 18 | 0.5080 | 1.0038 | 1.0000 | 1.0729 | 1.0928 | 0.5128 | 0.5510 | 0.5510 |
| `base|emb=12|sh=0.94` | 18 | 0.5080 | 1.0065 | 1.0000 | 1.0729 | 1.0928 | 0.5128 | 0.5501 | 0.5501 |
| `base|emb=24|sh=0.97` | 18 | 0.4930 | 1.0046 | 1.0000 | 1.0096 | -2.7843 | 0.5622 | 0.5436 | 0.5436 |
| `base|emb=24|sh=0.96` | 18 | 0.4930 | 1.0073 | 1.0000 | 1.0096 | -2.7843 | 0.5622 | 0.5426 | 0.5426 |
| `base|emb=24|sh=0.95` | 18 | 0.4930 | 1.0105 | 1.0000 | 1.0096 | -2.7843 | 0.5622 | 0.5415 | 0.5415 |
| `base|emb=24|sh=0.94` | 18 | 0.4930 | 1.0145 | 1.0000 | 1.0096 | -2.7843 | 0.5622 | 0.5400 | 0.5400 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=336, top_n=34, cutoff=0.8328

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6657 | 0.0892 | 0.9714 | 0.0262 |
| all validations | 0.5025 | 0.1312 | 1.0071 | 0.0348 |

- improvement vs all (primary fraction): `hit +16.31pp, mae +3.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.4286 | 1.0049 | 1.0000 | 0.9650 | -0.1238 | -11.5873 | -0.4822 | 0.3646 | 0.3646 |
| 2 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4000 | 1.0046 | 0.4167 | 0.4616 | -0.4363 | -40.8359 | -0.9625 | 0.3200 | 0.3200 |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4000 | 1.0062 | 0.4167 | 0.4616 | -0.4363 | -40.8359 | -0.9625 | 0.3194 | 0.3194 |
| 4 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4000 | 1.0077 | 0.4167 | 0.4616 | -0.4363 | -40.8359 | -0.9625 | 0.3188 | 0.3188 |
| 5 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4000 | 1.0093 | 0.4167 | 0.4616 | -0.4363 | -40.8359 | -0.9625 | 0.3182 | 0.3182 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 0.9759 | 1.2294 | 8.4662 | 0.2660 |
| 1 | 7 | 0.2857 | 1.0165 | 0.2850 | -79.6546 | -1.0953 |
| 2 | 7 | 0.1429 | 1.0416 | 1.0841 | -63.8528 | -1.0758 |
| 3 | 7 | 0.8333 | 0.9184 | 1.4230 | 75.7369 | 6.1545 |
| 4 | 7 | 0.4286 | 1.0247 | 4.5434 | 41.4727 | 4.4173 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 0.9759 | 1.2294 | 8.4662 | 0.2660 |
| top_20pct | 8 | 0.5000 | 1.0169 | 3.9716 | 48.0980 | 5.4790 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.3750 | 1.0025 | 0.8964 | -26.2303 | -0.7595 |
| 1 | 7 | 0.2857 | 1.0125 | 1.4550 | -18.5847 | -1.2779 |
| 2 | 7 | 0.4286 | 0.9853 | 0.4444 | -42.7836 | -1.6158 |
| 3 | 7 | 0.4286 | 1.0427 | 0.3954 | -36.4500 | -0.7124 |
| 4 | 7 | 0.6667 | 0.9786 | 2.9005 | 67.4030 | 6.0787 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.3750 | 1.0025 | 0.8964 | -26.2303 | -0.7595 |
| top_20pct | 8 | 0.5714 | 0.9980 | 3.1852 | 53.6212 | 5.6020 |

