from base64 import b64encode
from datetime import timedelta
from zoneinfo import ZoneInfo

from loguru import logger
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuration(BaseSettings):
    # config
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # config
    SECRET_KEY: str = Field(validation_alias="SECRET_KEY")

    # database
    POSTGRES_SERVER: str = Field(validation_alias="POSTGRES_SERVER")
    POSTGRES_USER: str = Field(validation_alias="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(validation_alias="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(validation_alias="POSTGRES_DB")
    POSTGRES_PORT: int = Field(validation_alias="POSTGRES_PORT")


CONFIGURATION = Configuration()  # type: ignore


SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
    CONFIGURATION.POSTGRES_USER,
    CONFIGURATION.POSTGRES_PASSWORD,
    CONFIGURATION.POSTGRES_SERVER,
    CONFIGURATION.POSTGRES_PORT,
    CONFIGURATION.POSTGRES_DB,
)

JWT_AUTH = {
    "JWT_SECRET_KEY": b64encode(CONFIGURATION.SECRET_KEY.encode()).decode(),
    "JWT_PUBLIC_KEY": None,
    "JWT_PRIVATE_KEY": None,
    "JWT_ALGORITHM": "HS256",
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LEEWAY": 0,
    "JWT_EXPIRATION_DELTA": timedelta(hours=24),
    "JWT_AUDIENCE": None,
    "JWT_ISSUER": "NIPA",
    "JWT_ALLOW_REFRESH": True,
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=30),  # timedelta(minutes=1),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
}

# TIMEZONE = ZoneInfo("Asia/Seoul")
logger.info(f"SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}")
