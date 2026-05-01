# Strict Multi-Cycle Research Result

- symbol: `SHIB`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6044 | 1.0036 | 0.4136 | 1.0055 | 16.2536 | 1.5135 | 0.6820 | 0.6820 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.6130 | 1.0010 | 0.4198 | 1.1711 | 22.9221 | 2.0139 | 0.6665 | 0.6665 |
| `base|emb=12|sh=0.97` | 18 | 0.5934 | 1.0061 | 1.0000 | 1.0825 | 15.2624 | 1.6305 | 0.6568 | 0.6568 |
| `base|emb=24|sh=0.97` | 18 | 0.5690 | 1.0102 | 1.0000 | 1.0263 | 10.9492 | 0.9181 | 0.6396 | 0.6396 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5339 | 1.0384 | 0.3688 | 1.3085 | 10.0321 | 1.8432 | 0.6323 | 0.6323 |
| `base|emb=12|sh=0.95` | 18 | 0.5594 | 1.0102 | 1.0000 | 1.0319 | 7.8812 | 0.7960 | 0.6283 | 0.6283 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5333 | 1.0288 | 0.3688 | 1.2890 | 9.0162 | 1.5074 | 0.6229 | 0.6229 |
| `base|emb=24|sh=0.95` | 18 | 0.5358 | 1.0169 | 1.0000 | 1.0491 | 6.4136 | 0.6390 | 0.5993 | 0.5993 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5186 | 1.0480 | 0.3688 | 1.1177 | 2.3955 | 0.3710 | 0.5986 | 0.5986 |
| `base|emb=12|sh=0.94` | 18 | 0.5522 | 1.0122 | 1.0000 | 1.0263 | 6.5651 | 0.7348 | 0.5980 | 0.5980 |
| `base|emb=12|sh=0.96` | 18 | 0.5595 | 1.0082 | 1.0000 | 1.0391 | 7.9626 | 1.1176 | 0.5965 | 0.5965 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5371 | 1.0060 | 0.4136 | 1.0031 | 3.4759 | 0.8567 | 0.5942 | 0.5942 |
| `base|emb=24|sh=0.96` | 18 | 0.5334 | 1.0136 | 1.0000 | 1.0346 | 5.3163 | 0.6879 | 0.5936 | 0.5936 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5302 | 1.0048 | 0.4136 | 1.0150 | 2.8397 | 0.7976 | 0.5926 | 0.5926 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5317 | 1.0072 | 0.4136 | 1.0146 | 3.1502 | 0.8555 | 0.5894 | 0.5894 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4860 | 1.0458 | 0.3796 | 1.3190 | -8.8308 | 1.2356 | 0.5837 | 0.5837 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4811 | 1.0343 | 0.3796 | 1.3315 | -9.9733 | 1.2429 | 0.5826 | 0.5826 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4838 | 1.0572 | 0.3796 | 1.2162 | -10.7236 | 0.5709 | 0.5794 | 0.5794 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5458 | 1.0016 | 0.4198 | 1.0542 | 6.6156 | 0.9573 | 0.5755 | 0.5755 |
| `base|emb=24|sh=0.94` | 18 | 0.5268 | 1.0203 | 1.0000 | 1.0415 | 4.6398 | 0.5802 | 0.5729 | 0.5729 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=356, top_n=36, cutoff=0.8285

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7031 | 0.0973 | 0.9904 | 0.0104 |
| all validations | 0.5386 | 0.1400 | 1.0204 | 0.0573 |

- improvement vs all (primary fraction): `hit +16.45pp, mae +2.9%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `base|emb=24|sh=0.97` | 0.6800 | 0.9812 | 1.0000 | 1.1618 | 0.3481 | 32.5775 | 3.5569 | 0.8319 | 0.8319 |
| 4 | `base|emb=12|sh=0.97` | 0.6786 | 0.9835 | 1.0000 | 0.5971 | 0.0798 | 7.4653 | 0.5926 | 0.7393 | 0.7393 |
| 5 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.5000 | 0.9950 | 0.4444 | 0.2827 | -0.3995 | -37.3905 | -0.9152 | 0.3365 | 0.3365 |
