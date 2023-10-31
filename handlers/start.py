from funcs.admins import AdminFilter
from funcs import dt
from messages import start as msg_start
from funcs import dhcphosts
from keyboards.inline import main_menu

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command


start_router = Router()


@start_router.message(AdminFilter(), CommandStart)
async def start_cmd(m: Message):
    await m.answer(msg_start.info % (
        dt.get_now()[1],
        dhcphosts.Lease().get_online(),
        dhcphosts.Lease().get_neg_dep(),
        dhcphosts.Lease().get_unk_dev()
    ), reply_markup=main_menu.kb_main_menu)


@start_router.message(AdminFilter(), Command('help'))
async def help_cmd(m: Message):
    ...


@start_router.callback_query(AdminFilter(), F.data == 'back_to_main')
async def back_to_main(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(msg_start.info % (
        dt.get_now()[1],
        dhcphosts.Lease().get_online(),
        dhcphosts.Lease().get_neg_dep(),
        dhcphosts.Lease().get_unk_dev()
    ), reply_markup=main_menu.kb_main_menu)
