from . import Session
from funcs.models.admins import Admin

from aiogram.filters import Filter
from aiogram.types import Message


class AdminFilter(Filter):
    # Класс фильтра aiogram для определения существования администратора в бд бота
    #
    # Функция проверки существования админа в бд и его статуса по id (должен быть активен)
    async def __call__(self, m: Message) -> bool:
        with Session() as session:
            admin = session.query(Admin).filter_by(tid=m.from_user.id, disable=0).first()
            if admin is not None:
                return True
            else:
                return False
