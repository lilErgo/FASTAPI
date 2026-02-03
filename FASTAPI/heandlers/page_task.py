from fastapi import APIRouter

router = APIRouter(prefix="/do_task",tags=['do_task'])

@router.get("/privet")
async def say():
    return {'hello'}

@router.post("/edit")
async def edition():
    return {"some edits"}