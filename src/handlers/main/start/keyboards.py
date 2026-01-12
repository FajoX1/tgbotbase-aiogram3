from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

async def start_keyboard(_) -> InlineKeyboardBuilder:

    keyboard = ReplyKeyboardBuilder()
    
    keyboard.add(
        types.KeyboardButton(text=f"💎‎⁢ {await _("menu-keyboard")}")
    )

    return keyboard.as_markup(resize_keyboard=True)