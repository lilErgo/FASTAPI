# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
# from FASTAPI.heandlers.page_main import router as page_main_router
from FASTAPI.heandlers.__init__ import routers


app = FastAPI()

for router in routers:
    app.include_router(router)