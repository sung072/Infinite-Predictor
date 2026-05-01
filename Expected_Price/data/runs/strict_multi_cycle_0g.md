# Strict Multi-Cycle Research Result

- symbol: `0G`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5038 | 1.0037 | 0.4861 | 1.6472 | 13.5670 | 2.2866 | 0.6806 | 0.6806 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5038 | 1.0049 | 0.4861 | 1.6472 | 13.5670 | 2.2866 | 0.6803 | 0.6803 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5038 | 1.0062 | 0.4861 | 1.6472 | 13.5670 | 2.2866 | 0.6801 | 0.6801 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5038 | 1.0074 | 0.4861 | 1.6472 | 13.5670 | 2.2866 | 0.6799 | 0.6799 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4822 | 1.0046 | 0.4722 | 1.2813 | -0.9528 | 1.5095 | 0.6516 | 0.6516 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4822 | 1.0062 | 0.4722 | 1.2813 | -0.9528 | 1.5095 | 0.6511 | 0.6511 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4822 | 1.0077 | 0.4722 | 1.2813 | -0.9528 | 1.5095 | 0.6506 | 0.6506 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4822 | 1.0093 | 0.4722 | 1.2813 | -0.9528 | 1.5095 | 0.6501 | 0.6501 |
| `base|emb=24|sh=0.97` | 18 | 0.5034 | 1.0069 | 1.0000 | 1.2212 | 5.7523 | 1.5542 | 0.6192 | 0.6192 |
| `base|emb=12|sh=0.97` | 18 | 0.5042 | 1.0097 | 1.0000 | 1.1927 | 5.0751 | 1.6367 | 0.6192 | 0.6192 |
| `base|emb=24|sh=0.96` | 18 | 0.5034 | 1.0104 | 1.0000 | 1.2212 | 5.7523 | 1.5542 | 0.6180 | 0.6180 |
| `base|emb=12|sh=0.96` | 18 | 0.5042 | 1.0143 | 1.0000 | 1.1927 | 5.0751 | 1.6367 | 0.6176 | 0.6176 |
| `base|emb=24|sh=0.95` | 18 | 0.5034 | 1.0139 | 1.0000 | 1.2212 | 5.7523 | 1.5542 | 0.6168 | 0.6168 |
| `base|emb=12|sh=0.95` | 18 | 0.5042 | 1.0190 | 1.0000 | 1.1927 | 5.0751 | 1.6367 | 0.6161 | 0.6161 |
| `base|emb=24|sh=0.94` | 18 | 0.5034 | 1.0177 | 1.0000 | 1.2212 | 5.7523 | 1.5542 | 0.6155 | 0.6155 |
| `base|emb=12|sh=0.94` | 18 | 0.5042 | 1.0241 | 1.0000 | 1.1927 | 5.0751 | 1.6367 | 0.6145 | 0.6145 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4711 | 1.0140 | 0.2330 | 1.4869 | 9.4576 | 1.2598 | 0.6031 | 0.6031 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4711 | 1.0187 | 0.2330 | 1.4869 | 9.4576 | 1.2598 | 0.6016 | 0.6016 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4711 | 1.0235 | 0.2330 | 1.4869 | 9.4576 | 1.2598 | 0.6002 | 0.6002 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4711 | 1.0291 | 0.2330 | 1.4869 | 9.4576 | 1.2598 | 0.5986 | 0.5986 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=316, top_n=32, cutoff=0.8557

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6585 | 0.0323 | 0.9723 | 0.0129 |
| all validations | 0.4909 | 0.1258 | 1.0141 | 0.0424 |

- improvement vs all (primary fraction): `hit +16.75pp, mae +4.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5714 | 1.0118 | 0.5278 | 1.3413 | 0.2334 | 21.8489 | 1.4689 | 0.7680 | 0.7680 |
| 2 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5714 | 1.0157 | 0.5278 | 1.3413 | 0.2334 | 21.8489 | 1.4689 | 0.7664 | 0.7664 |
| 3 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5714 | 1.0196 | 0.5278 | 1.3413 | 0.2334 | 21.8489 | 1.4689 | 0.7649 | 0.7649 |
| 4 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.5714 | 1.0235 | 0.5278 | 1.3413 | 0.2334 | 21.8489 | 1.4689 | 0.7634 | 0.7634 |
| 5 | `base|emb=24|sh=0.97` | 0.5556 | 1.0141 | 1.0000 | 0.8815 | 0.0393 | 3.6807 | 0.1623 | 0.6800 | 0.6800 |
