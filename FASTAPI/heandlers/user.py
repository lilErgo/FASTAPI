from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends

from POSTGRES.services.user import UserService
from FASTAPI.dependency import get_user_services

from FASTAPI.schema.user import UserSchemaModel, UserSchemaModelDoCreate

router = APIRouter(prefix="/user",tags=['user'])

@router.post("",response_model=UserSchemaModel)
def create_user(  # убрали async
    body: UserSchemaModelDoCreate, 
    user_service: Annotated[UserService, Depends(get_user_services)]
):
    return user_service.create_user(body.username, body.password)