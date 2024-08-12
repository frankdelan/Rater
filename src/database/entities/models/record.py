from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.entities import Base
from database.entities.mixins import BaseMixin


class Record(BaseMixin, Base):
    value: Mapped[str]

    property_id: Mapped[int] = mapped_column(ForeignKey('property.id', ondelete='CASCADE'))
    property: Mapped['Property'] = relationship(back_populates='records', lazy='selectin')

    position_id: Mapped[int] = mapped_column(ForeignKey('position.id', ondelete='CASCADE'))
    position: Mapped['Position'] = relationship(back_populates='records', lazy='selectin')

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship(back_populates='records', lazy='selectin')

