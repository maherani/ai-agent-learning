from app.llm.interface import LLM
from app.llm.response import LLMResponse
from app.tools.models import ToolCall


class MockLLM(LLM):
    def generate(self, prompt: str) -> LLMResponse:
        if (
            "CALCULATE 25 * 18" in prompt
            and "tool: 450" not in prompt
        ):
            return LLMResponse(
                tool_call=ToolCall(
                    tool_name="multiply",
                    arguments={"a": 25, "b": 18},
                )
            )

        if "tool: 450" in prompt:
            return LLMResponse(
                text="25 multiplied by 18 equals 450."
            )

        return LLMResponse(
            text=f"Mock response to: {prompt}"
        )
