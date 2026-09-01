from app.agents.agent import Agent
from app.llm.mock_llm import MockLLM
from app.tools.calculator import add, multiply
from app.tools.registry import ToolRegistry


def main():
    registry = ToolRegistry()

    registry.register("add", add)
    registry.register("multiply", multiply)

    agent = Agent(
        llm=MockLLM(),
        tools=registry,
    )

    result = agent.run("CALCULATE 25 * 18")
#    result = agent.run("Hello")

    print(result)


if __name__ == "__main__":
    main()
