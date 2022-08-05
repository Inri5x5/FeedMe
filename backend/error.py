from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    code = 403
    massage = 'No message specified'

class InputError(HTTPException):
    code = 400
    massage = 'No message specified'

class EmailAlreadyInUse(InputError):
    statusText = 'Email already in use, please enter a different email'