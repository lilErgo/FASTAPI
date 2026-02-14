from POSTGRES.models.crypto_table import Base

from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class UserProfile(Base):
    __tablename__ = "UserProfile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    access_tocken: Mapped[str] = mapped_column(nullable=False)