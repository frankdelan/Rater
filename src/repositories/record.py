from database.entities import Record
from repositories.base import DatabaseRepository


class RecordRepository(DatabaseRepository):
    model = Record
