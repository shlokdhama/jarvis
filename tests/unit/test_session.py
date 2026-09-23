from jarvis.llm.message import Message
from jarvis.core.session import Session

class FakeLLM:
    def __init__(self):
        self.received_messages = []
    def generate(self, messages: list[Message]) -> Message:
        self.received_messages.append(list(messages))
        return Message(
            role="assistant",
            content="fake response"
        )

def test_send_returns_response():
    fake = FakeLLM()
    session = Session(fake)
    result = session.send("hello")
    assert result == "fake response"

def test_session_stores_history():
    fake = FakeLLM()
    session = Session(fake)
    session.send("hello")
    assert len(session.messages) == 2
    assert session.messages[0].role == "user"
    assert session.messages[0].content == "hello"
    assert session.messages[1].role == "assistant"
    assert session.messages[1].content == "fake response"

def test_second_send_includes_previous_messages():
    fake = FakeLLM()
    session = Session(fake)
    session.send("hello")
    session.send("how are you?")
    second_call = fake.received_messages[1]
    assert len(second_call) == 3
    assert second_call[0].role == "user"
    assert second_call[0].content == "hello"
    assert second_call[1].role == "assistant"
    assert second_call[1].content == "fake response"
    assert second_call[2].role == "user"
    assert second_call[2].content == "how are you?"