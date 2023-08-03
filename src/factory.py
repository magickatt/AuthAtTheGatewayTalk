from sqlite3 import Connection
import order, user, key

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

def create_key_service(database_connection: Connection) -> key.KeyService:
    return key.KeyService(
        key.KeyRepository(
            key.KeyDatabaseAdapter(database_connection)
        )
    )
