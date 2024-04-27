import uuid
from calendar import timegm
from datetime import UTC, datetime, timedelta
from typing import Optional

import bcrypt
from fastapi import Header
from jose import jwt
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from backend.exceptions.login import UserNotFound
from backend.models.user import User
from backend.schemas.user import JWTAuthenticateUser, UserCreateIn, UserIn
from backend.settings.config import JWT_AUTH


def check_jwt(authorization: str = Header(...)):
    pass


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


def get_password_hash(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def update_user_password(
    db: Session,
    user_obj: User,
    password: str,
) -> User:
    user_obj.password = get_password_hash(password).decode("utf-8")
    db.commit()
    return user_obj


def authenticate(
    db: Session,
    user_login_data: UserIn,
) -> User:
    statement: Select = select(User).where(User.email == user_login_data.email)

    user: User = db.execute(statement).scalars().one_or_none()

    if not user:
        raise UserNotFound(
            email=user_login_data.email,
        )

    if verify_password(user_login_data.password, user.password):
        return user

    return None


def create_user(db: Session, user_register_data: UserCreateIn) -> User:
    user = User.create(
        name=user_register_data.name,
        email=user_register_data.email,
        password=get_password_hash(user_register_data.password).decode("utf-8"),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # statement: Select = select(User).where(User.email == user_register_data.email)
    # user = db.execute(statement).scalars().one()

    return user


def create_access_token(
    user: JWTAuthenticateUser,
    expires_delta: Optional[timedelta] = None,
):
    to_encode = {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "exp": datetime.now(UTC) + expires_delta
        if expires_delta
        else datetime.now(UTC) + JWT_AUTH["JWT_EXPIRATION_DELTA"],
        "refresh_exp": timegm(
            (
                datetime.now(UTC) + JWT_AUTH["JWT_REFRESH_EXPIRATION_DELTA"]
            ).utctimetuple()
        ),
        "jti": uuid.uuid4().hex,
        "orig_iat": timegm(datetime.now(UTC).utctimetuple()),
        "iss": JWT_AUTH["JWT_ISSUER"],
    }
    encoded_jwt = jwt.encode(
        to_encode, JWT_AUTH["JWT_SECRET_KEY"], algorithm=JWT_AUTH["JWT_ALGORITHM"]
    )
    return encoded_jwt


def refresh_access_token(db: Session, token: str):
    payload = jwt.decode(
        token,
        JWT_AUTH["JWT_SECRET_KEY"],
        algorithms=JWT_AUTH["JWT_ALGORITHM"],
        options={"verify_exp": False},
    )
    statement: Select = select(User).where(User.id == payload["id"])

    user: User = db.execute(statement).scalars().one()

    orig_iat = payload.get("orig_iat")
    if orig_iat:
        # Verify expiration
        now_timestamp = timegm(datetime.utcnow().utctimetuple())
        if now_timestamp > payload["refresh_exp"]:
            return None
        return create_access_token(user)
    return None
