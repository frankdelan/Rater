from typing import Optional

from pydantic import BaseModel

from schemas.property import PropertyReadSchema


class PositionReadSchema(BaseModel):
    name: str
    properties: list[Optional[PropertyReadSchema]]

    class Config:
        from_attributes = True


class PositionCreateSchema(BaseModel):
    name: str
    rating_id: int
    user_id: int

