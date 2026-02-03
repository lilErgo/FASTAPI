from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.sql import func
from ...config import settings

class Cryptocoin(settings):
    __tablename__ = "Cryptocoin"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String, index=True)
    price = Column(Float)
    time = Column(Float)
   