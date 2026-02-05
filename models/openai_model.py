import os
from openai import OpenAI
from models.base import LLMModel

class OpenAILLM(LLMProvider):

    def __init__(self, model: str | None = None):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY no configurada")

        self.client = OpenAI(api_key=api_key)
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    def generate(self, prompt: str) -> str:
        res = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a senior software engineer."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
        return res.choices[0].message.content.strip()
