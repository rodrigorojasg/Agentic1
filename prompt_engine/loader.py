from pathlib import Path

def load_prompt(agent: str, version: str) -> str:
    path = Path("prompts") / agent / f"{version}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Prompt not found: {path}")
    return path.read_text()
