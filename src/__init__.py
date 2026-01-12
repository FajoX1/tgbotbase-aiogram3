from .dependencies import check_dependencies

from .settings import get_redis
from .core import bot_core
# from .sdk import SDK

import asyncio

# sdk = SDK()

redis = asyncio.run(get_redis())

bot_manager = bot_core.BotManager()
bot_manager.initialize()

bot = bot_manager.bot
dp = bot_manager.dp