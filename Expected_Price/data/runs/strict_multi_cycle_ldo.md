# Strict Multi-Cycle Research Result

- symbol: `LDO`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5226 | 1.0066 | 0.2670 | 0.8765 | -4.5814 | 0.5665 | 0.5694 | 0.5694 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5226 | 1.0126 | 0.2670 | 0.8765 | -4.5814 | 0.5665 | 0.5675 | 0.5675 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5226 | 1.0196 | 0.2670 | 0.8765 | -4.5814 | 0.5665 | 0.5654 | 0.5654 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5226 | 1.0269 | 0.2670 | 0.8765 | -4.5814 | 0.5665 | 0.5633 | 0.5633 |
| `base|emb=24|sh=0.97` | 18 | 0.5012 | 1.0092 | 1.0000 | 0.9471 | -4.1783 | 0.0315 | 0.5346 | 0.5346 |
| `base|emb=24|sh=0.96` | 18 | 0.5012 | 1.0142 | 1.0000 | 0.9471 | -4.1783 | 0.0315 | 0.5328 | 0.5328 |
| `base|emb=24|sh=0.95` | 18 | 0.5012 | 1.0196 | 1.0000 | 0.9471 | -4.1783 | 0.0315 | 0.5309 | 0.5309 |
| `base|emb=24|sh=0.94` | 18 | 0.5012 | 1.0251 | 1.0000 | 0.9471 | -4.1783 | 0.0315 | 0.5290 | 0.5290 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4382 | 1.0249 | 0.4228 | 1.1637 | -11.7436 | 0.1898 | 0.5245 | 0.5245 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4382 | 1.0338 | 0.4228 | 1.1637 | -11.7436 | 0.1898 | 0.5215 | 0.5215 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4471 | 1.0251 | 0.4475 | 1.1151 | -9.6631 | 0.1900 | 0.5214 | 0.5214 |
| `base|emb=12|sh=0.97` | 18 | 0.5044 | 1.0075 | 1.0000 | 0.9197 | -4.6647 | -0.0828 | 0.5193 | 0.5193 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4382 | 1.0428 | 0.4228 | 1.1637 | -11.7436 | 0.1898 | 0.5187 | 0.5187 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4471 | 1.0339 | 0.4475 | 1.1151 | -9.6631 | 0.1900 | 0.5183 | 0.5183 |
| `base|emb=12|sh=0.96` | 18 | 0.5044 | 1.0122 | 1.0000 | 0.9197 | -4.6647 | -0.0828 | 0.5175 | 0.5175 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4382 | 1.0518 | 0.4228 | 1.1637 | -11.7436 | 0.1898 | 0.5159 | 0.5159 |
| `base|emb=12|sh=0.95` | 18 | 0.5044 | 1.0173 | 1.0000 | 0.9197 | -4.6647 | -0.0828 | 0.5156 | 0.5156 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4471 | 1.0428 | 0.4475 | 1.1151 | -9.6631 | 0.1900 | 0.5154 | 0.5154 |
| `base|emb=12|sh=0.94` | 18 | 0.5044 | 1.0227 | 1.0000 | 0.9197 | -4.6647 | -0.0828 | 0.5137 | 0.5137 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4471 | 1.0517 | 0.4475 | 1.1151 | -9.6631 | 0.1900 | 0.5126 | 0.5126 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=352, top_n=36, cutoff=0.7738

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6347 | 0.1064 | 0.9837 | 0.0314 |
| all validations | 0.4825 | 0.1469 | 1.0262 | 0.0564 |

- improvement vs all (primary fraction): `hit +15.21pp, mae +4.1%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4706 | 1.0040 | 0.5278 | 1.0575 | -0.0215 | -2.0105 | -0.1601 | 0.4502 | 0.4502 |
| 2 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4706 | 1.0083 | 0.5278 | 1.0575 | -0.0215 | -2.0105 | -0.1601 | 0.4485 | 0.4485 |
| 3 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4706 | 1.0126 | 0.5278 | 1.0575 | -0.0215 | -2.0105 | -0.1601 | 0.4469 | 0.4469 |
| 4 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.4706 | 1.0169 | 0.5278 | 1.0575 | -0.0215 | -2.0105 | -0.1601 | 0.4452 | 0.4452 |
| 5 | `base|emb=24|sh=0.97` | 0.4242 | 1.0080 | 1.0000 | 0.9918 | -0.1133 | -10.6072 | -0.6522 | 0.3584 | 0.3584 |
