from flask import Flask, render_template, request
from error import AccessError, InputError
from helper import get_contributor, get_ruser, check_password, valid_email, generate_token, validate_token
import json

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
            "body": {"token": token}
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

@app.route('/search/categories')
def form1():
    return render_template('categories.html')

@app.route('/search/ingredients')
def form2():
    return render_template('ingredients.html')

@app.route('/search/category/ingredients')
def form3():
    return render_template('ingredient_category.html')
 
@app.route('/categories', methods = ['GET'])
def categories():
    # Open json file of ingredients and load data
    f = open('data/ingredient_categories_table.json')
    data = json.load(f)

    # Append ingredient categories into a list
    categories = []
    for dict in data:
        categories.append(dict["name"])

    print(categories) 

    # Format return dict
    ret = {"status": 200,
            "body": {"categories": categories}}
        
    return ret

@app.route('/ingredients', methods = ['GET'])
def ingredients():
    # Get user input
    ingredient = request.args['Ingredient']

    # Open json file of ingredients and load data
    f = open('data/ingredients_table.json')
    data = json.load(f)

    # Search ingredient dict for string matches
    suggestions = []
    for dict in data:
        if ingredient.lower() in dict["name"].lower():
            suggestions.append(dict["name"])

    # Format return dict
    ret = {"status": 200,
            "body": {"suggestions": suggestions}}

    return ret

@app.route('/category/ingredients', methods = ['GET'])
def category_ingredients():
    # Get user input (string)
    category = request.args['Category']

    # Load category_id to category name mapping and get id
    i = open('data/ingredient_categories_table.json')
    category_data = json.load(i)
    category_id = 0
    for j in category_data:
        if category == j["name"]:
            category_id = j["category_id"]

    # Load ingredient data and get all ingredient in category
    f = open('data/ingredients_table.json')
    ingredient_data = json.load(f)
    ingredients = []
    for dict in ingredient_data:
        if category_id == dict["ingredient_category_id"]:
            ingredients.append(dict["name"])

    # Format return dict
    if len(ingredients) == 0:
        ret = {"status": 400,
                "body": {"error": "Invalid category name"}}
    else:
        ret = {"status": 200,
                "body": {"ingredients": ingredients}}
    
    return ret

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

