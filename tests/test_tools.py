import pytest

from app.tools.registry import ToolRegistry
from app.tools.calculator import multiply

def test_unknown_tool_raises_error():
    registry = ToolRegistry()

    with pytest.raises(ValueError, match="Unknown tool"):
        registry.execute(
            "unknown_tool",
            {},
        )

def test_multiply_tool():
    result = multiply(25, 18)

    assert result == 450
