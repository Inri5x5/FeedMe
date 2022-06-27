from flask import Flask, jsonify, request
import json
from data.create_token import generate_token
from werkzeug.exceptions import HTTPException
from json import dumps
from error import EmailAlreadyInUse, InputError

def defaultHandler(err):
    response = err.get_response()
    print(response)
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
            print('ERRORR')
            # raise EmailAlreadyInUse
            raise InputError("Email already in use!")

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

@app.route('/categories', methods = ['GET'])
def categories():
    # Open json file of ingredients and load data
    f = open('data/ingredient_categories_table.json')
    data = json.load(f)

    # Append ingredient categories into a list
    categories = []
    for dict in data:
        categories.append({"name": dict["name"], "c_id": dict["category_id"]})

    print(categories) 

    # Format return dict
    ret = {"status": 200,
            "body": {"categories": categories}}
        
    return ret
    
@app.route('/ingredients', methods = ['GET'])
def ingredients():
    # Get user input
    ingredient = request.args.get('query')

    # Open json file of ingredients and load data
    f = open('data/ingredients_table.json')
    data = json.load(f)

    # Search ingredient dict for string matches
    suggestions = []
    for dict in data:
        if ingredient.lower() in dict["name"].lower():
            suggestions.append({"name": dict["name"], "i_id": dict["ingredient_id"], "c_id": dict["ingredient_category_id"]})

    # Format return dict
    ret = {"status": 200,
            "body": {"suggestions": suggestions}}

    return ret

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
