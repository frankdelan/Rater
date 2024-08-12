from repositories.rating import RatingRepository
from services.base import BaseService


class RatingService(BaseService):
    def __init__(self, repository: RatingRepository = RatingRepository):
        super().__init__(repository)
