# Strict Multi-Cycle Research Result

- symbol: `QNT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5948 | 0.9803 | 0.3472 | 1.3173 | 26.7548 | 2.2566 | 0.6726 | 0.6726 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5948 | 0.9829 | 0.3472 | 1.3173 | 26.7548 | 2.2566 | 0.6712 | 0.6712 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5948 | 0.9856 | 0.3472 | 1.3173 | 26.7548 | 2.2566 | 0.6699 | 0.6699 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5666 | 0.9922 | 0.3349 | 1.5402 | 19.9935 | 4.8387 | 0.6697 | 0.6697 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5666 | 0.9926 | 0.3349 | 1.5402 | 19.9935 | 4.8387 | 0.6693 | 0.6693 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5666 | 0.9930 | 0.3349 | 1.5402 | 19.9935 | 4.8387 | 0.6689 | 0.6689 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5948 | 0.9883 | 0.3472 | 1.3173 | 26.7548 | 2.2566 | 0.6686 | 0.6686 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5666 | 0.9936 | 0.3349 | 1.5402 | 19.9935 | 4.8387 | 0.6685 | 0.6685 |
| `base|emb=12|sh=0.96` | 18 | 0.5223 | 0.9957 | 1.0000 | 1.1363 | 6.5978 | 0.7556 | 0.6554 | 0.6554 |
| `base|emb=12|sh=0.97` | 18 | 0.5223 | 0.9958 | 1.0000 | 1.1363 | 6.5978 | 0.7556 | 0.6553 | 0.6553 |
| `base|emb=12|sh=0.95` | 18 | 0.5223 | 0.9959 | 1.0000 | 1.1363 | 6.5978 | 0.7556 | 0.6553 | 0.6553 |
| `base|emb=12|sh=0.94` | 18 | 0.5223 | 0.9963 | 1.0000 | 1.1363 | 6.5978 | 0.7556 | 0.6552 | 0.6552 |
| `base|emb=24|sh=0.96` | 18 | 0.5038 | 0.9962 | 1.0000 | 1.1948 | 5.4198 | 0.7703 | 0.6219 | 0.6219 |
| `base|emb=24|sh=0.95` | 18 | 0.5038 | 0.9963 | 1.0000 | 1.1948 | 5.4198 | 0.7703 | 0.6218 | 0.6218 |
| `base|emb=24|sh=0.97` | 18 | 0.5038 | 0.9965 | 1.0000 | 1.1948 | 5.4198 | 0.7703 | 0.6217 | 0.6217 |
| `base|emb=24|sh=0.94` | 18 | 0.5038 | 0.9966 | 1.0000 | 1.1948 | 5.4198 | 0.7703 | 0.6217 | 0.6217 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4985 | 1.0007 | 0.3873 | 1.1339 | 0.9472 | 0.3032 | 0.5805 | 0.5805 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4985 | 1.0014 | 0.3873 | 1.1339 | 0.9472 | 0.3032 | 0.5803 | 0.5803 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4985 | 1.0028 | 0.3873 | 1.1339 | 0.9472 | 0.3032 | 0.5797 | 0.5797 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4985 | 1.0046 | 0.3873 | 1.1339 | 0.9472 | 0.3032 | 0.5791 | 0.5791 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=360, top_n=36, cutoff=0.8361

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.7189 | 0.1564 | 0.9624 | 0.0254 |
| all validations | 0.5227 | 0.1085 | 0.9968 | 0.0225 |

- improvement vs all (primary fraction): `hit +19.62pp, mae +3.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6429 | 0.9656 | 0.3889 | 1.1812 | 0.2826 | 26.4493 | 1.5814 | 0.7973 | 0.7973 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6429 | 0.9714 | 0.3889 | 1.1812 | 0.2826 | 26.4493 | 1.5814 | 0.7949 | 0.7949 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6429 | 0.9771 | 0.3889 | 1.1812 | 0.2826 | 26.4493 | 1.5814 | 0.7925 | 0.7925 |
| 4 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6000 | 0.9705 | 0.6944 | 0.7926 | 0.0646 | 6.0454 | 0.3752 | 0.7281 | 0.7281 |
| 5 | `base|emb=12|sh=0.96` | 0.6000 | 0.9792 | 1.0000 | 0.6781 | 0.0066 | 0.6180 | 0.0282 | 0.5932 | 0.5932 |
