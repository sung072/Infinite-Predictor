# Strict Multi-Cycle Research Result

- symbol: `NFP`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5628 | 0.9909 | 0.4228 | 1.1319 | 12.6500 | 1.4358 | 0.6677 | 0.6677 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5628 | 0.9923 | 0.4228 | 1.1319 | 12.6500 | 1.4358 | 0.6671 | 0.6671 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5628 | 0.9937 | 0.4228 | 1.1319 | 12.6500 | 1.4358 | 0.6665 | 0.6665 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5628 | 0.9952 | 0.4228 | 1.1319 | 12.6500 | 1.4358 | 0.6659 | 0.6659 |
| `base|emb=24|sh=0.97` | 18 | 0.5205 | 0.9978 | 1.0000 | 1.0771 | 5.0554 | 0.7610 | 0.6502 | 0.6502 |
| `base|emb=24|sh=0.96` | 18 | 0.5205 | 0.9980 | 1.0000 | 1.0771 | 5.0554 | 0.7610 | 0.6501 | 0.6501 |
| `base|emb=24|sh=0.95` | 18 | 0.5205 | 0.9985 | 1.0000 | 1.0771 | 5.0554 | 0.7610 | 0.6500 | 0.6500 |
| `base|emb=24|sh=0.94` | 18 | 0.5205 | 0.9991 | 1.0000 | 1.0771 | 5.0554 | 0.7610 | 0.6498 | 0.6498 |
| `base|emb=12|sh=0.97` | 18 | 0.5149 | 0.9989 | 1.0000 | 1.0507 | 3.0307 | 0.4114 | 0.5911 | 0.5911 |
| `base|emb=12|sh=0.96` | 18 | 0.5149 | 0.9994 | 1.0000 | 1.0507 | 3.0307 | 0.4114 | 0.5909 | 0.5909 |
| `base|emb=12|sh=0.95` | 18 | 0.5149 | 1.0002 | 1.0000 | 1.0507 | 3.0307 | 0.4114 | 0.5906 | 0.5906 |
| `base|emb=12|sh=0.94` | 18 | 0.5149 | 1.0009 | 1.0000 | 1.0507 | 3.0307 | 0.4114 | 0.5904 | 0.5904 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5114 | 1.0010 | 0.4306 | 1.0003 | 0.6711 | 0.4901 | 0.5588 | 0.5588 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5114 | 1.0015 | 0.4306 | 1.0003 | 0.6711 | 0.4901 | 0.5586 | 0.5586 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5114 | 1.0022 | 0.4306 | 1.0003 | 0.6711 | 0.4901 | 0.5584 | 0.5584 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5114 | 1.0029 | 0.4306 | 1.0003 | 0.6711 | 0.4901 | 0.5582 | 0.5582 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4926 | 0.9945 | 0.3735 | 1.0524 | -1.5702 | 0.1627 | 0.5525 | 0.5525 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4926 | 0.9941 | 0.3735 | 1.0524 | -1.5702 | 0.1627 | 0.5525 | 0.5525 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4926 | 0.9954 | 0.3735 | 1.0524 | -1.5702 | 0.1627 | 0.5525 | 0.5525 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4926 | 0.9943 | 0.3735 | 1.0524 | -1.5702 | 0.1627 | 0.5523 | 0.5523 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=360, top_n=36, cutoff=0.8022

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6441 | 0.0672 | 0.9790 | 0.0128 |
| all validations | 0.5143 | 0.0943 | 0.9992 | 0.0240 |

- improvement vs all (primary fraction): `hit +12.98pp, mae +2.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=24|sh=0.97` | 0.4118 | 1.0238 | 1.0000 | 0.8357 | -0.1392 | -13.0276 | -0.6277 | 0.3432 | 0.3432 |
