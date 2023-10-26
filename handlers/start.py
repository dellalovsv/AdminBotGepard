from funcs.admins import AdminFilter
from funcs import dt
from messages import start as msg_start
from funcs import dhcphosts

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


start_router = Router()


@start_router.message(AdminFilter(), CommandStart)
async def start_cmd(m: Message):
    await m.answer(msg_start.info % (
        dt.get_now()[1],
        dhcphosts.Lease().get_online(),
        dhcphosts.Lease().get_neg_dep(),
        dhcphosts.Lease().get_unk_dev()
    ))


@start_router.message(AdminFilter(), Command('help'))
async def help_cmd(m: Message):
    ...
