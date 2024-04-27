import bcrypt
from sqlalchemy.orm import Session

from backend.models.admin import Admin
from backend.models.user import User
from backend.schemas.admin import AdminCreateIn


def create_admin(
    db: Session,
    request_data: AdminCreateIn,
) -> Admin:
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
