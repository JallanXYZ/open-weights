# Sources

## Primary: Vercel AI Gateway Leaderboards

- **What:** Daily percentage share of AI Gateway traffic by model and by lab, for requests / tokens / spend (text modality used here).
- **Export:** `GET https://vercel.com/api/ai/leaderboard-export?dataset=models|labs&modality=text&format=csv`
- **Docs:** https://vercel.com/docs/ai-gateway/leaderboards
- **UI:** https://vercel.com/ai-gateway/leaderboards/models
- **License / attribution:** © 2026 Vercel. "AI Gateway Leaderboard Data" is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Local files:** `data/raw/vercel_models_text.csv`, `data/raw/vercel_labs_text.csv`
- **Coverage in this build:** 2026-07-15 → 2026-09-13 (rolling export window at build time).

## OpenRouter (attempted; key-gated)

- **Rankings UI (public):** https://openrouter.ai/rankings — usage through Sep 12, 2026 at fetch time; CC BY 4.0.
- **Machine-readable daily top-50 tokens:** `GET https://openrouter.ai/api/v1/datasets/rankings-daily` — **requires** `Authorization: Bearer $OPENROUTER_API_KEY`.
- **Docs:** https://openrouter.ai/docs/api/api-reference/datasets/daily-token-totals-for-top-50-models
- **Cookbook:** https://openrouter.ai/docs/cookbook/administration/data-api
- **Status in this repo:** No key → stub only (`data/stubs/openrouter_rankings_daily.STUB.md`). Script ready: `src/download_openrouter.py`.
- **Tokenizer caveat:** totals are provider-native `prompt_tokens + completion_tokens`; not strictly comparable across labs.

### Informal public snapshot (not a downloadable daily series)

From the public rankings page (weekly window ending ~2026-09-12), top models by tokens included Hy4 preview (Tencent), GPT-5.6 Luna (OpenAI), GLM 5.3 Flash (Z.ai), DeepSeek V4 Flash variants, MiMo-V2.5 (Xiaomi), Nemotron 3 Ultra (NVIDIA). This is a **point-in-time UI snapshot**, not used for the chart series.

## Hugging Face

- **Finding:** No comparable global **% of inference tokens** open-vs-closed series located.
- Stub: `data/stubs/huggingface_inference_share.STUB.md`
- Optional proxies (downloads, Spaces) are **not** inference-token share — do not substitute.

## Secondary commentary (context only, not series inputs)

- Vercel AI Gateway Production Index (July 2026): https://vercel.com/blog/ai-gateway-production-index-july-2026
- Guillermo Rauch LinkedIn note on open-weight token share record day (2026-08-22): cited for qualitative context; our Aug 22 **classified** open share computes to ~62.6%, consistent with a 62/38 open/closed framing among classified traffic.
