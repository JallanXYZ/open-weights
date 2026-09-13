# Claims & methodology

## Headline claim (this build)

**On Vercel AI Gateway text-token traffic, the latest complete ISO week (2026-W37: 2026-09-07 → 2026-09-13) averaged ~70.7% open-weight among models we could classify as open or closed** (`open_share_classified_pct`).

- Same week, open models were **~49.4% of all tokens** including the Vercel `Other` long-tail (`open_share_of_total_pct`).
- Same week, `Other` averaged **~33.8%** of tokens.
- Latest single day in the export (2026-09-13): **~87.1%** open among classified; **~75.9%** of all tokens; `Other` **~12.9%**.

These are **live computed** figures from the CSVs — not hardcoded constants. Re-run `src/process_vercel.py` after `src/download_vercel.py` to refresh.

## What we measure

1. Filter `vercel_models_text.csv` to `metric=tokens`, `modality=text`.
2. Classify each **named** model as `open`, `closed`, or `other` (see below). Vercel’s aggregate row named `Other` is always `other`.
3. Daily:
   - `open_known`, `closed_known`, `other_share` = sum of `share_percent` in each bucket (shares already sum to ~100% per day).
   - `open_share_classified_pct = open_known / (open_known + closed_known) * 100`
   - `open_share_of_total_pct = open_known` (percent of all gateway text tokens that day).
4. Weekly: arithmetic mean of daily values over ISO weeks (Mon–Sun). Partial first week (W29) has 5 days.

## Classification rules (models)

**Open** (weights published for download / open-weight lines): DeepSeek, Qwen, Llama, Mistral family, Gemma, Kimi, GLM, Step, Command R (when open), MiniMax, Nemotron, MiMo, Hunyuan/Hy*, GPT-OSS, etc. (pattern list in `src/classify.py`).

**Closed** (proprietary API-first): Claude, GPT-n / OpenAI o-series, Gemini (Google proprietary), Muse Spark (Meta proprietary — **not** Llama), Grok, Nova, etc.

**Other / unclassified:**
- Vercel’s `Other` long-tail bucket (cannot silently assign).
- Any named model that does not match open/closed patterns — tracked separately as `other_share`, never forced into open or closed.

Audit table: `data/processed/vercel_model_classification_audit.csv`.

### Notable call: Muse Spark 1.3 Contributor → closed

Public materials describe Muse Spark as Meta’s proprietary / closed-weights line (distinct from Llama). Classified **closed**, not open.

## Labs series (secondary)

`vercel_labs_*` files support a lab-level open/closed map (`data/processed/vercel_labs_open_share_*.csv`). Caveat: labs that ship **both** open and closed lines (e.g. Meta: Llama open + Muse closed) blur lab-level shares. **Headline chart uses model-level classification.**

## What we do **not** claim

- This is **not** “share of all AI inference on Earth.” It is share of **observable** traffic on Vercel AI Gateway (and, if keyed, OpenRouter).
- We do **not** hardcode “73.3%” or any other marketing figure.
- We do **not** invent an OpenRouter or Hugging Face open-share time series when data is missing.
- Token counts across providers are not perfectly comparable (esp. OpenRouter’s provider-native tokenizers).

## OpenRouter / Hugging Face status

| Source        | Daily open-share series?                         | Status in repo                          |
|---------------|--------------------------------------------------|-----------------------------------------|
| Vercel        | Yes (shares, not absolute tokens)                | Processed + charted                     |
| OpenRouter    | Yes via API, **API key required**                | Stub + retrieval steps; no key at build |
| Hugging Face  | No comparable global inference-token % found     | Documented gap only                     |

## Reproducibility

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/download_vercel.py
python src/process_vercel.py
python src/download_openrouter.py   # stub without key
python src/download_huggingface.py  # documents gap
python src/build_chart.py
```
