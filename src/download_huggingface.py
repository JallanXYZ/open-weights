#!/usr/bin/env python3
"""Hugging Face — no comparable global % inference-token open series.

This script documents the gap and optionally notes secondary proxies
(download counts, Hub model cards) that are NOT inference-token share.
It does not invent a time series.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUBS = ROOT / "data" / "stubs"
PROCESSED = ROOT / "data" / "processed"


def main() -> int:
    STUBS.mkdir(parents=True, exist_ok=True)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    note = STUBS / "huggingface_inference_share.STUB.md"
    note.write_text(
        """# Hugging Face — no global inference-token open-share series

## Finding

As of this build, Hugging Face does **not** publish a comparable, global,
daily/weekly **percentage of inference tokens** attributable to open-weight
models vs closed models.

What exists instead (secondary proxies only — do not treat as inference share):

- Hub model download / like counts (selection & packaging signal, not inference).
- Spaces / Inference Endpoints usage (partial, opt-in, not market-wide).
- Provider-specific telemetry (not aggregated into an open global %).

## Policy for this repo

- Do **not** invent an HF open-share time series.
- Primary observable series remains Vercel AI Gateway (and OpenRouter if keyed).
- Optional narrative: HF Hub activity is a supply-side proxy for open-weight
  proliferation, not demand-side inference share.

## Re-check later

Search HF blog / datasets / BigCode / HF Stats for any new "tokens served"
leaderboard before assuming the gap remains.
""",
        encoding="utf-8",
    )
    out = PROCESSED / "huggingface_open_share_daily.csv"
    out.write_text(
        "date,open_share_pct,note\n"
        ",,NO_COMPARABLE_SERIES: see data/stubs/huggingface_inference_share.STUB.md\n",
        encoding="utf-8",
    )
    print(f"Wrote {note} and {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
