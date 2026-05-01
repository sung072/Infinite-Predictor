# Strict Multi-Cycle Research Result

- symbol: `WLFI`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5748 | 0.9954 | 0.3920 | 1.3279 | 16.0030 | 1.3924 | 0.7283 | 0.7283 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5748 | 0.9957 | 0.3920 | 1.3279 | 16.0030 | 1.3924 | 0.7281 | 0.7281 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5748 | 0.9962 | 0.3920 | 1.3279 | 16.0030 | 1.3924 | 0.7279 | 0.7279 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5748 | 0.9971 | 0.3920 | 1.3279 | 16.0030 | 1.3924 | 0.7275 | 0.7275 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6076 | 0.9921 | 0.4074 | 0.9520 | 13.6432 | 1.1107 | 0.6895 | 0.6895 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6076 | 0.9929 | 0.4074 | 0.9520 | 13.6432 | 1.1107 | 0.6891 | 0.6891 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6076 | 0.9939 | 0.4074 | 0.9520 | 13.6432 | 1.1107 | 0.6886 | 0.6886 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6076 | 0.9954 | 0.4074 | 0.9520 | 13.6432 | 1.1107 | 0.6879 | 0.6879 |
| `base|emb=12|sh=0.97` | 18 | 0.5611 | 1.0005 | 1.0000 | 1.0552 | 7.3864 | 1.2659 | 0.6188 | 0.6188 |
| `base|emb=12|sh=0.96` | 18 | 0.5611 | 1.0009 | 1.0000 | 1.0552 | 7.3864 | 1.2659 | 0.6187 | 0.6187 |
| `base|emb=12|sh=0.95` | 18 | 0.5611 | 1.0020 | 1.0000 | 1.0552 | 7.3864 | 1.2659 | 0.6183 | 0.6183 |
| `base|emb=12|sh=0.94` | 18 | 0.5611 | 1.0037 | 1.0000 | 1.0552 | 7.3864 | 1.2659 | 0.6177 | 0.6177 |
| `base|emb=24|sh=0.96` | 18 | 0.5513 | 0.9995 | 1.0000 | 1.1346 | 8.9153 | 1.7826 | 0.6071 | 0.6071 |
| `base|emb=24|sh=0.97` | 18 | 0.5513 | 0.9995 | 1.0000 | 1.1346 | 8.9153 | 1.7826 | 0.6071 | 0.6071 |
| `base|emb=24|sh=0.95` | 18 | 0.5513 | 1.0001 | 1.0000 | 1.1346 | 8.9153 | 1.7826 | 0.6069 | 0.6069 |
| `base|emb=24|sh=0.94` | 18 | 0.5513 | 1.0013 | 1.0000 | 1.1346 | 8.9153 | 1.7826 | 0.6065 | 0.6065 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5125 | 0.9999 | 0.3025 | 1.8192 | 9.2551 | 1.8181 | 0.6043 | 0.6043 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5125 | 1.0003 | 0.3025 | 1.8192 | 9.2551 | 1.8181 | 0.6043 | 0.6043 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5125 | 1.0016 | 0.3025 | 1.8192 | 9.2551 | 1.8181 | 0.6039 | 0.6039 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5125 | 1.0043 | 0.3025 | 1.8192 | 9.2551 | 1.8181 | 0.6031 | 0.6031 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=328, top_n=33, cutoff=0.8492

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6346 | 0.0947 | 0.9851 | 0.0269 |
| all validations | 0.5546 | 0.0999 | 1.0005 | 0.0208 |

- improvement vs all (primary fraction): `hit +7.99pp, mae +1.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.3438 | 1.0606 | 1.0000 | 0.5109 | -0.4595 | -43.0052 | -0.9712 | 0.2899 | 0.2899 |
