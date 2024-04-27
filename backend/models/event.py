from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, String, false
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import UUIDBase

if TYPE_CHECKING:
    from .company import Company
    from .institute import Institute


class Event(UUIDBase):
    __tablename__ = "events"
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
    event_type: Mapped[str] = MappedColumn(String())
    school_type: Mapped[str | None] = MappedColumn(String(), nullable=True)
    title: Mapped[str] = MappedColumn(String())
    start_dt: Mapped[datetime] = MappedColumn(postgresql.TIMESTAMP(timezone=True))
    end_dt: Mapped[datetime] = MappedColumn(postgresql.TIMESTAMP(timezone=True))
    venue: Mapped[str] = MappedColumn(String())
    details: Mapped[str] = MappedColumn(String())
    contact_info: Mapped[str] = MappedColumn(String())
    rsvp_info: Mapped[str | None] = MappedColumn(String(), nullable=True)
    poster: Mapped[str] = MappedColumn(String())
    verified: Mapped[bool] = MappedColumn(Boolean(), server_default=false())

    @classmethod
    def create(
        cls,
        event_type: str,
        school_type: str,
        title: str,
        start_dt: datetime,
        end_dt: datetime,
        venue: str,
        details: str,
        contact_info: str,
        rsvp_info: str,
        poster: str,
    ) -> "Event":
        return cls(
            event_type=event_type,
            school_type=school_type,
            title=title,
            start_dt=start_dt,
            end_dt=end_dt,
            venue=venue,
            details=details,
            contact_info=contact_info,
            rsvp_info=rsvp_info,
            poster=poster,
        )

    def update(
        self,
        event_type: str,
        school_type: str,
        title: str,
        start_dt: datetime,
        end_dt: datetime,
        venue: str,
        details: str,
        contact_info: str,
        rsvp_info: str,
        poster: str,
    ) -> None:
        self.event_type = event_type
        self.school_type = school_type
        self.title = title
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.venue = venue
        self.details = details
        self.contact_info = contact_info
        self.rsvp_info = rsvp_info
        self.poster = poster

    def approve(self) -> None:
        self.verified = True
