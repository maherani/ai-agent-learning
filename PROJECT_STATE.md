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

The project is currently at the Agent foundation stage.

Current structure:

```text
ai-agent-learning/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── agent.py
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
│   └── test_llm.py
├── .env
├── .env.example
├── .gitignore
├── README.md
├── PROJECT_STATE.md
├── requirements.txt
└── .venv/
```

Current execution flow:

```text
User Prompt
    ↓
Agent
    ↓
AgentState
    ↓
LLM Abstraction
    ↓
Mock LLM
    │
    ├── Final Text ──────────────→ Final Answer
    │
    └── Tool Call
            ↓
       Tool Registry
            ↓
           Tool
            ↓
        Tool Result
            ↓
          State
            ↓
           LLM
            ↓
       Final Answer
```

The Agent receives its LLM implementation and Tool Registry through dependency injection.

## Implemented Features

* Python virtual environment created
* Git repository initialized
* GitHub repository configured
* Standard project structure established
* `.gitignore` configured
* `.env` and `.env.example` created
* Secret-management approach established
* `python-dotenv` added
* `pytest` added
* Initial Python application created
* Mock LLM implemented
* LLM abstraction implemented using an abstract base class
* Dependency Injection introduced
* Tool functions implemented (`add` and `multiply`)
* `ToolCall` model implemented
* `ToolRegistry` implemented
* `Agent` class implemented
* Agent Loop implemented
* `AgentState` implemented
* Tool results are retained in Agent State
* Mock LLM can request a tool and later return a final answer
* Automated tests implemented with pytest

## Repository Status

The project is maintained in Git and synchronized with GitHub.

Current branch:

```text
master
```

The working project uses `.venv` locally on each development machine.

Sensitive environment configuration is stored in `.env` and must never be committed to Git.

The public/example configuration is stored in `.env.example`.

GitHub repository:

```text
https://github.com/maherani/ai-agent-learning
```

## Major Lessons Learned

* A Python project should use an isolated virtual environment.
* Dependencies should be explicitly tracked.
* Secrets should not be hard-coded into source code.
* `.env` should be ignored by Git.
* `.env.example` should document required environment variables without containing real secrets.
* Application logic should depend on abstractions rather than concrete implementations.
* An LLM interface allows different LLM implementations to be substituted without changing Agent logic.
* Dependency Injection reduces coupling between application logic and concrete implementations.
* Mock implementations allow development and testing without requiring a real LLM API.
* Automated tests should verify expected behavior rather than relying only on manual execution.
* Tools should have focused responsibilities and be independently executable.
* A Tool Registry allows tools to be selected and executed by name without hard-coding every tool into Agent logic.
* An Agent must distinguish between a request for tool execution and a final response.
* An Agent Loop allows the result of a tool to be returned to the LLM for the next decision.
* Agent State is needed to retain information across multiple steps of an Agent execution.
* Project documentation should be updated together with meaningful implementation milestones.

## Current Known Good State

The current application can be executed from the project root with:

```bash
python -m app.main
```

The current test suite can be executed with:

```bash
python -m pytest
```

Current known-good test result:

```text
3 passed
```

The current Agent can demonstrate a Tool Calling flow using the Mock LLM:

```text
CALCULATE 25 * 18
        ↓
LLM requests multiply
        ↓
multiply(25, 18)
        ↓
450
        ↓
LLM produces final answer
```

No real LLM API key is currently required for the implemented functionality.

## Pending Work

* Improve and formalize the LLM message/response model
* Introduce structured messages for User, Assistant, Tool Call, and Tool Result
* Add stronger Agent tests
* Introduce a real LLM provider
* Learn structured output with a real model
* Replace the Mock LLM with a provider-backed implementation
* Improve Agent state handling
* Introduce conversation memory
* Implement RAG
* Introduce LangChain after understanding the underlying concepts
* Introduce LangGraph for stateful Agent workflows

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
* Observability
* Prometheus
* Grafana
* Agent evaluation
* Production deployment

## Next Recommended Step

The next learning step is to replace the current `list[str]` state representation with structured message objects.

The intended model is:

```text
Message
├── role
├── content
└── metadata
```

The Agent should be able to distinguish clearly between:

```text
User Message
Assistant Message
Tool Call
Tool Result
```

This will provide the foundation for conversation history, memory, real LLM integration, and later LangGraph state management.

## Notes For Future Sessions

Learning methodology:

1. Explain the concept first.
2. Explain why the architectural decision is being made.
3. Implement one small piece.
4. Run and verify it.
5. Test understanding with small modifications.
6. Update the project documentation.
7. Commit and push the known-good state.
8. Continue to the next step only after the current concept is understood.

The objective is understanding and engineering ability, not copying code.

The project is designed to be developed across multiple machines, with GitHub acting as the shared source of truth.

At the current stage, no real LLM API key is required.
