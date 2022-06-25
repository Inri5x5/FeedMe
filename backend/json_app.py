from flask import Flask, render_template, request
from helper import create_token
import json

app = Flask(__name__)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']

        # Get users json file
        f = open('users.json')
        users = json.load(f)
        f.close()

        user_exists = 0
        for user in users:
            # User exists
            if user["email"] == email & user["password"] == password:
                user_exists = 1
                is_contributor = user["is_contributor"]
            # User exists but wrong password
            elif user["email"] == email & user["password"] != password:
                return {
                    "status": 400,
                    "body": {"error": "Wrong password"}
                }
        
        # User does not exist
        if not user_exists:
            return {
                "status": 400,
                "body": {"error": "Email is not registered"}
            }
            
        # Get tokens json file
        f = open('tokens.json', 'r')
        tokens = json.load(f)
        f.close()
        
        # Create token and update tokens json file
        token = create_token(email)
        tokens[email] = token
        f = open('tokens.json', 'w+')
        f.write(json.dumps(tokens))
        f.close()

        return {
            "status": 200,
            "body": {"token": token, "is_contributor": is_contributor}
        }

@app.route('/logout', methods = ['GET'])
def logout():
    email = request.json['email']
    token = request.json['token']

    # Get tokens json file
    f = open('tokens.json', 'r')
    tokens = json.load(f)
    f.close()

    # Validate token
    if tokens[email] != token:
        return {
            "status": 400,
            "body": {"error": "Invalid token"}
        }
        
    # Delete token from tokens json file
    tokens.pop(email)
    f = open('tokens.json', 'w+')
    f.write(json.dumps(tokens))
    f.close()

    return {
        "status": 200
    }

 
if __name__ == '__main__':
    app.run(host='localhost', port=5000)