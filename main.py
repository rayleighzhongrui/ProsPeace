from Abilities.llm_current.openai_client import OpenAi
from Abilities.Plan.Plan import Plan
from Abilities.Write.Write import Write
apikey = 'sk-C6Qj454iHnDYekeH94358c7301534b99B42dE229A7E380Ca'
baseurl = 'https://burn.hair/v1'
Pangu_Plan = Plan(api_key= apikey, base_model='gpt-4o-2024-05-13', base_url=baseurl)
Pangu_Write = Write(api_key= apikey, base_model='gpt-4o-2024-05-13', base_url = baseurl)
blogplan = Pangu_Plan.generate_plan(name='盘古', description='一位无所不能，无所不知的中国创世神', prompt='写一篇普通人是如何使用ChatGPT来实现简单实用的小功能')
blog = Pangu_Write.WritePost(name='盘古',description='一位无所不能，无所不知的中国创世神', task=blogplan)
print(blogplan)
print(blog)
