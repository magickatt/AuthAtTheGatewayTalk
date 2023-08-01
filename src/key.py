from enum import Enum
from arrow import Arrow as DateTimeArrow, get as convert_string_to_datetime
from sqlite3 import Connection, Row
from user import User, PartialUser

class Key:

    def __init__(self, key: str, created_at: DateTimeArrow, updated_at: DateTimeArrow, expires_at: DateTimeArrow) -> None:
        self._key = key
        self._created_at = created_at
        self._updated_at = updated_at
        self._expires_at = expires_at

class KeyDatabaseAdapter:

    def __init__(self, database_connection: Connection):
        self._connection = database_connection

    def select_key(self, key: str) -> Row:
        sql = f"""SELECT * 
            FROM keys
            WHERE key = '{key}'"""
        cursor = self._connection.cursor()
        return cursor.execute(sql).fetchone()

    def select_key_by_user_id(self, user_id: str) -> Row:
        sql = f"""SELECT * 
            FROM keys
            WHERE user_id = '{user_id}'"""
        cursor = self._connection.cursor()
        return cursor.execute(sql).fetchone()

class KeyRepository:

    def __init__(self, adapter: KeyDatabaseAdapter) -> None:
        self._adapter = adapter

    def get_key(self, key: str) -> Key | None:
        record = self._adapter.select_key(key)
        return self._hydrate_key_from_record(record)

    def get_key_by_user(self, user: User) -> Key | None:
        record = self._adapter.select_key_by_user_id(user.id)
        return self._hydrate_order_from_record(record)

    @staticmethod
    def _hydrate_key_from_record(record: Row) -> Key:
        return Key(
            key=record["key"],
            user=PartialUser(user_id=record["user_id"]),
            created_at=convert_string_to_datetime(record["created_at"]),
            updated_at=convert_string_to_datetime(record["updated_at"]),
            expires_at=convert_string_to_datetime(record["expires_at"]),
        ) 

class KeyService:

    def __init__(self, repository: KeyRepository) -> None:
        self._repository = repository

    def get_key(self, key: str) -> Key | None:
        return self._repository.get_key(key)    

    def get_key_by_user(self, user: User) -> Key | None:
        return self._repository.get_key_by_user(user)
