from pydantic import BaseModel, EmailStr


class JWTAuthenticateUser(BaseModel):
    id: int
    username: str
    email: str


class RefreshToken(BaseModel):
    token: str


class AdminCreateIn(BaseModel):
    username: str
    email: str
    password1: str
    password2: str

    class Config:
        orm_mode = True


class AdminLoginIn(BaseModel):
    username: str
    password: str


class AdminLoginOut(BaseModel):
    token: str
    user_id: int
    username: str
    email: str


class AdminOut(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    email: EmailStr
    name: str


class UserIn(BaseModel):
    email: EmailStr
    password: str
