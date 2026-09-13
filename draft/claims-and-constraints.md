# OPEN WEIGHTS — claims and constraints
As of: 2026-09-13 (UTC). Classifier: `src/classify.py` on live Vercel text export.

## Locked don'ts
- Do not invent a Hugging Face token-share series.
- Navier–Stokes: OpenAI says Buckmaster Codex prompts did not influence the result (site update 10 Sep 2026). Make the *fear/uncertainty* the point, not “busted for IP.”
- Do not assert an SEC quiet period. Anthropic confidential draft S-1 announced 1 Jun 2026; OpenAI confidential S-1 announced 8 Jun 2026. Neither has a public prospectus or listing date. Use “run-up to a possible listing.”
- “Steering wheel” / “Faustian bargain” are our framing, not official quotes.
- Do not imply NVIDIA chips have a kill switch. NVIDIA says they do not and should not. House Chip Security Act ANS text tells Commerce not to require one. Hardware control = export, KYC, power, fabs — not a remote brick.
- Karp “means of production” / alpha: CNBC 1 Jun 2026. Ontology line is Diginomica/secondary — don’t quote it as CNBC.
- Do not assert that labs train on enterprise API inputs unless a primary source says so.
- Vercel figures are live. Do not hardcode 73.3%. That print was ~12 Sep. 13 Sep open-token share is 75.87%.
- OpenRouter daily top-50 + `other` bucket needs an API key. Until then, do not fake the series. Cite the stub.
- Chart spec (MajorDomo / repo): weekly averages, phone-friendly spaghetti, lines labeled at endpoints, transparent Other bucket.
- Source of truth: https://github.com/JallanXYZ/open-weights
- Optimise for reposts, not ragebait. No live post without James/MajorDomo go.

## Verified numbers (Vercel AI Gateway, modality=text, 13 Sep 2026)
Source: https://vercel.com/api/ai/leaderboard-export?dataset=models&modality=text&format=csv
License: © 2026 Vercel. "AI Gateway Leaderboard Data" CC BY 4.0.

Classification is model-name pattern match (`src/classify.py`). Vercel’s own “Other” row is kept in **other**. Unrecognised named models also go to **other**. Shares sum to 100.

| Metric   | Open | Closed | Other |
|----------|------|--------|-------|
| Tokens   | 75.87 | 11.22 | 12.91 |
| Requests | 37.19 | 22.34 | 40.48 |
| Spend    |  8.97 | 59.90 | 31.13 |

Weekly averages (ISO week, same classifier):

| Week     | Tokens open | Tokens closed | Tokens other |
|----------|-------------|---------------|--------------|
| 2026-W36 | 24.85 | 17.11 | 58.04 |
| 2026-W37 | 49.38 | 16.78 | 33.84 |

Named token leaders on 13 Sep 2026 (raw Vercel rows, not re-aggregated):
- DeepSeek V4.1 Flash 65.086
- Other 12.908
- GPT 5.6 Luna 4.226
- GLM 5.3 Flash 3.311
- DeepSeek V4 Flash 0731 3.272
- Step 3.7 Flash 2.907
- Muse Spark 1.3 Contributor 2.271 (classified **closed**)
- Gemini 3.8 Flash 2.049
- Claude Opus 4.8 1.671
- Kimi K3 1.292
- Claude Opus 5 1.007

Daily open-token share (last 5 days): 09-09 23.76 → 09-10 53.19 → 09-11 67.24 → 09-12 73.60 → 09-13 75.87.

## Scope caveats (must stay in the piece)
- This is Vercel AI Gateway production share, not global inference.
- Vercel publishes percentages, not absolute token counts.
- One named model (DeepSeek V4.1 Flash) dominates the latest print. The “open won” headline is mostly that line leaving the Other bucket and taking volume.
- Lab-level classification is imperfect (Meta ships Llama and Muse). Model-level is what the chart uses.

## Navier–Stokes — what we can say
Primary:
- OpenAI, 8 Sep 2026, updated 10 Sep: https://openai.com/index/navier-stokes-solution/
- Buckmaster statement: https://cims.nyu.edu/~tristanb/statement.pdf

Say:
- OpenAI launched agents on 1 Sep after rumors later tied to Alpöge/Buckmaster; resolution ~88 hours later; Lean via GPT-6 Astra.
- 10 Sep update: “Buckmaster’s Codex prompts over the two months preceding this announcement … could not have influenced the system in any way, including through training.”
- Buckmaster: he has not seen their proof; he does not know whether their data was used; he is “not accusing anyone”; he is stating what he was told, when, and what was proposed.
- That gap — rumor, then a sprint, then a denial — is the story. Not theft. Not “busted.”

Do not say:
- OpenAI trained on Buckmaster’s Codex.
- OpenAI stole the proof.
- They are in an SEC quiet period / September IPO.

## OpenRouter
Machine-readable daily top-50 + `other` requires `OPENROUTER_API_KEY`. Page: https://openrouter.ai/rankings (CC BY 4.0). Cite as: `Source: OpenRouter (openrouter.ai/rankings), as of {as_of}.` Tokenizer caveat: provider-native tokenizers, not comparable across labs.
