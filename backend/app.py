from flask import Flask, jsonify, render_template, request
from error import AccessError, InputError
from helper import *
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
    conn = db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM ingredientCategories")
    data = c.fetchall()
    conn.close()

    categories = []
    for (i, j) in data:
        categories.append({"name": j, "c_id": i})
        
    ret = {"status": 200,
            "body": {"categories": categories}}

    return ret
    
@app.route('/ingredients', methods = ['GET'])
def ingredients():
    ingredient = request.args.get('query')

    conn = db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM ingredients")
    data = c.fetchall()
    conn.close()

    suggestions = []
    for (i, j, k) in data:
        if ingredient.lower() in k.lower():
            suggestions.append({"name": k, "i_id": i, "c_id": j})
    
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

@app.route('/save_and_rate/save', methods = ['POST'])
def save():
    # Get user input
    req = request.get_json()
    recipe_id = req['recipe_id']
    token = req['token']

    # Connect to db 
    conn = db_connection()

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_recipe_id(conn, recipe_id):
        raise InputError("No such recipe id")

    # Get user id
    user_details = decode_token(conn, token)
    id = user_details["user_id"]
    
    c = conn.cursor()
    if has_saved(conn, recipe_id, id) == False:
        if user_details['is_contributor'] == False:
            c.execute("INSERT INTO recipeSaves(rusr_id, recipe_id) VALUES (?, ?)", (id, recipe_id))
        else:
            c.execute("INSERT INTO recipeSaves(contributor, recipe_id) VALUES (?, ?)", (id, recipe_id))
    else:
        if user_details["is_contributor"] == False:
            c.execute("DELETE FROM recipeSaves WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, id])
        else:
            c.execute("DELETE FROM recipeSaves WHERE recipe_id = ? AND contributor_id = ?", [recipe_id, id])
    
    conn.commit()
    conn.close()
    
    return

@app.route('/save_and_rate/rate', methods = ['POST'])
def rate():
    # Get user input
    req = request.get_json()
    recipe_id = req['recipe_id']
    token = req['token']
    rating = req['rating']

    # Connect to db 
    conn = db_connection()

     # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_recipe_id(conn, recipe_id):
        raise InputError("No such recipe id")

    #validate rating
    if rating > 5 or rating < 0:
        raise InputError("Rating out of range.")
    
    # Get user details 
    user_details = decode_token(conn, token)
    id = user_details["user_id"]

    c = conn.cursor()
    if user_details["is_contributor"] == False:
        c.execute("SELECT * FROM recipeRatings WHERE recipe_id = ? AND rusr_id = ?", [recipe_id, id])
        if has_rated(conn, recipe_id, user_details) == True:
            c.execute("DELETE FROM recipeRatings WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, id])
            c.execute("INSERT INTO recipeRatings(ruser_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
        else:
            c.execute("INSERT INTO recipeRatings(ruser_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
    else:
        c.execute("SELECT * FROM recipeRatings WHERE recipe_id = ? AND contributor_id_id = ?", [recipe_id, id])
        if has_rated(conn, recipe_id, user_details) == True:
            c.execute("DELETE FROM recipeRatings WHERE recipe_id = ? AND contributor_id = ?", [recipe_id, id])
            c.execute("INSERT INTO recipeRatings(contributor_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
        else:
            c.execute("INSERT INTO recipeRatings(contributor_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))

    conn.commit()
    conn.close()

    return

@app.route('/recipe_details/view', methods = ['GET'])
def recipe_details_view():
    # Get usr input
    recipe_id = request.args.get('query')

    # Connect to db 
    conn = db_connection()

    # Validate recipe id
    if not valid_recipe_id(conn, recipe_id):
        raise InputError("No such recipe id")
    
    # Get recipe details 
    ret = get_recipe_details(conn, recipe_id, user_details)
    
    conn.close()

    return ret

@app.route('/recipe_details/update', methods = ['PUT'])
def recipe_details_update():
    # Connect to db
    conn = db_connection()
    c = conn.cursor()

    # Validate token
    req = request.get_json()
    token = req['token']
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Decode token to get user details
    user_details = decode_token(conn, token)
    user_id = user_details["user_id"]

    # Get user input
    req = request.get_json()

    # Get recipe id
    recipe_id = req['recipe_id']
    # If recipe id == -1, assign new recipe id # chekcing is author_id matches user_id
    # check public state = if public state publish to public if not go to personal
    # if positive num, update recipe that could be public or private
    if recipe_id == -1:
        c.execute("SELECT * FROM recipes ORDER BY recipe_id DESC LIMIT 1")
        recipe_id = c.fetchall()[0]
        recipe_id = recipe_id + 1
    # if recipe id != -1, update the recipe
        # delete existing data first 
    else:
        c.execute('DELETE FROM recipes WHERE recipe_id = ?', [recipe_id])
    
    update_recipe_details(conn, user_details, recipe_id, req)

    return 

@app.route('/dash/my_recipes', methods = ['GET'])
def dash_my_recipes():
    # Connect to db
    conn = db_connection()
    c = conn.cursor()

    # Get user input
    req = request.get_json()
    token = req['token']
    # token = request.args.get('query')

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")
    
    # Gey user_id
    user = decode_token(conn, token)
    user_id = user["user_id"]

    # Get all Personal Recipes. For contributor this includes their drafts
    recipes = []
    if user["is_contributor"]:  # Contributor
        c.execute("SELECT recipe_id FROM personalRecipes WHERE contributor_id = ?", [user_id])
        recipe_ids = c.fetchall()
        for i in recipe_ids:
            r_id = i
            recipes.append(get_recipe_details(conn, r_id))
    else:
        c.execute("SELECT recipe_id FROM personalRecipes WHERE ruser_id = ?", [user_id])
        recipe_ids = c.fetchall()
        for i in recipe_ids:
            r_id = i
            recipes.append(get_recipe_details(conn, r_id))

    conn.close()

    ret = {"recipes" : recipes}

    return ret

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
