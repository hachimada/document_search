from .chat import Message, MessageList, ChatResponse
from dotenv import load_dotenv
import openai
import os

load_dotenv()
DOCUMENTS_PATH = os.environ.get('DOCUMENTS_PATH')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY


class ChatClient:

    def __init__(self, behavior=None, model: str = "gpt-4") -> None:
        if behavior is None:
            behavior = {"role": "system",
                        "content": "You are useful assistant and response in English."}
        self.model: str = model
        self.behavior: Message = Message(behavior)
        self.messages: MessageList = MessageList([self.behavior])

    def set_behavior(self, behavior: str) -> 'ChatClient':
        self.behavior = Message({"role": "system", "content": behavior})
        return self

    def add_user_message(self, content: str) -> 'ChatClient':
        self.messages.append(
            Message({"role": "user", "content": content})
        )
        return self

    def add_message(self, message: Message) -> 'ChatClient':
        self.messages.append(message)
        return self

    def latest_message(self) -> Message:
        return self.messages.get_latest()

    def request(self) -> ChatResponse:
        res = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages.to_dict()
        )
        return ChatResponse(res['choices'][0]['message'], res['usage'])
