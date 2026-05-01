"""
BTC OHLCV + Registry 갭 백테스트를 **눈으로** 확인하는 Streamlit 대시보드.

프로젝트 루트(Expected_Price)에서:
  pip install -r requirements-streamlit.txt
  streamlit run dashboard/btc_research_app.py
(기본 HTTP 포트 **7520**, 7000–7999. `.streamlit/config.toml` 또는 `scripts/run_streamlit_btc.*`)
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path
from typing import Any

# `code/*.py` 임포트: 레포 루트 = 이 파일의 상위
ROOT = Path(__file__).resolve().parent.parent
CODE = ROOT / "code"
if str(CODE) not in sys.path:
    sys.path.insert(0, str(CODE))

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

import run_registry_research as rrr
import vbt_gap_research as vg

_DEFAULT_OHLC = ROOT / "data" / "btcusdt_1h_30d.csv"
_REG_BTC4P = ROOT / "schemas" / "predictor_registry.btc_4p.json"
_FACTORS_4P = ROOT / "data" / "derived" / "btc_factors_4p.csv"
_REG_UNIFIED = ROOT / "schemas" / "predictor_registry.btc_unified.json"
_FACTORS_UNIFIED = ROOT / "data" / "derived" / "btc_factors_unified.csv"
_EXAMPLE = ROOT / "schemas" / "predictor_registry.example.json"
_COLORS = [
    "#636EFA",
    "#EF553B",
    "#00CC96",
    "#AB63FA",
    "#FFA15A",
    "#19D3F3",
    "#FF6692",
    "#B6E880",
    "#FF97FF",
    "#FECB52",
]

# 범례·라벨용(알 수 없는 id 는 그대로)
_PRED_ID_KO: dict[str, str] = {
    "btc_ema_fast": "빠른 EMA",
    "btc_ema_slow": "느린 EMA",
    "btc_resist_24h": "24봉 저항",
    "btc_support_24h": "24봉 지지",
    "vol_as_price_demo": "량가(거래량→가격)",
    "time_as_price_demo": "시간가(사이클→가격)",
    "war_news_fwd_4h": "뉴스가(4h·데모)",
    "sentiment_as_price_demo": "감성가(데모)",
    "eth_beta_pair_1d": "페어(ETH)가(데모)",
}
# 각 id 가 ‘숫자’가 아니라 읽힐 **문맥(연구·비유)** (한 줄)
_PRED_CONTEXT: dict[str, str] = {
    "btc_ema_fast": "짧은 기간 **추세/관성**을 눈금에 올린 축.",
    "btc_ema_slow": "긴 기간 **추세**를 눈금에 올린 축.",
    "btc_resist_24h": "직전 고점·저항 밴드 근처 **목표**.",
    "btc_support_24h": "직전 저점·지지 밴드 근처 **목표**.",
    "vol_as_price_demo": "**거래량(유동·참여)** 를 같은 가격축에 올린 **량가**.",
    "time_as_price_demo": "장중 **시간·사이클** 을 가격눈금에 올린 **시간가**.",
    "war_news_fwd_4h": "**뉴스·이벤트** 를 앞서 반영한 **뉴스가**(데모 열).",
    "sentiment_as_price_demo": "심리·**감정 스칼라** 를 가격으로 환산한 **감성가**(데모).",
    "eth_beta_pair_1d": "다른 기준자산(예: ETH)과의 **상대·페어** 를 **페어가**로 둔 축(데모).",
}
_GAP_COL_KO: dict[str, str] = {
    "mean_pairwise_rel": "평균 쌍간격(상대)",
    "gap_system_to_now_rel": "시스템·현재 괴리(상대)",
    "range_rel": "앵커 폭(상대)",
    "mean_pairwise_per_atr": "쌍간격 / ATR",
}


def _pred_legend_name(pid: str) -> str:
    return _PRED_ID_KO.get(pid, f"예측가 · {pid}")


def _gap_legend_name(col: str) -> str:
    return _GAP_COL_KO.get(col, col)


def _ai_summary_ko(
    df: pd.DataFrame,
    c_last: pd.Series,
    p_sys: pd.Series | None,
    pids: list[str],
) -> str:
    """규칙 기반 한국어: 선=문맥, 합의 vs 시장·여력(비유). LLM API 없음. 투자 권고 아님."""
    if len(c_last) == 0 or p_sys is None or len(p_sys) == 0:
        return "데이터가 없어 요약을 생성할 수 없습니다."
    v_n = float(c_last.iloc[-1])
    v_s = float(p_sys.iloc[-1])
    diff = v_s - v_n
    rel_pct = (diff / v_n * 100.0) if v_n else 0.0

    parts: list[str] = [
        "##### 문맥(선 이름 = 숫자 + 의미)\n"
        "각 **색 선**은 단일 스칼라가 아니라, Registry **축(뉴스·시간·감정·거시·추세 등)** 이 **같은 USDT 눈금**에 투영된 **문맥**으로 읽는 것이 이 대시보드의 전제입니다.\n\n"
        "**검토 예시(참고, 고정 시그널 아님):** (가상 예) **전쟁가·금리가** 눈금이 **가깝게 겹치면** 같은 **거시·불안** 쪽에서 같이 읽는지 점검, "
        "**유동(커뮤·체결)가** 가 **현재가와 붙으면** **단기 투기·흐름** 쪽을 의심해 봄. *(실제 id·데이터·레짐에 따름.)*",
    ]

    last = df.iloc[-1]
    ppr = last.get("predictor_prices") if hasattr(last, "get") else last["predictor_prices"]
    pp = _pp_row(ppr)
    line_rows: list[str] = ["**이번 봉 — 선별 문맥·가격(끝)**"]
    for pid in pids:
        name = _pred_legend_name(pid)
        ctx = _PRED_CONTEXT.get(
            pid,
            "Registry 에 맞는 **의미 축**으로 읽을 것(이름만으로 판정하지 않음).",
        )
        pv = pp.get(pid)
        pstr = f"{pv:,.2f} USDT" if pv is not None and np.isfinite(pv) else "—"
        line_rows.append(f"- **{name}** ({pstr}): {ctx}")
    parts.append("\n".join(line_rows))

    if "mean_pairwise_rel" in df.columns and len(df) > 2:
        mpw = float(df["mean_pairwise_rel"].iloc[-1])
        med = float(df["mean_pairwise_rel"].median())
        if mpw < med * 0.9:
            parts.append(
                f"**퍼짐(평균 쌍간격 {mpw:.5f}):** 뭉침 쪽 — 여러 문맥이 **같이 붙는** 국면으로 *해석·검토*할 수 있음(예측 아님)."
            )
        elif mpw > med * 1.1:
            parts.append(
                f"**퍼짐({mpw:.5f}):** **흩어짐** — 견해가 **엇갈리는** 식의 국면으로 *검토*해 볼 수 있음."
            )
        else:
            parts.append(
                f"**퍼짐({mpw:.5f}, 중앙 {med:.5f}):** **보통** — 위 두 극단만큼 **뾰족**히 말하진 않음(레짐·샘플에 민감)."
            )

    if abs(diff) <= max(1e-9, 1e-4 * v_n) if v_n else abs(diff) <= 1e-6:
        yuk = "합의(시스템가)와 **현재가**가 **거의 같음** — 단기로는 **의견이 수렴**한 쪽으로 읽는 질문을 던져 볼 수 있음(**수익 보장 아님**)."
    elif diff > 0:
        yuk = (
            f"**시스템가 > 현재가** ({v_s:,.2f} vs {v_n:,.2f}, **{rel_pct:+.2f}%**). "
            "**간격만의 비유:** 합의 눈금이 **위**에 있으면, (연구 맥락에서) 시장이 그 합의 쪽으로 **붙을 여지·공간**을 *질문*해 볼 수 있음. "
            "**‘상승’ 보장·매수 신호가 아님**."
        )
    else:
        yuk = (
            f"**시스템가 < 현재가** ({v_s:,.2f} vs {v_n:,.2f}, **{rel_pct:+.2f}%**). "
            "**간격만의 비유:** 합의가 **아래**이면, 가격이 합의 쪽으로 **내려와 맞을 여지**를 *질문*해 볼 수 있음. **하락·매도 권고·방향 예측이 아님**."
        )
    parts.append("##### 합의 vs 시장(‘상승·하락 **여력**’은 **비유**)\n" + yuk)

    if "gap_system_to_now_rel" in df.columns:
        g = float(df["gap_system_to_now_rel"].iloc[-1])
        parts.append(
            f"**시스템·현재 괴리(상대) {g:.5f}:** `gap_system_to_now_rel` 는 **절댓값** (위/아래 **방향**은 `signed`·문맥과 함께 봄)."
        )

    parts.append("\n*자동(규칙). **매수·매도·타점 권고 아님.***")
    return "\n\n".join(parts)


def _pp_row(r: Any) -> dict[str, float]:
    if isinstance(r, dict):
        return {k: float(v) for k, v in r.items() if v is not None and np.isfinite(float(v))}
    if isinstance(r, str) and "{" in r:
        try:
            d = ast.literal_eval(r)
        except (SyntaxError, ValueError, TypeError):
            return {}
        if isinstance(d, dict):
            return {k: float(v) for k, v in d.items() if v is not None and np.isfinite(float(v))}
    return {}


def _research_gap_x_fwd(
    ohlc: pd.DataFrame, df: pd.DataFrame
) -> tuple[pd.DataFrame, str]:
    """예측가 퍼짐(mean_pairwise) 3구간 × 다음봉 수익 3구간: 평균 수익·건수(연구용)."""
    c = ohlc["close"].astype(float)
    fwd = c.shift(-1) / c - 1.0
    mpw = pd.to_numeric(df.get("mean_pairwise_rel"), errors="coerce")
    t = pd.DataFrame({"fwd1": fwd, "mpw": mpw}).dropna()
    t = t.iloc[:-1]  # 마지막 봉: fwd 없음
    if len(t) < 20:
        return (
            pd.DataFrame(),
            "봉 수가 부족해 3×3을 만들 수 없습니다.",
        )
    try:
        t["g3"] = pd.qcut(
            t["mpw"],
            3,
            labels=["퍼짐_좁음", "퍼짐_중", "퍼짐_넓음"],
            duplicates="drop",
        )
        t["r3"] = pd.qcut(
            t["fwd1"],
            3,
            labels=["다음수익_하위", "다음수익_중", "다음수익_상위"],
            duplicates="drop",
        )
    except ValueError as e:
        return pd.DataFrame(), f"qcut 제한: {e!s}"
    agg = t.groupby(["g3", "r3"], observed=True)["fwd1"].agg(["mean", "count"])
    return agg.reset_index(), (
        "행: 예측가끼리 **상대 퍼짐** (mean_pairwise_rel) 낮을수록 '좁음' · "
        "열: **다음 봉** 단순 수익률(종가) 분위. **효과적 시스템가**는 퍼짐·괴리·레짐을 "
        "함께 봐야 하며, 이 표는 **가설 점검**용(인과·운용 신호 아님)."
    )


@st.cache_data(ttl=300, show_spinner="갭 시계열 계산 중…")
def compute_gap_frame(
    ohlc_path_str: str,
    registry_path_str: str,
    factors_path_str: str | None,
    *,
    gap_pairwise: bool,
    system_variants: bool,
    seed: int = 0,
) -> tuple[pd.DataFrame, list[str], dict[str, Any], pd.DataFrame]:
    ohlc_p = Path(ohlc_path_str)
    ohlc = vg.load_ohlcv_csv(ohlc_p)
    reg_p = Path(registry_path_str)
    fac: str | None = None
    if factors_path_str:
        fpath = Path(factors_path_str)
        if fpath.is_file():
            fac = str(fpath)
    df, prov, ids, reg = rrr.run_from_registry(
        reg_p,
        ohlcv=ohlc,
        seed=seed,
        data_snapshot_id="streamlit-dash-001",
        use_price_like=False,
        factors_path=fac,
        include_pairwise_columns=gap_pairwise,
        include_system_variants=system_variants,
    )
    if not df.index.equals(ohlc.index):
        df = df.reindex(ohlc.index)
    return df, list(ids), prov, ohlc


def main() -> None:
    st.set_page_config(page_title="Expected_Price — BTC 갭", layout="wide")
    st.markdown(
        """
