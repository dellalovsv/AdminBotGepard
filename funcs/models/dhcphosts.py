from . import BaseModel

from sqlalchemy import Column, Integer, Index, String, DateTime, Boolean


class Lease(BaseModel):
    __tablename__ = 'dhcphosts_leases'

    start = Column(DateTime, nullable=False, default="0000-00-00 00:00:00")
    ends = Column(DateTime, nullable=False, default="0000-00-00 00:00:00")
    state = Column(Boolean, nullable=False, default=0)
    hardware = Column(String(20), nullable=False, default="00:00:00:00:00:00")
    uid = Column(String(30), nullable=False, default="0")
    circuit_id = Column(String(25))
    remote_id = Column(String(25))
    hostname = Column(String(30))
    nas_id = Column(Integer, nullable=False, default=0)
    ip = Column(Integer, primary_key=True, nullable=False, default=0)
    port = Column(String(11))
    vlan = Column(Integer, default=0)
    switch_mac = Column(String(20))
    flag = Column(Boolean)

    indexes = [
        Index('ip', ip),
        Index('nas_id', nas_id)
    ]
