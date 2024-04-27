from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.crud.admin import create_admin
from backend.crud.student import create_student
from backend.schemas.admin import AdminOut
from backend.schemas.student import StudentCreateIn, StudentCreateOut
from backend.schemas.user import (RefreshToken, UserCreateIn, UserIn, UserOut,
                                  UserTokenOut)
from backend.settings.db import get_db_sess
from backend.utils.auth import (authenticate, create_access_token,
                                refresh_access_token)

router = APIRouter()


@router.post(
    "/login",
    response_model=UserTokenOut,
    status_code=status.HTTP_201_CREATED,
)
def login(
    request_data: UserIn,
    db: Session = Depends(get_db_sess),
):
    user = authenticate(db, request_data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = create_access_token(user)
    return UserTokenOut(
        token=access_token,
        user_id=user.id,
        email=user.email,
    )


@router.post(
    "/register-student",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def register_student(
    request_data: StudentCreateIn,
    db: Session = Depends(get_db_sess),
):
    student = create_student(db, request_data)
    return StudentCreateOut(
        id=student.id,
    )


@router.post(
    "/register-admin",
    response_model=AdminOut,
    status_code=status.HTTP_201_CREATED,
)
def register_admin(
    request_data: UserCreateIn,
    db: Session = Depends(get_db_sess),
):
    admin = create_admin(db, request_data)
    return AdminOut(
        id=admin.id,
    )


@router.post("/refresh-token")
def refresh_token(
    request_data: RefreshToken,
    db: Session = Depends(get_db_sess),
):
    refresh_token = refresh_access_token(db, request_data.token)
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Has Expired",
        )
    return refresh_token
