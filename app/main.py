from app.llm.interface import LLM
from app.llm.mock_llm import MockLLM


def run_agent(llm: LLM, prompt: str) -> str:
    return llm.generate(prompt)


def main():
    llm = MockLLM()

    response = run_agent(
        llm,
        "Why do AI agents need tools?",
    )

    print(response)


if __name__ == "__main__":
    main()
