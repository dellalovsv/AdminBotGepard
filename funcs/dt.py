from datetime import datetime as dt


def get_now():
    return [
        dt.now().strftime('%Y-%m-%d %H:%M:%S'),
        dt.now().strftime('%d.%m.%Y %H:%M:%S'),
        dt.now().strftime('%Y-%m-%d'),
        dt.now().strftime('%d.%m.%Y')
    ]
