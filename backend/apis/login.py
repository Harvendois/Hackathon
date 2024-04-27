from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.crud.admin import create_admin
from backend.crud.company import create_company
from backend.crud.institute import create_institute
from backend.crud.student import create_student
from backend.exceptions.user import EmailAlreadyTaken, UserNotFound
from backend.schemas.admin import AdminOut
from backend.schemas.company import CompanyCreateIn, CompanyCreateOut
from backend.schemas.institute import InstituteCreateIn, InstituteCreateOut
from backend.schemas.student import StudentCreateIn, StudentCreateOut
from backend.schemas.user import RefreshToken, UserCreateIn, UserIn, UserTokenOut
from backend.settings.db import get_db_sess
from backend.utils.auth import authenticate, create_access_token, refresh_access_token

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
    try:
        user = authenticate(db, request_data)
    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )
    else:
        access_token = create_access_token(user)
        return UserTokenOut(
            token=access_token,
            user_id=user.id,
            email=user.email,
        )


@router.post(
    "/register-student",
    response_model=StudentCreateOut,
    status_code=status.HTTP_201_CREATED,
)
def register_student(
    request_data: StudentCreateIn,
    db: Session = Depends(get_db_sess),
):
    try:
        student = create_student(db, request_data)
    except EmailAlreadyTaken as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    else:
        return StudentCreateOut(
            id=student.id,
        )


@router.post(
    "/register-company",
    response_model=CompanyCreateOut,
    status_code=status.HTTP_201_CREATED,
)
def register_company(
    request_data: CompanyCreateIn,
    db: Session = Depends(get_db_sess),
):
    try:
        company = create_company(db, request_data)
    except EmailAlreadyTaken as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    else:
        return CompanyCreateOut(
            id=company.id,
        )


@router.post(
    "/register-institute",
    response_model=InstituteCreateOut,
    status_code=status.HTTP_201_CREATED,
)
def register_institute(
    request_data: InstituteCreateIn,
    db: Session = Depends(get_db_sess),
):
    try:
        institute = create_institute(db, request_data)
    except EmailAlreadyTaken as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    else:
        return InstituteCreateOut(
            id=institute.id,
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
    try:
        admin = create_admin(db, request_data)
    except EmailAlreadyTaken as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    else:
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
