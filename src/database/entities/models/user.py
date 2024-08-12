from typing import Optional

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.entities import Base
from database.entities.mixins import BaseMixin


class User(BaseMixin, Base):
    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[Optional[str]]
    records: Mapped[list['Record']] = relationship(back_populates='user', lazy='selectin')
    ratings: Mapped[list['Rating']] = relationship(back_populates='user', lazy='selectin')
