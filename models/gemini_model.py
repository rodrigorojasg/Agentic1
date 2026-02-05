import os
import google.generativeai as genai
from models.base import LLMModel

class GeminiLLM(LLMProvider):

    def __init__(self, model: str | None = None):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY no configurada")

        genai.configure(api_key=api_key)
        self.model = model or os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        self.client = genai.GenerativeModel(self.model)

    def generate(self, prompt: str) -> str:
        res = self.client.generate_content(prompt)
        return res.text.strip()
