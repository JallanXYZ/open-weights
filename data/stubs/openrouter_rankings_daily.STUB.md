# OpenRouter rankings-daily — STUB

No API key available in this environment. Daily top-50 token totals are **not**
downloadable without authentication.

## Exact retrieval steps

1. Create an OpenRouter account and API key (same key used for inference).
2. Export:

```bash
export OPENROUTER_API_KEY=sk-or-...
curl -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  "https://openrouter.ai/api/v1/datasets/rankings-daily?start_date=2026-08-01&end_date=2026-09-12" \
  -o data/raw/openrouter_rankings_daily.json
```

3. Re-run: `python src/download_openrouter.py`

## Citation

Source: OpenRouter (openrouter.ai/rankings). Rankings data licensed CC BY 4.0.
When republishing: `Source: OpenRouter (openrouter.ai/rankings), as of {as_of}.`

## Tokenizer caveat

Token counts are `prompt_tokens + completion_tokens` as reported by each
upstream provider's tokenizer. Cross-provider totals are not apples-to-apples.
