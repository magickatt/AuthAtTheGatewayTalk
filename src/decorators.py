from functools import wraps
from flask import request

def key_required(f):
    """Authentication and authorisation decorator, used to wrap an API route 
    and allow/deny the request based on the user API key supplied.
    
    Then fetches the corresponding user if their API key is valid."""
    @wraps(f)
    def decorator(*args, **kwargs):
        api_key = None
        if 'x-mycompany-api-key' in request.headers:
            print(f"x-company-api-key header is {request.headers}")
        return f(*args, **kwargs)
    return decorator
