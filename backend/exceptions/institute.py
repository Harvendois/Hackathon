from uuid import UUID


class InstituteNotFound(Exception):
    def __init__(self, id: UUID) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Institute with id {self.id} not found"
