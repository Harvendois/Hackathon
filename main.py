#!/usr/bin/env python3
# import frontend
import uvicorn
from fastapi import FastAPI

from frontend import init as frontend_init

app = FastAPI(root_path="/api")


@app.get("/health")
def read_root() -> str:
    return "OK"


frontend_init(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

