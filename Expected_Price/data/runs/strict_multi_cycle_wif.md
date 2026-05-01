# Strict Multi-Cycle Research Result

- symbol: `WIF`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6357 | 1.0079 | 0.2716 | 1.2963 | 35.3840 | 2.3649 | 0.7189 | 0.7189 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6357 | 1.0106 | 0.2716 | 1.2963 | 35.3840 | 2.3649 | 0.7182 | 0.7182 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6357 | 1.0132 | 0.2716 | 1.2963 | 35.3840 | 2.3649 | 0.7176 | 0.7176 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6357 | 1.0158 | 0.2716 | 1.2963 | 35.3840 | 2.3649 | 0.7171 | 0.7171 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5707 | 1.0175 | 0.2716 | 1.1421 | 11.7698 | 1.3225 | 0.6463 | 0.6463 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5707 | 1.0233 | 0.2716 | 1.1421 | 11.7698 | 1.3225 | 0.6448 | 0.6448 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5707 | 1.0292 | 0.2716 | 1.1421 | 11.7698 | 1.3225 | 0.6436 | 0.6436 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5707 | 1.0350 | 0.2716 | 1.1421 | 11.7698 | 1.3225 | 0.6426 | 0.6426 |
| `base|emb=24|sh=0.97` | 18 | 0.5351 | 1.0134 | 1.0000 | 1.0085 | 4.7853 | 0.6581 | 0.6276 | 0.6276 |
| `base|emb=24|sh=0.96` | 18 | 0.5351 | 1.0179 | 1.0000 | 1.0085 | 4.7853 | 0.6581 | 0.6260 | 0.6260 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5520 | 1.0048 | 0.3642 | 1.0069 | 5.8015 | 0.9228 | 0.6260 | 0.6260 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5520 | 1.0063 | 0.3642 | 1.0069 | 5.8015 | 0.9228 | 0.6254 | 0.6254 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5520 | 1.0079 | 0.3642 | 1.0069 | 5.8015 | 0.9228 | 0.6249 | 0.6249 |
| `base|emb=24|sh=0.95` | 18 | 0.5351 | 1.0223 | 1.0000 | 1.0085 | 4.7853 | 0.6581 | 0.6245 | 0.6245 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5520 | 1.0095 | 0.3642 | 1.0069 | 5.8015 | 0.9228 | 0.6244 | 0.6244 |
| `base|emb=24|sh=0.94` | 18 | 0.5351 | 1.0268 | 1.0000 | 1.0085 | 4.7853 | 0.6581 | 0.6230 | 0.6230 |
| `base|emb=12|sh=0.97` | 18 | 0.5518 | 1.0106 | 1.0000 | 0.9870 | 6.6949 | 1.0270 | 0.6174 | 0.6174 |
| `base|emb=12|sh=0.96` | 18 | 0.5518 | 1.0142 | 1.0000 | 0.9870 | 6.6949 | 1.0270 | 0.6161 | 0.6161 |
| `base|emb=12|sh=0.95` | 18 | 0.5518 | 1.0177 | 1.0000 | 0.9870 | 6.6949 | 1.0270 | 0.6149 | 0.6149 |
| `base|emb=12|sh=0.94` | 18 | 0.5518 | 1.0213 | 1.0000 | 0.9870 | 6.6949 | 1.0270 | 0.6136 | 0.6136 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=360, top_n=36, cutoff=0.8302

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7421 | 0.0965 | 0.9846 | 0.0317 |
| all validations | 0.5537 | 0.1511 | 1.0164 | 0.0479 |

- improvement vs all (primary fraction): `hit +18.83pp, mae +3.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=24|sh=0.97` | 0.6667 | 0.9836 | 1.0000 | 0.9255 | 0.2595 | 24.2896 | 1.8361 | 0.7894 | 0.7894 |
| 2 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5500 | 0.9804 | 0.6667 | 0.7731 | -0.0245 | -2.2901 | -0.1292 | 0.4551 | 0.4551 |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5500 | 0.9837 | 0.6667 | 0.7731 | -0.0245 | -2.2901 | -0.1292 | 0.4537 | 0.4537 |
| 4 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5500 | 0.9869 | 0.6667 | 0.7731 | -0.0245 | -2.2901 | -0.1292 | 0.4524 | 0.4524 |
| 5 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5500 | 0.9902 | 0.6667 | 0.7731 | -0.0245 | -2.2901 | -0.1292 | 0.4510 | 0.4510 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.6667 | 0.9931 | 0.7521 | 16.8866 | 0.4975 |
| 1 | 7 | 0.3333 | 1.0096 | 0.6854 | -40.1169 | -0.6672 |
| 2 | 7 | 0.6667 | 0.9632 | 1.7003 | 47.6807 | 4.8609 |
| 3 | 7 | 0.8000 | 0.9491 | 0.3640 | 13.7165 | n/a |
| 4 | 7 | 1.0000 | 0.9932 | n/a | 160.8066 | n/a |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.6667 | 0.9931 | 0.7521 | 16.8866 | 0.4975 |
| top_20pct | 8 | 1.0000 | 0.9999 | n/a | 160.8066 | n/a |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1.0000 | 1.0047 | n/a | 166.2638 | n/a |
| 1 | 7 | 0.5000 | 0.9835 | 0.9995 | -0.0179 | -0.0174 |
| 2 | 7 | 0.5000 | 0.9994 | 0.6256 | -17.5571 | -0.3889 |
| 3 | 7 | 0.8333 | 0.9195 | 1.3894 | 84.9761 | 6.0108 |
| 4 | 7 | 0.6667 | 0.9913 | 0.7521 | 16.8866 | 0.4975 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 1.0000 | 1.0047 | n/a | 166.2638 | n/a |
| top_20pct | 8 | 0.6667 | 0.9931 | 0.7521 | 16.8866 | 0.4975 |

