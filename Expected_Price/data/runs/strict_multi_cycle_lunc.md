# Strict Multi-Cycle Research Result

- symbol: `LUNC`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4458 | 1.0112 | 0.2793 | 1.3643 | -11.3826 | 1.0090 | 0.5220 | 0.5220 |
| `base|emb=12|sh=0.97` | 18 | 0.4962 | 1.0002 | 1.0000 | 0.9268 | -5.2361 | -0.0227 | 0.5198 | 0.5198 |
| `base|emb=24|sh=0.97` | 18 | 0.4989 | 1.0012 | 1.0000 | 0.8957 | -5.8716 | -0.0328 | 0.5187 | 0.5187 |
| `base|emb=12|sh=0.95` | 18 | 0.4925 | 1.0030 | 1.0000 | 0.9323 | -5.4484 | -0.0240 | 0.5183 | 0.5183 |
| `base|emb=24|sh=0.95` | 18 | 0.4961 | 1.0047 | 1.0000 | 0.8977 | -6.0854 | -0.0431 | 0.5179 | 0.5179 |
| `base|emb=12|sh=0.94` | 18 | 0.4925 | 1.0054 | 1.0000 | 0.9323 | -5.4484 | -0.0240 | 0.5175 | 0.5175 |
| `base|emb=24|sh=0.94` | 18 | 0.4961 | 1.0076 | 1.0000 | 0.8977 | -6.0854 | -0.0431 | 0.5168 | 0.5168 |
| `base|emb=24|sh=0.96` | 18 | 0.4926 | 1.0026 | 1.0000 | 0.9017 | -6.4598 | -0.0790 | 0.5107 | 0.5107 |
| `base|emb=12|sh=0.96` | 18 | 0.4884 | 1.0013 | 1.0000 | 0.9379 | -5.8541 | -0.0576 | 0.5106 | 0.5106 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4815 | 1.0027 | 0.4429 | 0.8137 | -13.6575 | -0.1517 | 0.5025 | 0.5025 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4763 | 1.0063 | 0.4429 | 0.8285 | -13.9089 | -0.1619 | 0.5006 | 0.5006 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4763 | 1.0082 | 0.4429 | 0.8285 | -13.9089 | -0.1619 | 0.5000 | 0.5000 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4726 | 1.0045 | 0.4429 | 0.8266 | -14.5255 | -0.1754 | 0.4999 | 0.4999 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4404 | 1.0176 | 0.2793 | 1.2246 | -14.0492 | 0.8938 | 0.4954 | 0.4954 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4613 | 1.0065 | 0.4167 | 0.8738 | -18.7445 | -0.0441 | 0.4948 | 0.4948 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4447 | 1.0253 | 0.2793 | 1.1892 | -13.9622 | 0.9484 | 0.4929 | 0.4929 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4546 | 1.0139 | 0.4167 | 0.8917 | -18.8875 | -0.0536 | 0.4910 | 0.4910 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4447 | 1.0341 | 0.2793 | 1.1892 | -13.9622 | 0.9484 | 0.4900 | 0.4900 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4546 | 1.0179 | 0.4167 | 0.8917 | -18.8875 | -0.0536 | 0.4898 | 0.4898 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4528 | 1.0102 | 0.4167 | 0.8917 | -19.1555 | -0.0721 | 0.4844 | 0.4844 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=340, top_n=34, cutoff=0.7654

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.5911 | 0.0600 | 0.9760 | 0.0187 |
| all validations | 0.4691 | 0.1007 | 1.0105 | 0.0307 |

- improvement vs all (primary fraction): `hit +12.19pp, mae +3.4%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | n/a | n/a | 0.0000 | n/a | n/a | n/a | n/a | n/a | n/a |
| 2 | `base|emb=12|sh=0.95` | 0.5588 | 0.9888 | 1.0000 | 0.5334 | -0.1480 | -13.8556 | -0.6563 | 0.3712 | 0.3712 |
| 3 | `base|emb=12|sh=0.97` | 0.5588 | 0.9932 | 1.0000 | 0.5334 | -0.1480 | -13.8556 | -0.6563 | 0.3694 | 0.3694 |
| 4 | `base|emb=24|sh=0.95` | 0.5429 | 0.9876 | 1.0000 | 0.5381 | -0.1569 | -14.6890 | -0.7041 | 0.3672 | 0.3672 |
| 5 | `base|emb=24|sh=0.97` | 0.5429 | 0.9913 | 1.0000 | 0.5381 | -0.1569 | -14.6890 | -0.7041 | 0.3657 | 0.3657 |
