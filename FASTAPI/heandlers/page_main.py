from fastapi import APIRouter, HTTPException
from fixture import json_data
from ..schema.tasks import Task_FA
from FASTAPI.dependency import get_task_repo,get_task_cache_task,get_task_server
from POSTGRES.services.task_service import TaskService
from typing import Annotated
from fastapi import Depends
from POSTGRES.repository.connections import TaskRepo
from POSTGRES.repository.cache import CacheTask
from POSTGRES.services.task_service import TaskService



router = APIRouter(prefix="/page_main",tags=['page_main'])

@router.get(
    '/all',
    response_model=list[Task_FA]
)
async def get_all_tasks(
    task_service: Annotated[TaskService, Depends(get_task_server)]
) -> list[Task_FA]:
    return task_service.get_service_task()


@router.get(
    '/all/{id}',
    response_model=list[Task_FA]
)
async def get_id_task(
    id: int,
    task_repository: Annotated[TaskRepo, Depends(get_task_repo)]
) -> list[Task_FA]:
    tasks: list[Task_FA] = task_repository.get_tiker_by_rec_id(id)  # Fixed typo: get_tiker_by_id -> get_ticker_by_id
    return  tasks
# async def json_get(sender:str):
#     list_of_sender = []
#     for i in json_data:
#         for n in i.values():
#             if n == sender:
#                 list_of_sender.append(i)
#     return list_of_sender

@router.post(
            '/tas',
            response_model=Task_FA,
            )
async def main(task_res: Task_FA, 
               task_repository: Annotated[TaskRepo, Depends(get_task_repo)]):
    
    task_repository.create_task(task_res)
    return task_res

@router.patch(
            '/sender={sender}',
            response_model=list[Task_FA]
            )
async def patch_setings(record_id, price, task_repository: Annotated[TaskRepo, Depends(get_task_repo)]) -> list[Task_FA]:
    return task_repository.update_task(record_i=record_id,pric=price)

# @router.put('/{sender}')
# async def patch_setings(patch,name):
#     return f'вы успешно пропатчили {patch,name}'

@router.delete('/sender={sender}')
async def del_setings(reg_id: int,task_repository: Annotated[TaskRepo, Depends(get_task_repo)]):
    result:list[Task_FA] = task_repository.get_tiker_by_rec_id(reg_id)
    if result:
        task_repository.delete_task_by_id(reg_id=reg_id)
    return f'Запись: (id= {reg_id}, coin_id= {result[0].id}, price= {result[0].price}, time= {result[0].time}) успешно удаленна'







