from uuid import UUID


class EventNotFound(Exception):
    def __init__(
        self,
        event_id: UUID,
    ):
        self.event_id = event_id

    def __str__(self):
        return f"Event with id {self.event_id} not found."
