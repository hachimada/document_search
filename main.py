from openai_module.client import ChatClient
from openai_module.chat import ChatResponse

if __name__ == '__main__':

    client: ChatClient = ChatClient(model="gpt-3.5-turbo")

    while True:
        # 入力を受け付ける
        input_text = input("You: ")
        if input_text == "exit":
            break

        response: ChatResponse = client.add_user_message(input_text).request()
        client.add_message(response.get_message())
        print(response.get_message().get_content() + f"  (total token usage: {response.usage.get_total_tokens()}）")
