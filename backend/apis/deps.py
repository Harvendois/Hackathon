from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.requests import Request

from backend.models.admin import Admin
from backend.settings.db import get_db_sess


def get_admin(request: Request, db: Session = Depends(get_db_sess)) -> Admin:
    admin: Admin = (
        db.execute(select(Admin).where(Admin.user_id == request.state.user_id))
        .scalars()
        .one_or_none()
    )

    if admin is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admin Not Found",
        )

    return admin
