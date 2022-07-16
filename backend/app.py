from flask import Flask, jsonify, render_template, request
from error import AccessError, InputError
from helper import get_contributor, get_ruser, check_password, valid_email, generate_token, validate_token, decode_token, add_token, delete_token, db_connection, get_tag_categories, get_tags, get_recipe_details
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
    ingredients_req = req['ingredients_id']

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    cur.execute('''
        SELECT r.recipe_id, GROUP_CONCAT(ir.ingredient_id)
        FROM    Recipes r
                JOIN Ingredient_in_Recipe ir on ir.recipe_id = r.recipe_id
        GROUP BY r.recipe_id
    ''')
    info = cur.fetchall()
    cur.close()

    recipes = []
    for i in info:
        recipe_id, ingredients = i
        ingredients.split(",")

        if set(ingredients) <= set(ingredients_req) or ingredients_req is None:
            recipe_details = get_recipe_details(conn, recipe_id)
            recipes.append(recipe_details)
    
    return {
        "recipes": recipes
    }

@app.route('/dash/statistics', methods = ['GET'])
def dash_statistics():
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
        SELECT r.recipe_id, 
            SUM(CASE WHEN rr.rating = '1' THEN 1 ELSE 0 END) AS one_rating,
            SUM(CASE WHEN rr.rating = '2' THEN 1 ELSE 0 END) AS two_rating,
            SUM(CASE WHEN rr.rating = '3' THEN 1 ELSE 0 END) AS three_rating,
            SUM(CASE WHEN rr.rating = '4' THEN 1 ELSE 0 END) AS four_rating,
            SUM(CASE WHEN rr.rating = '5' THEN 1 ELSE 0 END) AS five_rating,
        FROM recipes r
            JOIN public_recipes pr ON pr.recipe_id = r.recipe_id
            JOIN recipe_ratings rr ON rr.recipe_id = r.recipe_id
        WHERE pr.author_id = %s
        GROUP BY r.recipe_id
    '''
    cur.execute(qry, [contributor_id])
    info = cur.fetchall()
    statistics = [] 

    for i in info:
        # Recipe id and number of ratings
        recipe_id, one_rating, two_rating, three_rating, four_rating, five_rating = i

        # Average rating = sum of ratings/total number of ratings
        avg_rating = (one_rating + two_rating * 2 + three_rating * 3 + four_rating * 4 + five_rating * 5)/(one_rating + two_rating + three_rating + four_rating + five_rating)

        # Number of recipe saves
        cur.execute('SELECT COUNT(*) FROM recipe_saves WHERE recipe_id = %s', [recipe_id])
        info = cur.fetchone()
        if not info:
            num_saves = 0
        else:
            num_saves = info

        recipe_stats = {
            "recipe_id": recipe_id,
            "stats": {
                "one star": one_rating,
                "two star": two_rating,
                "three star": three_rating,
                "four star": four_rating,
                "five star": five_rating,
                "avg rating": avg_rating,
                "num saves": num_saves
            }
        }

        statistics.append(recipe_stats)

    cur.close()

    return {
        "statistics": statistics
    }

@app.route('/dash/saved', methods = ['GET'])
def dash_saved():
    conn = db_connection()

    # Validate token
    req = request.get_json()
    token = req['token']
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Decode token to get user details
    user = decode_token(conn, token)

    cur = conn.cursor()
    if user["is_contributor"]:  # Contributor
        cur.execute('SELECT recipe_id FROM Recipe_Save WHERE contributor_id = %s', [user["user_id"]])
    else: # RUser
        cur.execute('SELECT recipe_id FROM Recipe_Save WHERE ruser_id = %s', [user["user_id"]])
    info = cur.fetchall()
    cur.close()

    recipes = []
    for i in info:
        recipe_details = get_recipe_details(conn, i)
        recipes.append(recipe_details)
    
    return {
        "recipes": recipes
    }

@app.route('/dash/rated', methods = ['GET'])
def dash_rated():
    conn = db_connection()

    # Validate token
    req = request.get_json()
    token = req['token']
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Decode token to get user details
    user = decode_token(conn, token)

    cur = conn.cursor()
    if user["is_contributor"]:  # Contributor
        cur.execute('''SELECT recipe_id, rating FROM Recipe_Ratings
            WHERE contributor_id = %s''', [user["user_id"]])
    else: # RUser
        cur.execute('''SELECT recipe_id, rating FROM Recipe_Ratings
            WHERE ruser_id = %s''', [user["user_id"]])
    info = cur.fetchall()
    cur.close()

    # Create recipes list
    one_star_recipes = []
    two_star_recipes = []
    three_star_recipes = []
    four_star_recipes = []
    five_star_recipes = []
    for i in info:
        recipe_id, rating = i
        if rating == 1:
            one_star_recipes.append(get_recipe_details(conn, recipe_id))
        elif rating == 2:
            two_star_recipes.append(get_recipe_details(conn, recipe_id))
        elif rating == 3:
            three_star_recipes.append(get_recipe_details(conn, recipe_id))
        elif rating == 4:
            four_star_recipes.append(get_recipe_details(conn, recipe_id))
        else: # rating == 5
            five_star_recipes.append(get_recipe_details(conn, recipe_id))

    return {
        "1-star recipes": one_star_recipes,
        "2-star recipes": two_star_recipes,
        "3-star recipes": three_star_recipes,
        "4-star recipes": four_star_recipes,
        "5-star recipes": five_star_recipes,
    }

@app.route('/recipe_details/delete', methods = ['DELETE'])
def recipe_details_delete():
    conn = db_connection()
    cur = conn.cursor()

    # Get params
    req = request.get_json()
    token = req['token']
    recipe_id = req['recipe_id']

    # Error if blank recipe id
    if not recipe_id: 
        raise InputError("Recipe ID cannot be empty")

    # Error if recipe does not exist
    cur.execute('SELECT * FROM recipe WHERE recipe_id = %s LIMIT 1', [recipe_id])
    info = cur.fetchall()
    if not info:
        raise InputError("Recipe ID does not exist")

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    cur.execute('DELETE FROM recipe WHERE recipe_id = %s', [recipe_id])
    conn.commit()
    cur.close()

    return {}

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
