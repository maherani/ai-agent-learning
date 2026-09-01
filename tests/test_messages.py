from app.agents.messages import Message
from app.agents.roles import MessageRole


def test_message_uses_typed_role():
    message = Message(
        role=MessageRole.USER,
        content="Hello",
    )

    assert message.role == MessageRole.USER
    assert message.role.value == "user"
