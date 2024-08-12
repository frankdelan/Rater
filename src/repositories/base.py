from abc import ABC, abstractmethod

from sqlalchemy import select, insert, delete, update

from database.connection import async_session_factory


class AbstractRepository(ABC):
    @abstractmethod
    async def retrieve(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def list(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *args, **kwargs):
        raise NotImplementedError


class DatabaseRepository(AbstractRepository):
    model = None

    async def retrieve(self, **kwargs):
        async with async_session_factory() as session:
            query = select(self.model).filter_by(**kwargs)
            result = await session.execute(query)
        return result.scalar_one_or_none()

    async def list(self, **kwargs):
        async with async_session_factory() as session:
            query = select(self.model).filter_by(**kwargs)
            result = await session.execute(query)
        return result.scalars().all()

    async def create(self, **kwargs):
        async with async_session_factory() as session:
            stmt = insert(self.model).values(**kwargs).returning(self.model)
            result = await session.execute(stmt)
            await session.commit()
        return result.scalar_one_or_none()

    async def update(self, pk: int, **kwargs):
        async with async_session_factory() as session:
            stmt = update(self.model).filter_by(id=pk).values(**kwargs).returning(self.model)
            result = await session.execute(stmt)
            await session.commit()
        return result.scalar_one_or_none()

    async def delete(self, **kwargs):
        async with async_session_factory() as session:
            stmt = delete(self.model).filter_by(**kwargs).returning(self.model)
            result = await session.execute(stmt)
            await session.commit()
        return result.scalar_one_or_none()
