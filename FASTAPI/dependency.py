from POSTGRES.repository import connections,TaskRepo
from POSTGRES.repository import get_db_session

def get_task_repo() -> TaskRepo:
    db_session = get_db_session()
    return TaskRepo(db_session)