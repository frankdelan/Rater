from typing import Optional

from pydantic import BaseModel

from schemas.position import PositionReadSchema


class RatingReadSchema(BaseModel):
    id: int
    title: str
    positions: list[Optional[PositionReadSchema]]

    class Config:
        from_attributes = True
