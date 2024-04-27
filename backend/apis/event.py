from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.crud.event import create_event, get_event, update_event
from backend.exceptions.event import EventNotFound
from backend.schemas.base import PaginationOut
from backend.schemas.event import (
    EventCreateIn,
    EventFilterIn,
    EventIDOut,
    EventOut,
    EventUpdateIn,
)
from backend.settings.db import get_db_sess

router = APIRouter()


@router.post(
    "/events{event_id}",
    response_model=EventIDOut,
    status_code=status.HTTP_201_CREATED,
)
def create_a_event(
    request_data: EventCreateIn,
    db: Session = Depends(get_db_sess),
):
    event = create_event(db, request_data)
    return EventIDOut(
        event_id=event.id,
    )


@router.patch(
    "/events{event_id}",
    response_model=EventIDOut,
    status_code=status.HTTP_200_OK,
)
def update_a_event(
    event_id: UUID,
    request_data: EventUpdateIn,
    db: Session = Depends(get_db_sess),
):
    try:
        update_event(db, request_data)
    except EventNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.get(
    "/events/{event_id}",
    response_model=EventIDOut,
    status_code=status.HTTP_200_OK,
)
def get_a_event(
    event_id: UUID,
    db: Session = Depends(get_db_sess),
):
    try:
        event = get_event(db, event_id)
    except EventNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    return EventOut(
        **event.model_dump(),
    )


@router.get(
    "/events",
    response_model=PaginationOut,
    status_code=status.HTTP_200_OK,
)
def get_events(
    request_data: EventFilterIn,
    db: Session = Depends(get_db_sess),
):
    events, count = get_events(db, **request_data.model_dump())
    return PaginationOut(
        total=count,
        page=request_data.page,
        per_page=request_data.per_page,
        items=events,
    )
