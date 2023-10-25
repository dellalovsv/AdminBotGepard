from config import DB

from pymysql import connect
from pymysql.cursors import DictCursor


def __get_conn():
    global conn
    conn = connect(
        host=DB.host,
        port=DB.port,
        user=DB.user,
        password=DB.passwd,
        db=DB.db,
        charset='utf8',
        cursorclass=DictCursor
    )
    try:
        yield conn
    finally:
        conn.close()


def query(sql: str = None, *args, commit: bool = False):
    try:
        with __get_conn() as conn:
            with conn.cursor() as cur:
                if len(args) > 0:
                    cur.execute(sql, args)
                else:
                    cur.execute(sql)
                if commit:
                    conn.commit()
                    return True
                else:
                    res = cur.fetchall()
                    if len(res) > 0:
                        return res
                    else:
                        return None
    except Exception as e:
        print(f'QUERY (ERROR): {e}')
        return False
