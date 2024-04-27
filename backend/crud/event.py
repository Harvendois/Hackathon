from datetime import datetime
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.exceptions.event import EventNotFound
from backend.models.event import Event
from backend.models.post import Post
from backend.schemas.enums import EventType, SchoolType
from backend.schemas.event import EventCreateIn, EventUpdateIn


def create_event(
    db: Session,
    request_data: EventCreateIn,
) -> Event:
    # create a event
    event = Event.create(
        **request_data.model_dump(),
    )
    db.add(event)
    db.commit()

    return event


def update_event(
    db: Session,
    request_data: EventUpdateIn,
) -> Event:
    # retrieve event from db
    statement = select(Event).where(Event.id == request_data.id)

    event: Event = db.execute(statement).scalars().one_or_none()

    if not event:
        raise EventNotFound(
            event_id=request_data.id,
        )

    # update event
    event.update(
        **request_data.model_dump(),
    )

    db.commit()
    db.refresh(event)

    return event


def get_event(
    db: Session,
    event_id: UUID,
) -> Event:
    # retrieve event from db
    statement = select(Event).where(Event.id == event_id)

    event: Event = db.execute(statement).scalars().one_or_none()

    if not event:
        raise EventNotFound(
            event_id=event_id,
        )

    return event


def get_events(
    db: Session,
    company_id: UUID | None,
    institute_id: UUID | None,
    event_type: EventType | None,
    school_type: SchoolType | None,
    title: str | None,
    start_dt: datetime | None,
    end_dt: datetime | None,
    venue: str | None,
    details: str | None,
    contact_info: str | None,
    verified: bool | None,
    page: int,
    per_page: int,
) -> tuple[list[Post], int]:
    # retrieve event from db
    statement = select(Event)

    if company_id:
        statement = statement.where(Event.company_id == company_id)
    if institute_id:
        statement = statement.where(Event.institute_id == institute_id)
    if event_type:
        statement = statement.where(Event.event_type == event_type)
    if school_type:
        statement = statement.where(Event.school_type == school_type)
    if title:
        statement = statement.where(Event.title == title)
    if start_dt:
        statement = statement.where(Event.start_dt == start_dt)
    if end_dt:
        statement = statement.where(Event.end_dt == end_dt)
    if venue:
        statement = statement.where(Event.venue == venue)
    if details:
        statement = statement.where(Event.details == details)
    if contact_info:
        statement = statement.where(Event.contact_info == contact_info)
    if verified:
        statement = statement.where(Event.verified == verified)

    # get total count
    total_count = (
        db.execute(select(func.count()).select_from(statement)).scalars().one()
    )

    # get events
    statement = statement.offset((page - 1) * per_page).limit(per_page)

    events = db.execute(statement).scalars().all()

    return events, total_count
