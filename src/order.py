from enum import Enum
from sqlite3 import Connection, Row
from user import User, PartialUser
from pdb import set_trace

class OrderStatus(Enum):

    ORDERED = "ordered"
    DELIVERED = "delivered"
    RETURNED = "returned"

class Order:

    def __init__(self, order_id: str, user: PartialUser, item: str, status: OrderStatus) -> None:
        self._id = order_id
        self._user = user
        self._item = item
        self._status = status

class OrderDatabaseAdapter:

    def __init__(self, database_connection: Connection):
        self._connection = database_connection

    def select_orders_by_user_id(self, user_id: str):
        sql = f"""SELECT o.* 
            FROM orders AS o 
            INNER JOIN users AS u 
            ON o.user_id = u.id 
            WHERE u.id = '{user_id}'"""
        cursor = self._connection.cursor()
        return cursor.execute(sql).fetchall()

class OrderRepository:

    def __init__(self, adapter: OrderDatabaseAdapter) -> None:
        self._adapter = adapter

    def get_orders_by_user(self, user: User) -> list[Order]:
        records = self._adapter.select_orders_by_user_id(user.id)
        return [self._hydrate_order_from_record(record) for record in records]

    @staticmethod
    def _hydrate_order_from_record(record: Row) -> Order:
        # set_trace()
        return Order(
            order_id=record["id"],
            user=PartialUser(user_id=record["user_id"]),
            item=record["item"],
            status=OrderStatus(record["status"])
        ) 

class OrderService:

    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def get_orders_by_user(self, user: User) -> list[Order]:
        return self._repository.get_orders_by_user(user)
