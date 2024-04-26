from typing import AsyncIterable, Optional

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine as Database
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from .config import SQLALCHEMY_DATABASE_URI

__all__ = [
    "get_db_conn",
    "get_db_sess",
    "open_database_connection_pools",
    "close_database_connection_pools",
]
_db_conn: Optional[Database] = None


async def open_database_connection_pools():
    global _db_conn
    _db_conn = create_engine(
        SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, pool_size=10, max_overflow=20
    )
    # Base.metadata.create_all(bind=_db_conn)
    return


async def close_database_connection_pools():
    global _db_conn
    if _db_conn:
        _db_conn.dispose()


async def get_db_conn() -> Database:
    assert _db_conn is not None
    return _db_conn


async def get_db_sess(db_conn=Depends(get_db_conn)) -> AsyncIterable[Session]:
    sess = Session(bind=db_conn)
    try:
        yield sess
    finally:
        sess.close()
