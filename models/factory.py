import os
from models.openai_model import OpenAIModel
from models.dummy_model import DummyModel
# from models.gemini_model import GeminiModel

class ModelFactory:

    @staticmethod
    def create(agent_name: str):
        """
        Permite configurar proveedores por agente:
        CODE_AGENT_PROVIDER=openai
        TEST_AGENT_PROVIDER=dummy
        """

        provider = os.getenv(
            f"{agent_name.upper()}_PROVIDER",
            os.getenv("LLM_PROVIDER", "dummy")
        )

        if provider == "openai":
            return OpenAIModel()

        if provider == "dummy":
            return DummyModel()

        # if provider == "gemini":
        #     return GeminiModel()

        raise ValueError(f"Unsupported provider: {provider}")
