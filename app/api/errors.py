```python
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from . import api

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

@api.errorhandler(400)
def bad_request(e):
    return error_response(400)

@api.errorhandler(404)
def not_found(e):
    return error_response(404)

@api.errorhandler(500)
def internal_server_error(e):
    return error_response(500)
```