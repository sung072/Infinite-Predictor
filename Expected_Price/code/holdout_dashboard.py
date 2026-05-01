"""홀드아웃 provenance JSON → 대시보드용 Markdown / HTML (연구용)."""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

__all__ = [
    "build_holdout_dashboard_markdown",
    "build_holdout_dashboard_html",
    "load_provenance_json",
]


def load_provenance_json(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def _md_table(rows: list[tuple[str, str]]) -> str:
    lines = ["| 항목 | 값 |", "|------|-----|"]
    for k, v in rows:
        lines.append(f"| {k} | {v} |")
    return "\n".join(lines)


def build_holdout_dashboard_markdown(jout: dict[str, Any]) -> str:
    prov = jout.get("provenance")
    if isinstance(prov, list):
        prov = prov[0] if prov else {}
    if not isinstance(prov, dict):
        prov = {}
    th = prov.get("temporal_holdout") or {}
    split = th.get("split") or {}
    cal = th.get("candle_alignment") or {}
    run_info = jout.get("holdout_run_info") or {}
    metrics = jout.get("holdout_metrics") or {}
    summary_ko = jout.get("holdout_accuracy_summary_ko") or ""
    preds = jout.get("predictor_ids") or []
    exp_short = (prov or {}).get("experiment_id_short", "")

    if not th and not metrics:
        return (
            "# 홀드아웃 대시보드\n\n"
            "이 JSON에는 `provenance.temporal_holdout` 또는 `holdout_metrics`가 없습니다. "
            "`--split holdout` 으로 생성한 `--out-prov-json` 파일을 사용하세요.\n"
        )

    # --- 1. Backtest window
    train = cal.get("train") or {}
    emb = cal.get("embargo") or {}
    val = cal.get("validation") or {}
    period_rows: list[tuple[str, str]] = [
        ("전체 창 봉 수 (train+embargo+val)", str(split.get("n_window", ""))),
        ("Train 봉 수", str(split.get("n_train", ""))),
        ("Embargo 봉 수", str(split.get("n_embargo", ""))),
        ("검증(Val) 봉 수", str(split.get("n_val", ""))),
        ("행 간격 추정 (DatetimeIndex일 때)", str(cal.get("median_step_between_rows") or "—")),
    ]
    if train.get("first_bar_label"):
        period_rows.append(("Train 첫 봉 라벨", str(train.get("first_bar_label"))))
        period_rows.append(("Train 마지막 봉 라벨", str(train.get("last_bar_label"))))
    if val.get("first_bar_label"):
        period_rows.append(("검증 첫 봉 라벨 (다음 캔들 구간 시작)", str(val.get("first_bar_label"))))
        period_rows.append(("검증 마지막 봉 라벨", str(val.get("last_bar_label"))))

    # --- 2. Predictors / gap research
    pred_rows: list[tuple[str, str]] = [
        ("Registry", str(run_info.get("registry") or "—")),
        ("OHLCV CSV", str(run_info.get("csv_ohlcv") or "— (합성/내부 데이터)")),
        ("Factors CSV", str(run_info.get("factors_csv") or "—")),
        ("쌍별 간격 열 gpr__*", "예" if run_info.get("gap_pairwise") else "아니오"),
        ("시스템 변형 열", "예" if run_info.get("system_variants") else "아니오"),
        ("예측가 id 목록", ", ".join(str(x) for x in preds) if preds else "—"),
    ]

    # --- 3. System price definition (same window as gap; scoring on val only)
    sys_rows: list[tuple[str, str]] = [
        ("검증 시 사용한 시스템가 정의 (`system_col`)", str(run_info.get("holdout_system_col") or metrics.get("system_col") or "—")),
        ("shrink 가중", str(run_info.get("holdout_shrink") if run_info.get("holdout_shrink") is not None else metrics.get("shrink_weight", "—"))),
        ("설명", "동일 OHLCV 창에서 열 산출 후, **검증 봉(val)** 구간에서만 정확도 집계."),
    ]

    # --- 4. Accuracy
    acc_block = summary_ko.strip() or "_요약 문자열 없음 — `holdout_metrics` 참고._"
    raw_metrics = "```json\n" + json.dumps(metrics, ensure_ascii=False, indent=2) + "\n```"

    parts = [
        "# 홀드아웃 연구 대시보드",
        "",
        f"실험 id (짧은 지문): `{exp_short}`",
        "",
        "## 1. 백테스트 기간 및 분석 (캔들·동일 그리드)",
        "",
        "같은 봉 간격으로 **연속된 train → embargo → 검증(val)** 구간입니다. "
        "검증은 train 마지막 봉 **이후**의 캔들(embargo가 있으면 그만큼 건너뛴 뒤)부터 집계합니다.",
        "",
        _md_table(period_rows),
        "",
        str(th.get("note") or cal.get("boundary_semantics") or ""),
        "",
        "## 2. 예측가·갭 산출 및 분석",
        "",
        _md_table(pred_rows),
        "",
        "## 3. 시스템가 산출 (맥락 창) 및 정의",
        "",
        _md_table(sys_rows),
        "",
        "## 4. 시스템가 정확도 (검증 캔들에서만)",
        "",
        acc_block,
        "",
        "### raw `holdout_metrics`",
        "",
        raw_metrics,
        "",
    ]
    return "\n".join(parts)


def build_holdout_dashboard_html(md_text: str, *, title: str = "홀드아웃 대시보드") -> str:
    """간단 뷰어용 HTML(본문은 이스케이프한 Markdown 텍스트)."""
    t = html.escape(title)
    body = html.escape(md_text)
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{t}</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 52rem; margin: 1.5rem auto; padding: 0 1rem; line-height: 1.55; }}
    pre {{ white-space: pre-wrap; background: #f4f4f5; padding: 1rem; border-radius: 6px; font-size: 0.9rem; }}
    h1 {{ font-size: 1.25rem; }}
  </style>
</head>
<body>
  <h1>{t}</h1>
  <p>아래는 Markdown 기반 텍스트입니다. 테이블·접기는 뷰어에 따라 다르게 보일 수 있습니다.</p>
  <pre>{body}</pre>
</body>
</html>
"""
