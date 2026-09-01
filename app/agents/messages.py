from dataclasses import dataclass
from typing import Any

from app.agents.roles import MessageRole


@dataclass
class Message:
    role: MessageRole
    content: str
    metadata: dict[str, Any] | None = None
