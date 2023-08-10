import logging
from sqlite3 import Connection

from factory import create_key_service, create_user_service
from user import User
from key import PartialKey


def authenticate_request(headers: dict, database_connection: Connection) -> User | None:
    """Try and extract the API key from the request. If it exists, try and
    fetch the corresponding user for that API key. Return the user if found."""
    key_service = create_key_service(database_connection)
    user_service = create_user_service(database_connection)

    if "x-mycompany-api-key" in headers:
        api_key = headers["x-mycompany-api-key"]
        if key_service.is_key_valid(api_key):
            user = user_service.get_user_by_api_key(api_key)
            logging.info(f"API key was supplied, {user} was found.")
            return user
        logging.warning("API key was supplied but no user found.")
    logging.error(f"No API key was supplied")


def extract_user_from_headers(headers: dict) -> User | None:
    if all(key in headers for key in (
        "x-mycompany-user-id",
        "x-mycompany-user-name",
        "x-mycompany-api-key"
    )):
        return User(
            user_id=headers["x-mycompany-user-id"],
            name=headers["x-mycompany-user-name"],
            key=PartialKey(key=headers["x-mycompany-api-key"])
        )
