# 시스템가 수축 튜닝 리포트 (OOS/WF 중심)

- 케이스 수: **4** (기본: BTC/ETH OOS/WF)
- baseline mean_mae_ratio: **2.7625** / mean_hit_rate: **0.5232**
- best overall: **shrink w=0.950** (ratio=0.9950, hit=0.5232)

## Top 10 (ratio 낮은 순)

| rank | family | param | mean_mae_ratio | mean_hit_rate |
|------|--------|-------|----------------|---------------|
| 1 | `shrink` | `w=0.950` | 0.9950 | 0.5232 |
| 2 | `shrink` | `w=1.000` | 1.0000 | nan |
| 3 | `shrink` | `w=0.900` | 1.0104 | 0.5232 |
| 4 | `shrink` | `w=0.850` | 1.0463 | 0.5232 |
| 5 | `shrink` | `w=0.800` | 1.0997 | 0.5232 |
| 6 | `shrink` | `w=0.750` | 1.1638 | 0.5232 |
| 7 | `shrink` | `w=0.700` | 1.2370 | 0.5232 |
| 8 | `shrink` | `w=0.650` | 1.3194 | 0.5232 |
| 9 | `shrink` | `w=0.600` | 1.4096 | 0.5232 |
| 10 | `shrink` | `w=0.500` | 1.6057 | 0.5232 |

## 후보 비교

- best shrink: `w=0.950` -> ratio=0.9950, hit=0.5232
- best tension: `cap=0.100,max_pull=0.750` -> ratio=2.3475, hit=0.5232

## 해석

- 목표는 ratio<1 이며, 여전히 1을 크게 넘으면 구조/앵커 자체 개선이 우선.
- 본 결과는 OOS/WF 연구용이며, 매매 권고가 아님.
