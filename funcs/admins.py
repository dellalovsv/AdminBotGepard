from . import query

from aiogram.filters import Filter
from aiogram.types import Message


class AdminFilter(Filter):
    # Класс фильтра aiogram для определения существования администратора в бд бота
    #
    # Функция проверки существования админа в бд и его статуса по id (должен быть активен)
    async def __call__(self, m: Message) -> bool:
        try:
            sql = 'select count(*) as count from admins where disable=0 and tid=%s'
            res = query(sql, m.from_user.id)
            if res is not None and res is not False and len(res) > 0:
                if res[0]['count'] == 1 or res[0]['count'] == '1':
                    return True
            else:
                return False
        except Exception as e:
            print(f'FUNCS.ADMINS.ADMINS_FILTER.__CALL__ (ERROR): {e}')
            return False
