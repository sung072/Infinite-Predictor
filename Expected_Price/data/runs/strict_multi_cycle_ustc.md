# Strict Multi-Cycle Research Result

- symbol: `USTC`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5268 | 1.0046 | 0.2901 | 1.1974 | 4.8770 | 1.1954 | 0.6492 | 0.6492 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5268 | 1.0038 | 0.2901 | 1.1974 | 4.8770 | 1.1954 | 0.6489 | 0.6489 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5268 | 1.0030 | 0.2901 | 1.1974 | 4.8770 | 1.1954 | 0.6488 | 0.6488 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5268 | 1.0023 | 0.2901 | 1.1974 | 4.8770 | 1.1954 | 0.6487 | 0.6487 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4928 | 1.0047 | 0.3071 | 1.2403 | 2.2816 | 1.1035 | 0.6137 | 0.6137 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4928 | 1.0062 | 0.3071 | 1.2403 | 2.2816 | 1.1035 | 0.6132 | 0.6132 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4928 | 1.0078 | 0.3071 | 1.2403 | 2.2816 | 1.1035 | 0.6128 | 0.6128 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4928 | 1.0093 | 0.3071 | 1.2403 | 2.2816 | 1.1035 | 0.6124 | 0.6124 |
| `base|emb=12|sh=0.97` | 18 | 0.5211 | 1.0021 | 1.0000 | 0.9956 | 2.0928 | 0.2969 | 0.6039 | 0.6039 |
| `base|emb=12|sh=0.96` | 18 | 0.5211 | 1.0032 | 1.0000 | 0.9956 | 2.0928 | 0.2969 | 0.6035 | 0.6035 |
| `base|emb=12|sh=0.95` | 18 | 0.5211 | 1.0043 | 1.0000 | 0.9956 | 2.0928 | 0.2969 | 0.6032 | 0.6032 |
| `base|emb=12|sh=0.94` | 18 | 0.5211 | 1.0054 | 1.0000 | 0.9956 | 2.0928 | 0.2969 | 0.6028 | 0.6028 |
| `base|emb=24|sh=0.97` | 18 | 0.5170 | 1.0039 | 1.0000 | 1.0021 | 1.1175 | 0.4880 | 0.5370 | 0.5370 |
| `base|emb=24|sh=0.96` | 18 | 0.5170 | 1.0055 | 1.0000 | 1.0021 | 1.1175 | 0.4880 | 0.5364 | 0.5364 |
| `base|emb=24|sh=0.95` | 18 | 0.5170 | 1.0071 | 1.0000 | 1.0021 | 1.1175 | 0.4880 | 0.5358 | 0.5358 |
| `base|emb=24|sh=0.94` | 18 | 0.5170 | 1.0087 | 1.0000 | 1.0021 | 1.1175 | 0.4880 | 0.5352 | 0.5352 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4177 | 1.0133 | 0.3426 | 0.8707 | -28.5890 | -0.1083 | 0.4576 | 0.4576 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4177 | 1.0177 | 0.3426 | 0.8707 | -28.5890 | -0.1083 | 0.4562 | 0.4562 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4177 | 1.0221 | 0.3426 | 0.8707 | -28.5890 | -0.1083 | 0.4548 | 0.4548 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4177 | 1.0266 | 0.3426 | 0.8707 | -28.5890 | -0.1083 | 0.4534 | 0.4534 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=316, top_n=32, cutoff=0.8121

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6431 | 0.0414 | 0.9835 | 0.0164 |
| all validations | 0.4915 | 0.1447 | 1.0092 | 0.0361 |

- improvement vs all (primary fraction): `hit +15.16pp, mae +2.6%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0556 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.6250 | 0.9915 | 1.0000 | 0.9457 | 0.1563 | 14.6293 | 1.0033 | 0.7565 | 0.7565 |
