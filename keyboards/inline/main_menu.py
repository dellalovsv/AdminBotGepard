from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


kb_main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Диллеры', callback_data='main_menu_dillers')]
])
