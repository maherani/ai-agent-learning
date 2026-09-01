## Current Stage

The project currently contains a foundational tool-using AI Agent implemented without relying on an Agent framework.

Implemented concepts:

* LLM abstraction
* Mock LLM
* Dependency Injection
* Structured LLM responses
* Tools
* Tool Registry
* Tool Calls
* Agent Loop
* Agent State
* Structured Messages
* Typed Message Roles
* Automated tests
* Tool error handling

Current flow:

```text
User
  ↓
Agent
  ↓
LLM
  ↓
Tool Call
  ↓
Tool Registry
  ↓
Tool
  ↓
Tool Result
  ↓
LLM
  ↓
Final Answer
```

The current implementation uses a Mock LLM so the Agent architecture can be developed and tested without an external API key.

## Testing

Run all tests with:

```bash
python -m pytest
```

The test suite currently verifies:

* LLM response behavior
* Message roles
* Agent Tool Calling
* Tool execution
* Unknown Tool error handling

## Next Learning Step

The next step is to improve conversation state and message representation before connecting a real LLM provider.

The goal is to understand the message protocol used by real LLM APIs before introducing higher-level Agent frameworks.
