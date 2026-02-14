from sqlalchemy import select,delete, update
from sqlalchemy.orm import Session

from POSTGRES.models.crypto_table import crypto_info,crypto_tag
from POSTGRES.database import get_db_session
from FASTAPI.schema import Task_FA

class TaskRepo:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_tiker(self) -> list[Task_FA]:
        with self.db_session() as session:
            task:crypto_info = session.execute(select(crypto_info)).scalars().all()
            return list(task)
        
        
    # def get_tiker_by_id(self, id: int) -> list[crypto_info]:
    #     with self.db_session() as session:
    #         tasks = session.execute(
    #             select(crypto_info).where(crypto_info.id == id)
    #         ).scalars().all()
    #         return tasks  # Always
    
    def get_tiker_by_rec_id(self, uid: int) -> list[Task_FA]:
        with self.db_session() as session:
            tasks: crypto_info = session.execute(select(crypto_info).where(crypto_info.record_id == uid)).scalars().all()
            # print(tasks.id)
            return list(tasks)
        
    def create_task(self, tasks: Task_FA) -> int:#, task: crypto_info
        task = crypto_info(id = tasks.id, price = tasks.price, time = tasks.time )
        with self.db_session() as session:
            session.add(task)
            session.commit()
            return task.record_id
        
    def update_task(self, record_i, pric) :
        querry = update(crypto_info).where(crypto_info.record_id == record_i).values(price=pric).returning(crypto_info.record_id)
        with self.db_session() as session:
            rec_id = session.execute(querry).scalar_one_or_none()
            session.commit()
            
            return self.get_tiker_by_rec_id(uid=rec_id)


            
    def delete_task_by_id(self,reg_id: int) -> list[Task_FA]:
        with self.db_session() as session:
            result:crypto_info = session.execute(delete(crypto_info).where(crypto_info.record_id == reg_id))
            session.commit()
            print(result)
            return result


    def get_crypto_by_name(self, name):
        query = select(crypto_info).join(crypto_tag,crypto_info.id == crypto_tag.id).where(crypto_tag.name == name)
        with self.db_session() as session:
            task: list[crypto_info] = session.execute(query).scalars().all()
            return task




    

def get_session():
    db_sessio = get_db_session()
    return TaskRepo(db_session=db_sessio)

