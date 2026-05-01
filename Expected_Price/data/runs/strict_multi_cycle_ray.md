# Strict Multi-Cycle Research Result

- symbol: `RAY`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5653 | 1.0260 | 0.2840 | 1.3663 | 9.4122 | 2.0546 | 0.6714 | 0.6714 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5653 | 1.0347 | 0.2840 | 1.3663 | 9.4122 | 2.0546 | 0.6693 | 0.6693 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5653 | 1.0433 | 0.2840 | 1.3663 | 9.4122 | 2.0546 | 0.6676 | 0.6676 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5653 | 1.0525 | 0.2840 | 1.3663 | 9.4122 | 2.0546 | 0.6659 | 0.6659 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6037 | 1.0073 | 0.3025 | 1.1062 | 14.8937 | 1.5633 | 0.6478 | 0.6478 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6037 | 1.0097 | 0.3025 | 1.1062 | 14.8937 | 1.5633 | 0.6472 | 0.6472 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6037 | 1.0121 | 0.3025 | 1.1062 | 14.8937 | 1.5633 | 0.6468 | 0.6468 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.6037 | 1.0152 | 0.3025 | 1.1062 | 14.8937 | 1.5633 | 0.6463 | 0.6463 |
| `base|emb=12|sh=0.97` | 18 | 0.5138 | 1.0054 | 1.0000 | 0.8134 | -5.7536 | -0.2490 | 0.4595 | 0.4595 |
| `base|emb=12|sh=0.96` | 18 | 0.5138 | 1.0071 | 1.0000 | 0.8134 | -5.7536 | -0.2490 | 0.4589 | 0.4589 |
| `base|emb=12|sh=0.95` | 18 | 0.5138 | 1.0089 | 1.0000 | 0.8134 | -5.7536 | -0.2490 | 0.4584 | 0.4584 |
| `base|emb=12|sh=0.94` | 18 | 0.5138 | 1.0111 | 1.0000 | 0.8134 | -5.7536 | -0.2490 | 0.4577 | 0.4577 |
| `base|emb=24|sh=0.97` | 18 | 0.5004 | 1.0061 | 1.0000 | 0.8345 | -6.6322 | -0.2753 | 0.4329 | 0.4329 |
| `base|emb=24|sh=0.96` | 18 | 0.5004 | 1.0081 | 1.0000 | 0.8345 | -6.6322 | -0.2753 | 0.4322 | 0.4322 |
| `base|emb=24|sh=0.95` | 18 | 0.5004 | 1.0101 | 1.0000 | 0.8345 | -6.6322 | -0.2753 | 0.4315 | 0.4315 |
| `base|emb=24|sh=0.94` | 18 | 0.5004 | 1.0126 | 1.0000 | 0.8345 | -6.6322 | -0.2753 | 0.4308 | 0.4308 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4528 | 1.0063 | 0.4213 | 0.6376 | -25.2011 | -0.3920 | 0.4305 | 0.4305 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4528 | 1.0084 | 0.4213 | 0.6376 | -25.2011 | -0.3920 | 0.4298 | 0.4298 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4528 | 1.0105 | 0.4213 | 0.6376 | -25.2011 | -0.3920 | 0.4291 | 0.4291 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4528 | 1.0126 | 0.4213 | 0.6376 | -25.2011 | -0.3920 | 0.4284 | 0.4284 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=376, top_n=38, cutoff=0.8201

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6514 | 0.0810 | 0.9703 | 0.0169 |
| all validations | 0.5095 | 0.1366 | 1.0133 | 0.0538 |

- improvement vs all (primary fraction): `hit +14.18pp, mae +4.2%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.5588 | 0.9984 | 1.0000 | 0.7824 | -0.0035 | -0.3249 | -0.0758 | 0.5320 | 0.5320 |
