# Database models using SQLAlchmemy ORM

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    """Administrative user"""

    __tablename__ = "user"

    # TODO: Ask the length of the employee code
    employee_code: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]

    # TODO: Pending fields


Base.metadata.create_all(engine)
