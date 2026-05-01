# Strict Multi-Cycle 10종목 요약

- success=10, failed=0
- symbols=BTC,ETH,SOL,BNB,XRP,ADA,DOGE,AVAX,LINK,TRX

## 종목별 best 공식

| symbol | hit_rate | mae_ratio | coverage | cluster_key |
|---|---:|---:|---:|---|
| ADA | 0.6061 | 0.9864 | 0.9444 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| AVAX | 0.6818 | 0.9854 | 0.8056 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| BNB | 0.5429 | 0.9813 | 1.0000 | `base|emb=12|sh=0.96` |
| BTC | 0.5429 | 0.9797 | 1.0000 | `base|emb=24|sh=0.97` |
| DOGE | 0.6571 | 0.9690 | 1.0000 | `base|emb=24|sh=0.95` |
| ETH | 0.5429 | 0.9809 | 1.0000 | `base|emb=24|sh=0.97` |
| LINK | 0.6000 | 0.9781 | 0.8056 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| SOL | 0.6000 | 0.9708 | 1.0000 | `base|emb=24|sh=0.95` |
| TRX | 0.5000 | 1.0059 | 1.0000 | `base|emb=12|sh=0.97` |
| XRP | 0.6562 | 0.9702 | 0.8889 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |

## 심볼쌍 연구 (공식 유사도 상위 20)

| pair | formula_similarity | hit_gap_abs | mae_ratio_gap_abs |
|---|---:|---:|---:|
| `BTC-ETH` | 1.0000 | 0.0000 | 0.0012 |
| `ADA-LINK` | 1.0000 | 0.0061 | 0.0082 |
| `AVAX-XRP` | 1.0000 | 0.0256 | 0.0152 |
| `BNB-TRX` | 1.0000 | 0.0429 | 0.0246 |
| `ADA-XRP` | 1.0000 | 0.0502 | 0.0162 |
| `LINK-XRP` | 1.0000 | 0.0563 | 0.0080 |
| `BTC-SOL` | 1.0000 | 0.0571 | 0.0088 |
| `DOGE-SOL` | 1.0000 | 0.0571 | 0.0018 |
| `ETH-SOL` | 1.0000 | 0.0571 | 0.0100 |
| `ADA-AVAX` | 1.0000 | 0.0758 | 0.0010 |
| `AVAX-LINK` | 1.0000 | 0.0818 | 0.0072 |
| `BTC-DOGE` | 1.0000 | 0.1143 | 0.0107 |
| `DOGE-ETH` | 1.0000 | 0.1143 | 0.0119 |
| `BNB-BTC` | 0.8000 | 0.0000 | 0.0016 |
| `BNB-ETH` | 0.8000 | 0.0000 | 0.0004 |
| `BTC-TRX` | 0.8000 | 0.0429 | 0.0262 |
| `ETH-TRX` | 0.8000 | 0.0429 | 0.0251 |
| `BNB-SOL` | 0.8000 | 0.0571 | 0.0105 |
| `SOL-TRX` | 0.8000 | 0.1000 | 0.0351 |
| `BNB-DOGE` | 0.8000 | 0.1143 | 0.0123 |
