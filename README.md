## AI Agent Learning Path

This repository is a project-based learning environment for learning AI Agent development with Python.

The project is intentionally developed step by step.

### Current Stage

The project is currently at the initial architecture stage.

Implemented:

* Python virtual environment
* Git repository
* Environment variable management
* `.env` / `.env.example`
* Basic application structure
* Mock LLM
* Initial LLM abstraction

### Learning Roadmap

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

### Development Principle

The project is developed with a mentor-style, project-based learning approach.

Each concept is first understood, then implemented, tested, and verified before moving to the next stage.

The project does not currently require a paid LLM API because a Mock LLM is being used during the initial learning stages.

### Run the Current Project

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the application from the project root:

```bash
python -m app.main
```
