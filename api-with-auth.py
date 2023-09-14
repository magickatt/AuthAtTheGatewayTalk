from flask import Response, jsonify
from database import get_database_connection
from decorators import key_required
from factory import create_order_service, create_user_service
from user import PartialUser
from app import create_app
import logging

app = create_app()

@app.route("/")
def list_users():
    logging.info("Listing Users with orders")
    service = create_user_service(get_database_connection())
    users = service.get_users()
    return jsonify({
        "users": [user.model_dump() for user in users]
    })

@app.route("/orders")
@key_required
def list_orders(authenticated_user):
    logging.info(f"Listing orders for User {authenticated_user.name}")
    service = create_order_service(get_database_connection())
    orders = service.get_orders_by_user(authenticated_user)
    return jsonify({
        "user": f"{authenticated_user.name}",
        "orders": [order.model_dump() for order in orders]
    })
