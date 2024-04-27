from uuid import UUID


class PostNotFound(Exception):
    def __init__(
        self,
        post_id: UUID,
    ):
        self.post_id = post_id

    def __str__(self):
        return f"Post with id {self.post_id} not found."
