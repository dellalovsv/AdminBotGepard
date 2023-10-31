from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb_dillers = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выдать карты', callback_data='dillers_issue_cards')],
    [InlineKeyboardButton(text='Показать выданные карты', callback_data='dillers_show_issue_cards')],
    [InlineKeyboardButton(text='Показать всех диллеров', callback_data='dillers_show_dillers')],
    [InlineKeyboardButton(text='Добавить диллера', callback_data='dillers_new')],
    [InlineKeyboardButton(text='Заблокировать/Разблокировать диллера', callback_data='dillers_disable_enable')],
    [InlineKeyboardButton(text='В главное меню', callback_data='back_to_main')],
])
