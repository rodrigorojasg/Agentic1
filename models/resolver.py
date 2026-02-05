import os
from .factory import get_llm

def get_llm_for_agent(agent_name: str):
    prefix = f"AGENT_{agent_name.upper()}"

    provider = os.getenv(f"{prefix}_PROVIDER", "dummy")
    model = os.getenv(f"{prefix}_MODEL")

    return get_llm(provider, model)
