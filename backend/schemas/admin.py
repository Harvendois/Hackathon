from uuid import UUID

from pydantic import BaseModel, EmailStr


class AdminCreateIn(BaseModel):
    email: EmailStr
    password: str
    name: str


class AdminOut(BaseModel):
    id: UUID
