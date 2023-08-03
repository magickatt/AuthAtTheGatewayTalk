from sqlite3 import Connection, Row

class PartialUser:
    """Lazy-loaded user, used to represent a user without having to fetch the 
    corresponding record from the data source (which is why it only has an ID)"""

    def __init__(self, user_id: str) -> None:
        self._id = user_id

    @property
    def id(self) -> str:
        return self._id

class User(PartialUser):
    "User that has placed orders"

    def __init__(self, user_id: str, name: str) -> None:
        self._name = name
        super().__init__(user_id)

    @property
    def name(self) -> str:
        return self._name

class UserDatabaseAdapter:

    def __init__(self, database_connection: Connection):
        self._connection = database_connection

    def select_users(self):
        sql = "SELECT * FROM users"
        cursor = self._connection.cursor()
        return cursor.execute(sql).fetchall()

class UserRepository:

    def __init__(self, adapter: UserDatabaseAdapter) -> None:
        self._adapter = adapter

    def get_users(self) -> list[User]:
        records = self._adapter.select_users()
        return [self._hydrate_user_from_record(record) for record in records]

    @staticmethod
    def _hydrate_user_from_record(record: Row) -> User:
        return User(
            user_id = record["id"],
            name = record["name"]
        ) 

class UserService:

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def get_users(self) -> list[User]:
        return self._repository.get_users()
