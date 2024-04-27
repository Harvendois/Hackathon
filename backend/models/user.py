from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

__all__ = ["User"]

if TYPE_CHECKING:
    from .admin import Admin
    from .company import Company
    from .institute import Institute
    from .student import Student


class User(UUIDBase):
    __tablename__ = "users"
    name: Mapped[str] = MappedColumn(String())
    email: Mapped[str] = MappedColumn(String(), unique=True)
    password: Mapped[str] = MappedColumn(String())

    student: Mapped["Student"] = relationship("Student", back_populates="user")
    institute: Mapped["Institute"] = relationship("Institute", back_populates="user")
    company: Mapped["Company"] = relationship("Company", back_populates="user")
    admin: Mapped["Admin"] = relationship("Admin", back_populates="user")

    @classmethod
    def create(
        cls,
        name: str,
        email: str,
        password: str,
    ) -> "User":
        return cls(
            id=uuid4(),
            name=name,
            email=email,
            password=password,
        )
