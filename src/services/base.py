from sqlalchemy.exc import NoResultFound, IntegrityError

from repositories.base import DatabaseRepository


class BaseService:
    def __init__(self, repository: DatabaseRepository = DatabaseRepository):
        self.repository: DatabaseRepository = repository()

    async def get(self, **kwargs):
        try:
            result = await self.repository.retrieve(**kwargs)
            return result
        except NoResultFound:
            return None

    async def list(self, **kwargs):
        try:
            result = await self.repository.list(**kwargs)
            return result
        except NoResultFound:
            return None

    async def add(self, **kwargs):
        try:
            return await self.repository.create(**kwargs)
        except IntegrityError as e:
            print(str(e))
            return None

    async def update(self, pk: int, **kwargs):
        try:
            return await self.repository.update(pk, **kwargs)
        except IntegrityError:
            return None

    async def delete(self, **kwargs):
        try:
            return await self.repository.delete(**kwargs)
        except IntegrityError:
            return None
