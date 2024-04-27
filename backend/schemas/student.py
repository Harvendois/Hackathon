from uuid import UUID

from pydantic import BaseModel, EmailStr

from .enums import SchoolType


class StudentCreateIn(BaseModel):
    email: EmailStr
    password: str
    name: str
    school: SchoolType
    major: str
    enrollment_cert: str
    student_id_card: str


class StudentCreateOut(BaseModel):
    id: UUID
