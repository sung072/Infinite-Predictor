# Strict Multi-Cycle 요약 (100종목)

- success=97, failed=3
- symbols=BTC,ETH,CHIP,DOGE,PLUME,SOL,MEGA,USD1,XRP,BIO,BNB,ZEC,PENGU,PEPE,RLUSD,U,TRX,ORCA,LUNC,EUR,APT,APE,ENSO,ADA,XAUT,WLFI,TAO,PAXG,UTK,LTC,TON,SUI,LINK,币安人生,AVAX,ZBT,WLD,VANA,PENDLE,AAVE,SHIB,WIF,KAT,CHZ,BANANAS31,LUNA,AI,ENA,ARB,TRUMP,API3,XLM,PUMP,NEAR,USTC,KITE,FLOW,LUMIA,STO,XUSD,NOM,SAND,AIXBT,HIGH,ASTER,FET,UNI,HBAR,DOT,POL,GIGGLE,ORDI,DASH,OPEN,NFP,KAITO,EDU,JST,ACH,BONK,FIL,0G,CRV,TIA,RAY,BCH,LRC,TRB,CGPT,XPL,HYPER,AXS,S,MOVR,ZAMA,BROCCOLI714,SOMI,DEXE,NIGHT,FLOKI

## 집계 정확도·오차 (finite만)

- n_finite_hit: 97, mean_hit: 0.5661, median_hit: 0.5588
- n_finite_mae_ratio: 97, mean_mae_ratio: 0.9905, median_mae_ratio: 0.9917

## 종목별 best 공식

