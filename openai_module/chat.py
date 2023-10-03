from .common import Usage


class Message:
    def __init__(self, message: dict[str, str]) -> None:
        """Messages that make up a conversation

        example: Message("user", "Hello!")

        :param message {"role": "user", "content": "Hello!"}
        """
        self.role: str = message["role"]
        self.content: str = message["content"]

    def get_role(self):
        """Get the role of the message"""
        return self.role

    def get_content(self):
        """Get the content of the message"""
        return self.content

    def to_dict(self) -> dict[str, str]:
        """Converts the message to a dictionary

        :return: A dictionary representation of the message. example is {"role": "user", "content": "Hello!"}
        """
        return {
            "role": self.role,
            "content": self.content
        }


class MessageList:
    def __init__(self, messages: list[Message]) -> None:
        """A list of messages that make up a conversation

        :param messages: A list of messages
        """
        self.messages: list[Message] = messages

    def append(self, message: Message) -> None:
        """Append a message to the list of messages

        :param message: The message to append
        """
        self.messages.append(message)

    def get_latest(self) -> Message:
        """Get the latest message"""
        return self.messages[-1]

    def to_dict(self) -> list[dict[str, str]]:
        """Converts the message list to a dictionary

        :return: A dictionary representation of the message list. example is [{"role": "user", "content": "Hello!"}].
        """
        return [message.to_dict() for message in self.messages]


class ChatResponse:

    def __init__(self, message: dict, usage: dict):
        self.message: Message = Message(message)
        self.usage: Usage = Usage(usage)

    def get_message(self) -> Message:
        return self.message

    def get_role(self) -> str:
        return self.message.get_role()

    def get_usage(self) -> Usage:
        return self.usage


if __name__ == '__main__':
    json_str = """
    {
      "id": "some-id",
      "object": "chat.completion",
      "created": 1234567890,
      "model": "gpt-3.5-turbo-0613",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "Hi there!"
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 11,
        "total_tokens": 21
      }
    }"""
