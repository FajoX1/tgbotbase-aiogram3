from aiogram_dialog.api.protocols import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text

from src import redis

from . import i18n
from .ai import ai_translator

import hashlib

class AioDialogTranslate(Text):
    def __init__(
        self, 
        text: str, 
        when: WhenCondition = None
    ):
        super().__init__(when)
        self.text = text

    async def _render_text(
        self, 
        data: dict, 
        dialog_manager: DialogManager
    ) -> str:
        return await dialog_manager.middleware_data["_"](
            self.text, **data.get('i18n_format', {})
        )

async def make_cache_key(template_text: str, target: str) -> str:
    h = hashlib.md5(template_text.encode("utf-8")).hexdigest()
    return f"translation:{target}:{h}"

async def get_translator(lang: str):
    async def _(key: str, **params):
        template_text = i18n.format_value(key)

        if lang != "en" and template_text != key:
            key_cache = await make_cache_key(template_text, lang)
            cached = await redis.get(key_cache)
            if cached:
                translated_template = cached
            else:
                print(f"Translating template to {lang}: {template_text}")
                translated_template = await ai_translator.translate(template_text, lang)

                await redis.set(key_cache, translated_template, ex=30*24*60*60)
        else:
            translated_template = template_text

        translated_template = translated_template.format(**params)

        return translated_template

    return _