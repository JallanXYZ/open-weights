#!/usr/bin/env python3
"""Process Vercel model/lab token shares into open-weight series.

Primary metric (models, metric=tokens, modality=text):
  open_share_classified_pct = open_known / (open_known + closed_known) * 100
Also reports open_known as share of total (incl. Other) as open_share_of_total_pct.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from classify import classify_lab, classify_model  # noqa: E402

RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"


def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df[df["date"].astype(str).str.match(r"^\d{4}-\d{2}-\d{2}$", na=False)].copy()
    df["date"] = pd.to_datetime(df["date"])
    df["share_percent"] = pd.to_numeric(df["share_percent"], errors="coerce")
    return df.dropna(subset=["share_percent"])


def daily_from_models(df: pd.DataFrame) -> pd.DataFrame:
    tok = df[(df["metric"] == "tokens") & (df["modality"] == "text")].copy()
    tok["class"] = tok["name"].map(classify_model)
    # classification audit
    audit = (
        tok.groupby(["name", "class"], as_index=False)["share_percent"]
        .max()
        .sort_values("share_percent", ascending=False)
    )
    daily = tok.groupby(["date", "class"])["share_percent"].sum().unstack(fill_value=0.0)
    for col in ("open", "closed", "other"):
        if col not in daily.columns:
            daily[col] = 0.0
    daily = daily.rename(
        columns={"open": "open_known", "closed": "closed_known", "other": "other_share"}
    )
    known = daily["open_known"] + daily["closed_known"]
    daily["open_share_classified_pct"] = daily["open_known"] / known * 100.0
    daily["open_share_of_total_pct"] = daily["open_known"]  # already % of total
    daily["closed_share_of_total_pct"] = daily["closed_known"]
    return daily.reset_index(), audit


def daily_from_labs(df: pd.DataFrame) -> pd.DataFrame:
    tok = df[(df["metric"] == "tokens") & (df["modality"] == "text")].copy()
    tok["class"] = tok["name"].map(classify_lab)
    daily = tok.groupby(["date", "class"])["share_percent"].sum().unstack(fill_value=0.0)
    for col in ("open", "closed", "other"):
        if col not in daily.columns:
            daily[col] = 0.0
    daily = daily.rename(
        columns={"open": "open_known", "closed": "closed_known", "other": "other_share"}
    )
    known = daily["open_known"] + daily["closed_known"]
    daily["open_share_classified_pct"] = daily["open_known"] / known * 100.0
    daily["open_share_of_total_pct"] = daily["open_known"]
    return daily.reset_index()


def to_weekly(daily: pd.DataFrame) -> pd.DataFrame:
    d = daily.copy()
    d["iso_year"] = d["date"].dt.isocalendar().year.astype(int)
    d["iso_week"] = d["date"].dt.isocalendar().week.astype(int)
    agg = {
        "week_start": ("date", "min"),
        "week_end": ("date", "max"),
        "n_days": ("date", "count"),
        "open_known": ("open_known", "mean"),
        "closed_known": ("closed_known", "mean"),
        "other_share": ("other_share", "mean"),
        "open_share_classified_pct": ("open_share_classified_pct", "mean"),
        "open_share_of_total_pct": ("open_share_of_total_pct", "mean"),
    }
    if "closed_share_of_total_pct" in d.columns:
        agg["closed_share_of_total_pct"] = ("closed_share_of_total_pct", "mean")
    w = d.groupby(["iso_year", "iso_week"], as_index=False).agg(**agg)
    return w


def main() -> int:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    models = load_csv(RAW / "vercel_models_text.csv")
    labs = load_csv(RAW / "vercel_labs_text.csv")

    daily_m, audit = daily_from_models(models)
    weekly_m = to_weekly(daily_m)
    daily_l = daily_from_labs(labs)
    weekly_l = to_weekly(daily_l)

    daily_m.to_csv(PROCESSED / "vercel_open_share_daily.csv", index=False, float_format="%.6f")
    weekly_m.to_csv(PROCESSED / "vercel_open_share_weekly.csv", index=False, float_format="%.6f")
    daily_l.to_csv(PROCESSED / "vercel_labs_open_share_daily.csv", index=False, float_format="%.6f")
    weekly_l.to_csv(PROCESSED / "vercel_labs_open_share_weekly.csv", index=False, float_format="%.6f")
    audit.to_csv(PROCESSED / "vercel_model_classification_audit.csv", index=False)

    latest_w = weekly_m.iloc[-1]
    latest_d = daily_m.sort_values("date").iloc[-1]
    print("Latest day:", latest_d["date"].date(), f"classified={latest_d['open_share_classified_pct']:.2f}%")
    print(
        "Latest ISO week:",
        int(latest_w["iso_year"]),
        f"W{int(latest_w['iso_week']):02d}",
        f"{latest_w['week_start'].date()}→{latest_w['week_end'].date()}",
        f"classified={latest_w['open_share_classified_pct']:.2f}%",
        f"of_total={latest_w['open_share_of_total_pct']:.2f}%",
        f"other={latest_w['other_share']:.2f}%",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
