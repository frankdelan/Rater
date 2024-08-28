from repositories.base import AbstractRepository
from services.base import BaseService


class UserService(BaseService):
    def __init__(self, repository: type[AbstractRepository]):
        super().__init__(repository)

