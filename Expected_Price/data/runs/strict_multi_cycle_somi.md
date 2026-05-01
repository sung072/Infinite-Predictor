# Strict Multi-Cycle Research Result

- symbol: `SOMI`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5389 | 0.9970 | 0.4090 | 1.1499 | 10.8108 | 1.2986 | 0.6326 | 0.6326 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5389 | 0.9967 | 0.4090 | 1.1499 | 10.8108 | 1.2986 | 0.6325 | 0.6325 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5389 | 0.9980 | 0.4090 | 1.1499 | 10.8108 | 1.2986 | 0.6324 | 0.6324 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5389 | 0.9973 | 0.4090 | 1.1499 | 10.8108 | 1.2986 | 0.6322 | 0.6322 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5184 | 1.0002 | 0.3750 | 1.3614 | 6.4638 | 2.0986 | 0.5785 | 0.5785 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5184 | 1.0007 | 0.3750 | 1.3614 | 6.4638 | 2.0986 | 0.5784 | 0.5784 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5184 | 1.0025 | 0.3750 | 1.3614 | 6.4638 | 2.0986 | 0.5778 | 0.5778 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5184 | 1.0056 | 0.3750 | 1.3614 | 6.4638 | 2.0986 | 0.5768 | 0.5768 |
| `base|emb=12|sh=0.96` | 18 | 0.5252 | 0.9987 | 1.0000 | 1.0068 | 1.9392 | 0.8648 | 0.5646 | 0.5646 |
| `base|emb=12|sh=0.97` | 18 | 0.5252 | 0.9988 | 1.0000 | 1.0068 | 1.9392 | 0.8648 | 0.5645 | 0.5645 |
| `base|emb=12|sh=0.95` | 18 | 0.5252 | 0.9993 | 1.0000 | 1.0068 | 1.9392 | 0.8648 | 0.5645 | 0.5645 |
| `base|emb=12|sh=0.94` | 18 | 0.5252 | 1.0004 | 1.0000 | 1.0068 | 1.9392 | 0.8648 | 0.5642 | 0.5642 |
| `base|emb=24|sh=0.96` | 18 | 0.5342 | 0.9982 | 1.0000 | 0.9702 | 3.0511 | 0.8399 | 0.5578 | 0.5578 |
| `base|emb=24|sh=0.95` | 18 | 0.5342 | 0.9985 | 1.0000 | 0.9702 | 3.0511 | 0.8399 | 0.5578 | 0.5578 |
| `base|emb=24|sh=0.97` | 18 | 0.5342 | 0.9984 | 1.0000 | 0.9702 | 3.0511 | 0.8399 | 0.5577 | 0.5577 |
| `base|emb=24|sh=0.94` | 18 | 0.5342 | 0.9994 | 1.0000 | 0.9702 | 3.0511 | 0.8399 | 0.5575 | 0.5575 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4839 | 1.0004 | 0.2793 | 1.0139 | -5.4012 | 0.3871 | 0.4742 | 0.4742 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4839 | 1.0008 | 0.2793 | 1.0139 | -5.4012 | 0.3871 | 0.4742 | 0.4742 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4839 | 1.0005 | 0.2793 | 1.0139 | -5.4012 | 0.3871 | 0.4742 | 0.4742 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4839 | 1.0007 | 0.2793 | 1.0139 | -5.4012 | 0.3871 | 0.4742 | 0.4742 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8437

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6908 | 0.0606 | 0.9756 | 0.0118 |
| all validations | 0.5093 | 0.1176 | 1.0011 | 0.0284 |

- improvement vs all (primary fraction): `hit +18.15pp, mae +2.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.96` | 0.4706 | 1.0034 | 1.0000 | 1.0727 | -0.0192 | -1.7994 | -0.1027 | 0.4603 | 0.4603 |
