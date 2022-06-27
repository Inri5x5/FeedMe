from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    status_code = 403
    message = 'No message specified'

class InputError(HTTPException):
    status_code = 400
    message = 'Incorrect input, please check and try again'

class EmailAlreadyInUse(InputError):
    message = 'Email already in use, please enter a different email'