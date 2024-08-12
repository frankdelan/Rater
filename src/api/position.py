from fastapi import APIRouter

from schemas.position import PositionCreateSchema
from schemas.response import ResponseSchema
from services.position import PositionService

position_router = APIRouter(
    prefix='/api/v1/positions',
    tags=['Position']
)


@position_router.post('/create')
async def add_position(data: PositionCreateSchema):
    result = await PositionService().add(**data.model_dump())
    if result:
        return ResponseSchema()
    return ResponseSchema(status=400, detail='Position not create')
