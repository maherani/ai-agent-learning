from dataclasses import dataclass
from typing import Any


@dataclass
class ToolCall:
    tool_name: str
    arguments: dict[str, Any]
