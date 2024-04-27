from uuid import UUID


class StudentNotFound(Exception):
    def __init__(self, id: UUID) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Student with id {self.id} not found"
