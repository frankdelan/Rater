from fastapi import Depends

from repositories.property import PropertyRepository
from services.base import BaseService


class PropertyService(BaseService):
    def __init__(self, repository: PropertyRepository = PropertyRepository):
        super().__init__(repository)
