from jarvis.config import API_KEY, MODEL
from jarvis.llm.message import Message
from google import genai
from google.genai import types

class GeminiProvider:
    def __init__(self):
        self.client=genai.GeminiClient(api_key=API_KEY)

    def generate(self, messages: list[Message]) -> Message:
        contents = []

        for message in messages:
            role = "model" if message.role == "assistant" else message.role

            contents.append(types.Message(role=role, content=message.content))

        response = self.client.generate_text(model=MODEL, messages=contents)

        return Message(role="assistant", content=response.text)
