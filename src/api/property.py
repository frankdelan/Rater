from fastapi import APIRouter

from schemas.property import PropertyCreateSchema
from schemas.response import ResponseSchema
from services.property import PropertyService

property_router = APIRouter(
    prefix='/api/v1/properties',
    tags=['Property']
)


@property_router.post('/create')
async def add_property(data: PropertyCreateSchema):
    result = await PropertyService().add(**data.model_dump())
    if result:
        return ResponseSchema()
    return ResponseSchema(status=400, detail='Property not create')
