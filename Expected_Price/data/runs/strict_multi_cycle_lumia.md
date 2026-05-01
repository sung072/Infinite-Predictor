# Strict Multi-Cycle Research Result

- symbol: `LUMIA`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5580 | 0.9965 | 0.3873 | 1.1623 | 4.7433 | 1.3604 | 0.6206 | 0.6206 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5580 | 0.9971 | 0.3873 | 1.1623 | 4.7433 | 1.3604 | 0.6203 | 0.6203 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5580 | 0.9977 | 0.3873 | 1.1623 | 4.7433 | 1.3604 | 0.6200 | 0.6200 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5580 | 0.9983 | 0.3873 | 1.1623 | 4.7433 | 1.3604 | 0.6197 | 0.6197 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5237 | 0.9979 | 0.3889 | 1.0248 | 3.4485 | 1.1032 | 0.6000 | 0.6000 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5237 | 0.9982 | 0.3889 | 1.0248 | 3.4485 | 1.1032 | 0.5998 | 0.5998 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5237 | 0.9986 | 0.3889 | 1.0248 | 3.4485 | 1.1032 | 0.5996 | 0.5996 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5237 | 0.9989 | 0.3889 | 1.0248 | 3.4485 | 1.1032 | 0.5994 | 0.5994 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5271 | 0.9820 | 0.3349 | 0.9010 | -4.2951 | 0.8842 | 0.5790 | 0.5790 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5271 | 0.9818 | 0.3349 | 0.9010 | -4.2951 | 0.8842 | 0.5790 | 0.5790 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5271 | 0.9831 | 0.3349 | 0.9010 | -4.2951 | 0.8842 | 0.5787 | 0.5787 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5271 | 0.9840 | 0.3349 | 0.9010 | -4.2951 | 0.8842 | 0.5780 | 0.5780 |
| `base|emb=24|sh=0.95` | 18 | 0.5308 | 0.9957 | 1.0000 | 0.9502 | 2.0492 | 0.9300 | 0.5742 | 0.5742 |
| `base|emb=24|sh=0.96` | 18 | 0.5308 | 0.9956 | 1.0000 | 0.9502 | 2.0492 | 0.9300 | 0.5741 | 0.5741 |
| `base|emb=24|sh=0.94` | 18 | 0.5308 | 0.9965 | 1.0000 | 0.9502 | 2.0492 | 0.9300 | 0.5739 | 0.5739 |
| `base|emb=24|sh=0.97` | 18 | 0.5308 | 0.9961 | 1.0000 | 0.9502 | 2.0492 | 0.9300 | 0.5739 | 0.5739 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5146 | 0.9781 | 0.3102 | 0.9706 | -1.4428 | 0.1021 | 0.5447 | 0.5447 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5146 | 0.9781 | 0.3102 | 0.9706 | -1.4428 | 0.1021 | 0.5446 | 0.5446 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5146 | 0.9797 | 0.3102 | 0.9706 | -1.4428 | 0.1021 | 0.5438 | 0.5438 |
| `base|emb=12|sh=0.95` | 18 | 0.5282 | 0.9943 | 1.0000 | 0.9063 | -0.5248 | 0.5877 | 0.5427 | 0.5427 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.8322

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6673 | 0.0951 | 0.9919 | 0.0149 |
| all validations | 0.5312 | 0.1299 | 0.9925 | 0.0228 |

- improvement vs all (primary fraction): `hit +13.61pp, mae +0.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.95` | 0.4000 | 1.0772 | 1.0000 | 1.6419 | 0.0231 | 2.1625 | 0.0181 | 0.6193 | 0.6193 |
| 2 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4118 | 1.0243 | 0.4722 | 1.1890 | -0.0701 | -6.5596 | -0.2863 | 0.3736 | 0.3736 |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4118 | 1.0385 | 0.4722 | 1.1890 | -0.0701 | -6.5596 | -0.2863 | 0.3682 | 0.3682 |
| 4 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4118 | 1.0536 | 0.4722 | 1.1890 | -0.0701 | -6.5596 | -0.2863 | 0.3627 | 0.3627 |
| 5 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4118 | 1.0687 | 0.4722 | 1.1890 | -0.0701 | -6.5596 | -0.2863 | 0.3574 | 0.3574 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.2857 | 1.0203 | 0.5365 | -67.2270 | -1.2004 |
| 1 | 7 | 0.4286 | 1.0404 | 1.8128 | 10.0667 | 0.3531 |
| 2 | 7 | 0.4286 | 1.0087 | 0.6596 | -25.7260 | -0.9545 |
| 3 | 7 | 0.5714 | 1.0617 | 7.7615 | 33.1593 | 10.0864 |
| 4 | 7 | 0.2857 | 1.5104 | 0.1376 | -96.1221 | -0.9911 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.2857 | 1.0203 | 0.5365 | -67.2270 | -1.2004 |
| top_20pct | 8 | 0.2500 | 1.4911 | 0.1375 | -108.1931 | -1.1929 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6250 | 0.9922 | 2.3340 | 29.8010 | 3.2065 |
| 1 | 7 | 0.3333 | 1.3008 | 0.6899 | -42.1449 | -1.1023 |
| 2 | 7 | 0.4286 | 1.4939 | 0.2931 | -44.4954 | -0.8215 |
| 3 | 7 | 0.1429 | 1.0869 | 2.5701 | -29.7308 | -0.7302 |
| 4 | 7 | 0.4286 | 1.0167 | 0.7598 | -20.7729 | -0.4563 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6250 | 0.9922 | 2.3340 | 29.8010 | 3.2065 |
| top_20pct | 8 | 0.3750 | 1.0373 | 0.7853 | -28.6058 | -0.5987 |

