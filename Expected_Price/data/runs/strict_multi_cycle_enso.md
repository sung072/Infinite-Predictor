# Strict Multi-Cycle Research Result

- symbol: `ENSO`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5022 | 1.0182 | 0.3333 | 1.5093 | 9.3499 | 0.9382 | 0.6194 | 0.6194 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4976 | 1.0260 | 0.3349 | 1.5885 | 6.2517 | 3.7378 | 0.6179 | 0.6179 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5022 | 1.0249 | 0.3333 | 1.5093 | 9.3499 | 0.9382 | 0.6174 | 0.6174 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4976 | 1.0353 | 0.3349 | 1.5885 | 6.2517 | 3.7378 | 0.6148 | 0.6148 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5022 | 1.0345 | 0.3333 | 1.5093 | 9.3499 | 0.9382 | 0.6146 | 0.6146 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5022 | 1.0459 | 0.3333 | 1.5093 | 9.3499 | 0.9382 | 0.6113 | 0.6113 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4976 | 1.0474 | 0.3349 | 1.5885 | 6.2517 | 3.7378 | 0.6110 | 0.6110 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4976 | 1.0603 | 0.3349 | 1.5885 | 6.2517 | 3.7378 | 0.6072 | 0.6072 |
| `base|emb=12|sh=0.97` | 18 | 0.4983 | 1.0149 | 1.0000 | 0.9582 | -3.3437 | 0.4346 | 0.5370 | 0.5370 |
| `base|emb=12|sh=0.96` | 18 | 0.4983 | 1.0204 | 1.0000 | 0.9582 | -3.3437 | 0.4346 | 0.5352 | 0.5352 |
| `base|emb=24|sh=0.97` | 18 | 0.4857 | 1.0170 | 1.0000 | 1.0366 | -2.4585 | 0.6991 | 0.5346 | 0.5346 |
| `base|emb=12|sh=0.95` | 18 | 0.4983 | 1.0273 | 1.0000 | 0.9582 | -3.3437 | 0.4346 | 0.5329 | 0.5329 |
| `base|emb=24|sh=0.96` | 18 | 0.4857 | 1.0229 | 1.0000 | 1.0366 | -2.4585 | 0.6991 | 0.5325 | 0.5325 |
| `base|emb=12|sh=0.94` | 18 | 0.4983 | 1.0346 | 1.0000 | 0.9582 | -3.3437 | 0.4346 | 0.5307 | 0.5307 |
| `base|emb=24|sh=0.95` | 18 | 0.4857 | 1.0302 | 1.0000 | 1.0366 | -2.4585 | 0.6991 | 0.5301 | 0.5301 |
| `base|emb=24|sh=0.94` | 18 | 0.4857 | 1.0382 | 1.0000 | 1.0366 | -2.4585 | 0.6991 | 0.5276 | 0.5276 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4987 | 0.9990 | 0.3179 | 1.0277 | -2.3943 | 0.4041 | 0.5136 | 0.5136 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4987 | 0.9992 | 0.3179 | 1.0277 | -2.3943 | 0.4041 | 0.5134 | 0.5134 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4987 | 0.9993 | 0.3179 | 1.0277 | -2.3943 | 0.4041 | 0.5132 | 0.5132 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4987 | 0.9995 | 0.3179 | 1.0277 | -2.3943 | 0.4041 | 0.5130 | 0.5130 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.8308

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7158 | 0.1080 | 0.9725 | 0.0219 |
| all validations | 0.5002 | 0.1427 | 1.0223 | 0.0551 |

- improvement vs all (primary fraction): `hit +21.56pp, mae +4.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.3871 | 1.0160 | 1.0000 | 0.7631 | -0.2828 | -26.4698 | -1.0237 | 0.3256 | 0.3256 |
