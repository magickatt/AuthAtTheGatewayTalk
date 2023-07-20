from user import User

class Order:
    ...

class OrderDatabaseAdapter:

    def select_orders_by_user_id(user_id: str):
        sql = f"""SELECT o.* 
            FROM orders AS o 
            INNER JOIN users AS u 
            ON o.user_id = u.id 
            WHERE u.id = '{user_id}'"""

class OrderRepository:

    def __init__(self, adapter: OrderDatabaseAdapter) -> None:
        self._adapter = adapter

    def get_orders_by_user(user: User) -> list[Order]:
        ...


class OrderService:
    ...
