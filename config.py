class Telegram(object):
    token = '942781206:AAEiozAlW4t-t30gCPP49wnSKCQzY1PJTYE'


class DB(object):
    host = 'billing.mygepard.ru'
    port = 3306
    user = 'abills_dev'
    passwd = '12345678'
    db = 'abills'


class CfgIPPools(object):
    ips = [
        '172.16.30.1',
        '172.16.105.254'
    ]
    neg_dep = [
        '10.0.0.1',
        '10.0.0.254'
    ]
    unk_dev = [
        '172.16.24.1',
        '172.16.24.254'
    ]
