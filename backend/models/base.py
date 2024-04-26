from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import func, text
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn

__all__ = ["UUIDBase"]


class UUIDBase(DeclarativeBase):
    id: Mapped[UUID] = MappedColumn(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        server_default=text("gen_random_uuid()"),
    )
    create_dt: Mapped[datetime] = MappedColumn(
        postgresql.TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
    update_dt: Mapped[datetime | None] = MappedColumn(
        postgresql.TIMESTAMP(timezone=True),
        onupdate=func.now(),
        nullable=True,
    )
