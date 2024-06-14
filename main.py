from Abilities.llm_current.openai_client import OpenAi
from Abilities.Plan.Plan import Plan
apikey = 'sk-C6Qj454iHnDYekeH94358c7301534b99B42dE229A7E380Ca'
baseurl = 'https://burn.hair/v1'
pangu = Plan(api_key= apikey, base_model='gpt-4o-2024-05-13', base_url=baseurl)
result = pangu.generate_plan(name='pangu', description='hi', prompt='生成一个厦门旅游计划')
print(result)