from pydantic import BaseModel, EmailStr

__all__ = [
    "JWTAuthenticateUser",
    "RefreshToken",
    "UserOut",
    "UserTokenOut",
    "UserIn",
    "UserCreateIn",
]


class JWTAuthenticateUser(BaseModel):
    id: int
    email: str


class RefreshToken(BaseModel):
    token: str


class UserOut(BaseModel):
    email: EmailStr
    name: str


class UserTokenOut(BaseModel):
    token: str
    user_id: int
    email: EmailStr


class UserIn(BaseModel):
    email: EmailStr
    password: str


class UserCreateIn(UserIn):
    name: str
