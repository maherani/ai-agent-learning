from app.agents.state import AgentState
from app.llm.interface import LLM
from app.tools.registry import ToolRegistry


class Agent:
    def __init__(self, llm: LLM, tools: ToolRegistry):
        self.llm = llm
        self.tools = tools

    def run(self, prompt: str) -> str:
        state = AgentState()
        state.messages.append(f"User: {prompt}")

        while True:
            current_prompt = "\n".join(state.messages)

            response = self.llm.generate(current_prompt)

            if response.tool_call is None:
                state.messages.append(
                    f"Assistant: {response.text or ''}"
                )
                return response.text or ""

            tool_call = response.tool_call

            state.messages.append(
                f"Tool Call: {tool_call.tool_name} {tool_call.arguments}"
            )

            tool_result = self.tools.execute(
                tool_call.tool_name,
                tool_call.arguments,
            )

            state.messages.append(
                f"Tool Result: {tool_result}"
            )
