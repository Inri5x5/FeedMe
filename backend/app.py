from flask import Flask, request
import json
from data.create_token import generate_token

app = Flask(__name__)

@app.route("/auth/register", methods = ['POST'])
def register():
    email = request.args['email']
    password = request.args['password']
    username = request.args['username']

    fp = open('data/rusers_table.json')
    ruser_data = json.load(fp)

    ruser_data.append({"ruser_id": len(fp.readlines()), "email": email, "password": password, "username": username})

    to_return = {"status": 200, "body": {generate_token(email)}}
    # error checking ? email already in use, email not a real email, password not long enough, etc.

    return to_return