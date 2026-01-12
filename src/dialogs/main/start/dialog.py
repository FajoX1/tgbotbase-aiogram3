from aiogram import types
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.kbd import Row, Url
from aiogram_dialog.api.entities.launch_mode import LaunchMode

from src.utils.files import Banner
from src.locales.translator import AioDialogTranslate as _

from .other import *
from . import states

dialog = Dialog(
    Window(
        _("start-msg"),
        StaticMedia(
            url=Banner("night.jpg"),
            type=types.ContentType.PHOTO,
        ),
        Row(
            Url(_("dev-kb"), Const("https://github.com/fajox1")),
            Url(_("repository-kb"), Const("https://github.com/fajox/tgbotbase-aiogram3")),
        ),
        getter=get_data,
        state=states.StartSG.default,
    ),
    launch_mode=LaunchMode.SINGLE_TOP
)