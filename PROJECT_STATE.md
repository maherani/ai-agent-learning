# PROJECT_STATE.md

## Objective

Build a project-based learning environment for developing AI Agents with Python.

The project is designed as a long-term learning project in which AI Agent concepts are learned by implementing software step by step rather than by copying isolated examples.

The planned learning path is:

```text
Python
  ↓
LLM API
  ↓
Structured Output
  ↓
Tool Calling
  ↓
Agent Loop
  ↓
Memory
  ↓
RAG
  ↓
LangChain
  ↓
LangGraph
  ↓
Multi-Agent
  ↓
Production AI Agent
```

## Current Architecture

The project currently contains the foundational components of a simple tool-using Agent.

```text
User
  ↓
Agent
  ↓
AgentState
  ↓
LLM
  ↓
ToolCall
  ↓
ToolRegistry
  ↓
Tool
  ↓
Tool Result
  ↓
AgentState
  ↓
LLM
  ↓
Final Answer
```

Current structure:

```text
ai-agent-learning/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── messages.py
│   │   ├── roles.py
│   │   └── state.py
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── interface.py
│   │   ├── mock_llm.py
│   │   └── response.py
│   └── tools/
│       ├── __init__.py
│       ├── calculator.py
│       ├── models.py
│       └── registry.py
├── tests/
│   ├── __init__.py
│   ├── test_agent.py
│   ├── test_llm.py
│   ├── test_messages.py
│   └── test_tools.py
├── .env
├── .env.example
├── .gitignore
├── README.md
├── PROJECT_STATE.md
├── requirements.txt
└── .venv/
```

## Implemented Features

* Python virtual environment
* Git and GitHub workflow
* Environment variable management
* `.env` and `.env.example`
* Dependency management
* Abstract LLM interface
* Mock LLM implementation
* Dependency Injection
* Structured `LLMResponse`
* ToolCall model
* Tool Registry
* Calculator tools
* Agent implementation
* Agent Loop
* Agent State
* Structured Message model
* Typed Message Roles
* Unit tests for LLM behavior
* Unit tests for Message behavior
* Unit tests for Agent behavior
* Unit tests for Tool behavior
* Error handling for unknown tools

Current tools:

```text
add
multiply
```

Current message roles:

```text
SYSTEM
USER
ASSISTANT
TOOL
```

## Repository Status

The project is maintained using Git and GitHub.

Current main development branch:

```text
master
```

GitHub is the shared source of truth so development can continue across multiple machines.

Real secrets must never be committed.

`.env` is ignored by Git.

## Major Lessons Learned

* Virtual environments isolate project dependencies.
* Dependencies should be explicitly tracked.
* Secrets must be separated from source code.
* LLM implementations should depend on an abstraction.
* Dependency Injection reduces coupling.
* Mock LLMs allow Agent development without a real API.
* Tests should verify behavior rather than implementation details.
* Parametrized tests can verify the same behavior across multiple inputs.
* Tools should have focused responsibilities.
* A Tool Registry decouples Agent logic from individual Tool implementations.
* Tool errors must have explicit and testable behavior.
* Agent responses can represent either a final answer or a Tool Call.
* Agent Loops allow a Tool result to be returned to the LLM for further reasoning.
* State allows the Agent to preserve information across multiple steps.
* Structured Messages are preferable to storing conversation history as unstructured strings.
* Typed message roles make the Agent state more explicit and maintainable.

## Current Known Good State

The application can be executed from the project root with:

```bash
python -m app.main
```

The test suite can be executed with:

```bash
python -m pytest
```

Current known-good behavior:

```text
Application
    ↓
Agent
    ↓
MockLLM
    ↓
ToolCall
    ↓
ToolRegistry
    ↓
Calculator
    ↓
Tool Result
    ↓
Agent Loop
    ↓
Final Answer
```

The current test suite passes successfully.

The project does not currently require a real LLM API key.

## Pending Work

* Improve the message model
* Introduce a more explicit conversation state
* Separate LLM request messages from Agent internal state
* Introduce a real LLM provider
* Learn structured output from a real model
* Implement real Tool Calling
* Improve Agent error handling and retry behavior
* Add more Agent tests
* Introduce Memory
* Implement RAG
* Introduce LangChain
* Introduce LangGraph

## Future Enhancements

* Cloud LLM providers
* Local LLM support
* FastAPI
* PostgreSQL
* Redis
* Vector database
* RAG pipeline
* Multi-Agent architecture
* Docker
* Prometheus
* Grafana
* Agent evaluation
* Production deployment

## Next Recommended Step

The next learning objective is to improve the conversation model.

Current State uses structured `Message` objects, but the Agent still converts the conversation into plain text before sending it to the Mock LLM.

The next step is to separate:

```text
Internal Agent State
        ↓
LLM Message Format
```

and understand how real LLM APIs represent:

```text
system
user
assistant
tool call
tool result
```

before connecting a real LLM provider.

## Notes For Future Sessions

Learning methodology:

1. Understand the concept first.
2. Understand why the architectural decision is being made.
3. Implement one small piece.
4. Run and verify it.
5. Test understanding with deliberate small changes.
6. Update documentation.
7. Commit and push the known-good state.
8. Continue only after the current concept is understood.

The objective is to develop independent AI Agent engineering ability, not merely reproduce code.

The current project is intentionally built from fundamentals before introducing LangChain or LangGraph.
