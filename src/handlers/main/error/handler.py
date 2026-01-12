from aiogram import types
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.api.entities.modes import ShowMode
from aiogram_dialog.api import exceptions

from src import dp
from src.dialogs.main.start.states import StartSG

@dp.error()
async def error_handler(
    event: types.ErrorEvent, dialog_manager: DialogManager = None
):
    exception = event.exception

    if isinstance(exception, exceptions.UnknownIntent) and dialog_manager:
        await dialog_manager.done()
        dialog_manager.show_mode = ShowMode.EDIT
        await dialog_manager.start(StartSG.default, mode=StartMode.RESET_STACK)
        return
    
    raise exception