# Hugging Face — no global inference-token open-share series

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
