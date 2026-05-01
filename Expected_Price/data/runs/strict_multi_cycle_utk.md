# Strict Multi-Cycle Research Result

- symbol: `UTK`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4808 | 1.0080 | 0.2747 | 1.3786 | -4.4378 | 1.3920 | 0.6418 | 0.6418 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4808 | 1.0117 | 0.2747 | 1.3786 | -4.4378 | 1.3920 | 0.6407 | 0.6407 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4808 | 1.0162 | 0.2747 | 1.3786 | -4.4378 | 1.3920 | 0.6394 | 0.6394 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4808 | 1.0206 | 0.2747 | 1.3786 | -4.4378 | 1.3920 | 0.6382 | 0.6382 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4687 | 1.0165 | 0.3056 | 1.1991 | -12.5320 | 1.1026 | 0.5767 | 0.5767 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4687 | 1.0224 | 0.3056 | 1.1991 | -12.5320 | 1.1026 | 0.5748 | 0.5748 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4687 | 1.0285 | 0.3056 | 1.1991 | -12.5320 | 1.1026 | 0.5729 | 0.5729 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4687 | 1.0347 | 0.3056 | 1.1991 | -12.5320 | 1.1026 | 0.5710 | 0.5710 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5587 | 1.0081 | 0.3071 | 0.8745 | 2.5172 | 0.9824 | 0.5506 | 0.5506 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5587 | 1.0125 | 0.3071 | 0.8745 | 2.5172 | 0.9824 | 0.5504 | 0.5504 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5587 | 1.0058 | 0.3071 | 0.8745 | 2.5172 | 0.9824 | 0.5501 | 0.5501 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5587 | 1.0034 | 0.3071 | 0.8745 | 2.5172 | 0.9824 | 0.5498 | 0.5498 |
| `base|emb=12|sh=0.97` | 18 | 0.5051 | 1.0014 | 1.0000 | 0.9998 | -0.8559 | 0.5022 | 0.5376 | 0.5376 |
| `base|emb=12|sh=0.96` | 18 | 0.5051 | 1.0026 | 1.0000 | 0.9998 | -0.8559 | 0.5022 | 0.5371 | 0.5371 |
| `base|emb=12|sh=0.95` | 18 | 0.5051 | 1.0041 | 1.0000 | 0.9998 | -0.8559 | 0.5022 | 0.5366 | 0.5366 |
| `base|emb=12|sh=0.94` | 18 | 0.5051 | 1.0066 | 1.0000 | 0.9998 | -0.8559 | 0.5022 | 0.5357 | 0.5357 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5466 | 1.0078 | 0.2978 | 0.8850 | 2.0933 | 0.9671 | 0.5311 | 0.5311 |
| `base|emb=24|sh=0.97` | 18 | 0.4967 | 1.0010 | 1.0000 | 0.9474 | -3.2990 | 0.1779 | 0.5311 | 0.5311 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5466 | 1.0051 | 0.2978 | 0.8850 | 2.0933 | 0.9671 | 0.5310 | 0.5310 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5466 | 1.0037 | 0.2978 | 0.8850 | 2.0933 | 0.9671 | 0.5305 | 0.5305 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=320, top_n=32, cutoff=0.8549

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7288 | 0.1145 | 0.9595 | 0.0192 |
| all validations | 0.5070 | 0.1491 | 1.0092 | 0.0613 |

- improvement vs all (primary fraction): `hit +22.18pp, mae +4.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.4688 | 1.0010 | 1.0000 | 1.5989 | 0.1392 | 13.0299 | 1.0369 | 0.7497 | 0.7497 |
| 2 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4545 | 1.0007 | 0.3333 | 0.0399 | -0.3026 | -28.3220 | -1.0199 | 0.3099 | 0.3099 |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4545 | 1.0009 | 0.3333 | 0.0399 | -0.3026 | -28.3220 | -1.0199 | 0.3098 | 0.3098 |
| 4 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4545 | 1.0011 | 0.3333 | 0.0399 | -0.3026 | -28.3220 | -1.0199 | 0.3097 | 0.3097 |
| 5 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.4545 | 1.0013 | 0.3333 | 0.0399 | -0.3026 | -28.3220 | -1.0199 | 0.3096 | 0.3096 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.5714 | 1.0003 | 1.0582 | 13.2287 | 0.5430 |
| 1 | 7 | 0.1667 | 1.0292 | 1.3988 | -42.7183 | -1.0710 |
| 2 | 7 | 0.6667 | 0.9869 | 3.7322 | 73.2517 | 7.9270 |
| 3 | 7 | 0.1667 | 1.0391 | 3.3930 | -13.6821 | -0.3323 |
| 4 | 7 | 0.7143 | 0.9543 | 1.8092 | 54.7866 | 3.5634 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.5714 | 1.0003 | 1.0582 | 13.2287 | 0.5430 |
| top_20pct | 8 | 0.6250 | 0.9634 | 1.5837 | 36.3259 | 2.8221 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.7143 | 0.9905 | 0.8029 | 28.9902 | 1.3917 |
| 1 | 7 | 0.4286 | 1.0013 | 3.8052 | 37.4937 | 4.0608 |
| 2 | 7 | 0.4286 | 0.9972 | 0.4154 | -31.8198 | -0.7744 |
| 3 | 7 | 0.1429 | 1.0317 | 2.5876 | -31.7989 | -0.7490 |
| 4 | 7 | 0.7500 | 0.9870 | 11.7625 | 109.5424 | 34.8089 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.7143 | 0.9905 | 0.8029 | 28.9902 | 1.3917 |
| top_20pct | 8 | 0.6000 | 0.9910 | 3.9161 | 62.4174 | 4.9251 |

