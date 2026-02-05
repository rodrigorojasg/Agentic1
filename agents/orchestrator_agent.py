import os
# agents/orchestration_agent.py
from agents.code_agent import CodeAgent
from models.factory import ModelFactory

class OrchestrationAgent:
    def __init__(self):
        self.code_agent = CodeAgent(
            ModelFactory.create("code_agent")
        )

    def run(self, stack, user_story):
        files = self.code_agent.run(stack, user_story)
        return files
