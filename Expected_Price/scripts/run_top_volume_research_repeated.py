#!/usr/bin/env python3
r"""거래대금 상위 N USDT 종목에 대해 strict_multi_cycle 배치를 **시드별로 여러 번** 연속 실행.

각 실행은 동일 유니버스·동일 캔들 CSV(이미 있으면 재다운로드 생략)이며, `--seed` 만 바꿔
`strict_multi_cycle_research` 내부 재현 노이즈·경로 차이를 분리한다.

예::

  python scripts/run_top_volume_research_repeated.py --top 100 --repeats 3 --parallel 2 --fetch-missing
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--top", type=int, default=100, help="거래대금(quoteVolume) 상위 N")
    p.add_argument("--repeats", type=int, default=3, help="배치 반복 횟수(시드 0..repeats-1)")
    p.add_argument("--parallel", type=int, default=2)
    p.add_argument("--fetch-missing", action="store_true")
    p.add_argument("--skip-universe-fetch", action="store_true", help="유니버스 txt만 이미 있을 때")
    p.add_argument(
        "--universe-out",
        type=Path,
        default=None,
        help="미지정 시 data/universe/binance_usdt_top{N}_by_quote_volume.txt",
    )
    p.add_argument(
        "--continue-on-error",
        action="store_true",
        default=True,
        help="배치가 일부 종목 실패로 exit 1 이더도 다음 repeat 진행(기본 True)",
    )
    p.add_argument(
        "--no-continue-on-error",
        action="store_false",
        dest="continue_on_error",
        help="배치 실패 시 즉시 중단",
    )
    args, batch_extra = p.parse_known_args(argv)

    py = sys.executable
    uni = (
        args.universe_out.resolve()
        if args.universe_out is not None
        else (ROOT / "data" / "universe" / f"binance_usdt_top{int(args.top)}_by_quote_volume.txt").resolve()
    )

    if not args.skip_universe_fetch:
        r = subprocess.run(
            [
                py,
                str(ROOT / "scripts" / "fetch_binance_top_usdt_by_volume.py"),
                "--top",
                str(int(args.top)),
                "--out",
                str(uni.relative_to(ROOT)),
            ],
            cwd=ROOT,
            check=False,
        )
        if r.returncode != 0:
            return int(r.returncode)

    if not uni.is_file():
        print("universe file missing:", uni, file=sys.stderr)
        return 2

    n = max(1, int(args.repeats))
    for run_id in range(n):
        outj = ROOT / "data" / "runs" / f"strict_multi_cycle_summary_top{int(args.top)}_run{run_id}.json"
        outm = outj.with_suffix(".md")
        cmd = [
            py,
            str(ROOT / "scripts" / "strict_multi_cycle_batch.py"),
            "--symbols-file",
            str(uni),
            "--parallel",
            str(int(args.parallel)),
            "--seed",
            str(run_id),
            "--out-summary-json",
            str(outj),
            "--out-summary-md",
            str(outm),
            *batch_extra,
        ]
        if args.fetch_missing:
            cmd.append("--fetch-missing")
        print("=== run", run_id, "seed", run_id, "===", flush=True)
        print("cmd:", " ".join(cmd), flush=True)
        br = subprocess.run(cmd, cwd=ROOT, check=False)
        if br.returncode != 0:
            print(
                "warning: batch exit",
                br.returncode,
                "(see strict_multi_cycle_summary / per-symbol logs)",
                flush=True,
            )
            if not args.continue_on_error:
                return int(br.returncode)
        print("wrote", outj.resolve(), flush=True)

    print("done", n, "batch runs; summaries under data/runs/", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
