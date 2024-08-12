from fastapi import APIRouter

from database.entities.models.user import User
from schemas.response import ResponseSchema
from schemas.user import UserReadSchema, UserCreateSchema
from services.user import UserService

user_router = APIRouter(
    prefix='/api/v1/users',
    tags=['Users']
)


@user_router.get('/list', response_model=ResponseSchema)
async def get_user_list():
    result: list[User] = await UserService().list()
    if result:
        return ResponseSchema(data=[UserReadSchema.model_validate(item) for item in result])
    return ResponseSchema(status=404, details='No users found')


@user_router.post('/create', response_model=ResponseSchema)
async def add_user(data: UserCreateSchema):
    result: User = await UserService().add(**data.model_dump())
    if result:
        return ResponseSchema(data=UserReadSchema.model_validate(result))
    return ResponseSchema(status=400, details='User add error')


@user_router.put('/update/{user_id}')
async def update_user(data: UserCreateSchema, user_id: int):
    result: User = await UserService().update(user_id, **data.model_dump())
    if result:
        return ResponseSchema(data=UserReadSchema.model_validate(result))
    return ResponseSchema(status=400, details='User update error')


@user_router.delete('/delete/{user_id}')
async def delete_user(user_id: int):
    result: User = await UserService().delete(id=user_id)
    if result:
        return ResponseSchema(data=UserReadSchema.model_validate(result))
    return ResponseSchema(status=400, details='User delete error')


@user_router.get('/{user_id}', response_model=ResponseSchema)
async def get_user(user_id: int):
    result: User = await UserService().get(id=user_id)
    if result:
        return ResponseSchema(data=UserReadSchema.model_validate(result))
    return ResponseSchema(status=404, details='User not found')
