from agents.base_agent import BaseAgent
from utils.prompt_loader import load_prompt, render_prompt

class CodeAgent(BaseAgent):

    name = "code_agent"

    def run(self, stack: str, user_story: str):
        variables = {
            "stack": stack,
            "user_story": user_story
        }

        # Caso dummy (salida estructurada)
        if hasattr(self.model, "generate_structured"):
            return self.model.generate_structured(
                agent_name=self.name,
                action="generate_code",
                variables=variables
            )

        # Caso LLM real
        template = load_prompt("code", self.prompt_version)
        prompt = render_prompt(template, variables)

        text = self.model.generate(prompt)

        # Normalizamos salida
        return [{
            "path": "output.txt",
            "content": text
        }]
