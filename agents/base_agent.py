from abc import ABC, abstractmethod

class BaseAgent(ABC):

    def __init__(self, model, prompt_version: str):
        self.model = model
        self.prompt_version = prompt_version

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
