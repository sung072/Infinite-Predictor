# Strict Multi-Cycle Research Result

- symbol: `TON`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5095 | 0.9994 | 0.2793 | 1.2390 | 3.3593 | 1.0516 | 0.5685 | 0.5685 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5095 | 0.9995 | 0.2793 | 1.2390 | 3.3593 | 1.0516 | 0.5685 | 0.5685 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5095 | 0.9995 | 0.2793 | 1.2390 | 3.3593 | 1.0516 | 0.5684 | 0.5684 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5095 | 1.0003 | 0.2793 | 1.2390 | 3.3593 | 1.0516 | 0.5683 | 0.5683 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5240 | 0.9986 | 0.3056 | 1.1725 | 5.7271 | 0.9034 | 0.5573 | 0.5573 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5240 | 0.9986 | 0.3056 | 1.1725 | 5.7271 | 0.9034 | 0.5572 | 0.5572 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5240 | 0.9989 | 0.3056 | 1.1725 | 5.7271 | 0.9034 | 0.5570 | 0.5570 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5240 | 0.9995 | 0.3056 | 1.1725 | 5.7271 | 0.9034 | 0.5570 | 0.5570 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4329 | 1.0112 | 0.3657 | 1.1853 | -8.2477 | 0.3648 | 0.5397 | 0.5397 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4329 | 1.0173 | 0.3657 | 1.1853 | -8.2477 | 0.3648 | 0.5375 | 0.5375 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4329 | 1.0242 | 0.3657 | 1.1853 | -8.2477 | 0.3648 | 0.5351 | 0.5351 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4329 | 1.0319 | 0.3657 | 1.1853 | -8.2477 | 0.3648 | 0.5324 | 0.5324 |
| `base|emb=12|sh=0.97` | 18 | 0.4782 | 1.0042 | 1.0000 | 1.0745 | -2.8332 | 0.5379 | 0.5322 | 0.5322 |
| `base|emb=12|sh=0.96` | 18 | 0.4782 | 1.0065 | 1.0000 | 1.0745 | -2.8332 | 0.5379 | 0.5314 | 0.5314 |
| `base|emb=12|sh=0.95` | 18 | 0.4782 | 1.0092 | 1.0000 | 1.0745 | -2.8332 | 0.5379 | 0.5304 | 0.5304 |
| `base|emb=12|sh=0.94` | 18 | 0.4782 | 1.0126 | 1.0000 | 1.0745 | -2.8332 | 0.5379 | 0.5293 | 0.5293 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4112 | 1.0272 | 0.3565 | 1.1576 | -12.8995 | 0.1704 | 0.4982 | 0.4982 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4112 | 1.0375 | 0.3565 | 1.1576 | -12.8995 | 0.1704 | 0.4949 | 0.4949 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4112 | 1.0494 | 0.3565 | 1.1576 | -12.8995 | 0.1704 | 0.4912 | 0.4912 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4112 | 1.0628 | 0.3565 | 1.1576 | -12.8995 | 0.1704 | 0.4872 | 0.4872 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.8197

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6053 | 0.0558 | 0.9911 | 0.0186 |
| all validations | 0.4668 | 0.1098 | 1.0147 | 0.0457 |

- improvement vs all (primary fraction): `hit +13.85pp, mae +2.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `base|emb=12|sh=0.97` | 0.5758 | 0.9926 | 1.0000 | 1.0702 | 0.1471 | 13.7724 | 1.1673 | 0.7565 | 0.7565 |
| 2 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5000 | 0.9950 | 0.1944 | 1.2211 | 0.0855 | 8.0005 | 0.3927 | 0.7215 | 0.7215 |
| 3 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5000 | 0.9958 | 0.1944 | 1.2211 | 0.0855 | 8.0005 | 0.3927 | 0.7212 | 0.7212 |
| 4 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5000 | 0.9966 | 0.1944 | 1.2211 | 0.0855 | 8.0005 | 0.3927 | 0.7208 | 0.7208 |
| 5 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5000 | 0.9975 | 0.1944 | 1.2211 | 0.0855 | 8.0005 | 0.3927 | 0.7205 | 0.7205 |

## Final rank-1 regime bins (gap / tension)

### `mean_pairwise_per_atr`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.4286 | 1.0077 | 0.8624 | -16.9360 | -0.5046 |
| 1 | 7 | 0.4286 | 1.0091 | 2.4946 | 22.0330 | 1.3443 |
| 2 | 7 | 0.8333 | 0.9793 | 0.5804 | 41.0533 | 1.9033 |
| 3 | 7 | 0.4286 | 1.0021 | 0.5846 | -29.3723 | -1.4398 |
| 4 | 7 | 0.8333 | 0.9729 | 1.2885 | 67.0203 | 5.4930 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.4286 | 1.0077 | 0.8624 | -16.9360 | -0.5046 |
| top_20pct | 8 | 0.8571 | 0.9743 | 1.3462 | 79.6108 | 7.1823 |

### `p_system_tension`

- q5

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0.1250 | 1.0390 | 0.6542 | -62.1963 | -0.9298 |
| 1 | 7 | 1.0000 | 0.9415 | n/a | 108.8408 | n/a |
| 2 | 7 | 0.5714 | 0.9935 | 1.0301 | 11.4474 | 0.5902 |
| 3 | 7 | 0.8000 | 0.9997 | 3.5859 | 80.7968 | 13.4623 |
| 4 | 7 | 0.5714 | 0.9809 | 0.7850 | 1.8809 | 0.0488 |

- tails_10_20

| bucket | n | hit | mae_ratio | mean_rr | sharpe_ann | calmar |
|---|---:|---:|---:|---:|---:|---:|
| bottom_20pct | 8 | 0.1250 | 1.0390 | 0.6542 | -62.1963 | -0.9298 |
| top_20pct | 8 | 0.6250 | 0.9825 | 0.7733 | 10.6318 | 0.3724 |

