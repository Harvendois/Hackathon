from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel

if TYPE_CHECKING:
    pass


class EventCreateIn(BaseModel):
    company_id: UUID | None
    institute_id: UUID | None
    event_type: str
    school_type: str | None
    title: str
    start_dt: datetime
    end_dt: datetime
    venue: str
    details: str
    contact_info: str
    rsvp_info: str | None
    poster: str


class EventUpdateIn(EventCreateIn):
    id: UUID


class EventOut(EventCreateIn):
    id: UUID


class EventIDOut(BaseModel):
    id: UUID


class EventFilterIn(BaseModel):
    company_id: UUID | None
    institute_id: UUID | None
    event_type: str | None
    school_type: str | None
    title: str | None
    start_dt: datetime | None
    end_dt: datetime | None
    venue: str | None
    details: str | None
    contact_info: str | None
    rsvp_info: str | None
    poster: str | None
    page: int | None
    per_page: int | None
