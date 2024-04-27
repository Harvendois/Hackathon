#!/usr/bin/env python3
# import frontend
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from backend.apis.login import router as login_router
from backend.settings.db import (close_database_connection_pools,
                                 open_database_connection_pools)
from frontend import init as frontend_init


@asynccontextmanager
async def lifespan(app: FastAPI):
    # open database connection pools
    open_database_connection_pools()

    yield

    # close database connection pools
    close_database_connection_pools()


app = FastAPI(root_path="/api", lifespan=lifespan)


@app.get("/health")
def read_root() -> str:
    return "OK"


app.include_router(login_router, tags=["login"])

frontend_init(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

