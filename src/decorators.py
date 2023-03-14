from functools import wraps
from flask import request

# Authentication decorator
def key_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        api_key = None
        if 'x-mycompany-api-key' in request.headers:
            print(f"x-company-api-key header is {request.headers}")
        return f(*args, **kwargs)
    return decorator