# Strict Multi-Cycle Research Result

- symbol: `RUNE`
- cycles: 19 (dev rows=540, unseen rows=180)
- strict rule: cycle(i) discovered formulas are validated only on cycle(i+1)

## Meta Synthesis (cluster summary)

| cluster_key | n_eval | hit_mean | mae_ratio_mean | coverage_mean | mean_rr_mean | sharpe_ann_mean | calmar_mean | composite_mean | rank_score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `base|emb=12|sh=0.97` | 18 | 0.5123 | 1.0105 | 1.0000 | 0.8450 | -4.8792 | 0.0263 | 0.5104 | 0.5104 |
| `base|emb=12|sh=0.96` | 18 | 0.5123 | 1.0143 | 1.0000 | 0.8450 | -4.8792 | 0.0263 | 0.5090 | 0.5090 |
| `base|emb=12|sh=0.95` | 18 | 0.5123 | 1.0181 | 1.0000 | 0.8450 | -4.8792 | 0.0263 | 0.5076 | 0.5076 |
| `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4961 | 1.0151 | 0.4259 | 0.9848 | -4.3892 | 0.0782 | 0.5069 | 0.5069 |
| `base|emb=12|sh=0.94` | 18 | 0.5123 | 1.0220 | 1.0000 | 0.8450 | -4.8792 | 0.0263 | 0.5061 | 0.5061 |
| `trust_low40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4961 | 1.0201 | 0.4259 | 0.9848 | -4.3892 | 0.0782 | 0.5051 | 0.5051 |
| `trust_low40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4961 | 1.0252 | 0.4259 | 0.9848 | -4.3892 | 0.0782 | 0.5033 | 0.5033 |
| `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4961 | 1.0302 | 0.4259 | 0.9848 | -4.3892 | 0.0782 | 0.5015 | 0.5015 |
| `base|emb=24|sh=0.97` | 18 | 0.5146 | 1.0083 | 1.0000 | 0.8397 | -4.8185 | -0.0323 | 0.4999 | 0.4999 |
| `base|emb=24|sh=0.96` | 18 | 0.5146 | 1.0116 | 1.0000 | 0.8397 | -4.8185 | -0.0323 | 0.4986 | 0.4986 |
| `base|emb=24|sh=0.95` | 18 | 0.5146 | 1.0150 | 1.0000 | 0.8397 | -4.8185 | -0.0323 | 0.4973 | 0.4973 |
| `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4803 | 1.0172 | 0.3765 | 0.9057 | -9.1065 | -0.1069 | 0.4969 | 0.4969 |
| `base|emb=24|sh=0.94` | 18 | 0.5146 | 1.0185 | 1.0000 | 0.8397 | -4.8185 | -0.0323 | 0.4960 | 0.4960 |
| `trust_high40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4803 | 1.0230 | 0.3765 | 0.9057 | -9.1065 | -0.1069 | 0.4949 | 0.4949 |
| `trust_low40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4828 | 1.0201 | 0.4429 | 0.8703 | -10.7887 | -0.0477 | 0.4933 | 0.4933 |
| `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4803 | 1.0287 | 0.3765 | 0.9057 | -9.1065 | -0.1069 | 0.4929 | 0.4929 |
| `trust_low40|emb=12|sh=0.96|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4828 | 1.0268 | 0.4429 | 0.8703 | -10.7887 | -0.0477 | 0.4910 | 0.4910 |
| `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` | 18 | 0.4803 | 1.0347 | 0.3765 | 0.9057 | -9.1065 | -0.1069 | 0.4909 | 0.4909 |
| `trust_low40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4828 | 1.0335 | 0.4429 | 0.8703 | -10.7887 | -0.0477 | 0.4888 | 0.4888 |
| `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` | 18 | 0.4828 | 1.0401 | 0.4429 | 0.8703 | -10.7887 | -0.0477 | 0.4867 | 0.4867 |

## Dev cohort (top fraction by composite_score)

- fraction=0.1, n_eligible=368, top_n=37, cutoff=0.7598

| scope | hit mean | hit pstdev | mae_ratio mean | mae_ratio pstdev |
|---|---:|---:|---:|---:|
| top bucket | 0.6113 | 0.0573 | 0.9955 | 0.0109 |
| all validations | 0.4944 | 0.1006 | 1.0210 | 0.0343 |

- improvement vs all (primary fraction): `hit +11.69pp, mae +2.5%rel` (hit=퍼센트포인트 차, mae=%rel은 전체 대비 낮아진 비율, 양수면 유리)

## Final Unseen Validation

| rank | cluster_key | hit_rate | mae_ratio | coverage | mean_rr | sharpe_bar | sharpe_ann | calmar | comp_raw | rank_score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` | 0.6667 | 1.0271 | 0.2222 | 0.9975 | 0.2642 | 24.7239 | n/a | 0.7209 | 0.7209 |
| 2 | `base|emb=12|sh=0.94` | 0.5455 | 0.9665 | 1.0000 | 0.6270 | -0.1142 | -10.6929 | -0.5591 | 0.3857 | 0.3857 |
| 3 | `base|emb=12|sh=0.95` | 0.5455 | 0.9701 | 1.0000 | 0.6270 | -0.1142 | -10.6929 | -0.5591 | 0.3841 | 0.3841 |
| 4 | `base|emb=12|sh=0.96` | 0.5455 | 0.9761 | 1.0000 | 0.6270 | -0.1142 | -10.6929 | -0.5591 | 0.3816 | 0.3816 |
| 5 | `base|emb=12|sh=0.97` | 0.5455 | 0.9821 | 1.0000 | 0.6270 | -0.1142 | -10.6929 | -0.5591 | 0.3791 | 0.3791 |
