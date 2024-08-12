from repositories.user import UserRepository
from services.base import BaseService


class UserService(BaseService):
    def __init__(self, repository: UserRepository = UserRepository):
        super().__init__(repository)
