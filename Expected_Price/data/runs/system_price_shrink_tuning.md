# 시스템가 수축 튜닝 리포트 (OOS/WF 중심)

- 케이스 수: **4** (기본: BTC/ETH OOS/WF)
- baseline mean_mae_ratio: **2.7625** / mean_hit_rate: **0.5232**
- best overall: **shrink w=0.600** (ratio=1.4096, hit=0.5232)

## Top 10 (ratio 낮은 순)

| rank | family | param | mean_mae_ratio | mean_hit_rate |
|------|--------|-------|----------------|---------------|
| 1 | `shrink` | `w=0.600` | 1.4096 | 0.5232 |
| 2 | `shrink` | `w=0.500` | 1.6057 | 0.5232 |
| 3 | `shrink` | `w=0.400` | 1.8228 | 0.5232 |
| 4 | `shrink` | `w=0.300` | 2.0490 | 0.5232 |
| 5 | `shrink` | `w=0.250` | 2.1648 | 0.5232 |
| 6 | `shrink` | `w=0.200` | 2.2821 | 0.5232 |
| 7 | `tension` | `cap=0.100,max_pull=0.750` | 2.3475 | 0.5232 |
| 8 | `shrink` | `w=0.150` | 2.4008 | 0.5232 |
| 9 | `tension` | `cap=0.100,max_pull=0.500` | 2.4847 | 0.5232 |
| 10 | `shrink` | `w=0.100` | 2.5203 | 0.5232 |

## 후보 비교

- best shrink: `w=0.600` -> ratio=1.4096, hit=0.5232
- best tension: `cap=0.100,max_pull=0.750` -> ratio=2.3475, hit=0.5232

## 해석

- 목표는 ratio<1 이며, 여전히 1을 크게 넘으면 구조/앵커 자체 개선이 우선.
- 본 결과는 OOS/WF 연구용이며, 매매 권고가 아님.
