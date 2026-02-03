from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crypto_table import crypto_info
from ...POSTGRES import get_db_session


class TaskRepo:
    def __init__(self,db_session: Session) -> None:
        self.db_session = db_session

    def get_tiker(self,c_id):
        query = select(crypto_info).where(crypto_info.id == c_id)
        with self.db_session as session:
            session.execute(query)

def get_session():
    db_sessio = get_db_session()
    return TaskRepo(db_session=db_sessio)