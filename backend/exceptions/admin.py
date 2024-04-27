from uuid import UUID


class AdminNotFound(Exception):
    def __init__(self, id: UUID) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Admin with id {self.id} not found"
