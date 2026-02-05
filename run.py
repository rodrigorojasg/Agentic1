# run.py
import os
import sys
from agents.orchestration_agent import OrchestrationAgent

def run():
    stack = sys.argv[1]
    user_story = sys.argv[2]

    orchestrator = OrchestrationAgent()
    files = orchestrator.run(stack, user_story)

    for f in files:
        os.makedirs(os.path.dirname(f["path"]) or ".", exist_ok=True)
        with open(f["path"], "w") as file:
            file.write(f["content"])

        print(f["path"])

if __name__ == "__main__":
    run()
