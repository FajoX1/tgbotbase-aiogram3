from aiogram import BaseMiddleware
from aiogram.types import Message

from typing import Callable, Dict, Any, Awaitable

from src.locales import translator

class InitMiddleware(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        
        data["_"] = await translator.get_translator(event.from_user.language_code)

        return await handler(event, data)