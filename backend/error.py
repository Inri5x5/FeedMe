from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    status = 403
    statusText = 'No message specified'

class InputError(HTTPException):
    code = 400
    massage = 'No message specified'

class EmailAlreadyInUse(InputError):
    statusText = 'Email already in use, please enter a different email'