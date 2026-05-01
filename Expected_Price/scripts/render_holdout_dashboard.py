#!/usr/bin/env python3
r"""`--out-prov-json` (holdout) → 대시보드 Markdown / HTML.

예:
  python scripts/render_holdout_dashboard.py --from-json data/runs/holdout_prov.json \\
    --out-md data/runs/holdout_dashboard.md --out-html data/runs/holdout_dashboard.html
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_CODE = ROOT / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import holdout_dashboard as hd  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--from-json", type=Path, required=True, help="holdout provenance JSON")
    p.add_argument("--out-md", type=Path, required=True)
    p.add_argument("--out-html", type=Path, default=None)
    args = p.parse_args(argv)

    jout = hd.load_provenance_json(args.from_json)
    md_text = hd.build_holdout_dashboard_markdown(jout)
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text(md_text, encoding="utf-8")
    print("wrote:", args.out_md.resolve())
    if args.out_html is not None:
        html_text = hd.build_holdout_dashboard_html(md_text)
        args.out_html.parent.mkdir(parents=True, exist_ok=True)
        args.out_html.write_text(html_text, encoding="utf-8")
        print("wrote:", args.out_html.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
