from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

if TYPE_CHECKING:
    from .company import Company


class Post(UUIDBase):
    __tablename__ = "posts"
    title: Mapped[str] = MappedColumn(String())
    company_id: Mapped[UUID] = MappedColumn(
        ForeignKey("companies.id", ondelete="CASCADE")
    )
    company: Mapped["Company"] = relationship(
        back_populates="posts",
    )

    start_dt: Mapped[datetime] = MappedColumn(postgresql.TIMESTAMP())
    end_dt: Mapped[datetime] = MappedColumn(postgresql.TIMESTAMP())
    type: Mapped[str] = MappedColumn(String())
    location: Mapped[str] = MappedColumn(String())
    responsibilities: Mapped[str] = MappedColumn(String())
    requirements: Mapped[str] = MappedColumn(String())
    salary: Mapped[str] = MappedColumn(String())
    documents: Mapped[str] = MappedColumn(String())
    deadline: Mapped[datetime] = MappedColumn(postgresql.TIMESTAMP())
    recruiter_contacts: Mapped[str] = MappedColumn(String())