<style>
    .stApp { background-color: #0a0a0c; }
    div[data-testid="stToolbar"] { background-color: #141417; }
    div[data-testid="stNotification"] { background-color: #141417; }
    div[data-testid="stAlert"] { background-color: #1a1a22 !important; border: 1px solid #2a2a33 !important; }
    [data-testid="stMetricValue"] { color: #f0f0f0; }
    [data-testid="stMetricLabel"] { color: #b0b0b0; }
</style>
        """,
        unsafe_allow_html=True,
    )
    st.title("BTC — 가격눈금 (량가·시간가·뉴스·감성 + 시스템가)")
    st.caption("모든 항은 Registry+`price_like`/factors로 **한 축(USDT)에 예측가**로 올립니다. 시스템가는 **그 위에서의 합의(기본: 산술평균)** 를 연구·시각화합니다.")
    st.info(
        "**운영 순서(권장): ① 이 대시보드(시각) 먼저** — 캔들=**현재가(종가)**·각 선=**예측가(가격 눈금)**·보라 굵은 선=**시스템가(합의)**. "
        "② **퍼짐(갭)** 은 **아래 축** ‘평균 쌍간격’ 등으로 확인. ③ **백테스팅 / OOS / 리포트** 는 터미널·문서가 **이 화면과 같은 계층**을 수치·기간으로 보조한다."
    )

    with st.sidebar:
        st.header("데이터")
        ohlc_default = str(_DEFAULT_OHLC)
        ohlc_path = st.text_input("OHLCV CSV", value=ohlc_default)
        st.caption("`timestamp`+OHLC, `data/btcusdt_1h_30d.csv` 권장 (없으면 Binance로 받을 수 있음)")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("Binance 1h fetch"):
                import subprocess

                out = Path(ohlc_path)
                out.parent.mkdir(parents=True, exist_ok=True)
                subprocess.check_call(
                    [sys.executable, str(ROOT / "scripts" / "fetch_btc_ohlcv.py"), "--out", str(out)]
                )
                st.success("다운로드 끔 — 아래 '다시 계산'")
        with c2:
            if st.button("F factors 빌드 (4p)"):
                import subprocess

                subprocess.check_call(
                    [sys.executable, str(ROOT / "scripts" / "build_btc_factor_csv.py")],
                    cwd=ROOT,
                )
                st.success("완료")
        if st.button("F factors 통합(량·시·뉴·감성+4p) 빌드"):
            import subprocess

            subprocess.check_call(
                [sys.executable, str(ROOT / "scripts" / "build_btc_unified_factor_csv.py")],
                cwd=ROOT,
            )
            st.success("btc_factors_unified.csv 완료")

        st.header("Registry (모든 축 → **예측가 가격**)")
        preset = st.selectbox(
            "프리셋",
            (
                "btc_unified (4p+량가+시간가+뉴스+감성+페어) ★",
                "btc_4p (EMA/밴드만)",
                "example (eth/war 샘플)",
            ),
        )
        if "unified" in preset:
            reg_path = str(_REG_UNIFIED)
            fac_default = str(_FACTORS_UNIFIED) if _FACTORS_UNIFIED.is_file() else ""
        elif preset.startswith("btc"):
            reg_path = str(_REG_BTC4P)
            fac_default = str(_FACTORS_4P) if _FACTORS_4P.is_file() else ""
        else:
            reg_path = str(_EXAMPLE)
            fac_default = ""
        reg_path = st.text_input("Registry JSON", value=reg_path)
        fac_path = st.text_input("Factors CSV (뉴스·EMA 등 절대가 열)", value=fac_default)
        if "unified" in preset and (not fac_path or not Path(fac_path).is_file()):
            st.warning("통합은 `data/derived/btc_factors_unified.csv` + `build_btc_unified_factor_csv.py` 필요.")
        if preset.startswith("btc_4p") and "unified" not in preset and (
            not fac_path or not Path(fac_path).is_file()
        ):
            st.warning("4p는 `data/derived/btc_factors_4p.csv` 가 있어야 합니다.")

        st.header("계산")
        gap_pairwise = st.checkbox("쌍 열 (gpr__*__, 느릴 수 있음)", value=False)
        system_variants = st.checkbox("시스템가 변형 (p_system_shrunk, tension)", value=True)
        hline_last = st.checkbox(
            "마지막 봉 **수평 가이드** (P_now·p_system·각 예측가)",
            value=True,
        )
        if st.button("캐시 지우기 & 다시 그리기"):
            st.cache_data.clear()
            st.rerun()

    ohlc_ok = Path(ohlc_path).is_file()
    if not ohlc_ok:
        st.error("OHLCV 가 없습니다. `fetch` 또는 경로를 맞추세요.")
        return

    try:
        df, pids, prov, ohlc = compute_gap_frame(
            str(Path(ohlc_path).resolve()),
            str(Path(reg_path).resolve()),
            str(Path(fac_path).resolve()) if fac_path and Path(fac_path).is_file() else None,
            gap_pairwise=gap_pairwise,
            system_variants=system_variants,
        )
    except Exception as e:
        st.exception(e)
        return

    c_last = ohlc["close"]
    t_index = ohlc.index
    p_sys = df.get("p_system")
    p_sh = df.get("p_system_shrunk") if system_variants and "p_system_shrunk" in df else None
    p_tn = df.get("p_system_tension") if system_variants and "p_system_tension" in df else None

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.68, 0.32],
        vertical_spacing=0.06,
        subplot_titles=(
            "① 가격 (캔들) + 현재가·시스템가·예측가",
            "② 퍼짐·갭 지표 (스케일 정규)",
        ),
    )
    fig.add_trace(
        go.Candlestick(
            x=t_index,
            open=ohlc["open"],
            high=ohlc["high"],
            low=ohlc["low"],
            close=ohlc["close"],
            name="캔들(시장)",
            increasing_line_color="#26A69A",
            decreasing_line_color="#EF5350",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=t_index,
            y=c_last,
            name="현재가(종가)",
            line=dict(color="#9E9E9E", width=1, dash="dot"),
            opacity=0.6,
        ),
        row=1,
        col=1,
    )
    if p_sys is not None:
        fig.add_trace(
            go.Scatter(
                x=t_index,
                y=p_sys,
                name="시스템가(합의)",
                line=dict(color="#AB47BC", width=1.4),
            ),
            row=1,
            col=1,
        )
    if p_sh is not None:
        fig.add_trace(
            go.Scatter(
                x=t_index,
                y=p_sh,
                name="시스템가(현재에 수렴)",
                line=dict(color="#6A1B9A", width=1, dash="dash"),
            ),
            row=1,
            col=1,
        )
    if p_tn is not None:
        fig.add_trace(
            go.Scatter(
                x=t_index,
                y=p_tn,
                name="시스템가(팽팽함·연구)",
                line=dict(color="#00897B", width=0.9, dash="dot"),
                visible="legendonly",
            ),
            row=1,
            col=1,
        )
    for i, pid in enumerate(pids):
        yv = [(_pp_row(df["predictor_prices"].iloc[k]).get(pid)) for k in range(len(df))]
        yv = pd.Series(yv, dtype=object)
        ynum = pd.to_numeric(yv, errors="coerce")
        if ynum.notna().any():
            col = _COLORS[i % len(_COLORS)]
            fig.add_trace(
                go.Scatter(
                    x=t_index,
                    y=ynum,
                    name=_pred_legend_name(pid),
                    line=dict(color=col, width=1.1),
                ),
                row=1,
                col=1,
            )
    y2_metrics: list[str] = [
        "mean_pairwise_rel",
        "gap_system_to_now_rel",
        "range_rel",
        "mean_pairwise_per_atr",
    ]
    m_available = [m for m in y2_metrics if m in df.columns]
    for i, mname in enumerate(m_available):
        s = pd.to_numeric(df[mname], errors="coerce")
        fig.add_trace(
            go.Scatter(
                x=t_index,
                y=s,
                name=_gap_legend_name(mname),
                line=dict(width=1.1, color=_COLORS[(i + 2) % len(_COLORS)]),
                visible="legendonly" if i > 0 else True,
            ),
            row=2,
            col=1,
        )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0a0a0c",
        plot_bgcolor="#101014",
        font=dict(color="#e0e0e0"),
        xaxis_rangeslider_visible=False,
        height=780,
        margin=dict(t=50, b=40, l=8, r=8),
        legend=dict(
            title=dict(text="범례 (클릭 토글)", font=dict(size=15, color="#c0c0c0")),
            orientation="h",
            yanchor="bottom",
            y=1.04,
            xanchor="right",
            x=1,
            font=dict(size=13, color="#d0d0d0"),
            bgcolor="rgba(10,10,12,0.6)",
        ),
        uirevision="1",
    )
    for row_i in (1, 2):
        fig.update_xaxes(
            gridcolor="rgba(255,255,255,0.08)",
            zerolinecolor="rgba(255,255,255,0.12)",
            row=row_i,
            col=1,
        )
        fig.update_yaxes(
            title_text="가격 (USDT)" if row_i == 1 else "갭·상대값 (무차원)",
            side="right",
            gridcolor="rgba(255,255,255,0.08)",
            zerolinecolor="rgba(255,255,255,0.12)",
            row=row_i,
            col=1,
        )
    fig.update_xaxes(title_text="시간 (UTC)", row=2, col=1)

    if hline_last and len(c_last) > 0:
        k = -1

        def _hl(y: float, lab: str, col: str) -> None:
            if y is None or (isinstance(y, float) and (np.isnan(y) or np.isinf(y))):
                return
            fig.add_hline(
                y=float(y),
                line_dash="dot",
                line_width=1.0,
                line_color=col,
                opacity=0.65,
                annotation_text=lab,
                annotation_position="right",
                row=1,
                col=1,
            )

        _hl(float(c_last.iloc[k]), "현재가(끝)", "#424242")
        if p_sys is not None:
            _hl(float(p_sys.iloc[k]), "시스템가", "#4A148C")
        for i, pid in enumerate(pids):
            yv = _pp_row(df["predictor_prices"].iloc[k]).get(pid)
            if yv is not None and np.isfinite(yv):
                _hl(float(yv), _pred_legend_name(pid), _COLORS[i % len(_COLORS)])
        if p_sh is not None and np.isfinite(p_sh.iloc[k]):
            _hl(float(p_sh.iloc[k]), "시스템가·수렴", "#5E35B1")

    st.caption(
        "가격눈금: **캔들**=시장·**현재가(점선)**=종가·**시스템가**=합의·**색 선**=각 예측가(Registry). "
        "하단: **퍼짐·갭** 지표. **수평 점선**은 **마지막 봉** 가격(전 구간에 투영)."
    )
    st.caption("범례(상단)에서 항목을 **클릭**해 켜고 끄세요.")
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"scrollZoom": True, "displaylogo": False},
    )

    mcols = st.columns(4)
    with mcols[0]:
        st.metric("현재가(종가)", f"{float(c_last.iloc[-1]):,.2f}" if len(c_last) else "—")
    with mcols[1]:
        st.metric("시스템가", f"{float(p_sys.iloc[-1]):,.2f}" if p_sys is not None and len(p_sys) else "—")
    with mcols[2]:
        if "mean_pairwise_rel" in df.columns:
            st.metric("평균 쌍간격(상대)", f"{float(df['mean_pairwise_rel'].iloc[-1]):.5f}")
    with mcols[3]:
        if "gap_system_to_now_rel" in df.columns:
            st.metric("시스템·현재 괴리(상대)", f"{float(df['gap_system_to_now_rel'].iloc[-1]):.5f}")

    st.markdown("##### AI 요약(자동 · 규칙 기반)")
    try:
        c_ai = st.container(border=True)
    except TypeError:
        c_ai = st.container()
    with c_ai:
        st.markdown(_ai_summary_ko(df, c_last, p_sys, pids))

    with st.expander("기술 메타 (Registry·provenance)"):
        st.json(
            {
                "predictor_ids": pids,
                "n_bars": int(len(df)),
                "provenance_keys": list(prov.keys()) if isinstance(prov, dict) else "—",
            }
        )

    rtab, rcap = _research_gap_x_fwd(ohlc, df)
    with st.expander("연구: **퍼짐(갭) 좁음/넓음** vs **다음 봉** 수익(3×3, 연관 점검)", expanded=False):
        st.markdown(rcap)
        if rtab is not None and not rtab.empty:
            st.dataframe(rtab, use_container_width=True, height=260)
        else:
            st.info("퍼짐×수익 요약을 만들지 못했습니다. 봉 수·중복 분위를 확인하세요.")

    with st.expander("원시 gap 테이블 (끝 12행)"):
        st.dataframe(
            df.tail(12).reset_index(),
            use_container_width=True,
            height=320,
        )

    st.markdown("---")
    st.caption("실체결·PNL·실서비스는 이 레포 README가 말하는 경계 밖 — **연구 시각화** 전용.")


if __name__ == "__main__":
    main()
