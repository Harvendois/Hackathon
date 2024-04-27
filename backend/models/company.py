from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

__all__ = ["Company"]

if TYPE_CHECKING:
    from .posts import Post
    from .user import User


class Company(UUIDBase):
    __tablename__ = "companies"

    location: Mapped[str] = MappedColumn(String())
    website: Mapped[str] = MappedColumn(String())
    business_license: Mapped[str] = MappedColumn(String())
    user_id: Mapped[UUID] = MappedColumn(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(
        back_populates="company",
        single_parent=True,
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="company",
    )

    @classmethod
    def create(
        cls,
        location: str,
        website: str,
        business_license: str,
        user_id: UUID,
    ) -> "Company":
        return cls(
            location=location,
            website=website,
            business_license=business_license,
            user_id=user_id,
        )

    def approve(self) -> None:
        self.user.approve()
