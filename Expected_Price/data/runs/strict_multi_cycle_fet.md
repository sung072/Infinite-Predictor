# Strict Multi-Cycle Research Result

- symbol: `FET`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5206 | 0.9959 | 0.4444 | 1.1675 | 4.4246 | 1.0896 | 0.6554 | 0.6554 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5206 | 0.9960 | 0.4444 | 1.1675 | 4.4246 | 1.0896 | 0.6553 | 0.6553 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5206 | 0.9962 | 0.4444 | 1.1675 | 4.4246 | 1.0896 | 0.6551 | 0.6551 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5206 | 0.9969 | 0.4444 | 1.1675 | 4.4246 | 1.0896 | 0.6547 | 0.6547 |
| `base|emb=24|sh=0.95` | 18 | 0.5267 | 0.9968 | 1.0000 | 1.1018 | 5.7144 | 0.9713 | 0.6507 | 0.6507 |
| `base|emb=24|sh=0.96` | 18 | 0.5267 | 0.9965 | 1.0000 | 1.1018 | 5.7144 | 0.9713 | 0.6507 | 0.6507 |
| `base|emb=24|sh=0.94` | 18 | 0.5267 | 0.9977 | 1.0000 | 1.1018 | 5.7144 | 0.9713 | 0.6506 | 0.6506 |
| `base|emb=24|sh=0.97` | 18 | 0.5267 | 0.9971 | 1.0000 | 1.1018 | 5.7144 | 0.9713 | 0.6503 | 0.6503 |
| `base|emb=12|sh=0.96` | 18 | 0.5298 | 0.9969 | 1.0000 | 1.0710 | 5.4572 | 0.5975 | 0.6436 | 0.6436 |
| `base|emb=12|sh=0.95` | 18 | 0.5298 | 0.9972 | 1.0000 | 1.0710 | 5.4572 | 0.5975 | 0.6436 | 0.6436 |
| `base|emb=12|sh=0.94` | 18 | 0.5298 | 0.9980 | 1.0000 | 1.0710 | 5.4572 | 0.5975 | 0.6434 | 0.6434 |
| `base|emb=12|sh=0.97` | 18 | 0.5298 | 0.9973 | 1.0000 | 1.0710 | 5.4572 | 0.5975 | 0.6433 | 0.6433 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5327 | 0.9775 | 0.2160 | 1.0515 | 3.7227 | 1.1854 | 0.6195 | 0.6195 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5327 | 0.9807 | 0.2160 | 1.0515 | 3.7227 | 1.1854 | 0.6174 | 0.6174 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5327 | 0.9840 | 0.2160 | 1.0515 | 3.7227 | 1.1854 | 0.6155 | 0.6155 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5327 | 0.9878 | 0.2160 | 1.0515 | 3.7227 | 1.1854 | 0.6134 | 0.6134 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4976 | 1.0007 | 0.4537 | 1.1244 | -0.7976 | 1.0093 | 0.5706 | 0.5706 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4976 | 1.0011 | 0.4537 | 1.1244 | -0.7976 | 1.0093 | 0.5705 | 0.5705 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4976 | 1.0019 | 0.4537 | 1.1244 | -0.7976 | 1.0093 | 0.5703 | 0.5703 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4976 | 1.0030 | 0.4537 | 1.1244 | -0.7976 | 1.0093 | 0.5700 | 0.5700 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8373

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7065 | 0.0554 | 0.9373 | 0.0445 |
| all validations | 0.5201 | 0.1272 | 0.9945 | 0.0365 |

- improvement vs all (primary fraction): `hit +18.64pp, mae +5.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=24|sh=0.95` | 0.5588 | 0.9911 | 1.0000 | 1.2941 | 0.2014 | 18.8523 | 1.6778 | 0.7771 | 0.7771 |
