from sqlalchemy import select,delete
from sqlalchemy.orm import Session

from POSTGRES.models.crypto_table import crypto_info,crypto_tag
from POSTGRES.database import get_db_session
from FASTAPI.schema import Task_FA

class TaskRepo:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_tiker(self):
        with self.db_session() as session:
            task:list[crypto_info] = session.execute(select(crypto_info)).scalars().all()
            return task
        
    def get_tiker_id(self,id: int) -> list[crypto_info]| None:
        with self.db_session() as session:
            task:list[crypto_info] = session.execute(select(crypto_info).where(crypto_info.id == id)).scalars()
            return task
        
    def create_task(self, tasks: Task_FA):#, task: crypto_info
        task = crypto_info(id = tasks.id, price = tasks.price, time = tasks.time )
        with self.db_session() as session:
            session.add(task)
            session.commit()
            
    def delete_task(self,id: int):
        with self.db_session() as session:
            session.execute(delete(crypto_info).where(crypto_info.record_id == id))
            session.commit()

    def get_crypto_by_name(self, name):
        query = select(crypto_info).join(crypto_tag,crypto_info.id == crypto_tag.id).where(crypto_tag.name == name)
        with self.db_session() as session:
            task: list[crypto_info] = session.execute(query).scalars().all()
            return task




    

def get_session():
    db_sessio = get_db_session()
    return TaskRepo(db_session=db_sessio)

