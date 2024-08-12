from pydantic import BaseModel


class PropertyReadSchema(BaseModel):
    name: str
    value: str

    class Config:
        from_attributes = True


class PropertyCreateSchema(BaseModel):
    name: str
    rating_id: int
    user_id: int
