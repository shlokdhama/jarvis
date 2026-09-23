from jarvis.config import API_KEY, MODEL
from jarvis.llm.message import Message
from google import genai
from google.genai import types

class GeminiProvider:
    def __init__(self):
        self.client=genai.Client(api_key=API_KEY)

    def generate(self, messages: list[Message]) -> Message:
        contents = []

        for message in messages:
            role = "model" if message.role == "assistant" else message.role

            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part(text=message.content)]
                )
            )

        response = self.client.models.generate_content(
            model=MODEL,
            contents=contents
    )

        return Message(role="assistant", content=response.text)
