from config import DB as db_cfg
# from . import logs

from contextlib import contextmanager
from typing import Optional, Union

from pymysql import connect
from pymysql.cursors import DictCursor


@contextmanager
def __get_conn() -> object:
    global conn
    conn = connect(
        host=db_cfg.host,
        port=db_cfg.port,
        user=db_cfg.user,
        password=db_cfg.passwd,
        db=db_cfg.db,
        charset='utf8',
        cursorclass=DictCursor
    )
    try:
        yield conn
    finally:
        conn.close()


def query(sql: str = None, *args, commit: bool = False) -> Optional[Union[list[dict], bool]] | None:
    try:
        with __get_conn() as db_conn:
            with db_conn.cursor() as cur:
                if len(args) > 0:
                    cur.execute(sql, args)
                else:
                    cur.execute(sql)
                if commit:
                    db_conn.commit()
                    return True
                else:
                    res = cur.fetchall()
                    if len(res) > 0:
                        return res
                    else:
                        return None
    except Exception as e:
        # logs.logger.error(f'INIT.query: {e}')
        return False
