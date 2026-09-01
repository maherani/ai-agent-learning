from typing import Callable


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Callable] = {}

    def register(self, name: str, tool: Callable) -> None:
        self._tools[name] = tool

    def execute(self, name: str, arguments: dict) -> object:
        tool = self._tools.get(name)

        if tool is None:
            raise ValueError(f"Unknown tool: {name}")

        return tool(**arguments)
