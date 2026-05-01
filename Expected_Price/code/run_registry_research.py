"""Registry JSON + 합성/CSV OHLCV → gap 시계열 + provenance (연구 **진입점**)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd
import vbt_gap_research as vg
import fdr_exploration as fdrx
import price_like as pl
import walkforward_oos as wfo
import predictor_data_feed as pdf
import execution_bridge as exb
from predictor_registry import (
    PredictorStatus,
    all_predictor_ids,
    anchor_cohort_map_for_ids,
    load_registry_file,
    predictor_ids_by_status,
    validate_registry,
)

# 프로젝트 루트(Expected_Price 폴더) — 스키마/예를 상대로 찾을 때
_PKG = Path(__file__).resolve().parent.parent


def resolve_predictor_ids(
    data: dict[str, Any],
    *,
    use_statuses: set[PredictorStatus] | None = None,
) -> list[str]:
    """`use_statuses`로 먼저 뽑고, 2개 미만이면 candidate→전체 순으로 보강."""
    u1: set[PredictorStatus] = use_statuses or {"active", "challenger"}
    ids = predictor_ids_by_status(data, u1)
    if len(ids) >= 2:
        return sorted(ids)
    u2: set[PredictorStatus] = {"active", "challenger", "candidate"}
    ids = predictor_ids_by_status(data, u2)
    if len(ids) >= 2:
        return sorted(ids)
    a = all_predictor_ids(data)
    if len(a) >= 2:
        return sorted(a)
    raise ValueError("Registry에 predictors 2개 이상이 없습니다 (gap 쌍거리에 필요).")


def resolve_predictor_ids_fused(
    data: dict[str, Any],
    *,
    use_statuses: set[PredictorStatus] | None = None,
    use_price_like: bool = False,
) -> list[str]:
    base = set(resolve_predictor_ids(data, use_statuses=use_statuses))
    if use_price_like:
        for req in (pl.PRED_ID_VOL, pl.PRED_ID_TIME):
            if not any(
                p.get("id") == req
                for p in data.get("predictors", [])
                if isinstance(p, dict)
            ):
                raise ValueError(
                    f"Registry에 {req!r} id가 있어야 use_price_like 를 켤 수 있습니다. "
                    "참고: docs/price_unification.md"
                )
        base |= {pl.PRED_ID_VOL, pl.PRED_ID_TIME}
    return sorted(base)


def run_from_registry(
    registry_path: str | Path,
    *,
    ohlcv: pd.DataFrame | None = None,
    n_synthetic_bars: int = 48,
    seed: int = 0,
    data_snapshot_id: str | None = None,
    use_statuses: set[PredictorStatus] | None = None,
    oos_train_ratio: float | None = None,
    oos_embargo_bars: int = 0,
    use_price_like: bool = False,
    factors_path: str | Path | None = None,
    factors_df: pd.DataFrame | None = None,
    include_pairwise_columns: bool = False,
    atr_window: int = 14,
    include_system_variants: bool = False,
) -> tuple[pd.DataFrame, dict[str, Any], list[str], dict[str, Any]]:
    """`ohlcv`를 주지 않으면 `synthetic_ohlcv_bars`로 둔다.
    * `oos_train_ratio`를 주면: 앞 구간=train(버림), `embargo` 뒤만 gap 연구(단일 OOS).
    * `use_price_like=True`: volume·time id 를 합쳐 **모든 앵커 = 가격** (code/price_like).
    * `factors_path` / `factors_df`: `meta.factor_column` 별 **절대가**로 id 덮어쓰기 (code/predictor_data_feed).
    * `include_pairwise_columns`: vbt `run_gap_research_ohlcv` 가 `gpr__*__*` 쌍 열(많은 id면 열 수 주의).
    * `atr_window`: ATR(간격/ATR 정규화) 봉 수.
    * `include_system_variants`: `p_system_shrunk`·`p_system_tension` (code/system_price_rules).
    * `meta.anchor_cohort` 가 **이번 run의 모든** `id`에 있으면 `gpr_cohort_inter_rel` / `gpr_cohort_intra_rel` (군간·군내).
    """
    path = Path(registry_path)
    data = load_registry_file(path)
    validate_registry(data, min_predictors=2)
    ids = resolve_predictor_ids_fused(
        data, use_statuses=use_statuses, use_price_like=use_price_like
    )
    if len(ids) < 2:
        raise ValueError("active/challenger 등에서 id를 2개 이상 뽑지 못했습니다")

    snap = data_snapshot_id
    if not snap and isinstance(data, dict) and "data_snapshot_id" in data:
        snap = str(data["data_snapshot_id"])
    if not snap:
        snap = "unspecified"

    ohlc = ohlcv if ohlcv is not None else vg.synthetic_ohlcv_bars(n_synthetic_bars, seed=seed)
    oos_meta: dict[str, Any] | None = None
    n_bars_in = len(ohlc)
    if oos_train_ratio is not None:
        _tr, meta, ohlc = wfo.oossplit_by_ratio(
            ohlc, train_ratio=oos_train_ratio, embargo_bars=oos_embargo_bars
        )
        oos_meta = meta.to_dict()
    f_merged: pd.DataFrame | None = factors_df
    if f_merged is None and factors_path is not None:
        f_raw = pdf.load_factors_table(Path(factors_path))
        f_merged = pdf.align_factors_to_ohlc(ohlc, f_raw)
    has_dyn = pdf.has_any_model_artifact(data, ids)
    cohort_map = anchor_cohort_map_for_ids(data, ids)
    use_merged = f_merged is not None or has_dyn
    fn = None
    if use_merged:
        fn = pdf.build_merged_predictor_prices_fn(
            ohlc,
            data,
            ids,
            factors=f_merged,
            use_price_like_vol_time=use_price_like,
            project_root=_PKG,
            registry_path=path,
        )
    cfg: dict[str, Any] = {
        "runner": "run_registry_research",
        "registry": str(path.resolve()),
        "registry_schema_version": data.get("schema_version", ""),
        "n_bars": len(ohlc),
        "n_bars_input": n_bars_in,
        "synthetic": ohlcv is None,
        "use_predictor_ids": ids,
        "oos": oos_meta,
        "use_price_like": use_price_like and not use_merged,
        "factors_merged": f_merged is not None,
        "model_artifact_merged": has_dyn,
        "factors_path": str(factors_path) if factors_path else None,
        "gap_pairwise": include_pairwise_columns,
        "atr_window": int(atr_window),
        "system_variants": include_system_variants,
        "anchor_cohort": bool(cohort_map),
        "anchor_cohort_labels": dict(cohort_map) if cohort_map else {},
    }
    out, prov = vg.run_gap_research_ohlcv(
        ohlc,
        active_predictor_ids=ids,
        research_config=cfg,
        data_snapshot_id=snap,
        seed=seed,
        use_price_like=use_price_like and not use_merged,
        predictor_prices_fn=fn,
        atr_window=int(atr_window),
        include_pairwise_columns=include_pairwise_columns,
        include_system_variants=include_system_variants,
        anchor_cohort=cohort_map,
    )
    return out, prov, ids, data


def run_wf_folds_from_registry(
    registry_path: str | Path,
    ohlcv: pd.DataFrame,
    *,
    n_train: int,
    n_test: int,
    n_embargo: int = 0,
    wf_step: int | None = None,
    seed: int = 0,
    data_snapshot_id: str | None = None,
    use_statuses: set[PredictorStatus] | None = None,
    use_price_like: bool = False,
    factors_path: str | Path | None = None,
    include_pairwise_columns: bool = False,
    atr_window: int = 14,
    include_system_variants: bool = False,
) -> tuple[pd.DataFrame, list[dict[str, Any]], list[str], dict[str, Any], dict[str, Any]]:
    """롤링 WF: 각 **test** 구간만 `run_gap_research_ohlcv`, 결과 `fold` 열로 합침."""
    path = Path(registry_path)
    data = load_registry_file(path)
    validate_registry(data, min_predictors=2)
    ids = resolve_predictor_ids_fused(
        data, use_statuses=use_statuses, use_price_like=use_price_like
    )
    snap = data_snapshot_id
    if not snap and isinstance(data, dict) and "data_snapshot_id" in data:
        snap = str(data["data_snapshot_id"])
    if not snap:
        snap = "unspecified"
    f_full: pd.DataFrame | None = None
    if factors_path is not None:
        f_raw = pdf.load_factors_table(Path(factors_path))
        f_full = pdf.align_factors_to_ohlc(ohlcv, f_raw)
    n = len(ohlcv)
    folds = list(
        wfo.iter_walkforward_folds(
            n, n_train=n_train, n_test=n_test, n_embargo=n_embargo, step=wf_step
        )
    )
    if not folds:
        raise ValueError("WF: 폴드 0 — n_train/embargo/test/길이를 늘려 볼 것")
    cohort_map = anchor_cohort_map_for_ids(data, ids)
    out_parts: list[pd.DataFrame] = []
    prov_list: list[dict[str, Any]] = []
    wrep = wfo.run_walkforward_report(
        n, n_train=n_train, n_test=n_test, n_embargo=n_embargo, step=wf_step
    )
    for f in folds:
        sub = ohlcv.iloc[f.test_slice]
        f_sub: pd.DataFrame | None = None
        if f_full is not None:
            f_sub = f_full.loc[sub.index]
        has_dyn = pdf.has_any_model_artifact(data, ids)
        fn: Any = None
        if f_sub is not None or has_dyn:
            fn = pdf.build_merged_predictor_prices_fn(
                sub,
                data,
                ids,
                factors=f_sub,
                use_price_like_vol_time=use_price_like,
                project_root=_PKG,
                registry_path=path,
            )
        cfg: dict[str, Any] = {
            "runner": "run_wf_folds",
            "registry": str(path.resolve()),
            "fold": f.fold_id,
            "n_train": n_train,
            "n_test": n_test,
            "n_embargo": n_embargo,
            "step": wf_step,
            "wf_folds": wrep,
            "use_predictor_ids": ids,
            "use_price_like": use_price_like and f_sub is None and not has_dyn,
            "factors_merged": f_sub is not None,
            "model_artifact_merged": has_dyn,
            "gap_pairwise": include_pairwise_columns,
            "atr_window": int(atr_window),
            "system_variants": include_system_variants,
            "anchor_cohort": bool(cohort_map),
            "anchor_cohort_labels": dict(cohort_map) if cohort_map else {},
        }
        o, pr = vg.run_gap_research_ohlcv(
            sub,
            active_predictor_ids=ids,
            research_config=cfg,
            data_snapshot_id=snap,
            seed=seed + f.fold_id,
            use_price_like=use_price_like and f_sub is None and not has_dyn,
            predictor_prices_fn=fn,
            atr_window=int(atr_window),
            include_pairwise_columns=include_pairwise_columns,
            include_system_variants=include_system_variants,
            anchor_cohort=cohort_map,
        )
        o2 = o.assign(fold=pd.Series(f.fold_id, index=o.index, dtype="int32"))
        out_parts.append(o2)
        prov_list.append(pr)
    return pd.concat(out_parts, axis=0), prov_list, ids, data, wrep


def _parse_statuses(s: str | None) -> set[PredictorStatus] | None:
    if not s or not s.strip():
        return None
    parts = {p.strip() for p in s.split(",") if p.strip()}
    allowed: set[PredictorStatus] = {
        "candidate",  # type: ignore[assignment]
        "active",
        "retired",
        "challenger",
    }
    bad = parts - allowed
    if bad:
        raise ValueError(f"unknown status in --status: {bad}")
    return parts  # type: ignore[return-value]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--registry",
        type=Path,
        default=_PKG / "schemas" / "predictor_registry.example.json",
        help="Registry JSON (기본: 예시 파일)",
    )
    p.add_argument("--n-bars", type=int, default=48, dest="n_bars")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument(
        "--csv-ohlcv", type=Path, default=None, help="합성 대신 이 CSV(ohlcv 열) 사용"
    )
    p.add_argument(
        "--status",
        type=str,
        default="active,challenger",
        help="콤마 구분. 예: active,challenger,candidate. 비우면 active+challenger",
    )
    p.add_argument(
        "--snapshot", type=str, default=None, help="data_snapshot_id 강제(없으면 Registry의 값)"
    )
    p.add_argument(
        "--out-csv", type=Path, default=None, help="gap 시계열 DataFrame을 CSV로 저장"
    )
    p.add_argument(
        "--out-parquet",
        type=Path,
        default=None,
        help="optional gap DataFrame Parquet (pyarrow 필요)",
    )
    p.add_argument(
        "--out-prov-json",
        type=Path,
        default=None,
        help="provenance + predictor_ids + registry 메타 json 저장",
    )
    p.add_argument(
        "--split",
        type=str,
        default="full",
        choices=["full", "oos", "wf", "holdout"],
        help=(
            "full=전 구간, oos=train+embargo 뒤만, wf=롤링 test 구간, "
            "holdout=앞 train·embargo·val 한 창에서 전 구간 gap 산출 후 **val 바만** 검증 지표"
        ),
    )
    p.add_argument(
        "--train-frac", type=float, default=0.7, help="(oos) train bar 비율(0,1), 기본 0.7"
    )
    p.add_argument(
        "--embargo",
        type=int,
        default=0,
        help="(oos/wf/holdout) train~test 사이에 버릴 bar 수",
    )
    p.add_argument(
        "--holdout-train-bars",
        type=int,
        default=None,
        help="(holdout) 학습·워밍업으로 쓸 연속 bar 수",
    )
    p.add_argument(
        "--holdout-val-bars",
        type=int,
        default=None,
        help="(holdout) 검증만 집계할 연속 bar 수(날짜 아님; 백테스트와 동일 봉 간격 기준)",
    )
    p.add_argument(
        "--holdout-system-col",
        default="p_system_shrunk_custom",
        help="(holdout) 검증 지표용 시스템가 열",
    )
    p.add_argument(
        "--holdout-shrink",
        type=float,
        default=0.96,
        help="(holdout) system_col=shrunk_custom 일 때 P_now 가중",
    )
    p.add_argument(
        "--out-validation-csv",
        type=Path,
        default=None,
        help="(holdout) 검증 구간 행만 gap CSV",
    )
    p.add_argument("--wf-train", type=int, default=24, help="(wf) train 길이(바)")
    p.add_argument("--wf-test", type=int, default=8, help="(wf) OOS test 길이(바)")
    p.add_argument(
        "--wf-step",
        type=int,
        default=None,
        help="(wf) 롤 step (기본=wf-test, 겹침 없이)",
    )
    p.add_argument(
        "--n-hypotheses",
        type=int,
        default=1,
        help="이번 러너에서 시도·가설 수(탐색 예산·FDR 메타에 씀)",
    )
    p.add_argument(
        "--explore-cap",
        type=int,
        default=None,
        help="가설/시도 **상한** (넘기면 이 CLI는 예외; 오프라인에선 권장)",
    )
    p.add_argument(
        "--fdr-q",
        type=float,
        default=None,
        help="(선택) p값 없이도 메타에 q만 남김; p는 후속 러너가 채움",
    )
    p.add_argument(
        "--price-like",
        action="store_true",
        help="거래량/시간 등 → 가격(예측가) : code/price_like + vbt. Registry에 vol_as_price_demo, time_as_price_demo 필요",
    )
    p.add_argument(
        "--factors-csv",
        type=Path,
        default=None,
        help="(선택) p_war 등 **절대가(예측가) 열** (timestamp+열). `meta.factor_column` 과 매핑. OHLCV와 **시간 정렬**.",
    )
    p.add_argument(
        "--gap-pairwise",
        action="store_true",
        help="쌍별 상대 간격 열 gpr__*__* 포함 (vbt_gap_research.include_pairwise_columns; 앵커 수 많으면 열 수 증가)",
    )
    p.add_argument(
        "--atr-window",
        type=int,
        default=14,
        help="ATR(간격/ATR 등) 봉 수, 기본 14",
    )
    p.add_argument(
        "--system-variants",
        action="store_true",
        help="p_system_shrunk, p_system_tension 열 추가 (system_price_rules)",
    )
    p.add_argument(
        "--out-execution-jsonl",
        type=Path,
        default=None,
        help="Nautilus 등용: gap DF + 앵커 딕셔너리 JSONL (execution_bridge)",
    )
    p.add_argument(
        "--out-dashboard-md",
        type=Path,
        default=None,
        help="(holdout) 홀드아웃 대시보드 Markdown 저장",
    )
    p.add_argument(
        "--out-dashboard-html",
        type=Path,
        default=None,
        help="(holdout) 동일 내용 간단 HTML 뷰어",
    )
    a = p.parse_args(argv)
    fdrx.assert_exploration_cap(a.n_hypotheses, a.explore_cap, label="CLI")
    ohl: pd.DataFrame | None
    if a.csv_ohlcv is not None:
        ohl = vg.load_ohlcv_csv(a.csv_ohlcv)
    else:
        ohl = None

    stat = _parse_statuses(a.status)
    ho_pack: dict[str, Any] | None = None
    if a.split == "full":
        df, prov, ids, reg = run_from_registry(
            a.registry,
            ohlcv=ohl,
            n_synthetic_bars=a.n_bars,
            seed=a.seed,
            data_snapshot_id=a.snapshot,
            use_statuses=stat,
            use_price_like=a.price_like,
            factors_path=a.factors_csv,
            include_pairwise_columns=a.gap_pairwise,
            atr_window=a.atr_window,
            include_system_variants=a.system_variants,
        )
        wrep: dict | None = None
        prows: list[dict[str, Any]] = [prov]
    elif a.split == "holdout":
        if a.holdout_train_bars is None or a.holdout_val_bars is None:
            print(
                "holdout: --holdout-train-bars 와 --holdout-val-bars 가 필요합니다.",
                file=sys.stderr,
            )
            return 2
        ohl0 = ohl
        if ohl0 is None:
            ohl0 = vg.synthetic_ohlcv_bars(a.n_bars, seed=a.seed)
        from temporal_validation import run_holdout_validation

        ho_pack = run_holdout_validation(
            a.registry,
            ohl0,
            n_train_bars=int(a.holdout_train_bars),
            n_embargo_bars=int(a.embargo),
            n_val_bars=int(a.holdout_val_bars),
            seed=a.seed,
            data_snapshot_id=a.snapshot,
            use_statuses=stat,
            use_price_like=a.price_like,
            factors_path=a.factors_csv,
            include_pairwise_columns=a.gap_pairwise,
            atr_window=a.atr_window,
            include_system_variants=a.system_variants,
            system_col=str(a.holdout_system_col),
            shrink_weight=float(a.holdout_shrink),
        )
        df = ho_pack["full_gap_df"]
        prov = ho_pack["provenance"]
        ids = ho_pack["predictor_ids"]
        reg = ho_pack["registry"]
        wrep = None
        prows = [prov]
        print("=== 1) 백테스트(gap)·예측가·시스템가 산출 → 2) 검증 캔들에서만 시스템가 정확도 ===")
        print(ho_pack.get("accuracy_summary_ko", ho_pack["metrics_validation"]))
        print("--- raw metrics ---")
        print(ho_pack["metrics_validation"])
    elif a.split == "oos":
        df, prov, ids, reg = run_from_registry(
            a.registry,
            ohlcv=ohl,
            n_synthetic_bars=a.n_bars,
            seed=a.seed,
            data_snapshot_id=a.snapshot,
            use_statuses=stat,
            oos_train_ratio=a.train_frac,
            oos_embargo_bars=a.embargo,
            use_price_like=a.price_like,
            factors_path=a.factors_csv,
            include_pairwise_columns=a.gap_pairwise,
            atr_window=a.atr_window,
            include_system_variants=a.system_variants,
        )
        wrep = None
        prows = [prov]
    else:  # wf
        ohl0 = ohl
        if ohl0 is None:
            ohl0 = vg.synthetic_ohlcv_bars(a.n_bars, seed=a.seed)
        (
            df,
            provl,
            ids,
            reg,
            wrep,
        ) = run_wf_folds_from_registry(
            a.registry,
            ohl0,
            n_train=a.wf_train,
            n_test=a.wf_test,
            n_embargo=a.embargo,
            wf_step=a.wf_step,
            seed=a.seed,
            data_snapshot_id=a.snapshot,
            use_statuses=stat,
            use_price_like=a.price_like,
            factors_path=a.factors_csv,
            include_pairwise_columns=a.gap_pairwise,
            atr_window=a.atr_window,
            include_system_variants=a.system_variants,
        )
        prows = provl
    ex_meta = fdrx.exploration_provenance(
        a.n_hypotheses, fdr_q=a.fdr_q, cap=a.explore_cap, p_values=None
    )
    jout = {
        "provenance": prows[0] if a.split != "wf" else prows,
        "walkforward": wrep,
        "predictor_ids": ids,
        "registry_data_snapshot": reg.get("data_snapshot_id"),
        "exploration": ex_meta,
    }
    if ho_pack is not None:
        jout["holdout_metrics"] = ho_pack["metrics_validation"]
        jout["holdout_accuracy_summary_ko"] = ho_pack.get("accuracy_summary_ko")
        jout["holdout_run_info"] = {
            "registry": str(a.registry.resolve()),
            "factors_csv": str(a.factors_csv.resolve()) if a.factors_csv else None,
            "csv_ohlcv": str(a.csv_ohlcv.resolve()) if a.csv_ohlcv else None,
            "holdout_train_bars": a.holdout_train_bars,
            "embargo": int(a.embargo),
            "holdout_val_bars": a.holdout_val_bars,
            "holdout_system_col": str(a.holdout_system_col),
            "holdout_shrink": float(a.holdout_shrink),
            "gap_pairwise": bool(a.gap_pairwise),
            "system_variants": bool(a.system_variants),
        }
    print("predictor_ids", ids)
    print("provenance", prows if a.split == "wf" else prows[0])
    print("df\n", df.head(3), "\n...", df.tail(1))
    if a.out_csv is not None:
        df.to_csv(a.out_csv)
    if a.out_validation_csv is not None:
        if ho_pack is None:
            print("--out-validation-csv 는 --split holdout 과 함께 쓰세요.", file=sys.stderr)
            return 2
        ho_pack["validation_gap_df"].to_csv(a.out_validation_csv)
        print("wrote validation-only csv:", a.out_validation_csv.resolve())
    if a.out_parquet is not None:
        try:
            df.to_parquet(a.out_parquet)
        except (ImportError, OSError) as e:
            alt = a.out_parquet.with_suffix(".csv")
            df.to_csv(alt)
            print("parquet save failed, wrote csv:", alt, "({})".format(e), file=sys.stderr)
    if a.out_prov_json is not None:
        with Path(a.out_prov_json).open("w", encoding="utf-8") as f:
            json.dump(jout, f, ensure_ascii=False, indent=2)
    if a.out_dashboard_md is not None or a.out_dashboard_html is not None:
        if ho_pack is None:
            print(
                "--out-dashboard-md/html 은 --split holdout 과 함께 사용하세요.",
                file=sys.stderr,
            )
            return 2
        import holdout_dashboard as hd

        md_text = hd.build_holdout_dashboard_markdown(jout)
        if a.out_dashboard_md is not None:
            Path(a.out_dashboard_md).parent.mkdir(parents=True, exist_ok=True)
            Path(a.out_dashboard_md).write_text(md_text, encoding="utf-8")
            print("wrote dashboard md:", a.out_dashboard_md.resolve())
        if a.out_dashboard_html is not None:
            html_text = hd.build_holdout_dashboard_html(md_text)
            Path(a.out_dashboard_html).parent.mkdir(parents=True, exist_ok=True)
            Path(a.out_dashboard_html).write_text(html_text, encoding="utf-8")
            print("wrote dashboard html:", a.out_dashboard_html.resolve())
    if a.out_execution_jsonl is not None:
        exb.write_execution_jsonl(
            df,
            a.out_execution_jsonl,
            header={
                "registry": str(a.registry.resolve()),
                "split": a.split,
                "predictor_ids": ids,
                "config_sha256": (prows[0] if a.split != "wf" else prows[-1]).get(
                    "config_sha256", ""
                ),
            },
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())

__all__ = [
    "resolve_predictor_ids",
    "resolve_predictor_ids_fused",
    "run_from_registry",
    "run_wf_folds_from_registry",
    "main",
]
