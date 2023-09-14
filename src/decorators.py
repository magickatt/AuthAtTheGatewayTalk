from functools import wraps

from flask import jsonify, make_response, request

from auth import authenticate_request, extract_user_from_headers
from database import get_database_connection


def key_required(f):
    """Authentication and authorisation decorator, used to wrap an API route
    and allow/deny the request based on the user API key supplied.

    Then fetches the corresponding user if their API key is valid.
    https://circleci.com/blog/authentication-decorators-flask/"""

    @wraps(f)
    def decorator(*args, **kwargs):
        """If the user can be found from the API key supplied, pass as an
        argument to the API route."""
        if user := authenticate_request(request.headers, get_database_connection()):
            return f(user, *args, **kwargs)
        return make_response(jsonify({"error": "Unauthorised"}), 401)

    return decorator


def headers_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if user := extract_user_from_headers(request.headers):
            return f(user, *args, **kwargs)
        return make_response(jsonify({"error": "Unauthorised"}), 401)

    return decorator
