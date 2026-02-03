from sqlalchemy.orm import DeclarativeMeta, Mapped, mapped_column

class crypto_info(DeclarativeMeta):
    __tablename__ = "crypto_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[int]
    time: Mapped[str]

class crypto_tag(DeclarativeMeta):
    __tablename__ = "crypto_tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


























# from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy.sql import func
# from ...config import settings

# class Cryptocoin(settings): # type: ignore
#     __tablename__ = "Cryptocoin"

#     id = Column(Integer, primary_key=True, index=True,autoincrement=True)
#     name = Column(String, index=True)
#     price = Column(Float)
#     time = Column(Float)
   