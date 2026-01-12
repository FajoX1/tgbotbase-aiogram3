from aiogram_dialog import DialogManager

async def get_data(dialog_manager: DialogManager, **kwargs):
    message = dialog_manager.event

    return {
        "i18n_format": {
            "name": message.from_user.full_name,
        }
    }