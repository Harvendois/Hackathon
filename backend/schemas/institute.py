from uuid import UUID

from pydantic import BaseModel, EmailStr


class InstituteCreateIn(BaseModel):
    email: EmailStr
    password: str
    name: str
    location: str
    website: str
    business_license: str


class InstituteCreateOut(BaseModel):
    id: UUID
