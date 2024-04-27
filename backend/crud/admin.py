from uuid import UUID

import bcrypt
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.exceptions.company import CompanyNotFound
from backend.exceptions.institute import InstituteNotFound
from backend.exceptions.student import StudentNotFound
from backend.exceptions.user import EmailAlreadyTaken
from backend.models.admin import Admin
from backend.models.company import Company
from backend.models.institute import Institute
from backend.models.student import Student
from backend.models.user import User
from backend.schemas.admin import AdminCreateIn


def create_admin(
    db: Session,
    request_data: AdminCreateIn,
) -> Admin:
    # verify that email is not already taken
    statement = select(User).where(User.email == request_data.email)
    user = db.execute(statement).scalars().one_or_none()

    if user:
        raise EmailAlreadyTaken(
            email=request_data.email,
        )

    # first create a user
    user = User.create(
        name=request_data.name,
        email=request_data.email,
        password=bcrypt.hashpw(
            request_data.password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8"),
    )

    # then create an admin
    admin = Admin.create(
        user_id=user.id,
    )

    db.add(user)
    db.add(admin)
    db.commit()

    return admin


def approve_student(
    db: Session,
    id: UUID,
) -> None:
    # get student
    statement = (
        select(Student).options(selectinload(Student.user)).where(Student.id == id)
    )
    student: Student | None = db.execute(statement).scalars().one_or_none()

    if not student:
        raise StudentNotFound(
            id=id,
        )

    # approve student
    student.approve()
    db.commit()


def reject_student(
    db: Session,
    id: UUID,
) -> None:
    # get student
    statement = (
        select(Student).options(selectinload(Student.user)).where(Student.id == id)
    )
    student: Student | None = db.execute(statement).scalars().one_or_none()

    if not student:
        raise StudentNotFound(
            id=id,
        )

    db.delete(student.user)
    db.commit()


def approve_company(
    db: Session,
    id: UUID,
) -> None:
    # get company
    statement = (
        select(Company).options(selectinload(Company.user)).where(Company.id == id)
    )
    company: Company | None = db.execute(statement).scalars().one_or_none()

    if not company:
        raise CompanyNotFound(
            id=id,
        )

    # approve company
    company.approve()
    db.commit()


def reject_company(
    db: Session,
    id: UUID,
) -> None:
    # get company
    statement = (
        select(Company).options(selectinload(Company.user)).where(Company.id == id)
    )

    company: Company | None = db.execute(statement).scalars().one_or_none()

    if not company:
        raise CompanyNotFound(
            id=id,
        )

    db.delete(company.user)
    db.commit()


def approve_institute(
    db: Session,
    id: UUID,
) -> None:
    # get institute
    statement = (
        select(Institute)
        .options(selectinload(Institute.user))
        .where(Institute.id == id)
    )
    institute: Institute | None = db.execute(statement).scalars().one_or_none()

    if not institute:
        raise InstituteNotFound(
            id=id,
        )

    # approve institute
    institute.approve()
    db.commit()


def reject_institute(
    db: Session,
    id: UUID,
) -> None:
    # get institute
    statement = (
        select(Institute)
        .options(selectinload(Institute.user))
        .where(Institute.id == id)
    )

    institute: Institute | None = db.execute(statement).scalars().one_or_none()

    if not institute:
        raise InstituteNotFound(
            id=id,
        )

    db.delete(institute.user)
    db.commit()
