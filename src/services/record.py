from fastapi import Depends

from repositories.record import RecordRepository
from services.base import BaseService


class RecordService(BaseService):
    def __init__(self, repository: RecordRepository = RecordRepository):
        super().__init__(repository)
