import os
from typing import List, Union
from jinja2 import Environment, FileSystemLoader
from Abilities.llm_current.openai_client import OpenAi
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Translate:
    def __init__(self, api_key: str, base_model: str, base_url: str = None):
        self.llm = OpenAi(api_key=api_key, model_id=base_model, base_url=base_url)
        self.env = Environment(loader=FileSystemLoader('Translate'))
        self.template = self.env.get_template('Translate.jinja2')

    def get_completion(self, prompt: str, system_message: str = "You are a helpful assistant.", temperature: float = 0.3) -> str:
        response = self.llm.inference(model_id=self.llm.model_id, prompt=prompt, system_message=system_message, temperature=temperature)
        return response

    def translate_text(self, text: str, target_language: str) -> str:
        # 初始翻译
        system_message = f"You are an expert linguist, specializing in translation to {target_language}."
        translation_prompt = self.template.render(source_text=text, target_language=target_language)
        initial_translation = self.get_completion(translation_prompt, system_message=system_message)

        # 反思并改进翻译
        reflection_prompt = f"""Your task is to carefully read a source text and a translation to {target_language}, and then give constructive criticism and helpful suggestions to improve the translation. 
        The source text and initial translation, delimited by XML tags <SOURCE_TEXT></SOURCE_TEXT> and <TRANSLATION></TRANSLATION>, are as follows:

        <SOURCE_TEXT>
        {text}
        </SOURCE_TEXT>

        <TRANSLATION>
        {initial_translation}
        </TRANSLATION>

        When writing suggestions, pay attention to whether there are ways to improve the translation's 
        (i) accuracy (by correcting errors of addition, mistranslation, omission, or untranslated text),
        (ii) fluency (by applying {target_language} grammar, spelling and punctuation rules, and ensuring there are no unnecessary repetitions),
        (iii) style (by ensuring the translations reflect the style of the source text and takes into account any cultural context),
        (iv) terminology (by ensuring terminology use is consistent and reflects the source text domain; and by only ensuring you use equivalent idioms {target_language}).

        Write a list of specific, helpful and constructive suggestions for improving the translation.
        Each suggestion should address one specific part of the translation.
        Output only the suggestions and nothing else."""

        reflection = self.get_completion(reflection_prompt, system_message=system_message)

        # 使用反思改进翻译
        improvement_prompt = f"""Based on the following suggestions, improve the translation:
        Suggestions:
        {reflection}

        Original Translation:
        {initial_translation}

        Improved Translation:"""

        improved_translation = self.get_completion(improvement_prompt, system_message=system_message)
        return improved_translation

# 使用示例
if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    base_model = "gpt-4-turbo"
    translator = Translate(api_key=api_key, base_model=base_model)
    source_text = "Last week, I spoke about AI and regulation at the U.S. Capitol at an event that was attended by legislative and business leaders."
    target_language = "Spanish"
    translated_text = translator.translate_text(source_text, target_language)
    print(translated_text)