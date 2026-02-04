from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from typing import Optional

class Base(DeclarativeBase):
    # УБРАТЬ это: id: Any
    # УБРАТЬ это: __name__: str (это не нужно)
    
    __allow_unmapped__ = False  # лучше False если не уверены

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class crypto_info(Base):
    # __tablename__ будет "cryptoinfo" из Base.__tablename__
    # но у вас есть явное объявление ниже, которое переопределит
    
    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[int]
    time: Mapped[str]

class crypto_tag(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]














# from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy.sql import func
# from ..config import settings

# class CryptoInfo(settings): # type: ignore
#     __tablename__ = "crypto_info"

#     id = Column(Integer, primary_key=True, index=True,autoincrement=True)
#     name = Column(String, index=True)
#     price = Column(Float)
#     time = Column(Float)

# class CryptoTag(settings): # type: ignore
#     __tablename__ = "crypto_tags"

#     id = Column(Integer, primary_key=True, index=True,autoincrement=True)
#     name = Column(String, index=True)






















   