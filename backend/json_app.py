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
        user_id = -1
        is_contributor = False

        # Check user type
        contributor = get_contributor(email)
        ruser = get_ruser(email)
        if (contributor < 0 and ruser < 0): # User does not exist
            return {
                "status": 400,
                "body": {"error": "Email is not registered"}
            }
        elif (contributor >= 0):            # User is a contributor
            user_id = contributor
            is_contributor = True
        elif (ruser >= 0):                  # User is a regular user
            user_id = ruser
            is_contributor = False

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