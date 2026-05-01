#!/usr/bin/env python3
"""
예측가·시스템가·현재가 **갭**과 **이후 가격 수익률**의 관계를 점검(연구용).

- 갭 시계열: `run_registry_research` / `gap_backtest_and_analyze` 가 쓰는 gap CSV
- 수익률: OHLCV `close` 기준 1봉·N봉 **선행** 단순 수익률
- 산출: `data/runs/gap_forward_return_report.md` (한국어: 상관·퀸타일 평균·부호/변화갭)

**주의:** 표본·비정상·레짐에 따라 "큰 갭=상승" 같은 식이 **뒤집힐 수** 있다. 이 스크립트는 **효과적 탐색·가설 점검**이지 운용 신호를 보장하지 않는다.
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent


def _read_gap_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    df = df.sort_index()
    return df


def _read_ohlcv(path: Path) -> pd.DataFrame:
    o = pd.read_csv(path, index_col=0, parse_dates=True)
    if "close" not in o.columns:
        raise ValueError("OHLCV needs close")
    return o.sort_index()


def _align(ohlc: pd.DataFrame, gap: pd.DataFrame) -> pd.DataFrame:
    both = ohlc.index.intersection(gap.index)
    if len(both) < 8:
        raise ValueError("aligned rows too few after index intersection")
    o2 = ohlc.loc[both, "close"]
    g2 = gap.reindex(both)
    m = g2.copy()
    m["close_ohlc"] = o2.values
    return m


def _signed_system_vs_now(m: pd.DataFrame) -> pd.Series:
    """(p_system - P_now) / scale — **부호** 있는 시스템가-현재가(상대)."""
    ps = m.get("p_system")
    pw = m.get("P_now")
    sc = m.get("scale_used")
    if ps is None or pw is None or sc is None:
        return pd.Series(np.nan, index=m.index)
    return (pd.to_numeric(ps, errors="coerce") - pd.to_numeric(pw, errors="coerce")) / (
        pd.to_numeric(sc, errors="coerce").replace(0, np.nan)
    )


def _one_anchor_gap_to_now(
    m: pd.DataFrame, anchor_id: str
) -> pd.Series:
    """특정 `predictor_id` 앵커 ↔ P_now 상대 거리 (뉴스가 등 단일 id 연구용)."""
    pr = m.get("predictor_prices")
    pw = m.get("P_now")
    sc = m.get("scale_used")
    if pr is None or pw is None or sc is None:
        return pd.Series(np.nan, index=m.index)
    out: list[float] = []
    for i in range(len(m)):
        pwi = float(pw.iloc[i]) if not pd.isna(pw.iloc[i]) else float("nan")
        sci = float(sc.iloc[i]) if not pd.isna(sc.iloc[i]) and float(sc.iloc[i]) > 0 else float("nan")
        cell = pr.iloc[i]
        if isinstance(cell, str) and cell.strip().startswith("{"):
            try:
                d = ast.literal_eval(cell)
            except (SyntaxError, ValueError):
                out.append(float("nan"))
                continue
        elif isinstance(cell, dict):
            d = cell
        else:
            out.append(float("nan"))
            continue
        if anchor_id not in d or not np.isfinite(pwi) or not np.isfinite(sci) or sci <= 0:
            out.append(float("nan"))
            continue
        out.append(abs(float(d[anchor_id]) - pwi) / sci)
    return pd.Series(out, index=m.index, dtype="float64")


def _min_anchor_gap_to_now(m: pd.DataFrame) -> pd.Series:
    """
    봉마다 min_k |P_anchor_k - P_now| / scale — '뉴스/개별' 예측가를 넣은 Registry면
    그 중 **현재가에 가장 가까운 앵커**에 해당하는 **상대 거리** (BTC 4p면 4개 중 min).
    """
    pr = m.get("predictor_prices")
    pw = m.get("P_now")
    sc = m.get("scale_used")
    if pr is None or pw is None or sc is None:
        return pd.Series(np.nan, index=m.index)
    out = []
    for i in range(len(m)):
        pwi = float(pw.iloc[i]) if not pd.isna(pw.iloc[i]) else float("nan")
        sci = float(sc.iloc[i]) if not pd.isna(sc.iloc[i]) and float(sc.iloc[i]) > 0 else float("nan")
        cell = pr.iloc[i]
        if isinstance(cell, str) and cell.strip().startswith("{"):
            try:
                d = ast.literal_eval(cell)
            except (SyntaxError, ValueError):
                out.append(float("nan"))
                continue
        elif isinstance(cell, dict):
            d = cell
        else:
            out.append(float("nan"))
            continue
        if not d or not np.isfinite(pwi) or not np.isfinite(sci) or sci <= 0:
            out.append(float("nan"))
            continue
        mns = [abs(float(v) - pwi) / sci for v in d.values() if v is not None and np.isfinite(float(v))]
        out.append(min(mns) if mns else float("nan"))
    return pd.Series(out, index=m.index, dtype="float64")


def add_features_and_forwards(
    merged: pd.DataFrame, *, anchor_id: str | None = None
) -> pd.DataFrame:
    m = merged.copy()
    c = m["close_ohlc"].astype(float)
    m["fwd_1"] = c.shift(-1) / c - 1.0
    m["signed_sys_vs_now_rel"] = _signed_system_vs_now(m)
    m["d_gap_system_rel"] = pd.to_numeric(m.get("gap_system_to_now_rel"), errors="coerce").diff()
    m["d_mean_pairwise_rel"] = pd.to_numeric(m.get("mean_pairwise_rel"), errors="coerce").diff()
    m["min_anchor_to_now_rel"] = _min_anchor_gap_to_now(m)
    if anchor_id:
        m[f"anchor__{anchor_id}__to_now_rel"] = _one_anchor_gap_to_now(m, anchor_id)
    return m


def _spearman(s: pd.Series, t: pd.Series) -> float:
    a = s.dropna()
    b = t.reindex(a.index)
    both = a.notna() & b.notna()
    a2 = a[both]
    b2 = b[both]
    if len(a2) < 5:
        return float("nan")
    return float(a2.corr(b2, method="spearman"))


def quintile_means(
    m: pd.DataFrame,
    feat: str,
    ret: str,
    *,
    n: int = 5,
) -> pd.DataFrame:
    s = pd.to_numeric(m[feat], errors="coerce")
    r = pd.to_numeric(m[ret], errors="coerce")
    d = pd.DataFrame({"f": s, "r": r}).dropna()
    if len(d) < n * 3:
        return pd.DataFrame()
    d["q"] = pd.qcut(d["f"], q=n, labels=False, duplicates="drop")
    g = d.groupby("q", observed=True)["r"].agg(["mean", "std", "count"])
    g.index = [f"Q{int(i) + 1}" for i in g.index]
    return g


def _report_md(
    m: pd.DataFrame,
    horizons: list[str],
    feats: list[str],
) -> str:
    lines: list[str] = []
    lines += [
        "# 갭(예측가·시스템가·현재가) — 선행 수익률 점검 (연구)",
        "",
        "이 문서는 **자동 생성**됩니다. (`scripts/gap_forward_return_research.py`)",
        "",
        "## 전제 (반드시 읽기)",
        "",
        "- `gap_system_to_now_rel` 는 코드에서 **절댓값** 상대 괴리(시스템가↔현재가)이므로, **방향**은 `signed_sys_vs_now_rel` (시스템이 현재가 위/아래)을 본다.",
        "- **뉴스가**가 Registry에 `id`로 잡혀 있으면 `predictor_prices`에 포함되고, “현재가와 가장 가까운 앵커”는 `min_anchor_to_now_rel` 로 대략 요약(여러 앵커일 때 min 거리)된다.",
        "- N봉 **선행** 수익률은 '알고리즘의 미래'가 아니라, **이후** 구간 **실제** 종가 변화를 붙인 것(연구용). 표본·레짐에 따라 **부호 뒤집힘이 흔함**.",
        "",
    ]

    for ret in horizons:
        if ret not in m.columns:
            continue
        lines += [f"## Spearman (갭 vs `{ret}`)", ""]
        rows: list[tuple[str, str]] = []
        for f in feats:
            if f not in m.columns:
                continue
            r = _spearman(m[f], m[ret])
            rows.append((f, f"{r:+.4f}" if np.isfinite(r) else "nan"))
        if rows:
            lines.append("| 갭/피처 | Spearman |")
            lines.append("|---------|----------|")
            for name, val in rows:
                lines.append(f"| `{name}` | {val} |")
        lines.append("")

    for ret in horizons:
        if ret not in m.columns:
            continue
        lines += [f"## 퀸타일 평균(갭이 낮은 구간 → 높은 구간, `{ret}` )", ""]
        for f in feats:
            if f not in m.columns:
                continue
            q = quintile_means(m, f, ret)
            if q.empty:
                continue
            lines.append(f"### `{f}`")
            lines.append("```")
            lines.append(q.to_string())
            lines.append("```")
            lines.append("")

    lines += [
        "## 읽는 법",
        "",
        "Spearman **양**이면 갭이 클수록 이후 수익(해당 `fwd_*`)이 **높은 경향**, **음**이면 **낮은 경향**(연관만, 인과는 아님). "
        "퀸타일 **Q1 vs Q5**의 평균 수익률 차이로 ‘퍼짐이 클 때 vs 작을 때’ **대략** 비교할 수 있다.",
        "",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--gap-csv",
        type=Path,
        default=ROOT / "data" / "runs" / "btc_4p_gap_backtest.csv",
    )
    p.add_argument(
        "--ohlcv",
        type=Path,
        default=ROOT / "data" / "btcusdt_1h_30d.csv",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=ROOT / "data" / "runs" / "gap_forward_return_report.md",
    )
    p.add_argument(
        "--fwd-bars",
        type=str,
        default="1,4,24",
        help="캔들(1h봉이면 1=1h) 선행, 콤마. 기본 1,4,24",
    )
    p.add_argument(
        "--anchor-id",
        type=str,
        default=None,
        help="Registry `predictors[].id` 하나 — 그 예측가와 P_now만의 상대갭 열 추가 (예: 뉴스 id)",
    )
    args = p.parse_args(argv)

    gpath = args.gap_csv if args.gap_csv.is_absolute() else (ROOT / args.gap_csv)
    ohl = args.ohlcv if args.ohlcv.is_absolute() else (ROOT / args.ohlcv)
    if not gpath.is_file():
        print("missing gap csv:", gpath, "— run gap_backtest_and_analyze first", file=sys.stderr)
        return 1
    if not ohl.is_file():
        print("missing ohlcv:", ohl, file=sys.stderr)
        return 1

    gap = _read_gap_csv(gpath)
    raw = _read_ohlcv(ohl)
    m0 = _align(raw, gap)
    m0 = add_features_and_forwards(m0, anchor_id=args.anchor_id)
    c = m0["close_ohlc"].astype(float)
    for s in str(args.fwd_bars).split(","):
        s2 = s.strip()
        if not s2:
            continue
        h = int(s2)
        m0[f"fwd_{h}"] = c.shift(-h) / c - 1.0

    feats = [
        "mean_pairwise_rel",
        "gap_system_to_now_rel",
        "signed_sys_vs_now_rel",
        "d_gap_system_rel",
        "d_mean_pairwise_rel",
        "min_anchor_to_now_rel",
        "mean_pairwise_per_atr",
    ]
    if args.anchor_id:
        col = f"anchor__{args.anchor_id}__to_now_rel"
        if col in m0.columns:
            feats.append(col)
    horizons = [c for c in m0.columns if c.startswith("fwd_")]
    out = _report_md(m0, sorted(horizons), feats)
    outp = args.out if args.out.is_absolute() else (ROOT / args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(out, encoding="utf-8")
    print("== wrote:", outp.resolve(), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
