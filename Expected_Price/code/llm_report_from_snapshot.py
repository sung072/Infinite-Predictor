"""4단계: `ai_analysis_snapshot.json` → (규칙) 마크다운 + (선택) OpenAI 호환 API."""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

__all__ = [
    "load_snapshot_json",
    "render_rule_markdown",
    "llm_openai_chat_completion",
    "write_merged_report",
]

DEFAULT_OUT_NAME = "ai_analysis_report.md"


def load_snapshot_json(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8"))


def render_rule_markdown(snap: dict[str, Any]) -> str:
    """LLM 없이, 스냅샷 구조를 읽을 수 있게 정리(투자 권고 아님)."""
    lines: list[str] = [
        "# 갭·시스템가 스냅샷 요약 (규칙·자동)",
        "",
        f"- **스키마:** `{snap.get('schema', '?')}`",
        f"- **생성(UTC):** {snap.get('generated_at_utc', '?')}",
        f"- **full 봉:** {snap.get('bars', {}).get('full', '?')}",
        "",
        "## last_bar (핵심 스칼라)",
        "",
    ]
    lb = snap.get("last_bar") or {}
    for k, v in sorted(lb.items(), key=lambda x: str(x[0])):
        if k == "timestamp":
            continue
        lines.append(f"- `{k}`: {v!r}")
    if lb.get("timestamp"):
        lines += ["", f"**끝 봉 시각:** {lb.get('timestamp')!r}", ""]

    lines += ["## tail (샘플)", ""]
    for i, row in enumerate((snap.get("tail_rows") or [])[:5]):
        lines.append(f"### tail[{i}]")
        lines.append(f"```\n{json.dumps(row, ensure_ascii=False)[:2000]}\n```\n")
    if snap.get("summary_numeric_full"):
        lines += [
            "", "## full 구간 describe (수치·레짐 참고·예측 아님)", "",
            "```",
            json.dumps(snap.get("summary_numeric_full"), ensure_ascii=False)[:12_000],
            "```",
            "",
        ]
    prov = snap.get("provenance") or {}
    if any(prov.values()):
        lines += ["", "## Provenance(출처) 스텁", "```json", json.dumps(prov, ensure_ascii=False)[:4000], "```", ""]
    lines += [
        "*규칙 기반. 매수·매도·타점 **아님**.*",
        "",
    ]
    return "\n".join(lines)


def _env(key: str, default: str | None = None) -> str | None:
    v = os.environ.get(key, "").strip()
    return v if v else default


def llm_openai_chat_completion(
    messages: list[dict[str, str]],
    *,
    timeout_s: int = 120,
) -> str | None:
    """`OPENAI_API_KEY` + `OPENAI_BASE_URL`(기본 `https://api.openai.com/v1`) + `OPENAI_MODEL`(기본 gpt-4o-mini). 실패 시 None."""
    key = _env("OPENAI_API_KEY")
    if not key:
        return None
    model = _env("OPENAI_MODEL", "gpt-4o-mini") or "gpt-4o-mini"
    base = _env("OPENAI_BASE_URL", "https://api.openai.com/v1")
    if not base or not model:
        return None
    url = base.rstrip("/") + "/chat/completions"
    body = json.dumps(
        {
            "model": model,
            "messages": messages,
            "max_tokens": 2500,
        },
        ensure_ascii=False,
    ).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as r:
            out = json.loads(r.read().decode("utf-8", errors="replace"))
    except (urllib.error.URLError, OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        return None
    try:
        ch = out.get("choices") or []
        if not ch:
            return None
        return str(ch[0].get("message", {}).get("content") or "").strip() or None
    except (TypeError, AttributeError):
        return None


def write_merged_report(
    snapshot_path: str | Path,
    out_path: str | Path,
    *,
    try_llm: bool = True,
) -> tuple[bool, str | None]:
    """
    규칙 MD + (성공 시) LLM 절. 반환: (llm_used, err_hint).
    `try_llm` True 인데 키/실패면 규칙만 쓰고 (False, "…") 를 돌려 **치명이 아님**."""
    path = Path(snapshot_path)
    snap = load_snapshot_json(path)
    rule = render_rule_markdown(snap)
    llm_used = False
    err: str | None = None
    llm_block: str = ""
    if try_llm:
        sys_prompt = (
            "당신은 시계열·갭 메트릭 **관찰**만 요약한다. "
            "매수·매도·수익·방향 예측·확률 **금지**."
        )
        user = (
            "아래 JSON(앵커·갭 스냅샷)에 대해 한국어로 3~6문장으로 불확실성·한계·검토 포인트만. "
            "필요한 키만 골라 언급.\n\n"
            f"```json\n{json.dumps(snap, ensure_ascii=False)[:24_000]}\n```"
        )
        msg: list[dict[str, str]] = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user},
        ]
        t = llm_openai_chat_completion(msg)
        if t:
            llm_used = True
            llm_block = f"\n---\n\n# LLM 요약(선택 API)\n\n{t}\n"
        else:
            if not _env("OPENAI_API_KEY"):
                err = "OPENAI_API_KEY unset — only rule report written"
            else:
                err = "LLM call failed or empty — only rule report written"
    p = Path(out_path)
    p.write_text(
        rule + (llm_block or "") + f"\n\n*merged report. llm_used={llm_used}*",
        encoding="utf-8",
    )
    return llm_used, err
