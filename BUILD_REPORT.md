# BUILD_REPORT — OPEN WEIGHTS

**Build date:** 2026-09-13  
**Target remote:** https://github.com/JallanXYZ/open-weights (public)

## Latest weekly open %

From `data/processed/vercel_open_share_weekly.csv` (Vercel AI Gateway, text tokens, model-level classification):

| Field | Value |
|-------|------:|
| ISO week | **2026-W37** |
| Range | 2026-09-07 → 2026-09-13 (7 days) |
| **`open_share_classified_pct`** | **70.72%** |
| `open_share_of_total_pct` | 49.38% |
| `other_share` | 33.84% |
| `open_known` (avg daily % pts) | 49.38 |
| `closed_known` (avg daily % pts) | 16.78 |

**Latest day (2026-09-13):** classified open **87.11%**; open of total **75.87%**; Other **12.91%**.

Do **not** substitute a hardcoded 73.3% — these figures are computed from the live export.

## Data gaps

1. **OpenRouter:** `GET /api/v1/datasets/rankings-daily` returns **401** without an API key. No daily series written. Stub + exact curl steps in `data/stubs/openrouter_rankings_daily.STUB.md`. Script `src/download_openrouter.py` will process JSON when `OPENROUTER_API_KEY` is set. Tokenizer caveat documented.
2. **Hugging Face:** No comparable global % inference-token open-vs-closed series found. Not invented. See `data/stubs/huggingface_inference_share.STUB.md`.
3. **Vercel `Other` bucket:** Large for much of the sample (often >50% until early September). Classified open% ≠ share of all tokens; both are published.
4. **Lab-level secondary series:** Available but Meta mixes Llama (open) and Muse (closed); headline uses **model-level** labels. Muse Spark 1.3 Contributor classified **closed**.

## Chart

- `charts/open_share_spaghetti.png`
- `charts/open_share_spaghetti.svg`
- Title: *OPEN MODELS ARE EATING INFERENCE*
- Weekly series, 0–100% Y, endpoint labels, phone-friendly dark theme.

## Scripts (runnable)

| Script | Role |
|--------|------|
| `src/download_vercel.py` | Live CC BY 4.0 CSV export |
| `src/process_vercel.py` | Classify + daily/weekly CSVs |
| `src/download_openrouter.py` | Keyed download or honest stub |
| `src/download_huggingface.py` | Documents gap |
| `src/build_chart.py` | PNG + SVG |
| `src/classify.py` | Shared open/closed/other rules |

Verified this build: `process_vercel.py`, `download_openrouter.py` (stub path), `download_huggingface.py`, `build_chart.py` all exit 0. `download_vercel.py` hit HTTP 200 against `https://vercel.com/api/ai/leaderboard-export`.

## File list

```
BUILD_REPORT.md
README.md
requirements.txt
.gitignore
charts/open_share_spaghetti.png
charts/open_share_spaghetti.svg
data/raw/vercel_models_text.csv
data/raw/vercel_labs_text.csv
data/processed/vercel_open_share_daily.csv
data/processed/vercel_open_share_weekly.csv
data/processed/vercel_labs_open_share_daily.csv
data/processed/vercel_labs_open_share_weekly.csv
data/processed/vercel_model_classification_audit.csv
data/processed/openrouter_open_share_daily.csv          # empty schema / NO_DATA row
data/processed/huggingface_open_share_daily.csv         # NO_COMPARABLE_SERIES row
data/stubs/openrouter_rankings_daily.STUB.md
data/stubs/huggingface_inference_share.STUB.md
draft/article.md
draft/x-post.md
draft/hooks.md
draft/claims-and-constraints.md
draft/vercel-snapshot-2026-09-13.json
research/claims.md
research/sources.md
src/classify.py
src/download_vercel.py
src/download_openrouter.py
src/download_huggingface.py
src/process_vercel.py
src/build_chart.py
```

## Attribution

© 2026 Vercel. "AI Gateway Leaderboard Data" is licensed under CC BY 4.0.  
https://creativecommons.org/licenses/by/4.0/
