"""Open / closed / other classification for model names and labs.

Rules of thumb (documented in research/claims.md):
- open: weights published for download (DeepSeek, Qwen, Llama, Mistral, Gemma,
  Kimi, GLM, Step, Command R when open, etc.)
- closed: proprietary API-only frontier lines (Claude, GPT/OpenAI, Gemini,
  Muse Spark, etc.)
- other: Vercel aggregate "Other" bucket, or any name we cannot confidently classify
"""

from __future__ import annotations

import re
from typing import Literal

ClassLabel = Literal["open", "closed", "other"]

OPEN_MODEL_PATTERNS = [
    r"(?i)^deepseek",
    r"(?i)^qwen",
    r"(?i)^llama",
    r"(?i)^mistral",
    r"(?i)^mixtral",
    r"(?i)^ministral",
    r"(?i)^codestral",
    r"(?i)^devstral",
    r"(?i)^magistral",
    r"(?i)^gemma",
    r"(?i)^kimi",
    r"(?i)^glm",
    r"(?i)^step",
    r"(?i)^command[- ]?r",
    r"(?i)^yi\b",
    r"(?i)^phi[- ]?\d",
    r"(?i)^nemotron",
    r"(?i)^olmo",
    r"(?i)^smol",
    r"(?i)^gpt-oss",
    r"(?i)^gpt oss",
    r"(?i)^dbrx",
    r"(?i)^jamba",
    r"(?i)^falcon",
    r"(?i)^mimo",
    r"(?i)^hunyuan",
    r"(?i)^minimax",
    r"(?i)^hy\d",  # Tencent Hunyuan / Hy* open lines when named that way
    r"(?i)^seed[- ]?\d",
]

CLOSED_MODEL_PATTERNS = [
    r"(?i)^claude",
    r"(?i)^gpt[- ]?\d",
    r"(?i)^o[1-9]\b",
    r"(?i)^chatgpt",
    r"(?i)^gemini",
    r"(?i)^grok",
    r"(?i)^amazon nova",
    r"(?i)^nova\b",
    r"(?i)^sonar",
    r"(?i)^muse\b",  # Meta Muse Spark: proprietary, not Llama
    r"(?i)^palm",
    r"(?i)^cohere",
]

# Lab-level map (imperfect when a lab ships both open and closed lines).
OPEN_LABS = {
    "deepseek",
    "zai",
    "stepfun",
    "meta",  # caveat: Muse is closed; Llama open — see claims.md
    "moonshotai",
    "xiaomi",
    "inclusionai",
    "minimax",
    "alibaba",
    "mistral",
    "tencent",
    "nvidia",
    "arcee-ai",
    "bytedance",
    "sakana",
    "kwaipilot",
}

CLOSED_LABS = {
    "openai",
    "anthropic",
    "google",
    "amazon",
    "cohere",
    "perplexity",
    "poolside",
    "thinkingmachines",
    "interfaze",
    "inception",
    "morph",
}


def classify_model(name: str) -> ClassLabel:
    n = (name or "").strip()
    if not n or n.lower() == "other":
        return "other"
    for pat in OPEN_MODEL_PATTERNS:
        if re.search(pat, n):
            return "open"
    for pat in CLOSED_MODEL_PATTERNS:
        if re.search(pat, n):
            return "closed"
    return "other"


def classify_lab(name: str) -> ClassLabel:
    n = (name or "").strip().lower()
    if n in OPEN_LABS:
        return "open"
    if n in CLOSED_LABS:
        return "closed"
    return "other"
