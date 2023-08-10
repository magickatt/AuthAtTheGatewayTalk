from factory import create_key_service, create_user_service
from user import User
from sqlite3 import Connection
from flask import Request

import logging

def authenticate_request(headers: dict, database_connection: Connection) -> User | None:
    """Try and extract the API key from the request. If it exists, try and 
    fetch the corresponding user for that API key. Return the user if found."""
    key_service = create_key_service(database_connection)
    user_service = create_user_service(database_connection)

    if 'x-mycompany-api-key' in headers:
        api_key = headers['x-mycompany-api-key']
        if key_service.is_key_valid(api_key):
            user = user_service.get_user_by_api_key(api_key)
            logging.info(f"API key was supplied, {user} was found.")            
            return user
        logging.warning("API key was supplied but no user found.")
    logging.error(f"No API key was supplied")            
