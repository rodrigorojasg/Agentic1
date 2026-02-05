from llm.resolver import get_llm_for_agent
from .base import Agent

class TestAgent(Agent):
    name = "test"

    def run(self, input_text: str) -> str:
        llm = get_llm_for_agent(self.name)
        return llm.generate(f"Generate tests for: {input_text}")
