from datetime import datetime
from sqlite3 import Connection, Row
from typing import Optional

from pydantic import BaseModel

class PartialKey(BaseModel):
    key: str

class Key(PartialKey):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    expires_at: Optional[datetime]

class KeyDatabaseAdapter:
    def __init__(self, database_connection: Connection):
        self._connection = database_connection

    def select_key(self, api_key: str) -> Row:
        sql = f"""SELECT * 
            FROM keys
            WHERE key = '{api_key}'"""
        cursor = self._connection.cursor()
        return cursor.execute(sql).fetchone()


class KeyRepository:
    def __init__(self, adapter: KeyDatabaseAdapter) -> None:
        self._adapter = adapter

    def get_key(self, api_key: str) -> Key | None:
        if record := self._adapter.select_key(api_key):
            return self.hydrate_key_from_record(record)

    @classmethod
    def hydrate_key_from_record(cls, record: Row) -> Key:
        return Key(
            key=record["key"],
            created_at=record["created_at"],
            updated_at=record["updated_at"],
            expires_at=record["expires_at"],
        )


class KeyService:
    def __init__(self, repository: KeyRepository) -> None:
        self._repository = repository

    def is_key_valid(self, api_key: str) -> bool:
        return isinstance(self._repository.get_key(api_key), Key)
