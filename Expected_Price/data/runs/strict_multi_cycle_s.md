# Strict Multi-Cycle Research Result

- symbol: `S`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5287 | 0.9765 | 0.3318 | 1.0798 | 6.3514 | 0.7359 | 0.6407 | 0.6407 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5287 | 0.9767 | 0.3318 | 1.0798 | 6.3514 | 0.7359 | 0.6405 | 0.6405 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5287 | 0.9797 | 0.3318 | 1.0798 | 6.3514 | 0.7359 | 0.6389 | 0.6389 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5287 | 0.9841 | 0.3318 | 1.0798 | 6.3514 | 0.7359 | 0.6368 | 0.6368 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4947 | 0.9973 | 0.2963 | 1.0889 | 0.7921 | 1.3957 | 0.5881 | 0.5881 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4947 | 0.9966 | 0.2963 | 1.0889 | 0.7921 | 1.3957 | 0.5881 | 0.5881 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4947 | 0.9968 | 0.2963 | 1.0889 | 0.7921 | 1.3957 | 0.5877 | 0.5877 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4947 | 0.9976 | 0.2963 | 1.0889 | 0.7921 | 1.3957 | 0.5871 | 0.5871 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5228 | 0.9950 | 0.3148 | 0.8982 | -3.9253 | 1.7807 | 0.5579 | 0.5579 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5228 | 0.9936 | 0.3148 | 0.8982 | -3.9253 | 1.7807 | 0.5578 | 0.5578 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5228 | 0.9939 | 0.3148 | 0.8982 | -3.9253 | 1.7807 | 0.5571 | 0.5571 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5253 | 0.9909 | 0.2978 | 0.9334 | -0.6513 | 0.2757 | 0.5562 | 0.5562 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5228 | 0.9952 | 0.3148 | 0.8982 | -3.9253 | 1.7807 | 0.5562 | 0.5562 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5253 | 0.9911 | 0.2978 | 0.9334 | -0.6513 | 0.2757 | 0.5560 | 0.5560 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5253 | 0.9928 | 0.2978 | 0.9334 | -0.6513 | 0.2757 | 0.5557 | 0.5557 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5253 | 0.9926 | 0.2978 | 0.9334 | -0.6513 | 0.2757 | 0.5553 | 0.5553 |
| `base|emb=24|sh=0.97` | 18 | 0.4969 | 0.9987 | 1.0000 | 0.9529 | -3.1152 | 0.0274 | 0.5331 | 0.5331 |
| `base|emb=24|sh=0.96` | 18 | 0.4969 | 0.9993 | 1.0000 | 0.9529 | -3.1152 | 0.0274 | 0.5330 | 0.5330 |
| `base|emb=24|sh=0.95` | 18 | 0.4969 | 1.0009 | 1.0000 | 0.9529 | -3.1152 | 0.0274 | 0.5324 | 0.5324 |
| `base|emb=24|sh=0.94` | 18 | 0.4969 | 1.0032 | 1.0000 | 0.9529 | -3.1152 | 0.0274 | 0.5316 | 0.5316 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=348, top_n=35, cutoff=0.8425

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6961 | 0.0437 | 0.9378 | 0.0317 |
| all validations | 0.5129 | 0.1239 | 0.9943 | 0.0382 |

- improvement vs all (primary fraction): `hit +18.32pp, mae +5.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5294 | 0.9626 | 0.4722 | 1.0431 | 0.0605 | 5.6608 | 0.3346 | 0.7259 | 0.7259 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5294 | 0.9689 | 0.4722 | 1.0431 | 0.0605 | 5.6608 | 0.3346 | 0.7233 | 0.7233 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5294 | 0.9751 | 0.4722 | 1.0431 | 0.0605 | 5.6608 | 0.3346 | 0.7206 | 0.7206 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5294 | 0.9813 | 0.4722 | 1.0431 | 0.0605 | 5.6608 | 0.3346 | 0.7180 | 0.7180 |
| 5 | `base|emb=24|sh=0.97` | 0.4571 | 1.0042 | 1.0000 | 0.8069 | -0.1428 | -13.3659 | -0.6285 | 0.3585 | 0.3585 |
