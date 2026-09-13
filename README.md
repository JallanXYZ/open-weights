# OPEN WEIGHTS

Observable share of AI **inference tokens** attributable to **open-weight** models — primarily from [Vercel AI Gateway leaderboards](https://vercel.com/ai-gateway/leaderboards/models) (CC BY 4.0).

This repo downloads public leaderboard CSVs, classifies named models as open / closed / other (never silently assigning the long tail), aggregates daily & weekly series, and builds a phone-friendly chart.

## Headline (this build)

| Week | Open among classified | Open of all tokens | Other |
|------|----------------------:|-------------------:|------:|
| ISO **2026-W37** (2026-09-07 → 2026-09-13) | **~70.7%** | **~49.4%** | **~33.8%** |

Recompute after refresh — do not hardcode. See `research/claims.md` and `BUILD_REPORT.md`.

## Quick start

```bash
git clone https://github.com/JallanXYZ/open-weights.git
cd open-weights
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Refresh Vercel CSVs (CC BY 4.0)
python src/download_vercel.py

# Build processed series
python src/process_vercel.py

# Optional: OpenRouter (needs OPENROUTER_API_KEY) / HF gap note
python src/download_openrouter.py
python src/download_huggingface.py

# Chart
python src/build_chart.py
```

Outputs:

- `data/processed/vercel_open_share_daily.csv`
- `data/processed/vercel_open_share_weekly.csv`
- `charts/open_share_spaghetti.png` (+ `.svg`)
- Drafts under `draft/`

## Methodology (short)

1. Filter Vercel models export to `metric=tokens`, `modality=text`.
2. Classify each model name → `open` | `closed` | `other` (`src/classify.py`).
3. `open_share_classified_pct = open_known / (open_known + closed_known) * 100`.
4. Also report `open_known` as % of **all** tokens (including Other).
5. Weekly = mean of daily values over ISO weeks.

Full write-up: `research/claims.md`. Sources: `research/sources.md`.

## Data gaps (honest)

| Source | Status |
|--------|--------|
| **Vercel** | Working end-to-end |
| **OpenRouter** | Daily top-50 API exists but **requires API key** — stub + steps only unless `OPENROUTER_API_KEY` is set |
| **Hugging Face** | No comparable global inference-token open-share series found — documented, not invented |

## License & attribution

- **Code** in this repository: MIT (unless noted).
- **Vercel AI Gateway Leaderboard Data:** © 2026 Vercel, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution required on reuse.
- **OpenRouter rankings data** (if/when downloaded): CC BY 4.0 — cite `Source: OpenRouter (openrouter.ai/rankings), as of {as_of}.`

## Repo layout

```
data/raw/          # Vercel CSVs (and OpenRouter JSON if keyed)
data/processed/    # Daily/weekly open-share tables
data/stubs/        # Honest placeholders for missing sources
src/               # Download / classify / chart scripts
charts/            # open_share_spaghetti.png|.svg
research/          # claims.md, sources.md
draft/             # article.md, x-post.md, hooks.md
```
