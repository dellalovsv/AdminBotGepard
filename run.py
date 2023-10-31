# import config for bot
from config import Telegram

# import routers
from handlers.start import start_router
from handlers.dillers import diller_routers

# from funcs import BaseModel, engine

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


async def main():
    bot = Bot(token=Telegram.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        start_router,
        diller_routers
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # BaseModel.metadata.create_all(engine)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit...')
