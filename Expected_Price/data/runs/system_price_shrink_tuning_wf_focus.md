# 시스템가 수축 튜닝 리포트 (OOS/WF 중심)

- 케이스 수: **4** (기본: BTC/ETH OOS/WF)
- baseline mean_mae_ratio: **2.7625** / mean_hit_rate: **0.5232**
- best overall: **shrink w=0.960** (ratio=0.9944, hit=0.5232)

## Top 10 (ratio 낮은 순)

| rank | family | param | mean_mae_ratio | mean_hit_rate |
|------|--------|-------|----------------|---------------|
| 1 | `shrink` | `w=0.960` | 0.9944 | 0.5232 |
| 2 | `shrink` | `w=0.970` | 0.9947 | 0.5232 |
| 3 | `shrink` | `w=0.950` | 0.9950 | 0.5232 |
| 4 | `regime_shrink` | `q=0.50,w_calm=0.950,w_stress=0.950` | 0.9950 | 0.5232 |
| 5 | `regime_shrink` | `q=0.70,w_calm=0.950,w_stress=0.950` | 0.9950 | 0.5232 |
| 6 | `regime_shrink` | `q=0.80,w_calm=0.950,w_stress=0.950` | 0.9950 | 0.5232 |
| 7 | `regime_shrink` | `q=0.50,w_calm=0.950,w_stress=0.970` | 0.9951 | 0.5232 |
| 8 | `regime_shrink` | `q=0.50,w_calm=0.930,w_stress=0.950` | 0.9957 | 0.5232 |
| 9 | `shrink` | `w=0.980` | 0.9958 | 0.5232 |
| 10 | `regime_shrink` | `q=0.50,w_calm=0.930,w_stress=0.970` | 0.9958 | 0.5232 |

## 후보 비교

- best shrink: `w=0.960` -> ratio=0.9944, hit=0.5232
- best tension: `cap=0.100,max_pull=0.750` -> ratio=2.3475, hit=0.5232

## 해석

- 목표는 ratio<1 이며, 여전히 1을 크게 넘으면 구조/앵커 자체 개선이 우선.
- 본 결과는 OOS/WF 연구용이며, 매매 권고가 아님.
