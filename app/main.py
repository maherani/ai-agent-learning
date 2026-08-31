from app.llm.mock_llm import MockLLM


def main():
    llm = MockLLM()

    response = llm.generate("Why do we need tools in an AI agent?")

    print(response)


if __name__ == "__main__":
    main()
