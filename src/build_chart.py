#!/usr/bin/env python3
"""Build charts/open_share_spaghetti.png (+ svg) — phone-friendly weekly series."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
CHARTS = ROOT / "charts"


def main() -> int:
    weekly = pd.read_csv(
        PROCESSED / "vercel_open_share_weekly.csv",
        parse_dates=["week_start", "week_end"],
    )
    if weekly.empty:
        print("No weekly data — run process_vercel.py first", file=sys.stderr)
        return 1

    weekly = weekly.copy()
    weekly["x"] = weekly["week_start"] + (weekly["week_end"] - weekly["week_start"]) / 2

    CHARTS.mkdir(parents=True, exist_ok=True)

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "axes.unicode_minus": False,
    })

    fig, ax = plt.subplots(figsize=(7.2, 10.4), dpi=180)
    fig.patch.set_facecolor("#0b0f14")
    ax.set_facecolor("#0b0f14")

    series = [
        ("open_share_classified_pct", "Open among classified", "#3DDC97", 2.8, "-"),
        ("open_share_of_total_pct", "Open share of all tokens", "#5B8CFF", 2.2, "--"),
        ("other_share", "Other (unclassified)", "#8B949E", 1.7, ":"),
    ]

    # Stagger endpoint labels so they never sit on top of each other
    end_offsets = {
        "open_share_classified_pct": 10,
        "open_share_of_total_pct": 0,
        "other_share": -10,
    }

    for col, label, color, lw, ls in series:
        ax.plot(
            weekly["x"],
            weekly[col],
            color=color,
            linewidth=lw,
            linestyle=ls,
            label=label,
            solid_capstyle="round",
        )
        x_end = weekly["x"].iloc[-1]
        y_end = float(weekly[col].iloc[-1])
        ax.annotate(
            f"{label}\n{y_end:.1f}%",
            xy=(x_end, y_end),
            xytext=(10, end_offsets[col]),
            textcoords="offset points",
            color=color,
            fontsize=8,
            fontweight="bold",
            va="center",
            ha="left",
            annotation_clip=False,
        )
        x0 = weekly["x"].iloc[0]
        y0 = float(weekly[col].iloc[0])
        ax.annotate(
            f"{y0:.1f}%",
            xy=(x0, y0),
            xytext=(-6, 0),
            textcoords="offset points",
            color=color,
            fontsize=7,
            va="center",
            ha="right",
            alpha=0.95,
            annotation_clip=False,
        )

    ax.set_ylim(0, 100)
    ax.yaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_minor_locator(MultipleLocator(10))
    ax.set_ylabel("Share of text-token volume", color="#E6EDF3", fontsize=10)
    pad = pd.Timedelta(days=4)
    ax.set_xlim(weekly["x"].min() - pad, weekly["x"].max() + pad)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %-d"))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=2))
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center", color="#E6EDF3", fontsize=8)
    plt.setp(ax.get_yticklabels(), color="#E6EDF3", fontsize=9)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(axis="y", color="#21262D", linewidth=0.8)
    ax.tick_params(length=0)

    fig.suptitle(
        "Open models are eating inference",
        color="#FFFFFF",
        fontsize=16,
        fontweight="bold",
        x=0.08,
        ha="left",
        y=0.975,
    )
    fig.text(
        0.08,
        0.932,
        "Vercel AI Gateway  ·  text tokens  ·  weekly averages  ·  CC BY 4.0",
        color="#8B949E",
        fontsize=8,
        ha="left",
        va="top",
    )

    latest = weekly.iloc[-1]
    fig.text(
        0.08,
        0.028,
        (
            f"Latest week (ISO {int(latest['iso_year'])}-W{int(latest['iso_week']):02d}): "
            f"{latest['open_share_classified_pct']:.1f}% open among classified, "
            f"{latest['open_share_of_total_pct']:.1f}% of all tokens."
        ),
        color="#3DDC97",
        fontsize=8,
        ha="left",
    )
    fig.text(
        0.08,
        0.008,
        "Source: Vercel AI Gateway Leaderboard Data (CC BY 4.0). Other = unclassified / long-tail bucket.",
        color="#6E7681",
        fontsize=6.5,
        ha="left",
    )

    fig.subplots_adjust(left=0.14, right=0.68, top=0.88, bottom=0.09)

    png = CHARTS / "open_share_spaghetti.png"
    svg = CHARTS / "open_share_spaghetti.svg"
    fig.savefig(png, facecolor=fig.get_facecolor(), edgecolor="none")
    fig.savefig(svg, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    print(f"Wrote {png} and {svg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
