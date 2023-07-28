from sqlite3 import Connection
import order, user

def create_order_service(database_connection: Connection) -> order.OrderService:
    return order.OrderService(
        order.OrderRepository(
            order.OrderDatabaseAdapter(database_connection)
        )
    )

def create_user_service(database_connection: Connection) -> user.UserService:
    return user.UserService(
        user.UserRepository(
            user.UserDatabaseAdapter(database_connection)
        )
    )
