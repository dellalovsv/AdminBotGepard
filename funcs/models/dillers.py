from . import BaseModel

from sqlalchemy import Column, Integer, String, Text, Boolean, Date


class Diller(BaseModel):
    __tablename__ = 'bot_dillers'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    phone = Column(String(25), nullable=False, default="0")
    address = Column(Text, nullable=False)
    disable = Column(Boolean, nullable=False, default=0)
    date_add = Column(Date, nullable=False, default='0000-00-00')
