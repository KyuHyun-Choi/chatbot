# config.py
MODEL_REGISTRY = {
    # ── Meta ───────────────────────────────
    "llama3-8b":        "meta-llama/Meta-Llama-3-8B-Instruct",
    "llama3-70b":       "meta-llama/Meta-Llama-3-70B-Instruct",
    "llama2-7b":        "meta-llama/Llama-2-7b-chat-hf",
    "llama2-13b":       "meta-llama/Llama-2-13b-chat-hf",
    "llama2-70b":       "meta-llama/Llama-2-70b-chat-hf",

    # ── Mistral & Mixtral ──────────────────
    "mistral-7b":       "mistralai/Mistral-7B-Instruct-v0.2",
    "mixtral-8x7b":     "mistralai/Mixtral-8x7B-Instruct-v0.1",

    # ── Google ─────────────────────────────
    "gemma-2b":         "google/gemma-2b-it",
    "gemma-7b":         "google/gemma-7b-it",
    "gemma2-9b":        "google/gemma-2-9b-it",
    "gemma2-27b":       "google/gemma-2-27b-it",

    # ── 01.AI ──────────────────────────────
    "yi-6b":            "01-ai/Yi-6B-Chat",
    "yi-34b":           "01-ai/Yi-34B-Chat",

    # ── Microsoft ──────────────────────────
    "phi-2":            "microsoft/phi-2",
    "phi-3-mini":       "microsoft/phi-3-mini-4k-instruct",
    "phi-3-small":      "microsoft/phi-3-small-8k-instruct",
    "phi-3-medium":     "microsoft/phi-3-medium-4k-instruct",

    # ── Qwen ───────────────────────────────
    "qwen1.5-7b":       "Qwen/Qwen1.5-7B-Chat",
    "qwen1.5-14b":      "Qwen/Qwen1.5-14B-Chat",
    "qwen2-1.5b":       "Qwen/Qwen2-1.5B-Instruct",
    "qwen2-7b":         "Qwen/Qwen2-7B-Instruct",
    "qwen2-72b":        "Qwen/Qwen2-72B-Instruct",

    # ── DeepSeek ───────────────────────────
    "deepseek-7b":      "deepseek-ai/deepseek-llm-7b-chat",
    "deepseek-moe":     "deepseek-ai/deepseek-moe-16b-instruct",

    # ── Falcon ─────────────────────────────
    "falcon-7b":        "tiiuae/falcon-7b-instruct",
    "falcon-40b":       "tiiuae/falcon-40b-instruct",

    # ── Baichuan ───────────────────────────
    "baichuan2-7b":     "baichuan-inc/Baichuan2-7B-Chat",
    "baichuan2-13b":    "baichuan-inc/Baichuan2-13B-Chat",

    # ── Vicuna ─────────────────────────────
    "vicuna-7b":        "lmsys/vicuna-7b-v1.5",
    "vicuna-13b":       "lmsys/vicuna-13b-v1.5",

    # ── WizardLM ───────────────────────────
    "wizardlm-13b":     "WizardLM/WizardLM-13B-V1.2",
    "wizardlm-70b":     "WizardLM/WizardLM-70B-V1.0",

    # ── Nous Hermes ────────────────────────
    "nous-hermes-13b":  "NousResearch/Nous-Hermes-13b",
    "nous-hermes-llama2-70b": "NousResearch/Nous-Hermes-llama-2-70b",

    # ── Orca ───────────────────────────────
    "orca-2-7b":        "microsoft/Orca-2-7b",
    "orca-2-13b":       "microsoft/Orca-2-13b",

    # ── Zephyr ─────────────────────────────
    "zephyr-7b":        "HuggingFaceH4/zephyr-7b-beta",

    # ── GPT-NeoX & GPT-J ───────────────────
    "gpt-j-6b":         "EleutherAI/gpt-j-6B",
    "gpt-neox-20b":     "EleutherAI/gpt-neox-20b",

    # ── GPT2 (baseline) ────────────────────
    "gpt2":             "gpt2",

    # ── OpenAI API ─────────────────────────
    "gpt-4":            "gpt-4",
    "gpt-4o":           "gpt-4o",
    "gpt-5":            "gpt-5",
}

ALIASES = {
    "gpt5": "gpt-5",
    "chatgpt": "gpt-5",
}

SYSTEM_PROMPT = "You must answer politely."

GEN_KWARGS = dict(
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    do_sample=True,
)

DTYPE = "float16"
