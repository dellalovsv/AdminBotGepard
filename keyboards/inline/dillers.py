from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb_dillers = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить диллера', callback_data='dillers_new')],
    [InlineKeyboardButton(text='В главное меню', callback_data='back_to_main')],
])
