from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.entities import Base
from database.entities.mixins import BaseMixin
from schemas.position import PositionReadSchema
from schemas.property import PropertyReadSchema
from schemas.rating import RatingReadSchema


class Rating(BaseMixin, Base):
    title: Mapped[str]
    positions: Mapped[list['Position']] = relationship(back_populates='rating', lazy='selectin')
    properties: Mapped[list['Property']] = relationship(back_populates='rating', lazy='selectin')
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship(back_populates='ratings', lazy='selectin')

    @staticmethod
    def to_schema(rating: 'Rating') -> RatingReadSchema:
        return RatingReadSchema(id=rating.id,
                                title=rating.title,
                                positions=[PositionReadSchema(name=position.name,
                                                              properties=[PropertyReadSchema(name=record.property.name,
                                                                                             value=record.value)
                                                                          for record in position.records])
                                           for position in rating.positions])
