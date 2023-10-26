from funcs.admins import AdminFilter
from funcs.dhcphosts import Lease
from funcs import dt
from messages import start as msg_start

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


start_router = Router()


@start_router.message(AdminFilter(), Command('start', 'info'))
async def start_cmd(m: Message):
    await m.answer(f'Hello... {m.from_user.username}!')


@start_router.message(AdminFilter(), Command('help'))
async def help_cmd(m: Message):
    ...
