class UserNotFound(Exception):
    def __init__(
        self,
        email: str,
    ) -> None:
        self.email = email

    def __str__(self) -> str:
        return f"User with email {self.email} not found"
