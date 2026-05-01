#!/usr/bin/env python3
"""
Run TODO P0 checks and record completion: docs/todo_state.json + checkboxes in docs/TODO.md.

- fast (default): run_ci --skip-pip --no-jsonl
- full: pip (research+dev) + run_ci --skip-pip, same as run_all.ps1 minus pre-commit
- --dry-run: do not run tests; still refresh state (use with care)

P1/P2 human tasks in TODO.md are never modified.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODO_MD = ROOT / "docs" / "TODO.md"
STATE = ROOT / "docs" / "todo_state.json"

MARK_FAST = "auto:p0-fast-ok"
MARK_FULL = "auto:p0-full-ok"


def _run_cmd(args: list[str], *, cwd: Path) -> None:
    print("==", " ".join(args), flush=True)
    subprocess.check_call(args, cwd=cwd)


def _run_full_pipeline() -> None:
    """Mirror scripts/run_all.ps1 up to run_ci, without pre-commit."""
    py = sys.executable
    _run_cmd([py, "-m", "pip", "install", "-U", "pip", "wheel"], cwd=ROOT)
    _run_cmd([py, "-m", "pip", "install", "-r", "requirements-research.txt"], cwd=ROOT)
    dev = ROOT / "requirements-dev.txt"
    if dev.is_file():
        _run_cmd([py, "-m", "pip", "install", "-r", str(dev)], cwd=ROOT)
    _run_cmd([py, str(ROOT / "scripts" / "run_ci.py"), "--skip-pip"], cwd=ROOT)


def _run_fast() -> None:
    py = sys.executable
    _run_cmd(
        [py, str(ROOT / "scripts" / "run_ci.py"), "--skip-pip", "--no-jsonl"],
        cwd=ROOT,
    )


def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _mark_todo_checkboxes(text: str, *, p0_fast_ok: bool, p0_full_ok: bool) -> str:
    for marker, should in ((MARK_FAST, p0_fast_ok), (MARK_FULL, p0_full_ok)):
        if not should:
            continue
        unc = f"- [ ] <!-- {marker} -->"
        done = f"- [x] <!-- {marker} -->"
        if unc in text:
            text = text.replace(unc, done, 1)
    return text


def _load_state() -> dict:
    if not STATE.is_file():
        return {"version": 1, "p0_fast_ok": False, "p0_full_ok": False, "last_run": None}
    with open(STATE, encoding="utf-8") as f:
        return json.load(f)


def _write_state(st: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--full",
        action="store_true",
        help="full P0: pip + run_ci (tests + JSONL); same as run_all minus pre-commit",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="do not run subprocesses; do not use for real verification",
    )
    args = p.parse_args(argv)

    if not TODO_MD.is_file():
        print("missing:", TODO_MD, file=sys.stderr)
        return 1

    st_prev = _load_state()

    if not args.dry_run:
        try:
            if args.full:
                _run_full_pipeline()
            else:
                _run_fast()
        except subprocess.CalledProcessError as e:
            print("== complete_todo: FAILED, exit", e.returncode, file=sys.stderr)
            return e.returncode or 1
    else:
        print("== complete_todo: dry-run (no tests)", flush=True)

    if args.dry_run:
        print("== not updating state/TODO in dry-run", file=sys.stderr)
        return 0

    p0_full_ok: bool
    p0_fast_ok: bool
    if args.full:
        p0_fast_ok = True
        p0_full_ok = True
    else:
        p0_fast_ok = True
        p0_full_ok = bool(st_prev.get("p0_full_ok", False))

    st = {
        **st_prev,
        "version": 1,
        "p0_fast_ok": p0_fast_ok,
        "p0_full_ok": p0_full_ok,
        "last_run": {
            "mode": "full" if args.full else "fast",
            "at": datetime.datetime.now(datetime.timezone.utc)
            .replace(microsecond=0)
            .isoformat(),
        },
    }
    _write_state(st)

    raw = _read_text(TODO_MD)
    new = _mark_todo_checkboxes(
        raw, p0_fast_ok=p0_fast_ok, p0_full_ok=p0_full_ok
    )
    if new != raw:
        TODO_MD.write_text(new, encoding="utf-8", newline="\n")
        print("== updated", TODO_MD.relative_to(ROOT), flush=True)
    print("== updated", STATE.relative_to(ROOT), flush=True)
    print("== OK (p0_fast_ok=%s, p0_full_ok=%s)" % (p0_fast_ok, p0_full_ok), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
