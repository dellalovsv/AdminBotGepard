from . import query

from aiogram.filters import Filter
from aiogram.types import Message


class AdminFilter(Filter):
    # Класс фильтра aiogram для определения существования администратора в бд бота
    #
    # Функция проверки существования админа в бд и его статуса по id (должен быть активен)
    async def __call__(self, m: Message) -> bool:
        try:
            sql = 'select id from bot_admins where disable=0'
            res = query(sql)
            if res is not None and res is not False and len(res) > 0:
                admins = []
                for r in res:
                    admins.append(r['id'])
                if len(admins) > 0:
                    if m.from_user.id in admins:
                        return True
            else:
                return False
        except Exception as e:
            print(f'FUNCS.ADMINS.ADMINS_FILTER.__CALL__ (ERROR): {e}')
            return False
