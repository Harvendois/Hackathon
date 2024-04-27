from uuid import UUID

from pydantic import BaseModel, EmailStr


class CompanyCreateIn(BaseModel):
    email: EmailStr
    password: str
    name: str
    location: str
    website: str
    business_license: str


class CompanyCreateOut(BaseModel):
    id: UUID
