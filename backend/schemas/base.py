from typing import Any

from pydantic import BaseModel


class PaginationOut(BaseModel):
    total: int
    page: int
    per_page: int
    items: list[Any]
