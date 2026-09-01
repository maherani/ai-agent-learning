from app.agents.messages import Message
from app.agents.state import AgentState
from app.llm.interface import LLM
from app.tools.registry import ToolRegistry
from app.agents.roles import MessageRole

class Agent:
    def __init__(self, llm: LLM, tools: ToolRegistry):
        self.llm = llm
        self.tools = tools

    def run(self, prompt: str) -> str:
        state = AgentState()

        state.messages.append(
            Message(
                role=MessageRole.USER,
                content=prompt,
            )
        )

        while True:
            current_prompt = "\n".join(
                f"{message.role.value}: {message.content}"
                for message in state.messages
            )

            response = self.llm.generate(current_prompt)

            if response.tool_call is None:
                state.messages.append(
                    Message(
                        role=MessageRole.ASSISTANT,
                        content=response.text or "",
                    )
                )
                return response.text or ""

            tool_call = response.tool_call

            state.messages.append(
                Message(
                    role=MessageRole.ASSISTANT,
                    content="Requesting tool execution",
                    metadata={
                        "tool_name": tool_call.tool_name,
                        "arguments": tool_call.arguments,
                    },
                )
            )

            tool_result = self.tools.execute(
                tool_call.tool_name,
                tool_call.arguments,
            )

            state.messages.append(
                Message(
                    role=MessageRole.TOOL,
                    content=str(tool_result),
                    metadata={
                        "tool_name": tool_call.tool_name,
                    },
                )
            )
