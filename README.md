## AI Agent Learning Path

This repository is a project-based learning environment for learning AI Agent development with Python.

The project is intentionally developed step by step, with an emphasis on understanding the underlying concepts and architecture before introducing higher-level frameworks.

## Current Stage

The project has completed its initial architecture and testing foundation.

Implemented so far:

* Python virtual environment
* Git and GitHub workflow
* Standard project structure
* Environment variable management
* `.env` / `.env.example`
* Dependency management
* Mock LLM
* LLM abstraction
* Dependency Injection
* Initial automated test with pytest

Current test status:

```text
1 passed
```

## Current Architecture

```text
Application
    ↓
Agent Execution Function
    ↓
LLM Abstraction
    ↓
Mock LLM
    ↓
Response
```

The LLM implementation is intentionally abstracted so that a real provider can be introduced later without changing the core Agent logic.

## Learning Roadmap

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

## Development Principles

This project follows a mentor-style, project-based learning approach.

For each topic:

1. Understand the concept.
2. Understand the architectural reason.
3. Implement a small piece.
4. Run it.
5. Test it.
6. Verify the behavior.
7. Update the documentation.
8. Commit the known-good state.

The goal is to develop the ability to design and build AI Agent systems independently, not simply reproduce code examples.

## Running the Project

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the application:

```bash
python -m app.main
```

Run tests:

```bash
python -m pytest
```

## Repository Workflow

Before starting work:

```bash
git pull
```

After completing a verified change:

```bash
git status
git add .
git commit -m "..."
git push origin master
```

The `master` branch is currently used as the main development branch.

## Security

Real API keys and secrets must never be committed to Git.

Use:

```text
.env
```

for local secrets and:

```text
.env.example
```

for documenting required environment variables.

The `.env` file is excluded through `.gitignore`.
