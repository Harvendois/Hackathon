from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

__all__ = ["Institute"]

if TYPE_CHECKING:
    from .post import Post
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
    posts: Mapped[list["Post"]] = relationship(
        back_populates="institute",
    )

    @classmethod
    def create(
        cls,
        location: str,
        website: str,
        business_license: str,
        user_id: UUID,
    ) -> "Institute":
        return cls(
            id=uuid4(),
            location=location,
            website=website,
            business_license=business_license,
            user_id=user_id,
        )

    def approve(self) -> None:
        self.user.approve()

    def update(
        self,
        location: str,
        website: str,
        business_license: str,
    ) -> None:
        self.location = location
        self.website = website
        self.business_license = business_license
