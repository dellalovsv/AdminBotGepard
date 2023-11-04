from . import Session
from funcs import dt
from funcs.models.dillers import Diller as model_diller


def check_exists_diller(diller: str = None) -> bool:
    session = Session()
    dillers = session.query(model_diller).filter(model_diller.name == f'{diller}').count()
    if dillers > 0:
        return True
    else:
        return False


def new_diller(name: str = None, phone: str = None, address: str = None) -> bool:
    if check_exists_diller(name) is False:
        session = Session()
        diller = model_diller(name=name, phone=phone, address=address, date_add=dt.get_now()[0])
        session.add(diller)
        session.commit()
        return True
    else:
        return False