| symbol | hit_rate | mae_ratio | coverage | mean_rr | sharpe_ann | calmar | comp_raw | rank_score | cluster_key |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0G | 0.5714 | 1.0118 | 0.5278 | 1.3413 | 21.8489 | 1.4689 | 0.7680 | 0.7680 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` |
| AAVE | 0.7500 | 1.0019 | 0.3611 | 0.3583 | 2.5478 | 0.0667 | 0.6729 | 0.6729 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` |
| ACH | 0.4857 | 0.9862 | 1.0000 | 0.9012 | -5.4662 | -0.4539 | 0.3891 | 0.3891 | `base|emb=12|sh=0.96` |
| ADA | 0.6061 | 0.9795 | 0.9444 | 0.7758 | 6.0896 | 0.3864 | 0.7252 | 0.7252 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| AI | 0.5455 | 0.9864 | 1.0000 | 1.1459 | 10.5031 | 0.9964 | 0.7511 | 0.7511 | `base|emb=24|sh=0.97` |
| AIXBT | 0.5000 | 1.0085 | 0.8056 | 0.7600 | -10.5917 | -0.6495 | 0.3628 | 0.3628 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| APE | 0.4706 | 1.0463 | 1.0000 | 0.8337 | -10.5835 | -0.6596 | 0.3457 | 0.3457 | `base|emb=12|sh=0.95` |
| API3 | 0.6857 | 0.9810 | 1.0000 | 0.8838 | 24.7499 | 3.7170 | 0.8224 | 0.8224 | `base|emb=24|sh=0.97` |
| APT | 0.8333 | 0.9400 | 0.3611 | 0.5570 | 26.9412 | 1.9281 | 0.8264 | 0.8264 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| ARB | 0.5161 | 0.9962 | 1.0000 | 1.2195 | 9.1268 | 0.6661 | 0.7337 | 0.7337 | `base|emb=12|sh=0.94` |
| ASTER | 0.6154 | 1.0028 | 0.4722 | 1.0239 | 18.9433 | 1.7468 | 0.7737 | 0.7737 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` |
| AVAX | 0.6818 | 0.9854 | 0.8056 | 1.0145 | 29.3607 | 2.6569 | 0.8121 | 0.8121 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| AXS | 0.5625 | 0.9719 | 0.5000 | 0.6199 | -8.1595 | -0.5743 | 0.3870 | 0.3870 | `trust_high40|emb=12|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| BANANAS31 | 0.4857 | 0.9821 | 1.0000 | 1.2650 | 6.8055 | 0.9451 | 0.7415 | 0.7415 | `base|emb=24|sh=0.94` |
| BCH | 0.6667 | 0.9523 | 0.8333 | 0.5501 | 3.5762 | 0.2755 | 0.7144 | 0.7144 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| BIO | 0.6250 | 0.9715 | 0.6667 | 0.4927 | -6.8167 | -0.4582 | 0.3991 | 0.3991 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| BNB | 0.5652 | 0.9647 | 0.6389 | 0.8727 | 4.2871 | 0.3058 | 0.7140 | 0.7140 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| BONK | 0.6818 | 0.9759 | 0.7222 | 0.7623 | 18.4843 | 1.0376 | 0.7668 | 0.7668 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| BROCCOLI714 | 0.6471 | 0.9751 | 1.0000 | 1.0906 | 22.4921 | 3.5634 | 0.8249 | 0.8249 | `base|emb=24|sh=0.97` |
| BTC | 0.5429 | 0.9797 | 1.0000 | 0.8150 | -1.1170 | -0.1120 | 0.4995 | 0.4995 | `base|emb=24|sh=0.97` |
| CGPT | 0.5714 | 1.0006 | 0.8333 | 1.1581 | 16.7270 | 0.7219 | 0.7428 | 0.7428 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` |
| CHZ | 0.3824 | 1.0299 | 1.0000 | 0.6876 | -28.9823 | -0.6701 | 0.3267 | 0.3267 | `base|emb=12|sh=0.97` |
| CRV | 0.5294 | 0.9963 | 1.0000 | 0.8440 | -1.9682 | -0.2653 | 0.4533 | 0.4533 | `base|emb=12|sh=0.97` |
| DASH | 0.4545 | 1.0016 | 1.0000 | 0.8462 | -12.9925 | -0.6912 | 0.3589 | 0.3589 | `base|emb=24|sh=0.97` |
| DEXE | 0.6400 | 0.9497 | 0.7222 | 0.8225 | 14.4802 | 2.0851 | 0.7994 | 0.7994 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| DOGE | 0.7000 | 0.9588 | 0.3056 | 1.2333 | 35.4034 | 3.7154 | 0.8501 | 0.8501 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| DOT | 0.8077 | 0.9554 | 0.7500 | 0.6767 | 36.1548 | 3.1669 | 0.8419 | 0.8419 | `trust_high40|emb=24|sh=0.95|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| EDU | 0.3636 | 1.0065 | 0.3611 | 1.1969 | -15.3155 | -0.5213 | 0.3598 | 0.3598 | `trust_high40|emb=12|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| ENA | 0.5588 | 0.9600 | 1.0000 | 0.9517 | 6.7878 | 0.5516 | 0.7395 | 0.7395 | `base|emb=24|sh=0.96` |
| ENSO | 0.3871 | 1.0160 | 1.0000 | 0.7631 | -26.4698 | -1.0237 | 0.3256 | 0.3256 | `base|emb=12|sh=0.97` |
| ETH | 0.6154 | 0.9368 | 0.7222 | 0.9988 | 16.8962 | 1.3754 | 0.7911 | 0.7911 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| EUR | 0.5429 | 0.9930 | 1.0000 | 0.8102 | -1.3141 | -0.1227 | 0.4851 | 0.4851 | `base|emb=12|sh=0.97` |
| FET | 0.5588 | 0.9911 | 1.0000 | 1.2941 | 18.8523 | 1.6778 | 0.7771 | 0.7771 | `base|emb=24|sh=0.95` |
| FIL | 0.6562 | 0.9859 | 1.0000 | 0.6261 | 6.3192 | 0.4168 | 0.7273 | 0.7273 | `base|emb=24|sh=0.97` |
| FLOKI | 0.7308 | 0.9364 | 0.7500 | 0.7992 | 29.1351 | 2.2969 | 0.8268 | 0.8268 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| FLOW | 0.5000 | 1.0127 | 0.3333 | 0.4508 | -25.6979 | -0.6531 | 0.3459 | 0.3459 | `trust_high40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| GIGGLE | 0.4848 | 1.0030 | 1.0000 | 0.5861 | -21.4964 | -0.7028 | 0.3517 | 0.3517 | `base|emb=12|sh=0.96` |
| HBAR | 0.5000 | 0.9983 | 1.0000 | 1.0450 | 1.6006 | 0.0964 | 0.6273 | 0.6273 | `base|emb=12|sh=0.95` |
| HIGH | 0.6333 | 0.9735 | 1.0000 | 0.8014 | 9.9325 | 0.7511 | 0.7508 | 0.7508 | `base|emb=24|sh=0.95` |
| HYPER | 0.6667 | 0.9795 | 0.4722 | 0.5307 | 2.1380 | 0.0939 | 0.6630 | 0.6630 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` |
| JST | 0.4800 | 0.9964 | 0.7222 | 1.3134 | 6.8814 | 0.6286 | 0.7269 | 0.7269 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| KAITO | 0.5714 | 0.9936 | 1.0000 | 0.8771 | 5.8803 | 0.2489 | 0.7120 | 0.7120 | `base|emb=24|sh=0.97` |
| KAT | 0.3824 | 1.0092 | 1.0000 | 1.4019 | -5.0281 | -0.4376 | 0.3839 | 0.3839 | `base|emb=12|sh=0.97` |
| KITE | 0.5000 | 0.9993 | 1.0000 | 2.2313 | 27.1294 | 6.2501 | 0.8419 | 0.8419 | `base|emb=24|sh=0.97` |
| LINK | 0.6000 | 0.9781 | 0.8056 | 1.1333 | 18.8520 | 1.7049 | 0.7845 | 0.7845 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| LRC | 0.3429 | 1.0222 | 1.0000 | 1.1050 | -19.0573 | -1.0142 | 0.3302 | 0.3302 | `base|emb=24|sh=0.97` |
| LTC | 0.7714 | 0.9343 | 1.0000 | 0.4633 | 14.0168 | 1.0804 | 0.7899 | 0.7899 | `base|emb=24|sh=0.95` |
| LUMIA | 0.4000 | 1.0772 | 1.0000 | 1.6419 | 2.1625 | 0.0181 | 0.6193 | 0.6193 | `base|emb=24|sh=0.95` |
| LUNA | 0.5000 | 0.9976 | 1.0000 | 0.8823 | -4.2740 | -0.3578 | 0.3984 | 0.3984 | `base|emb=12|sh=0.97` |
| LUNC | 0.5588 | 0.9888 | 1.0000 | 0.5334 | -13.8556 | -0.6563 | 0.3712 | 0.3712 | `base|emb=12|sh=0.95` |
| MOVR | 0.5882 | 0.9886 | 1.0000 | 0.9865 | 13.0522 | 1.3467 | 0.7619 | 0.7619 | `base|emb=24|sh=0.97` |
| NEAR | 0.6061 | 0.9861 | 1.0000 | 0.7832 | 6.8414 | 0.4236 | 0.7261 | 0.7261 | `base|emb=12|sh=0.94` |
| NFP | 0.4118 | 1.0238 | 1.0000 | 0.8357 | -13.0276 | -0.6277 | 0.3432 | 0.3432 | `base|emb=24|sh=0.97` |
| NIGHT | 0.5588 | 1.0304 | 1.0000 | 0.8415 | 2.1246 | 0.0982 | 0.6357 | 0.6357 | `base|emb=24|sh=0.94` |
| NOM | 0.5161 | 1.0212 | 1.0000 | 0.8559 | -3.4760 | -0.2790 | 0.4042 | 0.4042 | `base|emb=12|sh=0.97` |
| OPEN | 0.6522 | 0.9835 | 0.6667 | 1.4274 | 32.3867 | 3.6270 | 0.8372 | 0.8372 | `trust_low40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` |
| ORCA | 0.5588 | 1.0040 | 1.0000 | 1.9182 | 26.2059 | 3.7719 | 0.8299 | 0.8299 | `base|emb=12|sh=0.97` |
| ORDI | 0.5294 | 0.9918 | 1.0000 | 0.8219 | -2.7683 | -0.3411 | 0.4289 | 0.4289 | `base|emb=24|sh=0.97` |
| PAXG | 0.6316 | 0.9371 | 0.5556 | 1.0695 | 21.6018 | 1.9363 | 0.8113 | 0.8113 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| PENDLE | 0.4286 | 1.0111 | 1.0000 | 0.7825 | -18.1968 | -0.7294 | 0.3457 | 0.3457 | `base|emb=24|sh=0.97` |
| PENGU | 0.6571 | 0.9687 | 1.0000 | 1.2040 | 30.9216 | 3.3743 | 0.8325 | 0.8325 | `base|emb=12|sh=0.94` |
| PEPE | 0.5833 | 0.9899 | 1.0000 | 0.7762 | 2.9217 | 0.1602 | 0.6766 | 0.6766 | `base|emb=12|sh=0.94` |
| PLUME | 0.5152 | 0.9917 | 1.0000 | 2.1301 | 21.5447 | 4.1160 | 0.8359 | 0.8359 | `base|emb=24|sh=0.95` |
| POL | 0.5000 | 1.0065 | 1.0000 | 1.3643 | 10.8058 | 0.7340 | 0.7351 | 0.7351 | `base|emb=12|sh=0.97` |
| PUMP | 0.5938 | 0.9966 | 1.0000 | 1.0524 | 14.7343 | 0.7615 | 0.7455 | 0.7455 | `base|emb=12|sh=0.97` |
| RAY | 0.5588 | 0.9984 | 1.0000 | 0.7824 | -0.3249 | -0.0758 | 0.5320 | 0.5320 | `base|emb=12|sh=0.97` |
| RLUSD | 0.5333 | 1.0246 | 1.0000 | 0.9999 | 6.0379 | 0.4992 | 0.7065 | 0.7065 | `base|emb=24|sh=0.97` |
| S | 0.5294 | 0.9626 | 0.4722 | 1.0431 | 5.6608 | 0.3346 | 0.7259 | 0.7259 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| SAND | 0.4706 | 0.9987 | 1.0000 | 0.5972 | -22.5427 | -0.8382 | 0.3469 | 0.3469 | `base|emb=24|sh=0.96` |
| SHIB | 0.6800 | 0.9812 | 1.0000 | 1.1618 | 32.5775 | 3.5569 | 0.8319 | 0.8319 | `base|emb=24|sh=0.97` |
| SOL | 0.6000 | 0.9654 | 1.0000 | 0.8572 | 8.4455 | 0.5968 | 0.7446 | 0.7446 | `base|emb=24|sh=0.94` |
| SOMI | 0.4706 | 1.0034 | 1.0000 | 1.0727 | -1.7994 | -0.1027 | 0.4603 | 0.4603 | `base|emb=12|sh=0.96` |
| STO | 0.4062 | 1.0114 | 1.0000 | 1.3598 | -2.6298 | -0.1925 | 0.4283 | 0.4283 | `base|emb=12|sh=0.97` |
| SUI | 0.5385 | 0.9845 | 0.7500 | 1.2965 | 13.9463 | 1.5013 | 0.7713 | 0.7713 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| TAO | 0.5294 | 0.9870 | 1.0000 | 0.9379 | 2.1329 | 0.1427 | 0.6530 | 0.6530 | `base|emb=12|sh=0.97` |
| TIA | 0.5143 | 0.9919 | 1.0000 | 0.7603 | -8.0998 | -0.5268 | 0.3773 | 0.3773 | `base|emb=12|sh=0.97` |
| TON | 0.5758 | 0.9926 | 1.0000 | 1.0702 | 13.7724 | 1.1673 | 0.7565 | 0.7565 | `base|emb=12|sh=0.97` |
| TRB | 0.5517 | 0.9901 | 0.8611 | 0.8360 | 1.1556 | 0.0405 | 0.6115 | 0.6115 | `trust_high40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| TRUMP | 0.5938 | 0.9718 | 1.0000 | 0.8305 | 6.8594 | 0.5699 | 0.7366 | 0.7366 | `base|emb=24|sh=0.97` |
| TRX | 0.5000 | 1.0059 | 1.0000 | 1.1678 | 5.8988 | 0.5318 | 0.7150 | 0.7150 | `base|emb=12|sh=0.97` |
| U | 0.7500 | 0.9957 | 1.0000 | 1.1905 | 54.2558 | 6.0046 | 0.8547 | 0.8547 | `base|emb=24|sh=0.94` |
| UNI | 0.6364 | 0.9857 | 1.0000 | 0.6823 | 6.2985 | 0.5572 | 0.7305 | 0.7305 | `base|emb=12|sh=0.97` |
| USD1 | 0.7778 | 0.9895 | 1.0000 | 1.2857 | 63.0457 | 21.0143 | 0.8704 | 0.8704 | `base|emb=12|sh=0.97` |
| USTC | 0.6250 | 0.9915 | 1.0000 | 0.9457 | 14.6293 | 1.0033 | 0.7565 | 0.7565 | `base|emb=12|sh=0.97` |
| UTK | 0.4688 | 1.0010 | 1.0000 | 1.5989 | 13.0299 | 1.0369 | 0.7497 | 0.7497 | `base|emb=12|sh=0.97` |
| VANA | 0.4848 | 0.9966 | 1.0000 | 0.8339 | -9.0979 | -0.4852 | 0.3736 | 0.3736 | `base|emb=12|sh=0.97` |
| WIF | 0.6667 | 0.9836 | 1.0000 | 0.9255 | 24.2896 | 1.8361 | 0.7894 | 0.7894 | `base|emb=24|sh=0.97` |
| WLD | 0.5455 | 0.9962 | 0.9722 | 1.1505 | 11.4051 | 1.0712 | 0.7496 | 0.7496 | `trust_high40|emb=24|sh=0.96|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| WLFI | 0.3438 | 1.0606 | 1.0000 | 0.5109 | -43.0052 | -0.9712 | 0.2899 | 0.2899 | `base|emb=12|sh=0.97` |
| XAUT | 0.6667 | 0.9191 | 0.4444 | 0.9727 | 22.2882 | 2.1613 | 0.8273 | 0.8273 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |
| XLM | 0.4706 | 1.0053 | 1.0000 | 1.6362 | 14.2390 | 1.1253 | 0.7524 | 0.7524 | `base|emb=12|sh=0.97` |
| XPL | 0.5882 | 0.9980 | 1.0000 | 0.7380 | 1.8868 | 0.0774 | 0.6408 | 0.6408 | `base|emb=12|sh=0.94` |
| XRP | 0.6857 | 0.9847 | 1.0000 | 0.6491 | 12.2320 | 0.9134 | 0.7548 | 0.7548 | `base|emb=24|sh=0.97` |
| XUSD | 0.6667 | 1.0076 | 0.9444 | 0.8124 | 20.2146 | 0.9998 | 0.7521 | 0.7521 | `trust_low40|emb=24|sh=0.97|feat=mean_pairwise_per_atr|q=0.0-0.4` |
| ZAMA | 0.7143 | 0.9631 | 0.1944 | 2.2328 | 59.0457 | 7.9758 | 0.9020 | 0.9020 | `trust_low40|emb=12|sh=0.94|feat=mean_pairwise_per_atr|q=0.0-0.4` |
| ZBT | 0.4706 | 1.0313 | 1.0000 | 2.1126 | 20.2498 | 1.8800 | 0.7786 | 0.7786 | `base|emb=12|sh=0.97` |
| ZEC | 0.5333 | 0.9854 | 0.8611 | 0.9651 | 3.4988 | 0.1336 | 0.6872 | 0.6872 | `trust_high40|emb=24|sh=0.94|feat=mean_pairwise_per_atr|q=0.6-1.0` |

## 실패 종목

- `CHIP`: Command '['C:\\Users\\hadro\\AppData\\Local\\Programs\\Python\\Python311\\python.exe', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\scripts\\strict_multi_cycle_research.py', '--symbol', 'CHIP', '--ohlcv', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\chipusdt_1h_30d.csv', '--factors-csv', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\derived\\chipusdt_factors_4p.csv', '--train-bars', '120', '--val-bars', '36', '--cycle-step', '20', '--embargos', '12,24', '--shrinks', '0.94,0.95,0.96,0.97', '--top-k', '5', '--min-evals', '3', '--unseen-ratio', '0.25', '--seed', '0', '--out-json', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\runs\\strict_multi_cycle_chip.json', '--out-md', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\runs\\strict_multi_cycle_chip.md']' returned non-zero exit status 2.
- `MEGA`: Command '['C:\\Users\\hadro\\AppData\\Local\\Programs\\Python\\Python311\\python.exe', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\scripts\\strict_multi_cycle_research.py', '--symbol', 'MEGA', '--ohlcv', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\megausdt_1h_30d.csv', '--factors-csv', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\derived\\megausdt_factors_4p.csv', '--train-bars', '120', '--val-bars', '36', '--cycle-step', '20', '--embargos', '12,24', '--shrinks', '0.94,0.95,0.96,0.97', '--top-k', '5', '--min-evals', '3', '--unseen-ratio', '0.25', '--seed', '0', '--out-json', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\runs\\strict_multi_cycle_mega.json', '--out-md', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\runs\\strict_multi_cycle_mega.md']' returned non-zero exit status 2.
- `U`: Command '['C:\\Users\\hadro\\AppData\\Local\\Programs\\Python\\Python311\\python.exe', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\scripts\\fetch_btc_ohlcv.py', '--symbol', '币安人生USDT', '--interval', '1h', '--limit', '720', '--out', 'C:\\Users\\hadro\\Expected_Price\\Expected_Price\\data\\币安人生usdt_1h_30d.csv']' returned non-zero exit status 1.

## 심볼쌍 연구 (공식 유사도 상위 20)

| pair | formula_similarity | hit_gap_abs | mae_ratio_gap_abs |
|---|---:|---:|---:|
| `0G-CGPT` | 1.0000 | 0.0000 | 0.0112 |
| `AIXBT-FLOW` | 1.0000 | 0.0000 | 0.0042 |
| `APE-SOMI` | 1.0000 | 0.0000 | 0.0429 |
| `APE-XLM` | 1.0000 | 0.0000 | 0.0410 |
| `APE-ZBT` | 1.0000 | 0.0000 | 0.0149 |
| `API3-XRP` | 1.0000 | 0.0000 | 0.0037 |
| `ARB-NOM` | 1.0000 | 0.0000 | 0.0251 |
| `CHZ-KAT` | 1.0000 | 0.0000 | 0.0208 |
| `CRV-TAO` | 1.0000 | 0.0000 | 0.0093 |
| `ENA-FET` | 1.0000 | 0.0000 | 0.0311 |
| `ENA-NIGHT` | 1.0000 | 0.0000 | 0.0704 |
| `FET-NIGHT` | 1.0000 | 0.0000 | 0.0394 |
| `GIGGLE-VANA` | 1.0000 | 0.0000 | 0.0064 |
| `HBAR-LUNA` | 1.0000 | 0.0000 | 0.0007 |
| `HBAR-POL` | 1.0000 | 0.0000 | 0.0082 |
| `HBAR-TRX` | 1.0000 | 0.0000 | 0.0076 |
| `HYPER-XUSD` | 1.0000 | 0.0000 | 0.0281 |
| `LUNA-POL` | 1.0000 | 0.0000 | 0.0089 |
| `LUNA-TRX` | 1.0000 | 0.0000 | 0.0083 |
| `LUNC-ORCA` | 1.0000 | 0.0000 | 0.0152 |
