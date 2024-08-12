from typing import Optional

from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.entities import Base
from database.entities.mixins import BaseMixin


class Property(BaseMixin, Base):
    name: Mapped[str]

    rating_id: Mapped[int] = mapped_column(ForeignKey('rating.id', ondelete='CASCADE'))
    rating: Mapped['Rating'] = relationship(back_populates='properties', lazy='selectin')

    records: Mapped[list['Record']] = relationship(back_populates='property', lazy='selectin')

    user_id: Mapped[Optional[int]] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))
