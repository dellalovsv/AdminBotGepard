from messages import diilers as msg_dills

from funcs.admins import AdminFilter
from keyboards.inline.dillers import kb_dillers

from aiogram import F, Router
from aiogram.types import CallbackQuery


diller_routers = Router()


@diller_routers.callback_query(AdminFilter(), F.data == 'main_menu_dillers')
async def menu_dillers(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(msg_dills.title, reply_markup=kb_dillers)
