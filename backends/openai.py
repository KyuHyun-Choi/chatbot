from typing import List, Dict, Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

class OpenAIBackend:
    def __init__(self, model_id: str, max_tokens: int = 2048, api_key: Optional[str] = None):
        if OpenAI is None:
            raise RuntimeError("OpenAI SDK not installed. Run: pip install openai")
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()
        self.model_id = model_id
        self.max_tokens = max_tokens

    def generate(self, messages: List[Dict[str, str]]) -> str:
        resp = self.client.chat.completions.create(
            model=self.model_id,
            messages=messages,
            max_completion_tokens=self.max_tokens,
        )
        text = (resp.choices[0].message.content or "").strip()
        return text or "출력을 생성하지 못했습니다."
