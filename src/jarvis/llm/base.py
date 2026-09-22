#rules

from typing import Protocol
from .message import Message

class LLMProvider(Protocol):
    def generate(self,messages) -> Message:
        ...