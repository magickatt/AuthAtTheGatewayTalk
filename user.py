class User:

    def __init__(self, user_id: str) -> None:
        self._id = user_id

    @property
    def id(self) -> str:
        return self._id
