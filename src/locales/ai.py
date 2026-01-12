from openai import AsyncOpenAI
from googletrans import Translator

from src import config
from src.utils import entities

class AITranslator:
    
    def __init__(self):
        self.model = config.AI_MODEL
        self.ai = AsyncOpenAI(
            base_url=config.AI_API_URL,
            api_key=config.AI_API_KEY,
        )
        self.translator = Translator()

    async def translate(self, text: str, target: str) -> str:
        try:
            responses = await self.ai.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Translate the text into the language with language_code {target} strictly word-for-word, "
                            "preserving all characters, including spaces, invisible ones (ZWSP/ZWNJ/ZWJ), symbols, links, HTML/Markdown, ABSOLUTELY EVERYTHING. "
                            "Do not merge, delete, or replace letters with emojis. "
                            "Preserve the original structure completely. Only the translation, no explanations:\n\n"
                            f"{text}"
                        )
                    }
                ],
                timeout=4
            )
            translated = responses.choices[0].message.content
        except:
            text, html, fmt = entities.freeze_html(text)
            translated_frozen = (await self.translator.translate(text, dest=target)).text
            translated = entities.unfreeze_html(translated_frozen, html, fmt)
        
        return translated
        
ai_translator = AITranslator()