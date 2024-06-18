from jinja2 import Environment, BaseLoader, FileSystemLoader
from Abilities.llm_current.openai_client import OpenAi

class Translate:
    def __init__(self, api_key:str, base_model:str, base_url:str = None):
        self.llm = OpenAi(api_key=api_key, model_id=base_model, base_url=base_url)
        self.env = Environment(loader = FileSystemLoader('Translate'))
        self.template = self.env.get_template('Translate.jinja2')
    def Translate_text(self, text:str, target_language:str) -> str:
        prompt_llm = self.template.render()
        response = self.llm.inference(model_id=self.llm.model_id, prompt=prompt_llm)
        return response