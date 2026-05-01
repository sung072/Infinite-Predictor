# Strict Multi-Cycle Research Result

- symbol: `SOL`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `base|emb=24|sh=0.97` | 18 | 0.5535 | 0.9932 | 1.0000 | 0.9688 | 5.0136 | 0.8267 | 0.6040 | 0.6040 |
| `base|emb=24|sh=0.96` | 18 | 0.5535 | 0.9933 | 1.0000 | 0.9688 | 5.0136 | 0.8267 | 0.6040 | 0.6040 |
| `base|emb=24|sh=0.95` | 18 | 0.5535 | 0.9957 | 1.0000 | 0.9688 | 5.0136 | 0.8267 | 0.6030 | 0.6030 |
| `base|emb=24|sh=0.94` | 18 | 0.5535 | 0.9988 | 1.0000 | 0.9688 | 5.0136 | 0.8267 | 0.6018 | 0.6018 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5344 | 0.9969 | 0.3596 | 0.8569 | -3.4222 | 0.6723 | 0.5893 | 0.5893 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5344 | 0.9970 | 0.3596 | 0.8569 | -3.4222 | 0.6723 | 0.5891 | 0.5891 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5344 | 0.9972 | 0.3596 | 0.8569 | -3.4222 | 0.6723 | 0.5888 | 0.5888 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5344 | 0.9974 | 0.3596 | 0.8569 | -3.4222 | 0.6723 | 0.5886 | 0.5886 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5441 | 0.9938 | 0.3179 | 0.9832 | 3.8102 | 0.1621 | 0.5847 | 0.5847 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5441 | 0.9982 | 0.3179 | 0.9832 | 3.8102 | 0.1621 | 0.5833 | 0.5833 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5441 | 1.0076 | 0.3179 | 0.9832 | 3.8102 | 0.1621 | 0.5801 | 0.5801 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5441 | 1.0190 | 0.3179 | 0.9832 | 3.8102 | 0.1621 | 0.5764 | 0.5764 |
| `base|emb=12|sh=0.97` | 18 | 0.5323 | 0.9973 | 1.0000 | 0.9312 | 0.2330 | 0.3942 | 0.5492 | 0.5492 |
| `base|emb=12|sh=0.96` | 18 | 0.5323 | 0.9993 | 1.0000 | 0.9312 | 0.2330 | 0.3942 | 0.5484 | 0.5484 |
| `base|emb=12|sh=0.95` | 18 | 0.5323 | 1.0035 | 1.0000 | 0.9312 | 0.2330 | 0.3942 | 0.5468 | 0.5468 |
| `base|emb=12|sh=0.94` | 18 | 0.5323 | 1.0085 | 1.0000 | 0.9312 | 0.2330 | 0.3942 | 0.5449 | 0.5449 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5075 | 1.0168 | 0.3040 | 1.1895 | -5.0865 | 0.8522 | 0.5362 | 0.5362 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5075 | 1.0292 | 0.3040 | 1.1895 | -5.0865 | 0.8522 | 0.5324 | 0.5324 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5075 | 1.0445 | 0.3040 | 1.1895 | -5.0865 | 0.8522 | 0.5277 | 0.5277 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5075 | 1.0636 | 0.3040 | 1.1895 | -5.0865 | 0.8522 | 0.5224 | 0.5224 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=384, top_n=39, cutoff=0.8129

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6718 | 0.0651 | 0.9786 | 0.0200 |
| all validations | 0.5266 | 0.1078 | 1.0069 | 0.0489 |

- improvement vs all (primary fraction): `hit +14.51pp, mae +2.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `base|emb=24|sh=0.94` | 0.6000 | 0.9654 | 1.0000 | 0.8572 | 0.0902 | 8.4455 | 0.5968 | 0.7446 | 0.7446 |
| 3 | `base|emb=24|sh=0.95` | 0.6000 | 0.9708 | 1.0000 | 0.8572 | 0.0902 | 8.4455 | 0.5968 | 0.7423 | 0.7423 |
| 4 | `base|emb=24|sh=0.96` | 0.6000 | 0.9762 | 1.0000 | 0.8572 | 0.0902 | 8.4455 | 0.5968 | 0.7400 | 0.7400 |
| 5 | `base|emb=24|sh=0.97` | 0.6000 | 0.9818 | 1.0000 | 0.8572 | 0.0902 | 8.4455 | 0.5968 | 0.7377 | 0.7377 |
