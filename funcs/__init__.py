from config import DB as db

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


BaseModel = declarative_base()
engine = create_engine(f'mysql+pymysql://{db.user}:{db.passwd}@{db.host}:{db.port}/{db.db}')
Session = sessionmaker(engine)
