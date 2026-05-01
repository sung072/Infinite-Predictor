# Strict Multi-Cycle Research Result

- symbol: `XAUT`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5315 | 0.9913 | 0.4614 | 1.2624 | 9.1309 | 1.4592 | 0.6790 | 0.6790 |
| `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5315 | 0.9930 | 0.4614 | 1.2624 | 9.1309 | 1.4592 | 0.6784 | 0.6784 |
| `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5315 | 0.9956 | 0.4614 | 1.2624 | 9.1309 | 1.4592 | 0.6774 | 0.6774 |
| `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5315 | 0.9991 | 0.4614 | 1.2624 | 9.1309 | 1.4592 | 0.6761 | 0.6761 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5304 | 0.9902 | 0.4429 | 1.3725 | 9.5220 | 1.4658 | 0.6527 | 0.6527 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5304 | 0.9900 | 0.4429 | 1.3725 | 9.5220 | 1.4658 | 0.6527 | 0.6527 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5304 | 0.9910 | 0.4429 | 1.3725 | 9.5220 | 1.4658 | 0.6525 | 0.6525 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.5304 | 0.9928 | 0.4429 | 1.3725 | 9.5220 | 1.4658 | 0.6520 | 0.6520 |
| `base|emb=24|sh=0.96` | 18 | 0.5508 | 0.9914 | 1.0000 | 1.0440 | 6.3298 | 1.2708 | 0.6482 | 0.6482 |
| `base|emb=24|sh=0.95` | 18 | 0.5508 | 0.9916 | 1.0000 | 1.0440 | 6.3298 | 1.2708 | 0.6481 | 0.6481 |
| `base|emb=24|sh=0.97` | 18 | 0.5508 | 0.9917 | 1.0000 | 1.0440 | 6.3298 | 1.2708 | 0.6480 | 0.6480 |
| `base|emb=24|sh=0.94` | 18 | 0.5508 | 0.9927 | 1.0000 | 1.0440 | 6.3298 | 1.2708 | 0.6477 | 0.6477 |
| `base|emb=12|sh=0.95` | 18 | 0.5333 | 0.9936 | 1.0000 | 1.0704 | 4.9855 | 1.0908 | 0.5917 | 0.5917 |
| `base|emb=12|sh=0.96` | 18 | 0.5333 | 0.9935 | 1.0000 | 1.0704 | 4.9855 | 1.0908 | 0.5916 | 0.5916 |
| `base|emb=12|sh=0.97` | 18 | 0.5333 | 0.9938 | 1.0000 | 1.0704 | 4.9855 | 1.0908 | 0.5915 | 0.5915 |
| `base|emb=12|sh=0.94` | 18 | 0.5333 | 0.9943 | 1.0000 | 1.0704 | 4.9855 | 1.0908 | 0.5915 | 0.5915 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5225 | 0.9996 | 0.3056 | 1.0217 | -0.7111 | 0.5389 | 0.5861 | 0.5861 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5225 | 0.9999 | 0.3056 | 1.0217 | -0.7111 | 0.5389 | 0.5860 | 0.5860 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5225 | 1.0007 | 0.3056 | 1.0217 | -0.7111 | 0.5389 | 0.5857 | 0.5857 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.5225 | 1.0019 | 0.3056 | 1.0217 | -0.7111 | 0.5389 | 0.5853 | 0.5853 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=364, top_n=37, cutoff=0.8443

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6208 | 0.0610 | 0.9803 | 0.0100 |
| all validations | 0.5308 | 0.0894 | 0.9950 | 0.0215 |

- improvement vs all (primary fraction): `hit +9.00pp, mae +1.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9191 | 0.4444 | 0.9727 | 0.2381 | 22.2882 | 2.1613 | 0.8273 | 0.8273 |
| 2 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9326 | 0.4444 | 0.9727 | 0.2381 | 22.2882 | 2.1613 | 0.8210 | 0.8210 |
| 3 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9460 | 0.4444 | 0.9727 | 0.2381 | 22.2882 | 2.1613 | 0.8149 | 0.8149 |
| 4 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 0.6667 | 0.9595 | 0.4444 | 0.9727 | 0.2381 | 22.2882 | 2.1613 | 0.8089 | 0.8089 |
| 5 | `base|emb=24|sh=0.96` | 0.5143 | 0.9955 | 1.0000 | 1.1437 | 0.0741 | 6.9361 | 0.5843 | 0.7256 | 0.7256 |
