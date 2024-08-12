from sqlalchemy.orm import declared_attr, Mapped, mapped_column


class BaseMixin:
    # __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
