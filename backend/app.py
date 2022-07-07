from unicodedata import category
from flask import Flask, jsonify, render_template, request
from error import AccessError, InputError
from helper import get_contributor, get_ruser, check_password, valid_email, generate_token, validate_token, add_token, delete_token, db_connection
from json import dumps
import json


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

########################## SPRINT 1 ##########################
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
    
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        conn = db_connection()

        req = request.get_json()
        email = req['email']
        password = req['password']
        is_contributor = req['is_contributor']

        # Check email
        if not valid_email(email):
            raise InputError("Invalid email")

        # Get user id
        if is_contributor:
            user_id = get_contributor(conn, email)
        else:
            user_id = get_ruser(conn, email)
        
        # User does not exist
        if (user_id < 0):
            raise InputError("User is not registered")

        # Check password
        if not check_password(conn, email, password, is_contributor):
            raise InputError("Incorrect password")
        
        # Create token 
        token = generate_token(email)

        # Update tokens json file
        add_token(token, user_id, is_contributor)

        return {
            "status": 200,
            "body": {"token": token , "is_contributor": is_contributor}
        }

@app.route('/logout', methods = ['POST'])
def logout():
    conn = db_connection()

    req = request.get_json()
    token = req['token']

    # Validate token
    if not validate_token(conn, token):
        raise InputError("Invalid token")
        
    # Delete token from tokens json file
    delete_token(conn, token)

    return {
        "status": 200,
        "body": {}
    }

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

########################## SPRINT 2 ##########################

# Getting tag categories
@app.route('/search/tag/categories', methods = ['GET'])
def search_tag_categories():
    tag_categories = []

    conn = db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Tag_Categories')
    info = cur.fetchall()
    for i in info: 
        tag_category_id, name = i
        tag_categories.append(
            {"name": name, "category_id": tag_category_id}
        )
    cur.close()

    return {
        "tag_categories": tag_categories
    }

# Getting tags
@app.route('search/tag/tags', methods = ['GET'])
def search_tag_tags():
    tags = []

    conn = db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Tags')
    info = cur.fetchall()
    for i in info:
        tag_id, tag_category_id, name = i
        tags.append(
            {"name": name, "tag_id": tag_id}
        )
    cur.close()

    return {
        "tags": tags
    }


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
