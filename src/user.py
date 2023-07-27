class PartialUser:

    def __init__(self, user_id: str) -> None:
        self._id = user_id

    @property
    def id(self) -> str:
        return self._id

class User(PartialUser):

    def __init__(self, user_id: str, name: str) -> None:
        self._name = name
        super().__init__(user_id)

    @property
    def name(self) -> str:
        return self._name
