from os import times_result
from reprlib import recursive_repr
from flask import Flask, jsonify, render_template, request
from error import AccessError, InputError
from helper import get_contributor, get_ruser, check_password, valid_email, generate_token, validate_token, decode_token, add_token, delete_token, db_connection, get_recipe_steps, get_tag_categories, get_tags
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
        token = generate_token(email, is_contributor)

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
        raise AccessError("Invalid token")
        
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

@app.route('/search/tag/categories', methods = ['GET'])
def search_tag_categories():
    conn = db_connection()

    # Validate token
    req = request.get_json()
    token = req['token']
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Get tag categories
    tag_categories = get_tag_categories(conn)

    return {
        "tag_categories": tag_categories
    }

@app.route('/search/tag/tags', methods = ['GET'])
def search_tag_tags():
    conn = db_connection()

    # Get params
    req = request.get_json()
    token = req['token']
    tag_category_id = req['tag_category_id']

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Get tags
    tags = get_tags(conn, tag_category_id)

    return {
        "tags": tags
    }

@app.route('/search/recipes', methods = ['POST'])
def search_recipes():
    conn = db_connection()
    cur = conn.cursor()

    # Get params
    req = request.get_json()
    token = req['token']
    ingredients_id = req['ingredients_id']

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    recipes = []

    # cur.execute('''
    #     SELECT *, GROUP_CONCAT(i.ingredient_id)
    #     FROM    Recipes r
    #             LEFT JOIN Steps s on s.recipe_id = r.recipe_id
    #             LEFT JOIN Ingredient_In_Recipe ir on ir.recipe_id = r.recipe_id
    #             LEFT JOIN Ingredients i on i.ingredient_id = ir.ingredient_id
    #     GROUP BY r.recipe_id
    # ''')
    # info = cur.fetchall()
    # cur.close()

    # recipes = []
    # for i in info:
    #     recipes.append({
    #         "recipe_id": recipe_id,
    #         "title": title,
    #         "description": description,
    #         "img": img,
    #         "video": video,
    #         "time_required": time_required,
    #         "steps": steps,
    #         "tags": get_tags(conn, None),
    #         "author": author,
    #         "public_state": public_state,
    #         "ingredients": ingredients,
    #         "skill_videos": skill_vidoes
    #     })
    
    return {
        "recipes": recipes
    }

@app.route('/statistics', methods = ['GET'])
def statistics():
    conn = db_connection()

    # Validate token
    req = request.get_json()
    token = req['token']
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Check if user is a contributor
    user_details = decode_token(conn, token)
    if user_details["is_contributor"] is False:
        raise AccessError("User is not a Contributor")

    # Get contributor id
    contributor_id = user_details["user_id"]

    cur = conn.cursor()
    qry = '''
        SELECT r.recipe_id
        FROM recipes r
            JOIN public_recipes pr ON pr.recipe_id = r.recipe_id
            JOIN recipe_ratings rr ON rr.recipe_id = r.recipe_id
        WHERE pr.contributor_id = %s
        GROUP BY r.recipe_id
    '''
    cur.execute(qry, [contributor_id])
    info = cur.fetchall()
    cur.close()

    statistics = []

    return {
        "statistics": statistics
    }


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
