from database.entities import User
from repositories.base import DatabaseRepository


class UserRepository(DatabaseRepository):
    model = User
