from .common import Usage
import json


class EmbeddingResponse:

    def __init__(self, response: any) -> None:
        self.embedding: list[float] = response["data"][0]["embedding"]
        self.usage = Usage(response['usage'])

    def get_embedding(self) -> list[float]:
        return self.embedding

    def get_usage(self) -> Usage:
        return self.usage


if __name__ == '__main__':
    # 使用例
    json_str = '''{
      "data": [
        {
          "embedding": [
            -0.006929283495992422,
            -0.005336422007530928,
            -4.547132266452536e-05,
            -0.024047505110502243
          ],
          "index": 0,
          "object": "embedding"
        }
      ],
      "model": "text-embedding-ada-002",
      "object": "list",
      "usage": {
        "prompt_tokens": 5,
        "total_tokens": 5
      }
    }'''

    response = EmbeddingResponse(json.loads(json_str))
    print(response.get_embedding())
