# Strict Multi-Cycle 요약 (3종목)

- success=2, failed=1
- symbols=BTC,ETH,CHIP

## 집계 정확도·오차 (finite만)

- n_finite_hit: 2, mean_hit: 0.5791, median_hit: 0.6154
- n_finite_mae_ratio: 2, mean_mae_ratio: 0.9583, median_mae_ratio: 0.9797

## 종목별 best 공식

| symbol | hit_rate | mae_ratio | coverage | mean_rr | sharpe_ann | calmar | comp_raw | rank_score | cluster_key |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BTC | 0.5429 | 0.9797 | 1.0000 | 0.8150 | -1.1170 | -0.1120 | 0.4995 | 0.4995 | `base|emb=24|sh=0.97` |
| ETH | 0.6154 | 0.9368 | 0.7222 | 0.9988 | 16.8962 | 1.3754 | 0.7911 | 0.7911 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |

## 실패 종목

- `CHIP`: Command '['C:\\Users\\hadro\\AppData\\Local\\Programs\\Python\\Python311\\python.exe', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\scripts\\strict_multi_cycle_research.py', '--symbol', 'CHIP', '--ohlcv', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\chipusdt_1h_30d.csv', '--factors-csv', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\derived\\chipusdt_factors_4p.csv', '--train-bars', '120', '--val-bars', '36', '--cycle-step', '20', '--embargos', '12,24', '--shrinks', '0.94,0.95,0.96,0.97', '--top-k', '5', '--min-evals', '3', '--unseen-ratio', '0.25', '--seed', '1', '--out-json', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\runs\\strict_multi_cycle_chip.json', '--out-md', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\runs\\strict_multi_cycle_chip.md']' returned non-zero exit status 2.

## 심볼쌍 연구 (공식 유사도 상위 20)

| pair | formula_similarity | hit_gap_abs | mae_ratio_gap_abs |
|---|---:|---:|---:|
| `BTC-ETH` | 0.2000 | 0.0725 | 0.0428 |
