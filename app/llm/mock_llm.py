from app.llm.interface import LLM


class MockLLM(LLM):
    def generate(self, prompt: str) -> str:
        return f"Mock response to: {prompt}"
