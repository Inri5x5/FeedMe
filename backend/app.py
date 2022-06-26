from flask import Flask, request
import json
from data.create_token import generate_token

app = Flask(__name__)

@app.route("/auth/register", methods = ['POST'])
def register():
    email = request.args['email']
    password = request.args['password']
    username = request.args['username']

    fp1 = open('data/rusers_table.json', 'r')
    ruser_data = json.load(fp1)

    for ruser in ruser_data:
        if ruser['email'] == email:
            to_return = {"status": 400, "body": {"error": "Email already in use, please enter a different email"}}
            return to_return

    ruser_id = len(fp1.readlines())
    ruser_data.append({"ruser_id": ruser_id, "email": email, "password": password, "username": username})
    json.dump(ruser_data, fp1)
    fp1.close()

    token = generate_token(email)
    fp2 = open('data/tokens_table.json', 'w')
    token_data = json.load(fp2)
    token_data.append({"token": token, "user_id": ruser_id, "is_contributor": False})
    json.dump(token_data, fp2)
    fp2.close()

    to_return = {"status": 200, "body": {"token": token}}
    # error checking ? email already in use, email not a real email, password not long enough, etc.

    return to_return