from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

__all__ = ["Student"]

if TYPE_CHECKING:
    from .user import User


class Student(UUIDBase):
    __tablename__ = "students"
    school: Mapped[str] = MappedColumn(String())
    major: Mapped[str] = MappedColumn(String())
    enrollment_cert: Mapped[str] = MappedColumn(String())
    student_id_card: Mapped[str] = MappedColumn(String())

    user_id: Mapped[UUID] = MappedColumn(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(
        back_populates="student",
        single_parent=True,
    )

    @classmethod
    def create(
        cls,
        school: str,
        major: str,
        enrollment_cert: str,
        student_id_card: str,
        user_id: UUID,
    ) -> "Student":
        return cls(
            id=uuid4(),
            school=school,
            major=major,
            enrollment_cert=enrollment_cert,
            student_id_card=student_id_card,
            user_id=user_id,
        )
