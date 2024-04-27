from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Boolean, ForeignKey, String, false
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

if TYPE_CHECKING:
    from .company import Company
    from .institute import Institute


class Post(UUIDBase):
    __tablename__ = "posts"
    title: Mapped[str] = MappedColumn(String())
    company_id: Mapped[UUID | None] = MappedColumn(
        ForeignKey("companies.id", ondelete="CASCADE"), nullable=True
    )
    company: Mapped["Company"] = relationship(
        back_populates="posts",
    )
    institute_id: Mapped[UUID | None] = MappedColumn(
        ForeignKey("institutes.id", ondelete="CASCADE"), nullable=True
    )
    institute: Mapped["Institute"] = relationship(
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
    verified: Mapped[bool] = MappedColumn(Boolean(), server_default=false())

    @classmethod
    def create(
        cls,
        title: str,
        company_id: UUID,
        institute_id: UUID,
        start_dt: datetime,
        end_dt: datetime,
        type: str,
        location: str,
        responsibilities: str,
        requirements: str,
        salary: str,
        documents: str,
        deadline: datetime,
        recruiter_contacts: str,
    ) -> "Post":
        return cls(
            id=uuid4(),
            title=title,
            company_id=company_id,
            institute_id=institute_id,
            start_dt=start_dt,
            end_dt=end_dt,
            type=type,
            location=location,
            responsibilities=responsibilities,
            requirements=requirements,
            salary=salary,
            documents=documents,
            deadline=deadline,
            recruiter_contacts=recruiter_contacts,
        )

    def approve(self) -> None:
        self.verified = True

    def update(
        self,
        title: str,
        company_id: UUID,
        institute_id: UUID,
        start_dt: datetime,
        end_dt: datetime,
        type: str,
        location: str,
        responsibilities: str,
        requirements: str,
        salary: str,
        documents: str,
        deadline: datetime,
        recruiter_contacts: str,
    ) -> None:
        self.title = title
        self.company_id = company_id
        self.institute_id = institute_id
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.type = type
        self.location = location
        self.responsibilities = responsibilities
        self.requirements = requirements
        self.salary = salary
        self.documents = documents
        self.deadline = deadline
        self.recruiter_contacts = recruiter_contacts
        self.verified = False
