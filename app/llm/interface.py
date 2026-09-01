from abc import ABC, abstractmethod

from app.llm.response import LLMResponse


class LLM(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> LLMResponse:
        pass
