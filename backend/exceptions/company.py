from uuid import UUID


class CompanyNotFound(Exception):
    def __init__(self, id: UUID) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Company with id {self.id} not found"
