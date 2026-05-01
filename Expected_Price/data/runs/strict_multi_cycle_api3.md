# Strict Multi-Cycle Research Result

- symbol: `API3`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5238 | 0.9933 | 0.3904 | 1.6406 | 14.8599 | 2.6670 | 0.6819 | 0.6819 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5238 | 0.9943 | 0.3904 | 1.6406 | 14.8599 | 2.6670 | 0.6817 | 0.6817 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5238 | 0.9935 | 0.3904 | 1.6406 | 14.8599 | 2.6670 | 0.6816 | 0.6816 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5238 | 0.9973 | 0.3904 | 1.6406 | 14.8599 | 2.6670 | 0.6808 | 0.6808 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4872 | 1.0037 | 0.3827 | 1.4192 | 5.8669 | 1.3405 | 0.6062 | 0.6062 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4872 | 1.0063 | 0.3827 | 1.4192 | 5.8669 | 1.3405 | 0.6054 | 0.6054 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4872 | 1.0102 | 0.3827 | 1.4192 | 5.8669 | 1.3405 | 0.6042 | 0.6042 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4872 | 1.0164 | 0.3827 | 1.4192 | 5.8669 | 1.3405 | 0.6022 | 0.6022 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4772 | 1.0071 | 0.3133 | 1.1765 | -0.7676 | 1.0033 | 0.5640 | 0.5640 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4772 | 1.0096 | 0.3133 | 1.1765 | -0.7676 | 1.0033 | 0.5633 | 0.5633 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4772 | 1.0121 | 0.3133 | 1.1765 | -0.7676 | 1.0033 | 0.5626 | 0.5626 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4772 | 1.0150 | 0.3133 | 1.1765 | -0.7676 | 1.0033 | 0.5619 | 0.5619 |
| `base|emb=24|sh=0.97` | 18 | 0.4721 | 1.0093 | 1.0000 | 1.1556 | -1.2275 | 0.5034 | 0.5558 | 0.5558 |
| `base|emb=24|sh=0.96` | 18 | 0.4721 | 1.0136 | 1.0000 | 1.1556 | -1.2275 | 0.5034 | 0.5542 | 0.5542 |
| `base|emb=24|sh=0.95` | 18 | 0.4721 | 1.0188 | 1.0000 | 1.1556 | -1.2275 | 0.5034 | 0.5523 | 0.5523 |
| `base|emb=24|sh=0.94` | 18 | 0.4721 | 1.0253 | 1.0000 | 1.1556 | -1.2275 | 0.5034 | 0.5500 | 0.5500 |
| `base|emb=12|sh=0.97` | 18 | 0.4746 | 1.0080 | 1.0000 | 1.1940 | 1.5265 | 0.5898 | 0.5408 | 0.5408 |
| `base|emb=12|sh=0.96` | 18 | 0.4746 | 1.0116 | 1.0000 | 1.1940 | 1.5265 | 0.5898 | 0.5395 | 0.5395 |
| `base|emb=12|sh=0.95` | 18 | 0.4746 | 1.0157 | 1.0000 | 1.1940 | 1.5265 | 0.5898 | 0.5381 | 0.5381 |
| `base|emb=12|sh=0.94` | 18 | 0.4746 | 1.0209 | 1.0000 | 1.1940 | 1.5265 | 0.5898 | 0.5362 | 0.5362 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8384

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6782 | 0.1376 | 0.9722 | 0.0304 |
| all validations | 0.4815 | 0.1337 | 1.0107 | 0.0418 |

- improvement vs all (primary fraction): `hit +19.67pp, mae +3.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=24|sh=0.97` | 0.6857 | 0.9810 | 1.0000 | 0.8838 | 0.2644 | 24.7499 | 3.7170 | 0.8224 | 0.8224 |
