# Strict Multi-Cycle Research Result

- symbol: `APT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5144 | 1.0034 | 0.3873 | 0.9330 | -1.7889 | 0.3287 | 0.5612 | 0.5612 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5144 | 1.0047 | 0.3873 | 0.9330 | -1.7889 | 0.3287 | 0.5610 | 0.5610 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5144 | 1.0073 | 0.3873 | 0.9330 | -1.7889 | 0.3287 | 0.5603 | 0.5603 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5144 | 1.0105 | 0.3873 | 0.9330 | -1.7889 | 0.3287 | 0.5595 | 0.5595 |
| `base|emb=12|sh=0.97` | 18 | 0.5135 | 1.0016 | 1.0000 | 0.8594 | -3.8487 | 0.0460 | 0.5320 | 0.5320 |
| `base|emb=12|sh=0.96` | 18 | 0.5135 | 1.0023 | 1.0000 | 0.8594 | -3.8487 | 0.0460 | 0.5318 | 0.5318 |
| `base|emb=12|sh=0.95` | 18 | 0.5135 | 1.0038 | 1.0000 | 0.8594 | -3.8487 | 0.0460 | 0.5312 | 0.5312 |
| `base|emb=12|sh=0.94` | 18 | 0.5135 | 1.0063 | 1.0000 | 0.8594 | -3.8487 | 0.0460 | 0.5304 | 0.5304 |
| `base|emb=24|sh=0.97` | 18 | 0.5213 | 1.0004 | 1.0000 | 0.8502 | -2.8494 | 0.0538 | 0.5269 | 0.5269 |
| `base|emb=24|sh=0.96` | 18 | 0.5213 | 1.0007 | 1.0000 | 0.8502 | -2.8494 | 0.0538 | 0.5268 | 0.5268 |
| `base|emb=24|sh=0.95` | 18 | 0.5213 | 1.0017 | 1.0000 | 0.8502 | -2.8494 | 0.0538 | 0.5265 | 0.5265 |
| `base|emb=24|sh=0.94` | 18 | 0.5213 | 1.0037 | 1.0000 | 0.8502 | -2.8494 | 0.0538 | 0.5258 | 0.5258 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5159 | 1.0000 | 0.4105 | 0.8510 | -8.5910 | 0.2773 | 0.5113 | 0.5113 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5159 | 0.9999 | 0.4105 | 0.8510 | -8.5910 | 0.2773 | 0.5112 | 0.5112 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5159 | 1.0006 | 0.4105 | 0.8510 | -8.5910 | 0.2773 | 0.5111 | 0.5111 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5159 | 1.0025 | 0.4105 | 0.8510 | -8.5910 | 0.2773 | 0.5104 | 0.5104 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4987 | 1.0079 | 0.4090 | 0.7447 | -13.5198 | 0.0229 | 0.4625 | 0.4625 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4987 | 1.0105 | 0.4090 | 0.7447 | -13.5198 | 0.0229 | 0.4616 | 0.4616 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4987 | 1.0135 | 0.4090 | 0.7447 | -13.5198 | 0.0229 | 0.4605 | 0.4605 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4987 | 1.0170 | 0.4090 | 0.7447 | -13.5198 | 0.0229 | 0.4593 | 0.4593 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=372, top_n=38, cutoff=0.7753

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6293 | 0.0840 | 0.9804 | 0.0264 |
| all validations | 0.5072 | 0.1011 | 1.0088 | 0.0440 |

- improvement vs all (primary fraction): `hit +12.21pp, mae +2.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.8333 | 0.9400 | 0.3611 | 0.5570 | 0.2878 | 26.9412 | 1.9281 | 0.8264 | 0.8264 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.8333 | 0.9500 | 0.3611 | 0.5570 | 0.2878 | 26.9412 | 1.9281 | 0.8219 | 0.8219 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.8333 | 0.9600 | 0.3611 | 0.5570 | 0.2878 | 26.9412 | 1.9281 | 0.8175 | 0.8175 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.8333 | 0.9700 | 0.3611 | 0.5570 | 0.2878 | 26.9412 | 1.9281 | 0.8132 | 0.8132 |
| 5 | `base|emb=12|sh=0.97` | 0.5312 | 0.9920 | 1.0000 | 0.9518 | 0.0281 | 2.6263 | 0.1630 | 0.6666 | 0.6666 |
