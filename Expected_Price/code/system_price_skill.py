"""시스템가(p_system) vs **실현된 다음 봉 종가** — 연구용 스킬 지표(운용 신호 아님).

`gap_forward_return_research` 과 함께 쓴다: 같은 인덱스에서 `close[t+1]` 과 비교."""
from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

__all__ = [
    "compute_system_price_skill",
]


def compute_system_price_skill(
    m: pd.DataFrame,
    *,
    close_col: str = "close_ohlc",
    fwd_col: str = "fwd_1",
) -> dict[str, Any]:
    """
    * **directional_hit_rate**: 부호(시스템가−현재가) == 부호(다음종가−현재가) 비율.
    * **mae_sys_next_close**: 평균 |p_system − close_{t+1}| (USDT).
    * **mae_naive_now_next_close**: 평균 |P_now − close_{t+1}| — ‘현재가만 기준’ 단순 비교.
    * **mae_ratio**: mae_sys / mae_naive (<1 이면 시스템가가 다음 종가에 **평균적으로 더 가까움**).

    `fwd_1` 이 없으면 `close` 에서 계산: close[t]*(1+fwd_1)=close[t+1].
    """
    ps = pd.to_numeric(m.get("p_system"), errors="coerce")
    pw = pd.to_numeric(m.get("P_now"), errors="coerce")
    ct = pd.to_numeric(m.get(close_col), errors="coerce")
    if ps is None or pw is None or ct is None:
        raise ValueError("need p_system, P_now, close_ohlc columns")

    if fwd_col in m.columns:
        fwd = pd.to_numeric(m[fwd_col], errors="coerce")
        cn = ct * (1.0 + fwd)
    else:
        cn = ct.shift(-1)
    ok = ps.notna() & pw.notna() & cn.notna()
    if ok.sum() < 5:
        return {
            "n_used": int(ok.sum()),
            "directional_hit_rate": float("nan"),
            "mae_sys_next_close": float("nan"),
            "mae_naive_now_next_close": float("nan"),
            "mae_ratio_sys_over_naive": float("nan"),
            "mae_ratio_sys_over_naive_p90": float("nan"),
        }

    psb = ps[ok]
    pwb = pw[ok]
    cnb = cn[ok]

    dir_hit = np.sign(psb - pwb) == np.sign(cnb - pwb)
    near_zero = (np.abs(psb - pwb) < 1e-9) | (np.abs(cnb - pwb) < 1e-9)
    dir_valid = ~(near_zero)
    hit_rate = float(dir_hit[dir_valid].mean()) if dir_valid.any() else float("nan")

    err_sys = (psb - cnb).abs().to_numpy(dtype=float)
    err_naive = (pwb - cnb).abs().to_numpy(dtype=float)
    mae_sys = float(err_sys.mean())
    mae_naive = float(err_naive.mean())
    ratio = mae_sys / mae_naive if mae_naive > 1e-12 else float("nan")
    ratio_bar = err_sys / np.maximum(err_naive, 1e-12)
    mae_ratio_sys_over_naive_p90 = float(np.nanquantile(ratio_bar, 0.9))

    return {
        "n_used": int(ok.sum()),
        "directional_hit_rate": hit_rate,
        "mae_sys_next_close": mae_sys,
        "mae_naive_now_next_close": mae_naive,
        "mae_ratio_sys_over_naive": ratio,
        "mae_ratio_sys_over_naive_p90": mae_ratio_sys_over_naive_p90,
    }
