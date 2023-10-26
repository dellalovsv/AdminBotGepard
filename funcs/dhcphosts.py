from . import query
from config import CfgIPPools

from datetime import datetime as dt

from netaddr import IPAddress


class Lease:
    def __init__(self):
        self.table = 'dhcphosts_leases'

    def get_online(self):
        try:
            sql = f'select count(*) as count from {self.table} where ends>=%s'
            res = query(sql, dt.now().strftime('%Y-%m-%d %H:%M:%S'))
            if res is not None and res is not False and len(res) > 0:
                return res[0]['count']
            else:
                return None
        except Exception as e:
            print(f'FUNCS.DHCPHOSTS.LEASE.GET_ONLINE (ERROR): {e}')
            return False

    def get_neg_dep(self):
        try:
            begin_ip = int(IPAddress(CfgIPPools.neg_dep[0]))
            end_ip = int(IPAddress(CfgIPPools.neg_dep[1]))
            sql = f'select count(*) as count from {self.table} where ends>=%s and ip>=%s and ip<=%s'
            res = query(sql, dt.now().strftime('%Y-%m-%d %H:%M:%S'), begin_ip, end_ip)
            if res is not None and res is not False and len(res) > 0:
                return res[0]['count']
            else:
                return None
        except Exception as e:
            print(f'FUNCS.DHCPHOSTS.LEASE.GET_NEG_DEP (ERROR): {e}')
            return False

    def get_unk_dev(self):
        try:
            begin_ip = int(IPAddress(CfgIPPools.unk_dev[0]))
            end_ip = int(IPAddress(CfgIPPools.unk_dev[1]))
            sql = f'select count(*) as count from {self.table} where ends>=%s and ip>=%s and ip<=%s'
            res = query(sql, dt.now().strftime('%Y-%m-%d %H:%M:%S'), begin_ip, end_ip)
            if res is not None and res is not False and len(res) > 0:
                return res[0]['count']
            else:
                return None
        except Exception as e:
            print(f'FUNCS.DHCPHOSTS.LEASE.GET_UNK_DEV (ERROR): {e}')
            return False
