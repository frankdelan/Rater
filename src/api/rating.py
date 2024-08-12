from fastapi import APIRouter

from database.entities.models.rating import Rating
from schemas.response import ResponseSchema
from services.rating import RatingService

rating_router = APIRouter(
    prefix='/api/v1/ratings',
    tags=['Ratings']
)


@rating_router.get('/user/{user_id}', response_model=ResponseSchema)
async def get_ratings_by_user(user_id: int):
    result: list[Rating] = await RatingService().list(user_id=user_id)
    if result:
        data = [Rating.to_schema(item) for item in result]
        return ResponseSchema(data=data)
    return ResponseSchema(status=404, detail='Ratings of this user not found')


@rating_router.get('/{rating_id}', response_model=ResponseSchema)
async def get_rating_by_id(rating_id: int):
    result = await RatingService().get(id=rating_id)
    if result:
        return ResponseSchema(data=Rating.to_schema(result))
    return ResponseSchema(status=404, detail='Rating not found')


@rating_router.post('/create/', response_model=ResponseSchema)
async def add_rating(user_id: int, title: str):
    result = await RatingService().add(user_id=user_id, title=title)
    if result:
        return ResponseSchema(data=Rating.to_schema(result))
    return ResponseSchema(status=404, detail='Rating not create')
