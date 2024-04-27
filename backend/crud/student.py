import bcrypt
from sqlalchemy.orm import Session

from backend.models.student import Student
from backend.models.user import User
from backend.schemas.student import StudentCreateIn


def create_student(
    db: Session,
    request_data: StudentCreateIn,
) -> Student:
    # first create a user
    user = User.create(
        name=request_data.name,
        email=request_data.email,
        password=bcrypt.hashpw(
            request_data.password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8"),
    )

    # then create a student
    student = Student.create(
        school=request_data.school,
        major=request_data.major,
        enrollment_cert=request_data.enrollment_cert,
        student_id_card=request_data.student_id_card,
        user_id=user.id,
    )

    db.add(user)
    db.add(student)
    db.commit()

    return student
