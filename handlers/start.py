from funcs.admins import AdminFilter

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart


start_router = Router()


@start_router.message(AdminFilter(), CommandStart())
async def start_cmd(m: Message):
    ...
