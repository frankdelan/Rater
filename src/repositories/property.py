from database.entities.models.property import Property
from repositories.base import DatabaseRepository


class PropertyRepository(DatabaseRepository):
    model = Property
