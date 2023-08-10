from functools import wraps
from flask import request, make_response, jsonify
from factory import create_key_service, create_user_service
from database import get_database_connection
import logging

def key_required(f):
    """Authentication and authorisation decorator, used to wrap an API route 
    and allow/deny the request based on the user API key supplied.
    
    Then fetches the corresponding user if their API key is valid.
    https://circleci.com/blog/authentication-decorators-flask/"""

    @wraps(f)
    def decorator(*args, **kwargs):
        database_connection = get_database_connection()
        key_service = create_key_service(database_connection)
        user_service = create_user_service(database_connection)
        if 'x-mycompany-api-key' in request.headers:
            api_key = request.headers['x-mycompany-api-key']
            if key_service.is_key_valid(api_key):
                user = user_service.get_user_by_api_key(api_key)
                logging.info(f"API key was supplied, {user} was found.")            
                return f(user, *args, **kwargs)
            logging.warning("API key was supplied but no user found.")            
            return make_response(jsonify({"error": "Forbidden"}), 403)
        logging.error(f"No API key was supplied")            
        return make_response(jsonify({"error": "Unauthorised"}), 401)
    return decorator

