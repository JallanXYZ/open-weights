# OPEN WEIGHTS
Locked rewrite — 13 Sep 2026 UTC / 14 Sep Brisbane. Not live.
Chart: `charts/open_share_spaghetti.png` (do not rebuild unless the CSVs drift).
Figures: `BUILD_REPORT.md` + `data/processed/vercel_open_share_*.csv`.
Repo: https://github.com/JallanXYZ/open-weights

---

Dario Amodei published *We Must Pace the Frontier* on Saturday. He wants embedded evaluators inside the labs, democratic coordination, and a slower climb so safety work can keep up. He is allowed to make that case. Training still looks oligopolistic. **Serving does not.**

He is also making it in the run-up to possible public listings. Anthropic confidentially submitted a draft S-1 on 1 June; OpenAI announced theirs on 8 June. Neither has posted a public prospectus or a date. That is not a quiet-period claim. It is the weather.

The question this piece answers is narrower, and checkable: **is open-weight share rising across independent, observable inference datasets?**

On the one public daily series we can rebuild without a key, yes.

## The chart

![Open share spaghetti](../charts/open_share_spaghetti.png)

**Source:** Vercel AI Gateway Leaderboard Data, text tokens, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Method: `research/claims.md`. We do not invent a Hugging Face token-share series. OpenRouter’s daily top-50 + `other` bucket needs an API key — stubbed, not faked.

Latest ISO week, 2026-W37 (7–13 Sep):

| | |
|---|---:|
| Open among classified (`open / (open+closed)`) | **70.72%** |
| Open as % of all text tokens (Other left in) | **49.38%** |
| Other / unclassified long-tail | **33.84%** |

The last *day* in the export (13 Sep) is hotter: **75.87%** of all text tokens, **87.11%** among classified; closed **11.22%**, Other **12.91%**. DeepSeek V4.1 Flash alone is **65.09%** that day. Weekly averages are the headline. Single days spike.

Two months back, open-as-%-of-all sat near **10–12%** and Other was ~75%. The Other line falling is part of the story: a named open Flash model left the long tail and took the volume.

Same gateway, same day, **spend** ran the other way: closed **59.90%**, open **8.97%**, Other **31.13%**. Volume went open. The invoice did not.

This is one router, text only, percentages not absolute counts. Enterprise VPCs and apps that never hit a public gateway are invisible. If your take quotes only the 70.7 or only the 75.9, you are spinning.

## Intelligence got cheap. The pie got bigger.

“Open taking share” is the wrong picture if you imagine a fixed pie. Inference demand is the exploding denominator — more agents, more tools, more cheap tokens per task. We cannot print Vercel’s absolute token counts; they do not publish them. What we *can* say: on the observable slice, open-weight lines are taking a larger *share* of a traffic mix the rest of the industry is openly describing as growing. Share of a growing denominator is how a commodity wins.

When two models are good enough, the alpha leaves the checkpoint.

## Karp, not the model card

Alex Karp’s line this summer (CNBC *Squawk Box*, 1 July) is the enterprise version of that sentence. Customers who rent frontier tokens, he said, want “control over their compute, their models, their data stack and their alpha” — they want to “own the means of production.” Cognition is becoming a commodity. The moat is the application layer, not the checkpoint.

We are not claiming labs train on enterprise API inputs. Nobody in the primary sources used here said that. The claim is smaller and worse for the pure-model story: once the middle of the distribution is “good enough and downloadable,” enterprises will pay for **harness, rights, and failover**, not for a logo on a checkpoint.

## The other spaghetti

OpenAI’s Navier–Stokes write-up (8 Sep; “Concurrent work” updated 10 Sep) is a vortex that “spirals inward and gets increasingly elongated, like spaghetti.”

They say they launched agents on 1 Sep after rumors they later tied to Levent Alpöge and Tristan Buckmaster. About 88 hours later, a resolution; Lean took another 17 hours. They say they will not claim the Millennium Prize.

