from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

__all__ = ["Admin"]

if TYPE_CHECKING:
    from .user import User


class Admin(UUIDBase):
    __tablename__ = "admins"
    user_id: Mapped[UUID] = MappedColumn(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(
        back_populates="admin",
        single_parent=True,
    )

    @classmethod
    def create(
        cls,
        user_id: UUID,
    ) -> "Admin":
        return cls(
            id=uuid4(),
            user_id=user_id,
        )
