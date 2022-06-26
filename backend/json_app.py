from flask import Flask, render_template, request
from helper import get_contributor, get_ruser, check_password, generate_token
import json

app = Flask(__name__)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        is_contributor = request.form.get('is_contributor')

        # Get user id
        if is_contributor:
            user_id = get_contributor(email)
        else:
            user_id = get_ruser(email)
        
        # User does not exist
        if (user_id < 0):
            return {
                "status": 400,
                "body": {"error": "Email is not registered"}
            }

        # Check password
        if not check_password(email, password, is_contributor):
            return {
                "status": 400,
                "body": {"error": "Wrong password"}
            }
        
        # Get tokens json file
        f = open('backend/data/tokens_table.json', 'r')
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
        f = open('backend/data/tokens_table.json', 'w')
        f.write(json.dumps(tokens))
        f.close()

        return {
            "status": 200,
            "body": {"token": token, "is_contributor": is_contributor}
        }

@app.route('/logout', methods = ['GET'])
def logout():
    token = request.form.get('token')

    # Get tokens json file
    f = open('backend/data/tokens_table.json', 'r')
    tokens = json.load(f)
    f.close()

    # Validate token
    token_exists = False
    for t in tokens:
        if t["token"] == token:
            token_exists = True
            
    if not token_exists:
        return {
            "status": 400,
            "body": {"error": "Invalid token"}
        }
        
    # Delete token from tokens json file
    tokens = [i for i in tokens if not (i["token"] == token)]
    f = open('backend/data/tokens_table.json', 'w+')
    f.write(json.dumps(tokens))
    f.close()

    return {
        "status": 200
    }

 
if __name__ == '__main__':
    app.run(host='localhost', port=5000)