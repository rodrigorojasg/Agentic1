import yaml
from pathlib import Path

class DummyModel:
    def __init__(self, responses_file="dummy_responses/responses.yaml"):
        self.responses = self._load_responses(responses_file)

    def _load_responses(self, path):
        with open(Path(path), "r") as f:
            return yaml.safe_load(f)

    def generate(self, agent_name: str, action: str, variables: dict):
        agent_responses = self.responses.get(agent_name, {})
        response = agent_responses.get(action)

        if not response:
            raise ValueError(
                f"No dummy response for agent='{agent_name}', action='{action}'"
            )

        return response
