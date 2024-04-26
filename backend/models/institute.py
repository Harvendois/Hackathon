from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

__all__ = ["Institute"]

if TYPE_CHECKING:
    from .user import User


class Institute(UUIDBase):
    __tablename__ = "institutes"

    location: Mapped[str] = MappedColumn(String())
    website: Mapped[str] = MappedColumn(String())
    business_license: Mapped[str] = MappedColumn(String())

    user_id: Mapped[UUID] = MappedColumn(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(
        back_populates="institute",
        single_parent=True,
    )