On 10 Sep they added: Buckmaster’s Codex prompts over the prior two months “could not have influenced the system in any way, including through training.”

Buckmaster’s statement is careful in the other direction. He has not seen their proof. He does not know whether their data was used. He is “not accusing anyone of anything.” He is writing down what he was told, when, and what was proposed, because the alternative was to let the announcements say something he believes is false.

That gap is the point. Not “busted for IP.” The question now exists in public. Fear and uncertainty are the product, even when the official answer is no.

## The steering wheel is a Faustian bargain

Washington does not need a holy war over GitHub. Both parties already want a steering wheel: provenance, evals, export controls, something they can defend at a town hall.

Dario’s own open-weights note (27 July) is the bargain in one page. He does **not** want a ban on open weights. He wants chips kept out of authoritarian hands, industrial-scale distillation cracked down, and mandatory testing of *sufficiently capable* models, open or closed. Open weights without dangerous capabilities he calls a public good. Once the weights are out, he says, you cannot pull them back.

The Faustian part: the steering wheel the democracies can actually hold is **compute and clusters**, not LICENSE files. You can pace the labs you can see. Meanwhile Chinese open-weight lines (DeepSeek, Qwen, GLM, Kimi, Step) are already a named share of *Western* gateway logs. A policy that only sermons at closed US labs is holding a wheel that is not attached to the axle.

Bipartisan rails that could land:

- Provenance and disclosure for large training runs and high-risk fine-tunes.
- KYC for frontier-class inference clusters above power / FLOP thresholds.
- Liability on *uses* (money, medicine, kids) — independent of whether weights are downloadable.
- Chip and fab controls, not star-counts on GitHub.

## China is not a vibe

DeepSeek V4.1 Flash printing 65% of one day’s Vercel text tokens is not a think-piece. Open-enough Chinese labs learned that shipping weights and cheap APIs buys distribution that branding wars do not fully block.

That is not “China wins AI.” It is: US strategy that treats closed APIs as durable lock-in is incomplete. Energy, fabs, talent, and standards matter more when the model layer commoditises.

## Capex and credit, if tokens stay cheap

If the fat middle of inference is ubiquitous and cheap, model-API gross margins compress. The cash still has to live somewhere. It lives in **chips, power, interconnect, and the credit that builds data centres**, plus the workflow software that makes model-swapping dull.

Investors who only underwrite “one model to rule them all” are underwriting a 2023 story with 2026 traffic. The blended stack (closed for the hard tail, open for the middle) is already how cost-sensitive systems ship.

## Control lives on hardware, not in a LICENSE file

Dario told CBS a kill switch “could be a good idea.” NVIDIA’s public line is the opposite: no backdoors, no kill switches, no spyware. Proposed Chip Security Act text (House ANS to H.R. 3447) even tells Commerce *not* to require a kill switch or geofence. So do not hear “hardware control” as “remote-brick every GPU.”

Once weights and a stack of accelerators exist outside a lab VPC, a LICENSE file cannot brick every copy. The levers that actually exist sit next to **electrons and wafers**: chip export and smuggling enforcement, cluster KYC, attestation, power and fab chokepoints. Argue about those honestly. Do not cosplay it as a weights-only debate.

## What to do with this

- **Builders:** Model-agnostic harness. Evals. Assume next month’s open Flash is cheaper and good enough for half your traffic.
- **Labs:** If secrecy of weights is the product, the roadmap is a prayer. Compete on reliability, tools, and taste.
- **Policymakers:** Regulate high-risk *uses* and *compute*. Measure open diffusion with public series. Stop treating “open” as sacrament or heresy.
- **Everyone else:** Refresh the chart. Yesterday’s round number expires.

Data and code: [github.com/JallanXYZ/open-weights](https://github.com/JallanXYZ/open-weights). Primary series: Vercel AI Gateway (CC BY 4.0). OpenRouter daily tokens: not included pending API key. Hugging Face: no comparable global inference-token series — we did not invent one.

<!-- citation-pass 2026-09-13 -->
