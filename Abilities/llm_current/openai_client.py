from openai import OpenAI

class OpenAi:
    def __init__(self, api_key:str, model_id:str, base_url:str = None):
        self.api_key = api_key
        self.model_id = model_id
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def inference(self, model_id: str, prompt: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt.strip(),
                }
            ],
            model=model_id,
            temperature=0
        )
        # 添加调试信息
        #print(f"chat_completion: {chat_completion}")
        return chat_completion.choices[0].message.content
