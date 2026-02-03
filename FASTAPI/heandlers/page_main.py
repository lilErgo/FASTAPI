from fastapi import APIRouter, HTTPException
from fixture import json_data
from ..schema.tasks import Task



router = APIRouter(prefix="/page_main",tags=['page_main'])


@router.get(
            '/all',
            response_model=list[Task]
           )
async def json_get(sender:str):
    list_of_sender = []
    for i in json_data:
        for n in i.values():
            if n == sender:
                list_of_sender.append(i)
    return list_of_sender
                

@router.post(
            '/tas',
            response_model=Task
            )
async def main(task: Task):
    json_data.append(task.model_dump())
    return task

@router.patch(
            '/{sender}',
            response_model=Task
            )
async def patch_setings(sender,price):
    for task in json_data:
        if task['sender'] == sender:
            task['price'] = price
            return task

# @router.put('/{sender}')
# async def patch_setings(patch,name):
#     return f'вы успешно пропатчили {patch,name}'

@router.delete('/{sender}')
async def del_setings(sender):
    for id,task in enumerate(json_data):
        if task['sender'] == sender:
            del json_data[id]
            return f'вы успешно удалили {task}'
            