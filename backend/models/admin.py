from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

__all__ = ["Admin"]

if TYPE_CHECKING:
    from .user import User


class Admin(UUIDBase):
    __tablename__ = "admins"

    name: Mapped[str] = MappedColumn(String())
    email: Mapped[str] = MappedColumn(String())

    user_id: Mapped[UUID] = MappedColumn(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(
        back_populates="admin",
        single_parent=True,
    )
