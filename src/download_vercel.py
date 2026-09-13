#!/usr/bin/env python3
"""Download Vercel AI Gateway leaderboard CSVs (CC BY 4.0).

Endpoint (documented):
  GET https://vercel.com/api/ai/leaderboard-export
    ?dataset=models|labs&modality=text&format=csv

Attribution: © 2026 Vercel. "AI Gateway Leaderboard Data" is licensed under
CC BY 4.0. https://creativecommons.org/licenses/by/4.0/
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
EXPORT_URL = "https://vercel.com/api/ai/leaderboard-export"


def download(dataset: str, modality: str, out: Path) -> Path:
    params = {"dataset": dataset, "modality": modality, "format": "csv"}
    r = requests.get(EXPORT_URL, params=params, timeout=60)
    r.raise_for_status()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(r.content)
    print(f"Wrote {out} ({len(r.content)} bytes)")
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--modality", default="text", choices=["text", "all", "image", "video"])
    p.add_argument("--models-out", type=Path, default=RAW / "vercel_models_text.csv")
    p.add_argument("--labs-out", type=Path, default=RAW / "vercel_labs_text.csv")
    args = p.parse_args()
    download("models", args.modality, args.models_out)
    download("labs", args.modality, args.labs_out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
