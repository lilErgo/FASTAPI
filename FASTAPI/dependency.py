# from POSTGRES.repository import TaskRepo, CacheTask
# from POSTGRES.repository import get_db_session
from sqlalchemy.orm import Session

from POSTGRES.repository.connections import TaskRepo
from POSTGRES.repository.cache import CacheTask
from POSTGRES.services.task_service import TaskService
from POSTGRES.database import get_db_session
from POSTGRES.accsessors import create_connection
from POSTGRES.repository.user import UserRepository
from POSTGRES.services.user import UserService

from fastapi import Depends



def get_task_repo(db_session: Session = Depends(get_db_session())) -> TaskRepo:
    return TaskRepo(db_session)

def get_task_cache_task() -> CacheTask:
    redis_session = create_connection()
    return CacheTask(redis_session)

def get_task_server(
        task_repository: TaskRepo = Depends(get_task_repo),
        task_cache: CacheTask = Depends(get_task_cache_task)
) -> TaskService:
    return TaskService(
        task_cache=get_task_cache_task(),
        task_repository= get_task_repo()
    )

def get_user_repo(db_session: Session = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)

def get_user_services(
        user_repo: UserRepository = Depends(get_user_repo)
) -> UserService:
    return UserService(user_repository=user_repo)