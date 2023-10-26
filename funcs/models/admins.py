from . import BaseModel

from sqlalchemy import Column, Integer, BigInteger, String, Date, Float, Text, Boolean


class Admin(BaseModel):
    __tablename__ = 'admins'
    id = Column(String(12), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    position = Column(Integer, nullable=False, default=0)
    regdate = Column(Date, nullable=False, default="0000-00-00")
    password = Column(String(255), nullable=False)
    gid = Column(Integer, nullable=False, default=0)
    aid = Column(Integer, primary_key=True, unique=True, nullable=False)
    disable = Column(Integer, nullable=False, default=False)
    phone = Column(String(16), nullable=False, default="")
    web_options = Column(Text, nullable=False)
    email = Column(String(35), nullable=False, default="")
    comments = Column(Text, nullable=False)
    domain_id = Column(Integer, nullable=False, default=0)
    min_search_chars = Column(Integer, nullable=False, default=0)
    max_rows = Column(Integer, nullable=False, default=0)
    address = Column(String(60), nullable=False, default="")
    cell_phone = Column(String(20), nullable=False, default="")
    pasport_num = Column(String(16), nullable=False, default="")
    pasport_date = Column(Date, nullable=False, default="0000-00-00")
    pasport_grant = Column(String(100), nullable=False, default="")
    inn = Column(String(20), nullable=False, default="")
    birthday = Column(Date, nullable=False, default="0000-00-00")
    max_credit = Column(Float, nullable=False, default=0.00)
    credit_days = Column(Integer, nullable=False, default=0)
    full_log = Column(Boolean, nullable=False, default=False)
    api_key = Column(String(100), nullable=False, default="")
    gps_imei = Column(String(15), nullable=False, default="")
    start_work = Column(Date, nullable=False, default="0000-00-00")
    tid = Column(BigInteger, nullable=False, default=0, comment="id пользователя телеграм")
