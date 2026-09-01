from dataclasses import dataclass, field

from app.agents.messages import Message


@dataclass
class AgentState:
    messages: list[Message] = field(default_factory=list)
