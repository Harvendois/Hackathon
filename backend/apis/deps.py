# from typing import Optional

# from fastapi import Depends, Path
# from sqlalchemy.orm import Session
# from starlette.requests import Request
# from settings.db import get_db_sess

# from app.models import Admin, Customer
# from app.utils.s3 import S3Wrapper


# def get_admin(request: Request, db: Session = Depends(get_db_sess)) -> Admin:
#     admin = db.query(Admin).filter_by(id=request.state.user_id).one_or_none()
#     if admin is None:
#         raise APIException(
#             APIExceptionErrorCodes.OBJECT_NOT_FOUND,
#             message="Admin Not Found",
#         )
#     return admin


# def check_super_admin_status(
#     admin: Admin = Depends(get_admin),
#     db: Session = Depends(get_db_sess),
# ) -> Admin:
#     if not admin.is_super_admin:
#         raise APIException(
#             APIExceptionErrorCodes.FORBIDDEN,
#             message="Not Super Admin",
#         )


# def get_customer_and_check_existence(
#     db: Session = Depends(get_db_sess),
#     customer_id: Optional[int] = Path(..., example="1"),
# ) -> Customer:
#     customer = db.query(Customer).get(customer_id)

#     if not customer:
#         raise APIException(
#             APIExceptionErrorCodes.OBJECT_NOT_FOUND,
#             message="Customer Not Found",
#             data=customer_id,
#         )

#     return customer


# def get_s3_wrapper() -> S3Wrapper:
#     return S3Wrapper()
