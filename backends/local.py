from typing import List, Dict
import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

class LocalBackend:
    def __init__(self, model_id: str, gen_kwargs: Dict, dtype: str = "float16"):
        self.model_id = model_id
        self.gen_kwargs = gen_kwargs
        self.dtype = dtype
        self.tok = None
        self.mdl = None
        self._load()

    def _device_map(self):
        if torch.cuda.is_available(): return "auto"
        if torch.backends.mps.is_available(): return {"": "mps"}
        return {"": "cpu"}

    def _load(self):
        with tqdm(total=1, desc="Load", unit="step"):
            self.tok = AutoTokenizer.from_pretrained(self.model_id, use_fast=True, trust_remote_code=True)
            self.mdl = AutoModelForCausalLM.from_pretrained(
                self.model_id,
                torch_dtype=getattr(torch, self.dtype),
                device_map=self._device_map(),
                trust_remote_code=True,
            )
            if self.tok.pad_token_id is None:
                self.tok.pad_token = self.tok.eos_token

    def _prompt(self, messages: List[Dict[str, str]]) -> str:
        if getattr(self.tok, "chat_template", None):
            return self.tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        parts = []
        for m in messages:
            r, c = m["role"], m["content"]
            if r == "system": parts.append(f"System: {c}")
            elif r == "user": parts.append(f"User: {c}")
            elif r == "assistant": parts.append(f"Assistant: {c}")
        parts.append("Assistant:")
        return "\n".join(parts)

    @torch.inference_mode()
    def generate(self, messages: List[Dict[str, str]]) -> str:
        prompt = self._prompt(messages)
        inputs = self.tok(prompt, return_tensors="pt").to(self.mdl.device)
        out = self.mdl.generate(**inputs, generation_config=GenerationConfig(**self.gen_kwargs))
        text = self.tok.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True).strip()
        return text or "출력을 생성하지 못했습니다."