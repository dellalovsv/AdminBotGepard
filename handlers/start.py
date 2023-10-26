from funcs.admins import AdminFilter
from funcs.dhcphosts import Lease
from funcs import dt
from messages import start as msg_start

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


start_router = Router()


@start_router.message(AdminFilter(), CommandStart())
async def start_cmd(m: Message):
    await m.answer(msg_start.info % (
        dt.get_now()[1],
        Lease().get_online(),
        Lease().get_neg_dep(),
        Lease().get_unk_dev()
    ))
