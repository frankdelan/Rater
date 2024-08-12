from database.entities.models.position import Position
from repositories.base import DatabaseRepository


class PositionRepository(DatabaseRepository):
    model = Position
