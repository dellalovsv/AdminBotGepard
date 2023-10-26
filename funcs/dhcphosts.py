from . import Session
from config import CfgIPPools
from funcs import dt
from funcs.models.dhcphosts import Lease as model_lease

from netaddr import IPAddress


class Lease:
    def __init__(self):
        self.table = 'dhcphosts_leases'

    def get_online(self):
        with Session() as session:
            online = session.query(model_lease).filter(model_lease.ends >= dt.get_now()[0]).all()
            return len(online)

    def get_neg_dep(self):
        with Session() as session:
            neg_dep = session.query(model_lease).filter(
                model_lease.ends > dt.get_now()[0],
                model_lease.ip >= int(IPAddress(CfgIPPools.neg_dep[0])),
                model_lease.ip <= int(IPAddress(CfgIPPools.neg_dep[1]))
            ).all()
            return len(neg_dep)

    def get_unk_dev(self):
        with Session() as session:
            unk_dev = session.query(model_lease).filter(
                model_lease.ends >= dt.get_now()[0],
                model_lease.ip >= int(IPAddress(CfgIPPools.unk_dev[0])),
                model_lease.ip <= int(IPAddress(CfgIPPools.unk_dev[1]))
            ).all()
            return len(unk_dev)
