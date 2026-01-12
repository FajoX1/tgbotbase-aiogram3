from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.telegram import TelegramAPIServer
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage

from src import config

class BotManager:
    def __init__(self):
        self.bot_token = config.BOT_TOKEN
        self.api_url = config.BOT_API_URL

    def initialize(self):

        self.storage = MemoryStorage()

        self.dp = Dispatcher(
            storage=self.storage, 
            fsm_strategy=FSMStrategy.USER_IN_CHAT
        )

        self.bot = Bot(
            token=self.bot_token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML,
            ),
            session=AiohttpSession(
                api=TelegramAPIServer(
                    base=self.api_url + "/bot{token}/{method}",
                    file=self.api_url + "/file/bot{token}/{path}",
                )
            )
        )