from app.agents.agent import Agent
from app.llm.mock_llm import MockLLM
from app.tools.calculator import add, multiply
from app.tools.registry import ToolRegistry


def test_agent_executes_tool_and_returns_final_answer():
    registry = ToolRegistry()

    registry.register("add", add)
    registry.register("multiply", multiply)

    agent = Agent(
        llm=MockLLM(),
        tools=registry,
    )

    result = agent.run("CALCULATE 25 * 18")

    assert result == "25 multiplied by 18 equals 450."
