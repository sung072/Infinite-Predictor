# Strict Multi-Cycle Research Result

- symbol: `ASTER`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5649 | 1.0005 | 0.3935 | 1.1224 | 12.6117 | 1.0166 | 0.6932 | 0.6932 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5649 | 1.0006 | 0.3935 | 1.1224 | 12.6117 | 1.0166 | 0.6932 | 0.6932 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5649 | 1.0008 | 0.3935 | 1.1224 | 12.6117 | 1.0166 | 0.6932 | 0.6932 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5649 | 1.0009 | 0.3935 | 1.1224 | 12.6117 | 1.0166 | 0.6931 | 0.6931 |
| `base|emb=24|sh=0.97` | 18 | 0.5449 | 1.0041 | 1.0000 | 1.0351 | 6.9406 | 0.8521 | 0.6290 | 0.6290 |
| `base|emb=24|sh=0.96` | 18 | 0.5449 | 1.0054 | 1.0000 | 1.0351 | 6.9406 | 0.8521 | 0.6285 | 0.6285 |
| `base|emb=24|sh=0.95` | 18 | 0.5449 | 1.0068 | 1.0000 | 1.0351 | 6.9406 | 0.8521 | 0.6280 | 0.6280 |
| `base|emb=24|sh=0.94` | 18 | 0.5449 | 1.0081 | 1.0000 | 1.0351 | 6.9406 | 0.8521 | 0.6275 | 0.6275 |
| `base|emb=12|sh=0.97` | 18 | 0.5483 | 1.0035 | 1.0000 | 0.9896 | 5.5811 | 0.8359 | 0.5899 | 0.5899 |
| `base|emb=12|sh=0.96` | 18 | 0.5483 | 1.0047 | 1.0000 | 0.9896 | 5.5811 | 0.8359 | 0.5895 | 0.5895 |
| `base|emb=12|sh=0.95` | 18 | 0.5483 | 1.0058 | 1.0000 | 0.9896 | 5.5811 | 0.8359 | 0.5891 | 0.5891 |
| `base|emb=12|sh=0.94` | 18 | 0.5483 | 1.0070 | 1.0000 | 0.9896 | 5.5811 | 0.8359 | 0.5886 | 0.5886 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5235 | 1.0042 | 0.3935 | 0.9078 | -0.8798 | 0.5177 | 0.5859 | 0.5859 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5235 | 1.0056 | 0.3935 | 0.9078 | -0.8798 | 0.5177 | 0.5853 | 0.5853 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5235 | 1.0071 | 0.3935 | 0.9078 | -0.8798 | 0.5177 | 0.5848 | 0.5848 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5235 | 1.0085 | 0.3935 | 0.9078 | -0.8798 | 0.5177 | 0.5843 | 0.5843 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5482 | 1.0046 | 0.3395 | 0.9773 | 3.3856 | 0.7136 | 0.5500 | 0.5500 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5482 | 1.0061 | 0.3395 | 0.9773 | 3.3856 | 0.7136 | 0.5495 | 0.5495 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5482 | 1.0077 | 0.3395 | 0.9773 | 3.3856 | 0.7136 | 0.5492 | 0.5492 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5482 | 1.0092 | 0.3395 | 0.9773 | 3.3856 | 0.7136 | 0.5488 | 0.5488 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8055

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6594 | 0.0770 | 0.9833 | 0.0182 |
| all validations | 0.5436 | 0.0990 | 1.0062 | 0.0244 |

- improvement vs all (primary fraction): `hit +11.58pp, mae +2.3%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6154 | 1.0028 | 0.4722 | 1.0239 | 0.2024 | 18.9433 | 1.7468 | 0.7737 | 0.7737 |
| 2 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6154 | 1.0037 | 0.4722 | 1.0239 | 0.2024 | 18.9433 | 1.7468 | 0.7733 | 0.7733 |
| 3 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6154 | 1.0047 | 0.4722 | 1.0239 | 0.2024 | 18.9433 | 1.7468 | 0.7729 | 0.7729 |
| 4 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6154 | 1.0056 | 0.4722 | 1.0239 | 0.2024 | 18.9433 | 1.7468 | 0.7726 | 0.7726 |
| 5 | `base|emb=24|sh=0.97` | 0.5556 | 1.0006 | 1.0000 | 0.8031 | 0.0017 | 0.1554 | -0.0030 | 0.5578 | 0.5578 |
