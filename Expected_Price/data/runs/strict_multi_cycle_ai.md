# Strict Multi-Cycle Research Result

- symbol: `AI`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5308 | 1.0043 | 0.4414 | 1.0645 | 5.2532 | 0.4435 | 0.5734 | 0.5734 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5308 | 1.0058 | 0.4414 | 1.0645 | 5.2532 | 0.4435 | 0.5729 | 0.5729 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5308 | 1.0072 | 0.4414 | 1.0645 | 5.2532 | 0.4435 | 0.5723 | 0.5723 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5308 | 1.0087 | 0.4414 | 1.0645 | 5.2532 | 0.4435 | 0.5718 | 0.5718 |
| `base|emb=24|sh=0.97` | 18 | 0.4994 | 1.0110 | 1.0000 | 1.0129 | -0.7682 | 0.3033 | 0.5415 | 0.5415 |
| `base|emb=24|sh=0.96` | 18 | 0.4994 | 1.0147 | 1.0000 | 1.0129 | -0.7682 | 0.3033 | 0.5401 | 0.5401 |
| `base|emb=24|sh=0.95` | 18 | 0.4994 | 1.0183 | 1.0000 | 1.0129 | -0.7682 | 0.3033 | 0.5388 | 0.5388 |
| `base|emb=24|sh=0.94` | 18 | 0.4994 | 1.0221 | 1.0000 | 1.0129 | -0.7682 | 0.3033 | 0.5374 | 0.5374 |
| `base|emb=12|sh=0.97` | 18 | 0.5013 | 1.0102 | 1.0000 | 0.9948 | -1.6500 | 0.1667 | 0.5370 | 0.5370 |
| `base|emb=12|sh=0.96` | 18 | 0.5013 | 1.0135 | 1.0000 | 0.9948 | -1.6500 | 0.1667 | 0.5357 | 0.5357 |
| `base|emb=12|sh=0.95` | 18 | 0.5013 | 1.0169 | 1.0000 | 0.9948 | -1.6500 | 0.1667 | 0.5345 | 0.5345 |
| `base|emb=12|sh=0.94` | 18 | 0.5013 | 1.0203 | 1.0000 | 0.9948 | -1.6500 | 0.1667 | 0.5333 | 0.5333 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4712 | 1.0167 | 0.2500 | 1.0074 | -8.9725 | 0.3766 | 0.5205 | 0.5205 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4712 | 1.0222 | 0.2500 | 1.0074 | -8.9725 | 0.3766 | 0.5187 | 0.5187 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4712 | 1.0278 | 0.2500 | 1.0074 | -8.9725 | 0.3766 | 0.5169 | 0.5169 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4712 | 1.0333 | 0.2500 | 1.0074 | -8.9725 | 0.3766 | 0.5153 | 0.5153 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5197 | 1.0119 | 0.2948 | 0.9992 | -1.6884 | 0.5869 | 0.5082 | 0.5082 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5197 | 1.0158 | 0.2948 | 0.9992 | -1.6884 | 0.5869 | 0.5070 | 0.5070 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5197 | 1.0198 | 0.2948 | 0.9992 | -1.6884 | 0.5869 | 0.5059 | 0.5059 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5197 | 1.0237 | 0.2948 | 0.9992 | -1.6884 | 0.5869 | 0.5049 | 0.5049 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=316, top_n=32, cutoff=0.7883

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6582 | 0.0401 | 0.9844 | 0.0183 |
| all validations | 0.5055 | 0.1140 | 1.0148 | 0.0306 |

- improvement vs all (primary fraction): `hit +15.26pp, mae +3.0%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0278 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=24|sh=0.97` | 0.5455 | 0.9864 | 1.0000 | 1.1459 | 0.1122 | 10.5031 | 0.9964 | 0.7511 | 0.7511 |
