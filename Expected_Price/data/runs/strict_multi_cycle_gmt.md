# Strict Multi-Cycle Research Result

- symbol: `GMT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4641 | 1.0190 | 0.3657 | 1.6519 | 2.2969 | 1.7049 | 0.5880 | 0.5880 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4641 | 1.0256 | 0.3657 | 1.6519 | 2.2969 | 1.7049 | 0.5863 | 0.5863 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4641 | 1.0330 | 0.3657 | 1.6519 | 2.2969 | 1.7049 | 0.5844 | 0.5844 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4641 | 1.0404 | 0.3657 | 1.6519 | 2.2969 | 1.7049 | 0.5828 | 0.5828 |
| `base|emb=12|sh=0.97` | 18 | 0.5108 | 1.0043 | 1.0000 | 1.0575 | 1.5340 | 0.5972 | 0.5783 | 0.5783 |
| `base|emb=12|sh=0.96` | 18 | 0.5108 | 1.0060 | 1.0000 | 1.0575 | 1.5340 | 0.5972 | 0.5777 | 0.5777 |
| `base|emb=12|sh=0.95` | 18 | 0.5108 | 1.0083 | 1.0000 | 1.0575 | 1.5340 | 0.5972 | 0.5769 | 0.5769 |
| `base|emb=12|sh=0.94` | 18 | 0.5108 | 1.0107 | 1.0000 | 1.0575 | 1.5340 | 0.5972 | 0.5761 | 0.5761 |
| `base|emb=24|sh=0.97` | 18 | 0.5222 | 1.0007 | 1.0000 | 1.0133 | 0.9275 | 0.5291 | 0.5754 | 0.5754 |
| `base|emb=24|sh=0.96` | 18 | 0.5222 | 1.0012 | 1.0000 | 1.0133 | 0.9275 | 0.5291 | 0.5752 | 0.5752 |
| `base|emb=24|sh=0.95` | 18 | 0.5222 | 1.0024 | 1.0000 | 1.0133 | 0.9275 | 0.5291 | 0.5748 | 0.5748 |
| `base|emb=24|sh=0.94` | 18 | 0.5222 | 1.0038 | 1.0000 | 1.0133 | 0.9275 | 0.5291 | 0.5743 | 0.5743 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5135 | 1.0110 | 0.3364 | 1.4581 | 5.9070 | 1.9872 | 0.5590 | 0.5590 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5135 | 1.0152 | 0.3364 | 1.4581 | 5.9070 | 1.9872 | 0.5579 | 0.5579 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5135 | 1.0211 | 0.3364 | 1.4581 | 5.9070 | 1.9872 | 0.5564 | 0.5564 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5135 | 1.0270 | 0.3364 | 1.4581 | 5.9070 | 1.9872 | 0.5550 | 0.5550 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5047 | 1.0017 | 0.3688 | 1.1112 | -1.2431 | 0.7032 | 0.5550 | 0.5550 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5047 | 1.0025 | 0.3688 | 1.1112 | -1.2431 | 0.7032 | 0.5548 | 0.5548 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5047 | 1.0037 | 0.3688 | 1.1112 | -1.2431 | 0.7032 | 0.5545 | 0.5545 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5047 | 1.0049 | 0.3688 | 1.1112 | -1.2431 | 0.7032 | 0.5542 | 0.5542 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=396, top_n=40, cutoff=0.8537

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6625 | 0.1181 | 0.9624 | 0.0202 |
| all validations | 0.4974 | 0.1521 | 1.0114 | 0.0505 |

- improvement vs all (primary fraction): `hit +16.51pp, mae +4.8%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.1111 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=12|sh=0.97` | 0.4848 | 0.9945 | 1.0000 | 0.7864 | -0.1148 | -10.7403 | -0.5389 | 0.3701 | 0.3701 |
