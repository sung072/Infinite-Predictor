"""최소 워크포워드 / OOS 구간(바·인덱스). 숫자 기준은 **행(바) 개수** (시간 t 정의는 OHLCV 인덱스)."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Iterator

import pandas as pd

__all__ = [
    "OosSplitMeta",
    "oossplit_by_ratio",
    "HoldoutBarSplit",
    "holdout_split_by_bars",
    "holdout_candle_alignment_summary",
    "iter_walkforward_folds",
    "run_walkforward_report",
]


@dataclass(frozen=True)
class OosSplitMeta:
    n_total: int
    train_bars: int
    embargo_bars: int
    oos_bars: int
    train_index_start: int
    train_index_end: int
    oos_index_start: int
    oos_index_end: int
    oos_time_start: Any
    oos_time_end: Any

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        for k in ("oos_time_start", "oos_time_end"):
            v = d.get(k)
            if v is not None and hasattr(v, "isoformat"):
                d[k] = v.isoformat()  # Timestamp / datetime — JSON·해시에 안전
        return d


def oossplit_by_ratio(
    ohlcv: pd.DataFrame,
    *,
    train_ratio: float,
    embargo_bars: int = 0,
) -> tuple[pd.DataFrame, OosSplitMeta, pd.DataFrame]:
    """
    * 앞부분 `round(n * train_ratio)` 바 = train (휴지용, gap 계산 **안 함**),
    * 그다음 `embargo_bars` = 버림,
    * 나머지 = **OOS** (여기에만 `run_gap_research_ohlcv` 권장).
    """
    if not 0.0 < train_ratio < 1.0:
        raise ValueError("train_ratio must be in (0,1)")
    if embargo_bars < 0:
        raise ValueError("embargo_bars must be >= 0")
    n = len(ohlcv)
    n_train = int(round(n * train_ratio))
    if n_train < 1:
        raise ValueError("train too short (increase n or train_ratio)")
    oos_i = n_train + embargo_bars
    if oos_i >= n:
        raise ValueError(
            f"no OOS after train+embargo: n={n}, n_train={n_train}, emb={embargo_bars} → oos start {oos_i}"
        )
    train_df = ohlcv.iloc[:n_train]
    oos_df = ohlcv.iloc[oos_i:]
    idx = ohlcv.index
    t0, t1 = (idx[oos_i], idx[n - 1]) if n > 0 else (None, None)
    meta = OosSplitMeta(
        n_total=n,
        train_bars=n_train,
        embargo_bars=embargo_bars,
        oos_bars=len(oos_df),
        train_index_start=0,
        train_index_end=n_train,
        oos_index_start=oos_i,
        oos_index_end=n,
        oos_time_start=t0,
        oos_time_end=t1,
    )
    return train_df, meta, oos_df


@dataclass(frozen=True)
class HoldoutBarSplit:
    """연속 인덱스 [0, n_window): train → embargo → validation.

    **봉 정렬(날짜가 아니라 “몇 개의 동일 간격 봉”이 기준)**  
    백테스트에 쓴 OHLCV와 검증에 쓰는 OHLCV는 **같은 봉 간격**(예: 전부 1m 또는 전부 1h)이어야 한다.
    각 행은 한 봉을 나타내므로, train 마지막 행 = 산출·맥락이 닿는 마지막 캔들, 그 **다음 행**부터가
    시간상 “그 다음 캔들”이다. `embargo`>0이면 그만큼 중간 봉을 건너뛴 뒤 첫 행이 검증(val)의 시작이다.
    검증 길이는 **캔들 개수**(`n_val`)로만 정한다(몇 분·몇 시간·며칠은 “봉 간격 × 개수”로 환산).
    """

    n_train: int
    n_embargo: int
    n_val: int
    n_window: int
    train_slice: slice
    embargo_slice: slice
    val_slice: slice

    def to_dict(self) -> dict[str, Any]:
        return {
            "n_train": self.n_train,
            "n_embargo": self.n_embargo,
            "n_val": self.n_val,
            "n_window": self.n_window,
            "train_slice": [self.train_slice.start, self.train_slice.stop],
            "embargo_slice": [self.embargo_slice.start, self.embargo_slice.stop],
            "val_slice": [self.val_slice.start, self.val_slice.stop],
        }


def holdout_split_by_bars(
    n_available: int,
    *,
    n_train: int,
    n_embargo: int,
    n_val: int,
) -> HoldoutBarSplit:
    """
    `n_available` 중 앞에서부터 `n_train + n_embargo + n_val` 바만 사용.

    - train: 인디케이터·앵커 맥락(과거) — gap 행은 산출되나 검증 집계에서는 제외 가능
    - embargo: train과 val 사이 누수 방지용 생략 바
    - val: **검증 구간** — 시스템가·예측가 정확도 집계에 사용
    """
    if n_available < 1:
        raise ValueError("n_available must be >= 1")
    if n_train < 1:
        raise ValueError("n_train must be >= 1")
    if n_embargo < 0:
        raise ValueError("n_embargo must be >= 0")
    if n_val < 1:
        raise ValueError("n_val must be >= 1")
    n_window = int(n_train) + int(n_embargo) + int(n_val)
    if n_available < n_window:
        raise ValueError(
            f"need at least {n_window} bars (train+embargo+val), have {n_available}"
        )
    tr_e = int(n_train)
    em_e = tr_e + int(n_embargo)
    return HoldoutBarSplit(
        n_train=int(n_train),
        n_embargo=int(n_embargo),
        n_val=int(n_val),
        n_window=n_window,
        train_slice=slice(0, tr_e),
        embargo_slice=slice(tr_e, em_e),
        val_slice=slice(em_e, em_e + int(n_val)),
    )


def _json_safe_label(x: Any) -> str:
    if hasattr(x, "isoformat"):
        return str(x.isoformat())
    return str(x)


def holdout_candle_alignment_summary(
    ohlcv_window: pd.DataFrame,
    split: HoldoutBarSplit,
) -> dict[str, Any]:
    """
    홀드아웃이 **동일 봉 그리드**에서 끊김 없이 이어지는지 메타로 고정한다.

    Parameters
    ----------
    ohlcv_window
        앞에서 `split.n_window`행만 의미 있음(호출부에서 이미 잘랐는지 확인).
    """
    if len(ohlcv_window) < split.n_window:
        raise ValueError(
            f"need at least {split.n_window} rows for holdout window, got {len(ohlcv_window)}"
        )
    w = ohlcv_window.iloc[: split.n_window]

    def segment(sl: slice) -> dict[str, Any]:
        seg = w.iloc[sl]
        out: dict[str, Any] = {"n_bars": int(len(seg))}
        if len(seg) == 0:
            return out
        out["first_bar_label"] = _json_safe_label(seg.index[0])
        out["last_bar_label"] = _json_safe_label(seg.index[-1])
        return out

    idx = w.index
    median_delta: str | None = None
    if isinstance(idx, pd.DatetimeIndex) and len(idx) >= 2:
        md = pd.Series(idx).diff().dropna().median()
        median_delta = str(md) if pd.notna(md) else None

    train_seg = segment(split.train_slice)
    emb_seg = segment(split.embargo_slice)
    val_seg = segment(split.val_slice)

    boundary_note = (
        "행 순서가 시간 순서와 같다면: train의 last_bar 직후 다음 행은 embargo 첫 행(embargo>0), "
        "embargo가 비었으면 val 첫 행이 곧 '산출 마지막 봉 종료 직후의 다음 캔들'에 해당."
    )

    return {
        "same_bar_grid_as_backtest": True,
        "validation_is_measured_in_bars_not_calendar_dates": True,
        "median_step_between_rows": median_delta,
        "train": train_seg,
        "embargo": emb_seg,
        "validation": val_seg,
        "n_validation_bars": split.n_val,
        "boundary_semantics": boundary_note,
    }


@dataclass(frozen=True)
class WalkforwardFold:
    fold_id: int
    train_slice: slice
    test_slice: slice
    n_train: int
    n_test: int
    n_embargo: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "fold_id": self.fold_id,
            "train_index": [self.train_slice.start, self.train_slice.stop],
            "test_index": [self.test_slice.start, self.test_slice.stop],
            "n_train": self.n_train,
            "n_test": self.n_test,
            "n_embargo": self.n_embargo,
        }


def iter_walkforward_folds(
    n_bars: int,
    *,
    n_train: int,
    n_test: int,
    n_embargo: int = 0,
    step: int | None = None,
) -> Iterator[WalkforwardFold]:
    """
    롤링 WF: `train = [a, a+n_train)`, `test`는 train 직후 `embargo` 뒤 `n_test` 바.
    `step`: 다음 폴드 시작 오프셋(기본 `n_test` — 겹침 없는 OOS).
    """
    if n_bars < 1:
        raise ValueError("n_bars must be >= 1")
    for x in (n_train, n_test, n_embargo, step or n_test):
        if x is not None and int(x) < 0:  # type: ignore[operator]
            raise ValueError("n_train, n_test, n_embargo, step must be non-negative where used")
    step_ = n_test if step is None else int(step)
    if step_ < 1:
        raise ValueError("step must be >= 1")
    if n_train < 1 or n_test < 1:
        raise ValueError("n_train, n_test must be >= 1")
    t = 0
    fid = 0
    n_emb = int(n_embargo)
    n_tr = int(n_train)
    n_te = int(n_test)
    while True:
        tr0, tr1 = t, t + n_tr
        te0 = tr1 + n_emb
        te1 = te0 + n_te
        if te1 > n_bars:
            return
        yield WalkforwardFold(
            fold_id=fid,
            train_slice=slice(tr0, tr1),
            test_slice=slice(te0, te1),
            n_train=n_tr,
            n_test=n_te,
            n_embargo=n_emb,
        )
        t += step_
        fid += 1


def run_walkforward_report(
    n_bars: int, *, n_train: int, n_test: int, n_embargo: int, step: int | None
) -> dict[str, Any]:
    folds = list(
        iter_walkforward_folds(
            n_bars,
            n_train=n_train,
            n_test=n_test,
            n_embargo=n_embargo,
            step=step,
        )
    )
    return {
        "n_folds": len(folds),
        "folds": [f.to_dict() for f in folds],
    }
