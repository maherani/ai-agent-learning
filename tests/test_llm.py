from  app.llm.mock_llm import MockLLM

def test_mock_llm_generates_response():
    llm = MockLLM()

    response = llm.generate("Hello")

    assert response == "Mock response to: Hello"
