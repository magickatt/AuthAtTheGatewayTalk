from flask import Response
from database import get_database_connection
from decorators import key_required
from factory import create_order_service
from user import PartialUser
from app import create_app

app = create_app()

@app.route("/")
@key_required
def hello_world():
    return Response({
        "greeting2": ["hello", "world"]
    })

@app.route("/users")
def list_users():
    service = create_order_service(get_database_connection())
    orders = service.get_orders_by_user(PartialUser(user_id="7fdbaa00-d971-47e2-8988-024e78bb6224"))
    return Response(orders)

@app.route("/orders")
def list_orders():
    service = create_order_service(get_database_connection())
    orders = service.get_orders_by_user(PartialUser(user_id="7fdbaa00-d971-47e2-8988-024e78bb6224"))
    return Response(orders)
