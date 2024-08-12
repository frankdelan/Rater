from pydantic import BaseModel, ConfigDict


class UserReadSchema(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class UserCreateSchema(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True
