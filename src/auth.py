import logging
from sqlite3 import Connection

from factory import create_key_service, create_user_service
from user import User
from key import PartialKey
from headers import API_KEY, USER_ID, USER_NAME




def authenticate_request(headers: dict, database_connection: Connection) -> User | None:
    """Try and extract the API key from the request. If it exists, try and
    fetch the corresponding user for that API key. Return the user if found."""
    key_service = create_key_service(database_connection)
    user_service = create_user_service(database_connection)

    if API_KEY in headers:
        api_key = headers[API_KEY]
        if key_service.is_key_valid(api_key):
            user = user_service.get_user_by_api_key(api_key)
            logging.info(f"API key was supplied, {user} was found.")
            return user
        logging.warning("API key was supplied but no user found.")
    else:
        logging.error(f"No API key was supplied")


def extract_user_from_headers(headers: dict) -> User | None:
    if all(key in headers for key in (
        USER_ID,
        USER_NAME,
        # Probably want to still check this is set ideally,
        # commenting out for demonstration purposes
        # API_KEY
    )):
        logging.warn(f"User {headers[USER_NAME]} found in headers sent from standalone auth")        
        return User(
            user_id=headers[USER_ID],
            name=headers[USER_NAME],
            key=PartialKey(key=headers[API_KEY])
        )
    else:
        logging.error(f"User cannot be extracted from headers (headers found are {' '.join(headers.keys())})")        
