from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel

if TYPE_CHECKING:
    pass


class PostCreateIn(BaseModel):
    title: str
    company_id: UUID | None
    institute_id: UUID | None
    start_dt: datetime
    end_dt: datetime
    type: str
    location: str
    responsibilities: str
    requirements: str
    salary: str
    documents: str
    deadline: datetime
    recruiter_contacts: str


class PostFilterIn(BaseModel):
    title: str | None
    company_id: UUID | None
    institute_id: UUID | None
    start_dt: datetime | None
    end_dt: datetime | None
    type: str | None
    location: str | None
    responsibilities: str | None
    requirements: str | None
    salary: str | None
    documents: str | None
    deadline: datetime | None
    recruiter_contacts: str | None
    page: int | None
    per_page: int | None


class PostUpdateIn(PostCreateIn):
    id: UUID


class PostOut(PostCreateIn):
    id: UUID


class PostIDOut(BaseModel):
    id: UUID
