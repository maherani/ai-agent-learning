import pytest

from app.llm.mock_llm import MockLLM


@pytest.mark.parametrize(
    "prompt",
    [
        "Hello",
        "What is tool calling?",
        "Why do AI agents need tools?",
    ],
)
def test_mock_llm_generates_response(prompt):
    llm = MockLLM()

    response = llm.generate(prompt)

    assert response == f"Mock response to: {prompt}"
