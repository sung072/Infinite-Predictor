"""시간순 홀드아웃 검증: 학습·워밍업(과거 봉) + 검증 봉만 지표 집계.

**봉 단위 일관성**  
백테스트에 사용한 OHLCV의 봉 간격(1m, 5m, 1h …)과 검증에 쓰는 데이터는 **동일해야** 한다.
길이는 날짜가 아니라 **캔들 개수**로만 정한다(예: 1시간 검증 = 1분봉이면 약 60봉, 1h봉이면 1봉).

**캔들 경계**  
행은 시간순 동일 그리드상의 연속 봉이다. 산출·맥락 구간의 마지막 행(train 마지막 봉) 다음부터가
“그 다음 캔들”이며, `embargo` 봉만큼 건너뛴 뒤의 행들이 검증(val) 집계 구간이다.

(`split=oos`처럼 train을 통째로 제거하면 롱 윈도우가 깨질 수 있어, 여기서는 train+embargo+val을
한 번에 넣고 인과적으로 계산한 뒤 val 행만 채점한다.)
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pandas as pd

import walkforward_oos as wfo
from predictor_registry import PredictorStatus
from run_registry_research import run_from_registry

_PKG = Path(__file__).resolve().parent.parent
_SCRIPTS = _PKG / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import gap_forward_return_research as gfr  # noqa: E402
import system_price_validation_matrix as spm  # noqa: E402

__all__ = ["run_holdout_validation", "format_system_price_accuracy_ko"]


def _fmt(x: Any, *, nd: int = 4) -> str:
    if x is None:
        return "n/a"
    try:
        xf = float(x)
    except (TypeError, ValueError):
        return str(x)
    if not (xf == xf):  # nan
        return "n/a"
    return f"{xf:.{nd}f}"


def format_system_price_accuracy_ko(metrics: dict[str, Any]) -> str:
    """검증 구간만 집계한 시스템가 스킬 지표를 한 줄 요약(연구용 정의 그대로)."""
    hr = metrics.get("directional_hit_rate")
    ratio = metrics.get("mae_ratio_sys_over_naive")
    n_dir = metrics.get("n_used")
    rho = metrics.get("spearman_signed_sys_vs_fwd1")
    col = metrics.get("system_col", "")
    lines = [
        "[시스템가 검증 결과] (바로 직전까지 백테스트·예측가·시스템가 산출 후, 다음 검증 캔들들만 채점)",
        f"  · 검증에 사용한 표본 수(유효 행): {_fmt(n_dir, nd=0)}",
        f"  · 방향 적중률 directional_hit_rate: {_fmt(hr)} (시스템가 방향과 다음 종가 방향이 같은 비율)",
        f"  · 대비 단순 기준 대비 오차 비율 mae_ratio_sys_over_naive: {_fmt(ratio)} (< 1 이면 시스템가가 다음 종가에 더 가깝다)",
        f"  · Spearman(signed_sys_vs_now, fwd_1): {_fmt(rho)}",
        f"  · 적용 시스템가 정의: `{col}`",
        "",
        "한 줄: "
        + f"정확도(방향)= {_fmt(hr)}"
        + ", "
        + f"오차비율(naive 대비)= {_fmt(ratio)}"
        + " - 위 수치는 검증 캔들 구간에서만 계산됨.",
    ]
    return "\n".join(lines)


def run_holdout_validation(
    registry_path: str | Path,
    ohlcv: pd.DataFrame,
    *,
    n_train_bars: int,
    n_embargo_bars: int,
    n_val_bars: int,
    seed: int = 0,
    data_snapshot_id: str | None = None,
    use_statuses: set[PredictorStatus] | None = None,
    use_price_like: bool = False,
    factors_path: str | Path | None = None,
    include_pairwise_columns: bool = False,
    atr_window: int = 14,
    include_system_variants: bool = True,
    system_col: str = "p_system_shrunk_custom",
    shrink_weight: float = 0.96,
) -> dict[str, Any]:
    """
    Parameters
    ----------
    n_train_bars, n_embargo_bars, n_val_bars
        **동일 OHLCV 그리드**에서의 연속 바 개수. 합 = 사용 창 길이.
        검증 구간의 실제 시간 길이 = `n_val_bars × (한 봉의 시간)`.
    system_col, shrink_weight
        검증 지표용 시스템가 정의 (`system_price_validation_matrix._skill_from_system_col`).
    """
    split = wfo.holdout_split_by_bars(
        len(ohlcv),
        n_train=n_train_bars,
        n_embargo=n_embargo_bars,
        n_val=n_val_bars,
    )
    ohlc_win = ohlcv.iloc[: split.n_window].copy()

    full_df, prov, ids, reg = run_from_registry(
        registry_path,
        ohlcv=ohlc_win,
        seed=seed,
        data_snapshot_id=data_snapshot_id,
        use_statuses=use_statuses,
        use_price_like=use_price_like,
        factors_path=factors_path,
        include_pairwise_columns=include_pairwise_columns,
        atr_window=atr_window,
        include_system_variants=include_system_variants,
    )

    merged = gfr.add_features_and_forwards(gfr._align(ohlc_win, full_df))
    m_val = merged.iloc[split.val_slice]

    sk, rho, _ps = spm._skill_from_system_col(
        m_val,
        gfr,
        system_col=system_col,
        shrink_weight=shrink_weight,
    )

    val_gap_only = full_df.iloc[split.val_slice]

    metrics = {
        **sk,
        "spearman_signed_sys_vs_fwd1": float(rho),
        "system_col": system_col,
        "shrink_weight": float(shrink_weight),
        "n_rows_validation": int(len(m_val)),
    }

    prov2 = dict(prov)
    prov2["temporal_holdout"] = {
        "split": split.to_dict(),
        "candle_alignment": wfo.holdout_candle_alignment_summary(ohlc_win, split),
        "note": (
            "검증 지표(metrics_validation)는 embargo 이후 val 바만 사용. "
            "full_gap_df는 train·embargo·val 전 구간 gap 행. "
            "백테스트와 검증은 반드시 같은 봉 간격 CSV에서 바 개수로 맞출 것."
        ),
    }

    summary_ko = format_system_price_accuracy_ko(metrics)

    return {
        "holdout_split": split,
        "merged_full_df": merged,
        "full_gap_df": full_df,
        "validation_gap_df": val_gap_only,
        "metrics_validation": metrics,
        "accuracy_summary_ko": summary_ko,
        "provenance": prov2,
        "predictor_ids": ids,
        "registry": reg,
        "merged_validation_df": m_val,
    }
