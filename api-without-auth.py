from flask import Response, jsonify
from database import get_database_connection
from decorators import key_required
from factory import create_order_service, create_user_service
from user import PartialUser
from app import create_app

app = create_app()

@app.route("/")
def list_users():
    service = create_user_service(get_database_connection())
    users = service.get_users()
    return jsonify({
        "users": [user.model_dump() for user in users]
    })

@app.route("/orders")
def list_orders(authenticated_user):
    service = create_order_service(get_database_connection())
    orders = service.get_orders_by_user(PartialUser(user_id=authenticated_user.user_id))
    return jsonify({
        "user": f"{authenticated_user.name}",
        "orders": [order.model_dump() for order in orders]
    })
