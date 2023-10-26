from . import BaseModel

from sqlalchemy import Column, Integer, BigInteger, String, Date, Float, Text, Boolean


class Lease(BaseModel):
    __tablename__ = 'dhcphosts_leases'

