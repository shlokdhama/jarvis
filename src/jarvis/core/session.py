from jarvis.llm.message import Message

class Session:
    def __init__(self,llm):
        self.messages=[]
        self.llm=llm

    def send(self,user_text: str) -> str:
        self.messages.append(Message(role="user", content=user_text))
        response=self.llm.generate(self.messages)
        self.messages.append(response)
        return response.content