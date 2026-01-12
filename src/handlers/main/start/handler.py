from aiogram import types, F
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.api.entities.modes import ShowMode

from src import dp
from src.dialogs.main.start.states import StartSG

from . import keyboards

def is_menu_call(text: str) -> bool:
    return text == "/start" or "‎⁢ " in text

async def cmd_start(
    message: types.Message, dialog_manager: DialogManager, _
):
    if not dialog_manager.has_context():
        await message.answer(
            text="👋",
            reply_markup=await keyboards.start_keyboard(_)
        )
    
    await message.delete()
    dialog_manager.show_mode = ShowMode.EDIT
    await dialog_manager.start(StartSG.default, mode=StartMode.RESET_STACK)

def register_handlers():
    dp.message.register(cmd_start, F.text.func(is_menu_call))

register_handlers()