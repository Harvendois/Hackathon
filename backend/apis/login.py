from fastapi import APIRouter, Depends
from schemas.user import UserIn, UserOut
from settings.db import get_db_sess
from sqlalchemy.orm import Session

router = APIRouter()


@router.post(
    "/login",
    response_model=UserOut,
)
async def login(
    request_data: UserIn,
    db: Session = Depends(get_db_sess),
):
    ...
