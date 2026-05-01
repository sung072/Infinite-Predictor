# Strict Multi-Cycle Research Result

- symbol: `EUR`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5590 | 1.0205 | 0.3179 | 1.0316 | 9.6989 | 0.7367 | 0.6209 | 0.6209 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5590 | 1.0300 | 0.3179 | 1.0316 | 9.6989 | 0.7367 | 0.6176 | 0.6176 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5590 | 1.0449 | 0.3179 | 1.0316 | 9.6989 | 0.7367 | 0.6127 | 0.6127 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5590 | 1.0631 | 0.3179 | 1.0316 | 9.6989 | 0.7367 | 0.6069 | 0.6069 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5707 | 1.0135 | 0.3164 | 0.8890 | 3.9221 | 0.2953 | 0.5790 | 0.5790 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5707 | 1.0201 | 0.3164 | 0.8890 | 3.9221 | 0.2953 | 0.5768 | 0.5768 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5707 | 1.0296 | 0.3164 | 0.8890 | 3.9221 | 0.2953 | 0.5736 | 0.5736 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5707 | 1.0426 | 0.3164 | 0.8890 | 3.9221 | 0.2953 | 0.5693 | 0.5693 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4341 | 1.0128 | 0.3935 | 0.8902 | -12.7662 | -0.1390 | 0.5018 | 0.5018 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4341 | 1.0171 | 0.3935 | 0.8902 | -12.7662 | -0.1390 | 0.5005 | 0.5005 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4341 | 1.0215 | 0.3935 | 0.8902 | -12.7662 | -0.1390 | 0.4993 | 0.4993 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4341 | 1.0279 | 0.3935 | 0.8902 | -12.7662 | -0.1390 | 0.4974 | 0.4974 |
| `base|emb=12|sh=0.97` | 18 | 0.4842 | 1.0141 | 1.0000 | 0.9603 | -4.4193 | -0.0270 | 0.4962 | 0.4962 |
| `base|emb=12|sh=0.96` | 18 | 0.4842 | 1.0200 | 1.0000 | 0.9603 | -4.4193 | -0.0270 | 0.4941 | 0.4941 |
| `base|emb=12|sh=0.95` | 18 | 0.4842 | 1.0265 | 1.0000 | 0.9603 | -4.4193 | -0.0270 | 0.4918 | 0.4918 |
| `base|emb=12|sh=0.94` | 18 | 0.4842 | 1.0348 | 1.0000 | 0.9603 | -4.4193 | -0.0270 | 0.4889 | 0.4889 |
| `base|emb=24|sh=0.97` | 18 | 0.4842 | 1.0119 | 1.0000 | 0.9722 | -4.1448 | -0.1329 | 0.4759 | 0.4759 |
| `base|emb=24|sh=0.96` | 18 | 0.4842 | 1.0172 | 1.0000 | 0.9722 | -4.1448 | -0.1329 | 0.4739 | 0.4739 |
| `base|emb=24|sh=0.95` | 18 | 0.4842 | 1.0241 | 1.0000 | 0.9722 | -4.1448 | -0.1329 | 0.4715 | 0.4715 |
| `base|emb=24|sh=0.94` | 18 | 0.4842 | 1.0328 | 1.0000 | 0.9722 | -4.1448 | -0.1329 | 0.4686 | 0.4686 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=372, top_n=38, cutoff=0.7751

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6943 | 0.0928 | 0.9728 | 0.0507 |
| all validations | 0.4908 | 0.1428 | 1.0245 | 0.0489 |

- improvement vs all (primary fraction): `hit +20.36pp, mae +5.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.5429 | 0.9930 | 1.0000 | 0.8102 | -0.0140 | -1.3141 | -0.1227 | 0.4851 | 0.4851 |
| 2 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.0836 | 0.1667 | 0.5999 | -0.2101 | -19.6622 | -0.4002 | 0.3355 | 0.3355 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.1115 | 0.1667 | 0.5999 | -0.2101 | -19.6622 | -0.4002 | 0.3262 | 0.3262 |
| 4 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.1609 | 0.1667 | 0.5999 | -0.2101 | -19.6622 | -0.4002 | 0.3109 | 0.3109 |
| 5 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 1.2430 | 0.1667 | 0.5999 | -0.2101 | -19.6622 | -0.4002 | 0.2881 | 0.2881 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.3750 | 0.9923 | 0.4913 | -41.0220 | -0.9485 |
| 1 | 7 | 0.6667 | 0.9646 | 0.4999 | -0.0087 | -0.0014 |
| 2 | 7 | 0.4286 | 1.0170 | 3.2808 | 32.5340 | 1.8984 |
| 3 | 7 | 0.7143 | 0.9955 | 1.1092 | 42.8000 | 2.6602 |
| 4 | 7 | 0.5714 | 0.9940 | 1.6884 | 30.4326 | 1.2513 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.3750 | 0.9923 | 0.4913 | -41.0220 | -0.9485 |
| top_20pct | 8 | 0.5000 | 1.0003 | 1.5010 | 15.6249 | 0.5007 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5000 | 1.0154 | 1.3093 | 9.0762 | 0.4220 |
| 1 | 7 | 0.5714 | 0.9791 | 1.3569 | 23.3411 | 0.8090 |
| 2 | 7 | 0.5000 | 0.9777 | 0.2383 | -30.6513 | -0.8425 |
| 3 | 7 | 0.4286 | 0.9940 | 0.9371 | -14.0416 | -0.3938 |
| 4 | 7 | 0.7143 | 0.9931 | 1.0175 | 38.7903 | 2.1227 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5000 | 1.0154 | 1.3093 | 9.0762 | 0.4220 |
| top_20pct | 8 | 0.6250 | 0.9940 | 1.0494 | 23.2825 | 0.9216 |

