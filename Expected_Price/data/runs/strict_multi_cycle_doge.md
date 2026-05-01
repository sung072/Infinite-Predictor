# Strict Multi-Cycle Research Result

- symbol: `DOGE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5141 | 1.0069 | 0.2870 | 1.1146 | 0.0347 | 0.5127 | 0.6088 | 0.6088 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5141 | 1.0137 | 0.2870 | 1.1146 | 0.0347 | 0.5127 | 0.6069 | 0.6069 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5141 | 1.0236 | 0.2870 | 1.1146 | 0.0347 | 0.5127 | 0.6040 | 0.6040 |
| `base|emb=12|sh=0.97` | 18 | 0.5289 | 0.9955 | 1.0000 | 0.9843 | 3.0907 | 0.4348 | 0.6007 | 0.6007 |
| `base|emb=12|sh=0.96` | 18 | 0.5289 | 0.9957 | 1.0000 | 0.9843 | 3.0907 | 0.4348 | 0.6006 | 0.6006 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5141 | 1.0365 | 0.2870 | 1.1146 | 0.0347 | 0.5127 | 0.6001 | 0.6001 |
| `base|emb=12|sh=0.95` | 18 | 0.5289 | 0.9974 | 1.0000 | 0.9843 | 3.0907 | 0.4348 | 0.6000 | 0.6000 |
| `base|emb=12|sh=0.94` | 18 | 0.5289 | 1.0002 | 1.0000 | 0.9843 | 3.0907 | 0.4348 | 0.5990 | 0.5990 |
| `base|emb=24|sh=0.96` | 18 | 0.5416 | 0.9932 | 1.0000 | 0.9848 | 4.4698 | 0.4681 | 0.5927 | 0.5927 |
| `base|emb=24|sh=0.95` | 18 | 0.5416 | 0.9937 | 1.0000 | 0.9848 | 4.4698 | 0.4681 | 0.5926 | 0.5926 |
| `base|emb=24|sh=0.97` | 18 | 0.5416 | 0.9938 | 1.0000 | 0.9848 | 4.4698 | 0.4681 | 0.5925 | 0.5925 |
| `base|emb=24|sh=0.94` | 18 | 0.5416 | 0.9950 | 1.0000 | 0.9848 | 4.4698 | 0.4681 | 0.5921 | 0.5921 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5036 | 1.0054 | 0.2855 | 1.1277 | 0.7633 | 0.3005 | 0.5760 | 0.5760 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5036 | 1.0119 | 0.2855 | 1.1277 | 0.7633 | 0.3005 | 0.5738 | 0.5738 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5036 | 1.0262 | 0.2855 | 1.1277 | 0.7633 | 0.3005 | 0.5690 | 0.5690 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5036 | 1.0440 | 0.2855 | 1.1277 | 0.7633 | 0.3005 | 0.5632 | 0.5632 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5233 | 0.9933 | 0.4491 | 1.0501 | 1.8969 | 0.9214 | 0.5547 | 0.5547 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5233 | 0.9940 | 0.4491 | 1.0501 | 1.8969 | 0.9214 | 0.5544 | 0.5544 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5233 | 0.9947 | 0.4491 | 1.0501 | 1.8969 | 0.9214 | 0.5540 | 0.5540 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5233 | 0.9955 | 0.4491 | 1.0501 | 1.8969 | 0.9214 | 0.5536 | 0.5536 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=360, top_n=36, cutoff=0.7962

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6373 | 0.0760 | 0.9722 | 0.0201 |
| all validations | 0.5244 | 0.0957 | 1.0023 | 0.0423 |

- improvement vs all (primary fraction): `hit +11.29pp, mae +3.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7000 | 0.9588 | 0.3056 | 1.2333 | 0.3783 | 35.4034 | 3.7154 | 0.8501 | 0.8501 |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7000 | 0.9641 | 0.3056 | 1.2333 | 0.3783 | 35.4034 | 3.7154 | 0.8478 | 0.8478 |
| 3 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.7000 | 0.9716 | 0.3056 | 1.2333 | 0.3783 | 35.4034 | 3.7154 | 0.8446 | 0.8446 |
| 4 | `base|emb=12|sh=0.96` | 0.5882 | 0.9891 | 1.0000 | 0.8449 | 0.0704 | 6.5859 | 0.3288 | 0.7204 | 0.7204 |
| 5 | `base|emb=12|sh=0.97` | 0.5882 | 0.9918 | 1.0000 | 0.8449 | 0.0704 | 6.5859 | 0.3288 | 0.7193 | 0.7193 |
