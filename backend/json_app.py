from operator import is_
from flask import Flask, render_template, request
from error import AccessError, InputError
from helper import get_contributor, get_ruser, check_password, generate_token, validate_token, valid_email
import json
from json import dumps

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

app = Flask(__name__)

app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.register_error_handler(Exception, defaultHandler)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        req = request.get_json()
        email = req['email']
        password = req['password']
        is_contributor = req['is_contributor']

        # Check email
        if not valid_email(email):
            raise InputError("Invalid email")

        # Get user id
        if is_contributor:
            user_id = get_contributor(email)
        else:
            user_id = get_ruser(email)
        
        # User does not exist
        if (user_id < 0):
            raise InputError("User is not registered")

        # Check password
        if not check_password(email, password, is_contributor):
            raise InputError("Incorrect password")
        
        # Get tokens json file
        f = open('./data/tokens_table.json', 'r')
        tokens = json.load(f)
        f.close()
        
        # Create token 
        token = generate_token(email)

        # Update tokens json file
        tokens.append({
            "token": token,
            "user_id": user_id,
            "is_contributor": is_contributor
            })
        f = open('./data/tokens_table.json', 'w')
        f.write(json.dumps(tokens))
        f.close()

        return {
            "status": 200,
            "body": {"token": token , "is_contributor": is_contributor}
        }

@app.route('/logout', methods = ['POST'])
def logout():

    req = request.get_json()
    token = req['token']

    # Validate token
    if not validate_token(token):
        raise InputError("Invalid token")
        
    # Delete token from tokens json file
    f = open('./data/tokens_table.json', 'r')
    tokens = json.load(f)
    f.close()

    tokens = [i for i in tokens if not (i["token"] == token)]

    f = open('./data/tokens_table.json', 'w+')
    f.write(json.dumps(tokens))
    f.close()

    return {
        "status": 200,
        "body": {}
    }
 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)