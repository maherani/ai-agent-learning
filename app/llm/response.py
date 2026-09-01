from dataclasses import dataclass
from typing import Optional

from app.tools.models import ToolCall


@dataclass
class LLMResponse:
    text: Optional[str] = None
    tool_call: Optional[ToolCall] = None
