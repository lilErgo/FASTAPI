from fastapi import FastAPI
# from FASTAPI.heandlers.page_main import router as page_main_router
from FASTAPI import routers


app = FastAPI()

for router in routers:
    app.include_router(router)