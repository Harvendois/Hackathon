# import uuid
# from calendar import timegm
# from datetime import datetime, timedelta
# from typing import Optional

# import bcrypt
# from fastapi import Header
# from jose import jwt
# from models.user import User
# from schemas.user import JWTAuthenticateUser, UserIn
# from settings.config import JWT_AUTH
# from sqlalchemy import Select, select
# from sqlalchemy.orm import Session

# from backend.exceptions.login import UserNotFound

# # from app.schemas import AdminCreateIn, AdminLoginIn, JWTAuthenticateUser
# # from app.settings import JWT_AUTH, TIMEZONE


# def check_jwt(authorization: str = Header(...)):
#     pass


# def verify_password(plain_password, hashed_password):
#     return bcrypt.checkpw(
#         plain_password.encode("utf-8"), hashed_password.encode("utf-8")
#     )


# def get_password_hash(password):
#     return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


# async def update_user_password(
#     db: Session,
#     user_obj: User,
#     password: str,
# ) -> User:
#     user_obj.password = get_password_hash(password).decode("utf-8")
#     db.commit()
#     return user_obj


# async def authenticate(
#     db: Session,
#     user_login_data: UserIn,
# ) -> User:
#     # user: User = (
#     #     db.query(Admin)
#     #     .filter(Admin.username == admin_login_data.username)
#     #     .one_or_none()
#     # )

#     # if not admin:
#     #     raise APIException(
#     #         APIExceptionErrorCodes.OBJECT_NOT_FOUND, message="Admin Not Found"
#     #     )

#     # if verify_password(admin_login_data.password, admin.password):
#     #     return admin
#     # return None
#     statement: Select = select(User).where(User.email == user_login_data.email)

#     user: User | None = await db.execute(statement).scalars().one_or_none()

#     if not user:
#         raise UserNotFound(
#             email=user_login_data.email,
#         )

#     if verify_password(user_login_data.password, user.password):
#         return user

#     return None


# # async def create_admin(db: Session, admin_register_data: AdminCreateIn) -> Admin:
# #     db_obj = Admin(
# #         username=admin_register_data.username,
# #         email=admin_register_data.email,
# #         password=get_password_hash(admin_register_data.password1).decode("utf-8"),
# #         date_joined=datetime.now(TIMEZONE),
# #     )
# #     db.add(db_obj)
# #     db.commit()
# #     db.refresh(db_obj)
# #     return db_obj


# def create_access_token(
#     user: JWTAuthenticateUser,
#     expires_delta: Optional[timedelta] = None,
# ):
#     to_encode = {
#         "id": user.id,
#         "email": user.email,
#         "username": user.username,
#         "exp": datetime.utcnow() + expires_delta
#         if expires_delta
#         else datetime.utcnow() + JWT_AUTH["JWT_EXPIRATION_DELTA"],
#         "refresh_exp": timegm(
#             (
#                 datetime.utcnow() + JWT_AUTH["JWT_REFRESH_EXPIRATION_DELTA"]
#             ).utctimetuple()
#         ),
#         "jti": uuid.uuid4().hex,
#         "orig_iat": timegm(datetime.utcnow().utctimetuple()),
#         "iss": JWT_AUTH["JWT_ISSUER"],
#     }
#     encoded_jwt = jwt.encode(
#         to_encode, JWT_AUTH["JWT_SECRET_KEY"], algorithm=JWT_AUTH["JWT_ALGORITHM"]
#     )
#     return encoded_jwt


# def refresh_access_token(db: Session, token: str):
#     payload = jwt.decode(
#         token,
#         JWT_AUTH["JWT_SECRET_KEY"],
#         algorithms=JWT_AUTH["JWT_ALGORITHM"],
#         options={"verify_exp": False},
#     )
#     admin = db.query(Admin).filter(Admin.id == payload["id"]).one()
#     orig_iat = payload.get("orig_iat")
#     if orig_iat:
#         # Verify expiration
#         now_timestamp = timegm(datetime.utcnow().utctimetuple())
#         if now_timestamp > payload["refresh_exp"]:
#             return None
#         return create_access_token(admin)
#     return None
