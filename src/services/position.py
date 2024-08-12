from repositories.position import PositionRepository
from services.base import BaseService


class PositionService(BaseService):
    def __init__(self, repository: PositionRepository = PositionRepository):
        super().__init__(repository)
