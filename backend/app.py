from flask import Flask, jsonify, request
import json
from data.create_token import generate_token
from werkzeug.exceptions import HTTPException
from error import EmailAlreadyInUse, InputError

app = Flask(__name__)

@app.route("/auth/register", methods = ['POST'])
def register():
    req = request.get_json()
    email = req['email']
    password = req['password']
    username = req['username']

    if not email or not password or not username:
        raise InputError

    fp1 = open('./data/rusers_table.json', 'r')
    ruser_data = json.load(fp1)
    for ruser in ruser_data:
        if ruser['email'] == email:
            raise EmailAlreadyInUse

    ruser_id = len(ruser_data)
    print(ruser_id)
    ruser_data.append({"ruser_id": ruser_id, "email": email, "password": password, "username": username, "profile_picture": ''})
    fp1.close()
    fp = open('./data/rusers_table.json', 'w')
    fp.write(json.dumps(ruser_data))
    fp.close()

    token = generate_token(email)
    fp2 = open('data/tokens_table.json', 'r')
    token_data = json.load(fp2)
    token_data.append({"token": token, "user_id": ruser_id, "is_contributor": False})
    fp2.close()
    fp = open('./data/tokens_table.json', 'w')
    json.dump(token_data, fp)
    fp.close()

    status_code = 200
    response = {
        "success": True,
        "body": {
            "token": token
        }
    }

    return jsonify(response), status_code

# @app.errorhandler(HTTPException)
# def handle_error(error):
#     message = error.message
#     status_code = error.status_code
#     success = False
#     response = {
#         'success': success,
#         'error': {
#             'type': error.__class__.__name__,
#             'message': message
#         }
#     }
#     print(error)

#     return jsonify(response), status_code

    

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)