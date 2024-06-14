from jinja2 import Environment, BaseLoader, FileSystemLoader
from Abilities.llm_current.openai_client import OpenAi
#Some Configuration
#apikey = 'sk-C6Qj454iHnDYekeH94358c7301534b99B42dE229A7E380Ca'
#baseurl = 'https://burn.hair/v1'
#PROMPT = open("Plan.jinja2").read().strip()
class Plan:
    def __init__(self, api_key:str, base_model:str, base_url:str = None):
        self.llm = OpenAi(api_key=api_key, model_id=base_model, base_url=base_url)
        self.env = Environment(loader = FileSystemLoader('Abilities/Plan'))
        self.template = self.env.get_template('Plan.jinja2')
        
    def generate_plan(self, name:str, description:str, prompt:str):
        #渲染模板
        prompt_llm = self.template.render(name=name, description=description, prompt=prompt)
        #调用OpenAI
        response = self.llm.inference(model_id=self.llm.model_id, prompt=prompt_llm)
        
        return response

        
        