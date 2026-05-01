# Strict Multi-Cycle Research Result

- symbol: `BTC`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5217 | 0.9920 | 0.3580 | 1.3784 | 5.3966 | 2.1602 | 0.5850 | 0.5850 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5217 | 0.9931 | 0.3580 | 1.3784 | 5.3966 | 2.1602 | 0.5844 | 0.5844 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5217 | 0.9944 | 0.3580 | 1.3784 | 5.3966 | 2.1602 | 0.5838 | 0.5838 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5217 | 0.9956 | 0.3580 | 1.3784 | 5.3966 | 2.1602 | 0.5832 | 0.5832 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4965 | 0.9938 | 0.3673 | 1.1842 | 0.7247 | 1.2085 | 0.5665 | 0.5665 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4965 | 0.9947 | 0.3673 | 1.1842 | 0.7247 | 1.2085 | 0.5661 | 0.5661 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4965 | 0.9958 | 0.3673 | 1.1842 | 0.7247 | 1.2085 | 0.5656 | 0.5656 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4965 | 0.9968 | 0.3673 | 1.1842 | 0.7247 | 1.2085 | 0.5651 | 0.5651 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4672 | 1.0206 | 0.3627 | 1.1429 | -2.8685 | 0.7895 | 0.5648 | 0.5648 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4672 | 1.0295 | 0.3627 | 1.1429 | -2.8685 | 0.7895 | 0.5624 | 0.5624 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4672 | 1.0407 | 0.3627 | 1.1429 | -2.8685 | 0.7895 | 0.5595 | 0.5595 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4672 | 1.0549 | 0.3627 | 1.1429 | -2.8685 | 0.7895 | 0.5559 | 0.5559 |
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4781 | 1.0078 | 0.3765 | 1.1678 | 0.7885 | 0.2637 | 0.5555 | 0.5555 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4781 | 1.0115 | 0.3765 | 1.1678 | 0.7885 | 0.2637 | 0.5543 | 0.5543 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4781 | 1.0167 | 0.3765 | 1.1678 | 0.7885 | 0.2637 | 0.5526 | 0.5526 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4781 | 1.0246 | 0.3765 | 1.1678 | 0.7885 | 0.2637 | 0.5500 | 0.5500 |
| `base|emb=24|sh=0.97` | 18 | 0.4905 | 1.0009 | 1.0000 | 1.0849 | -0.2905 | 0.4393 | 0.5148 | 0.5148 |
| `base|emb=24|sh=0.96` | 18 | 0.4905 | 1.0019 | 1.0000 | 1.0849 | -0.2905 | 0.4393 | 0.5145 | 0.5145 |
| `base|emb=24|sh=0.95` | 18 | 0.4905 | 1.0034 | 1.0000 | 1.0849 | -0.2905 | 0.4393 | 0.5139 | 0.5139 |
| `base|emb=24|sh=0.94` | 18 | 0.4905 | 1.0060 | 1.0000 | 1.0849 | -0.2905 | 0.4393 | 0.5130 | 0.5130 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=372, top_n=38, cutoff=0.8222

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6386 | 0.0645 | 0.9709 | 0.0178 |
| all validations | 0.4907 | 0.0964 | 1.0081 | 0.0500 |

- improvement vs all (primary fraction): `hit +14.79pp, mae +3.7%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Dev cohort sensitivity (multiple top fractions)

각 fraction마다 `dev_cohort_sensitivity` 에 전체 코호트 dict가 들어가므로 fraction 개수는 적게 유지하는 것이 좋다.

Improvement vs all: hit 은 (top−all)을 퍼센트포인트로, mae_ratio 는 (all−top)/|all|×100 상대% (양수면 top 이 더 우수).

| fraction | n_top | cutoff | hit_top | mae_top | rr_top | sharpe_ann_top | calmar_top | vs all |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0.05 | 19 | 0.8666 | 0.6603 | 0.9647 | 1.8650 | 45.9063 | 8.1533 | `hit +16.96pp, mae +4.3%rel` |
| 0.1 | 38 | 0.8222 | 0.6386 | 0.9709 | 1.8199 | 40.4556 | 6.9314 | `hit +14.79pp, mae +3.7%rel` |
| 0.2 | 75 | 0.7752 | 0.5928 | 0.9790 | 1.9040 | 31.5166 | 4.6043 | `hit +10.21pp, mae +2.9%rel` |

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 3 | `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | `base|emb=24|sh=0.97` | 0.5429 | 0.9797 | 1.0000 | 0.8150 | -0.0119 | -1.1170 | -0.1120 | 0.4995 | 0.4995 |
