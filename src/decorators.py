from functools import wraps
from flask import request, make_response, jsonify

def key_required(f):
    """Authentication and authorisation decorator, used to wrap an API route 
    and allow/deny the request based on the user API key supplied.
    
    Then fetches the corresponding user if their API key is valid.
    https://circleci.com/blog/authentication-decorators-flask/"""

    @wraps(f)
    def decorator(*args, **kwargs):
        if 'x-mycompany-api-key' in request.headers:
            api_key = request.headers['x-mycompany-api-key']
            return f(api_key, *args, **kwargs)
        return make_response(jsonify({"error": "Unauthorised"}), 401)
    return decorator

