from sqlite3 import Connection, Row

from pydantic import BaseModel

from key import KeyRepository, PartialKey


class PartialUser(BaseModel):
    """Lazy-loaded user, used to represent a user without having to fetch the
    corresponding record from the data source (which is why it only has an ID)"""

    user_id: str

    def __str__(self) -> str:
        return f"User ID '{self.user_id}'"


class User(PartialUser):
    "User that has placed orders."
    name: str
    key: PartialKey

    def __str__(self) -> str:
        return f"User '{self.name}'"


class UserDatabaseAdapter:
    def __init__(self, database_connection: Connection):
        self._connection = database_connection

    def select_users(self) -> list[Row]:
        sql = f"""SELECT * 
            FROM users AS u
            INNER JOIN keys AS k
            ON u.id = k.user_id"""
        cursor = self._connection.cursor()
        return cursor.execute(sql).fetchall()

    def select_user_by_api_key(self, api_key: str) -> Row:
        sql = f"""SELECT * 
            FROM users AS u
            INNER JOIN keys AS k
            ON u.id = k.user_id
            WHERE k.key = '{api_key}'"""
        cursor = self._connection.cursor()
        return cursor.execute(sql).fetchone()


class UserRepository:
    def __init__(self, adapter: UserDatabaseAdapter) -> None:
        self._adapter = adapter

    def get_users(self) -> list[User]:
        records = self._adapter.select_users()
        return [self._hydrate_user_from_record(record) for record in records]

    def get_user_by_api_key(self, api_key: str) -> list[User]:
        record = self._adapter.select_user_by_api_key(api_key)
        return self._hydrate_user_from_record(record)

    @staticmethod
    def _hydrate_user_from_record(record: Row) -> User:
        return User(
            user_id=record["id"],
            name=record["name"],
            key=KeyRepository.hydrate_key_from_record(record),
        )


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def get_users(self) -> list[User]:
        return self._repository.get_users()

    def get_user_by_api_key(self, api_key: str) -> User | None:
        return self._repository.get_user_by_api_key(api_key)
