#!/usr/bin/env python3
"""Fetch OpenRouter daily top-model token volumes.

Public status (as of 2026-09-13):
  - Rankings page is public: https://openrouter.ai/rankings (CC BY 4.0)
  - Machine-readable daily series requires an API key:
      GET https://openrouter.ai/api/v1/datasets/rankings-daily
      Authorization: Bearer $OPENROUTER_API_KEY

Without a key this script writes a stub + documents retrieval steps.
With OPENROUTER_API_KEY set it downloads JSON and writes a processed CSV.

Tokenizer caveat: OpenRouter token totals come from each upstream provider's
own tokenizer, so a "token" is not strictly comparable across providers.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
STUBS = ROOT / "data" / "stubs"

sys.path.insert(0, str(ROOT / "src"))
from classify import classify_model  # noqa: E402

RANKINGS_DAILY = "https://openrouter.ai/api/v1/datasets/rankings-daily"


def write_stub() -> None:
    STUBS.mkdir(parents=True, exist_ok=True)
    stub = STUBS / "openrouter_rankings_daily.STUB.md"
    stub.write_text(
        """# OpenRouter rankings-daily — STUB

No API key available in this environment. Daily top-50 token totals are **not**
downloadable without authentication.

## Exact retrieval steps

1. Create an OpenRouter account and API key (same key used for inference).
2. Export:

```bash
export OPENROUTER_API_KEY=sk-or-...
curl -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
  "https://openrouter.ai/api/v1/datasets/rankings-daily?start_date=2026-08-01&end_date=2026-09-12" \\
  -o data/raw/openrouter_rankings_daily.json
```

3. Re-run: `python src/download_openrouter.py`

## Citation

Source: OpenRouter (openrouter.ai/rankings). Rankings data licensed CC BY 4.0.
When republishing: `Source: OpenRouter (openrouter.ai/rankings), as of {as_of}.`

## Tokenizer caveat

Token counts are `prompt_tokens + completion_tokens` as reported by each
upstream provider's tokenizer. Cross-provider totals are not apples-to-apples.
""",
        encoding="utf-8",
    )
    # Minimal empty processed schema for downstream scripts
    PROCESSED.mkdir(parents=True, exist_ok=True)
    out = PROCESSED / "openrouter_open_share_daily.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "date",
                "open_tokens",
                "closed_tokens",
                "other_tokens",
                "open_share_classified_pct",
                "open_share_of_total_pct",
                "note",
            ]
        )
        w.writerow(
            [
                "",
                "",
                "",
                "",
                "",
                "",
                "NO_DATA: set OPENROUTER_API_KEY and re-run download_openrouter.py",
            ]
        )
    print(f"Wrote stub {stub} and empty schema {out}")


def slug_to_display(permaslug: str) -> str:
    # e.g. "deepseek/deepseek-v4-flash" -> "deepseek-v4-flash"
    if permaslug == "other":
        return "Other"
    return permaslug.split("/")[-1].replace("-", " ")


def classify_or_row(permaslug: str) -> str:
    if permaslug == "other":
        return "other"
    # Prefer org prefix when informative
    org = permaslug.split("/")[0].lower() if "/" in permaslug else ""
    name = slug_to_display(permaslug)
    # Org-level shortcuts
    open_orgs = {
        "deepseek",
        "meta-llama",
        "qwen",
        "mistralai",
        "google",  # careful: Gemma open, Gemini closed — fall through to name
        "z-ai",
        "zai",
        "moonshotai",
        "xiaomi",
        "nvidia",
        "tencent",
        "minimax",
        "stepfun",
    }
    closed_orgs = {"openai", "anthropic", "x-ai", "cohere", "perplexity", "amazon"}
    # google: classify by model name (gemma vs gemini)
    if org == "google":
        return classify_model(name)
    if org in closed_orgs:
        return "closed"
    if org in open_orgs and org != "google":
        # still run name classify for Muse-like exceptions under meta
        label = classify_model(name)
        if label != "other":
            return label
        if org in {"deepseek", "meta-llama", "qwen", "mistralai", "z-ai", "zai", "moonshotai", "xiaomi", "nvidia", "tencent", "minimax", "stepfun"}:
            return "open"
    return classify_model(name)


def download_and_process(start: str, end: str) -> Path:
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        write_stub()
        return PROCESSED / "openrouter_open_share_daily.csv"

    headers = {"Authorization": f"Bearer {key}"}
    params = {"start_date": start, "end_date": end, "period": "day"}
    r = requests.get(RANKINGS_DAILY, headers=headers, params=params, timeout=90)
    if r.status_code == 401:
        print("OpenRouter returned 401 — writing stub instead.", file=sys.stderr)
        write_stub()
        return PROCESSED / "openrouter_open_share_daily.csv"
    r.raise_for_status()
    payload = r.json()
    RAW.mkdir(parents=True, exist_ok=True)
    raw_path = RAW / "openrouter_rankings_daily.json"
    raw_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    rows = payload.get("data") or payload
    by_date: dict[str, dict[str, float]] = {}
    for row in rows:
        d = row["date"]
        slug = row["model_permaslug"]
        tokens = float(row["total_tokens"])
        label = classify_or_row(slug)
        bucket = by_date.setdefault(d, {"open": 0.0, "closed": 0.0, "other": 0.0})
        bucket[label] += tokens

    PROCESSED.mkdir(parents=True, exist_ok=True)
    out = PROCESSED / "openrouter_open_share_daily.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "date",
                "open_tokens",
                "closed_tokens",
                "other_tokens",
                "open_share_classified_pct",
                "open_share_of_total_pct",
                "note",
            ]
        )
        for d in sorted(by_date):
            b = by_date[d]
            known = b["open"] + b["closed"]
            total = known + b["other"]
            classified = (b["open"] / known * 100.0) if known else float("nan")
            of_total = (b["open"] / total * 100.0) if total else float("nan")
            w.writerow(
                [
                    d,
                    f"{b['open']:.0f}",
                    f"{b['closed']:.0f}",
                    f"{b['other']:.0f}",
                    f"{classified:.4f}",
                    f"{of_total:.4f}",
                    "tokenizer_caveat: provider-native tokenizers",
                ]
            )
    print(f"Wrote {raw_path} and {out}")
    return out


def main() -> int:
    today = date.today()
    default_end = today - timedelta(days=1)
    default_start = default_end - timedelta(days=30)
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--start-date", default=default_start.isoformat())
    p.add_argument("--end-date", default=default_end.isoformat())
    p.add_argument("--stub-only", action="store_true")
    args = p.parse_args()
    if args.stub_only or not os.environ.get("OPENROUTER_API_KEY"):
        write_stub()
        print(
            "OpenRouter daily series not downloaded (no OPENROUTER_API_KEY). "
            "See data/stubs/openrouter_rankings_daily.STUB.md"
        )
        return 0
    download_and_process(args.start_date, args.end_date)
    return 0


if __name__ == "__main__":
    sys.exit(main())
