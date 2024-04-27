import bcrypt
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.exceptions.user import EmailAlreadyTaken
from backend.models.company import Company
from backend.models.user import User
from backend.schemas.company import CompanyCreateIn


def create_company(
    db: Session,
    request_data: CompanyCreateIn,
) -> Company:
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

    # then create a company
    company = Company.create(
        location=request_data.location,
        website=request_data.website,
        business_license=request_data.business_license,
        user_id=user.id,
    )

    db.add(user)
    db.add(company)
    db.commit()

    return company
