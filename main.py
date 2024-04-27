#!/usr/bin/env python3
# import frontend
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt  # type: ignore
from jose.exceptions import ExpiredSignatureError, JWTError  # type: ignore
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from backend.apis.admin import router as admin_router
from backend.apis.login import router as login_router
from backend.settings.config import JWT_AUTH
from backend.settings.db import (
    close_database_connection_pools,
    open_database_connection_pools,
)
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


class AuthMiddelware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if not (
            "ping" in str(request.url)
            or "openapi.json" in str(request.url)
            or "redoc" in str(request.url)
            or "doc" in str(request.url)
            or "login" in str(request.url)
            or "refresh-token" in str(request.url)
            or "register" in str(request.url)
        ):
            if not request.headers.get("authorization"):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Request Does Not Include Auth Header",
                )
            token = (
                request.headers.get("authorization")  # type: ignore
                .split(" ")[1]
                .strip()
                .replace("Bearer", "")
            )
            try:
                decoded_jwt = jwt.decode(
                    token,
                    JWT_AUTH["JWT_SECRET_KEY"],
                    algorithms=JWT_AUTH["JWT_ALGORITHM"],
                )
            except ExpiredSignatureError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token Expired",
                )
            except JWTError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid Token",
                )
            user_id = decoded_jwt["id"]
            request.state.user_id = user_id
        try:
            response = await call_next(request)
        except Exception as e:
            exception_dict = {
                "vendor": "IGOTCAREER",
                "type": "error",
                "code": "internal_server_error",
                "detail": f"{e}",
            }
            response = JSONResponse(
                exception_dict, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response


app.add_middleware(AuthMiddelware)

origins = [
    "http://localhost",
    "https://localhost",
    "https://localhost:3000",
    "http://localhost:3000",
    "http://moceancrm.com",
    "https://moceancrm.com",
    "moceancrm.com",
    "moceancrm.com",
    "https://www.moceanbackend.com",
    "http://www.moceanbackend.com",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login_router, tags=["login"])
app.include_router(admin_router, tags=["admin"])

frontend_init(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
