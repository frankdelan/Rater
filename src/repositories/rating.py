from database.entities import Rating
from repositories.base import DatabaseRepository


class RatingRepository(DatabaseRepository):
    model = Rating
