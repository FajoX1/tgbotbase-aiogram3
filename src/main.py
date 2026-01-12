from aiogram_dialog import setup_dialogs

from src import loader

from . import bot, dp

async def _run():
    print("Starting the bot...")

    try:
        setup_dialogs(dp)
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()