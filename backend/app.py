from encodings import search_function
from flask import Flask, jsonify, render_template, request
from error import AccessError, InputError
from helper import *
from json import dumps
import json

from search import *
from dash import *
from auth import *

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

    token = register_helper(email, password, username)

    return {
        "body": {"token": token}
    }
    
@app.route('/login', methods = ['POST'])
def login():
    # Get params
    req = request.get_json()
    email = req['email']
    password = req['password']
    is_contributor = req['is_contributor']

    # Log in user
    token = login_helper(email, password, is_contributor)

    return {
        "body": {"token": token , "is_contributor": is_contributor}
    }

@app.route('/logout', methods = ['POST'])
def logout():
    conn = db_connection()

    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")
        
    delete_token(conn, token)

    return {
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

    # Get tag categories
    tag_categories = get_tag_categories(conn)

    return {
        "tag_categories": tag_categories
    }

@app.route('/search/tag/tags', methods = ['GET'])
def search_tag_tags():
    conn = db_connection()

    # Get params
    tag_category_id = request.args.get('tag_category_id')

    # Get tags
    tags = get_tags(conn, tag_category_id)

    return {
        "tags": tags
    }

@app.route('/search/recipes', methods = ['POST'])
def search_recipes():
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Get params
    req = request.get_json()
    ingredients_req = req['ingredients_id']
    token = request.headers.get('token')

    # Get recipes
    recipes = search_for_recipes(token, ingredients_req)

    return {
        "recipes": recipes
    }

@app.route('/dash/statistics', methods = ['GET'])
def dash_statistics():
    conn = db_connection()

    # Validate token
    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Check if user is a contributor
    user_details = decode_token(conn, token)
    if user_details["is_contributor"] is False:
        raise AccessError("User is not a Contributor")
    contributor_id = user_details["user_id"]

    statistics_list = statistics(contributor_id)

    return {
        "statistics": statistics_list
    }

@app.route('/dash/saved', methods = ['GET'])
def dash_saved():
    conn = db_connection()

    # Validate token
    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    recipes = saved_recipes(token)

    return {
        "recipes": recipes
    }

@app.route('/dash/rated', methods = ['GET'])
def dash_rated():
    conn = db_connection()

    # Validate token
    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    one, two, three, four, five = rated_recipes(token)

    return {
        "1-star recipes": one,
        "2-star recipes": two,
        "3-star recipes": three,
        "4-star recipes": four,
        "5-star recipes": five,
    }

@app.route('/recipe_details/delete', methods = ['DELETE'])
def recipe_details_delete():
    conn = db_connection()
    cur = conn.cursor()

    # Get params
    req = request.get_json()
    token = request.headers.get('token')
    recipe_id = (req['recipe_id'])

    # Error if blank recipe id
    if recipe_id is None: 
        raise InputError("Recipe ID cannot be empty")

    # Error if recipe does not exist
    if not valid_recipe_id(conn, recipe_id):
        raise InputError("Recipe ID does not exist")

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    print("WHAT IS THE RECIPE ID???")
    print(recipe_id)
    cur.execute('DELETE FROM recipes WHERE id = ?', [recipe_id])
    conn.commit()
    cur.close()

    return {}

@app.route('/save_and_rate/save', methods = ['POST'])
def save():
    # Get user input
    req = request.get_json()
    recipe_id = req['recipe_id']
    token = request.headers.get('token')

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
    if has_saved(conn, recipe_id, user_details) == False:
        if user_details['is_contributor'] == False:
            c.execute("INSERT INTO recipeSaves(ruser_id, recipe_id) VALUES (?, ?)", (id, recipe_id))
        else:
            c.execute("INSERT INTO recipeSaves(contributor_id, recipe_id) VALUES (?, ?)", (id, recipe_id))
    else:
        if user_details["is_contributor"] == False:
            c.execute("DELETE FROM recipeSaves WHERE ruser_id = ? AND recipe_id = ?", [id, recipe_id])
        else:
            c.execute("DELETE FROM recipeSaves WHERE contributor_id = ? AND recipe_id = ?", [id, recipe_id])
    
    conn.commit()
    conn.close()
    
    return {}

@app.route('/save_and_rate/rate', methods = ['POST'])
def rate():
    # Get user input
    req = request.get_json()
    recipe_id = req['recipe_id']
    token = request.headers.get('token')
    rating = req['rating']

    # Connect to db 
    conn = db_connection()

     # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_recipe_id(conn, recipe_id):
        raise InputError("No such recipe id")

    # #validate rating
    # if rating > 5 or rating < 0:
    #     raise InputError("Rating out of range.")
    
    # Get user details 
    user_details = decode_token(conn, token)
    id = user_details["user_id"]

    c = conn.cursor()
    if user_details["is_contributor"] == False:
        c.execute("SELECT * FROM recipeRatings WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, id])
        if has_rated(conn, recipe_id, user_details) == True:
            c.execute("DELETE FROM recipeRatings WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, id])
            c.execute("INSERT INTO recipeRatings(ruser_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
        else:
            c.execute("INSERT INTO recipeRatings(ruser_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
    else:
        c.execute("SELECT * FROM recipeRatings WHERE recipe_id = ? AND contributor_id = ?", [recipe_id, id])
        if has_rated(conn, recipe_id, user_details) == True:
            c.execute("DELETE FROM recipeRatings WHERE recipe_id = ? AND contributor_id = ?", [recipe_id, id])
            c.execute("INSERT INTO recipeRatings(contributor_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
        else:
            c.execute("INSERT INTO recipeRatings(contributor_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))

    conn.commit()
    conn.close()

    return {}

@app.route('/recipe_details/view', methods = ['GET'])
def recipe_details_view():
    # Get usr input
    recipe_id = request.args.get('id')
    print(recipe_id)
    # Connect to db 
    conn = db_connection()
    
    token = request.headers.get('token')

    # Validate token
    if not validate_token(conn, token):
        user = -1
    else :
        # Gey user_id
        user = decode_token(conn, token)

    print(user)

    # Validate recipe id
    if not valid_recipe_id(conn, recipe_id):
        raise InputError("No such recipe id")
    
    # Get recipe details 
    ret = get_recipe_details(conn, recipe_id, user)
    
    conn.close()

    return ret

@app.route('/recipe_details/update', methods = ['PUT'])
def recipe_details_update():
    # Connect to db
    conn = db_connection()
    c = conn.cursor()

    # Validate token
    req = request.get_json()
    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Decode token to get user details
    user_details = decode_token(conn, token)
    user_id = user_details["user_id"]

    #print(req)
    # Get recipe id
    recipe_id = req['recipe_id']
    # If recipe id == -1, assign new recipe id # chekcing is author_id matches user_id
    # check public state = if public state publish to public if not go to personal
    # if positive num, update recipe that could be public or private
    if recipe_id == -1:
        c.execute("SELECT * FROM recipes ORDER BY id DESC LIMIT 1")
        recipe_id = c.fetchone()[0]
        recipe_id = recipe_id + 1
        insert_recipe_details(conn, user_details, recipe_id, req)
    # if recipe id != -1, update the recipe
        # delete existing data first 
    else:
        update_recipe_details(conn, user_details, recipe_id, req)
        conn.commit()
    
    c.close()

    return {}

@app.route('/dash/my_recipes', methods = ['GET'])
def dash_my_recipes():
    # Connect to db
    conn = db_connection()
    c = conn.cursor()

    # Get user input
    # req = request.get_json()
    token = request.headers.get('token')
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
            recipes.append(get_recipe_details(conn, r_id[0], user))
    else:
        c.execute("SELECT recipe_id FROM personalRecipes WHERE ruser_id = ?", [user_id])
        recipe_ids = c.fetchall()
        for i in recipe_ids:
            r_id = i
            recipes.append(get_recipe_details(conn, r_id[0], user))

    conn.close()

    ret = {"recipes" : recipes}

    return ret

# Erivan here u go
@app.route('/get/tags', methods = ['GET'])
def get_all_tags():
    conn = db_connection()

    # Validate token
    # token = request.args.get('req')['token']
    # if not validate_token(conn, token):
    #     raise AccessError("Invalid token")

    # Get tags
    tags = get_tags_and_categories(conn)

    return {
        "tags": tags
    }

########################## SPRINT 3 ##########################

@app.route('/ingredients/new', methods = ['PUT'])
def ingredients_new():
    conn = db_connection()
    c = conn.cursor()

    token = request.headers.get('token')
    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")
    
    # Get user_id
    user = decode_token(conn, token)
    # Validate contributor status
    if not user["is_contributor"]:
        raise AccessError("Action not permitted.")
    
    # Get Body
    req = request.get_json()
    ingredient_name = req['ingredient_name']
    category_id = req['category_id']

    # Check valid category id
    c.execute("SELECT * FROM ingredientCategories ORDER BY id DESC LIMIT 1")
    max_cat_id = c.fetchone()[0]
    if category_id > max_cat_id:
        raise InputError("Incorrect category id")
    
    # Check ingredient doesn't already exist
    c.execute("SELECT * FROM ingredients WHERE name = ? COLLATE NOCASE", [ingredient_name])
    if c.fetchone() is not None:
        raise InputError("Ingredient already exists")

    # make new ingredient id
    c.execute("SELECT * FROM ingredients ORDER BY id DESC LIMIT 1")
    new_ingredient_id = c.fetchone()[0]
    new_ingredient_id = new_ingredient_id + 1

    # add ingredient to "Ingredients" database
    c.execute("INSERT INTO ingredients VALUES (?, ?, ?)", (new_ingredient_id, category_id, ingredient_name))
    conn.commit()

    return {
        "ingredient_id" : new_ingredient_id
    }

@app.route('/skill_videos', methods = ['GET'])
def skill_videos():
    conn = db_connection()
    c = conn.cursor()

    video_list = []

    c.execute("SELECT * FROM SkillVideos")
    videos = c.fetchall()
    for row in videos:
        c.execute("SELECT username FROM Contributors WHERE id = ? AND is_full_recipe_video = ?", [row[1], 0])
        name = c.fetchone()[0]
        video_list.append({"id" : row[0], "title" : row[2], "url" : row[3], "creator": name, "is_full_recipe_video" : row[4]})

    ret = {"video_list" : video_list}

    return ret

@app.route('/skill_videos/contributor', methods = ['GET'])
def skill_videos_contributor():
    conn = db_connection()
    c = conn.cursor()
    token = request.headers.get('token')
    
    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")
    
    # Get user_id
    user = decode_token(conn, token)
    
    # Validate contributor status
    if not user["is_contributor"]:
        raise AccessError("Action not permitted.")
    
    contributor_id = user["user_id"]
    video_list = []

    c.execute("SELECT * FROM SkillVideos WHERE contributor_id = ?", [contributor_id])
    videos = c.fetchall()
    for row in videos:
        video_list.append({"id" : row[0], "title" : row[2], "url" : row[3], "is_full_recipe_video" : row[4]})
    
    ret = {"video_list" : video_list}

    return ret

@app.route('/skill_videos/r_user', methods = ['GET'])
def skill_videos_ruser():
    conn = db_connection()
    c = conn.cursor()
    token = request.headers.get('token')
    
    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")
    
    # Validate contributor status
    if user["is_contributor"]:
        raise AccessError("Action not permitted.")
    
    # Get user_id
    user = decode_token(conn, token)
    user_id = user["user_id"]

    c.execute("SELECT video_id FROM SkillVideoSaves WHERE ruser_id = ?", [user_id])

    if c.fetchone() is None:
        return{"video_list" : []}

    videos = c.fetchall()
    video_list = []
    for v in videos:
        c.execute("SELECT * FROM SkillVideos WHERE id = ?", [v])
        row = c.fetchone()
        c.execute("SELECT username FROM Contributors WHERE id = ?", [row[1]])
        name = c.fetchone()[0]
        video_list.append({"id" : row[0], "title" : row[2], "url" : row[3], "creator": name})

    ret = {"video_list" : video_list}

    return ret

@app.route('/dash/update_details', methods = ['PUT'])
def dash_update_details():
    conn = db_connection()
    c = conn.cursor()
    
    token = request.headers.get('token')
     # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")
    
    user = decode_token(conn, token)
    user_id = user["user_id"]

    req = request.get_json()
    username = req['username']
    password = req['password']
    dp = req['profile_pic']
    email = req['email']

    if user["is_contributor"]:
        c.execute("UPDATE contributors SET email = ? WHERE id = ?", [email, user_id])
        c.execute("UPDATE contributors SET username = ? WHERE id = ?", [username, user_id])
        c.execute("UPDATE contributors SET password = ? WHERE id = ?", [password, user_id])
        c.execute("UPDATE contributors SET profile_picture = ? WHERE id = ?", [dp, user_id])
    else:
        c.execute("UPDATE rusers SET email = ? WHERE id = ?", [email, user_id])
        c.execute("UPDATE rusers SET username = ? WHERE id = ?", [username, user_id])
        c.execute("UPDATE rusers SET password = ? WHERE id = ?", [password, user_id])
        c.execute("UPDATE rusers SET profile_picture = ? WHERE id = ?", [dp, user_id])
    
    conn.commit()

    return {}

@app.route('/search/has_searched', methods = ['POST'])
def search_hassearched():
    '''Add a search combination.'''

    # Get params
    req = request.get_json()
    ingredients_req = req['ingredient_id_list']

    has_searched(ingredients_req)
    
    return {}

@app.route('/search/recommendation', methods = ['GET'])
def search_recommendation():
    '''Get ingredient recommendations in homepage search.'''

    ingredients = recommendation()

    return {
        "ingredients_list": ingredients[:30]
    }

@app.route('/search/no_recipe', methods = ['GET'])
def search_norecipe():
    '''Get top ingredient search combinations which don't
    have recipes yet.'''

    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Validate token
    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Check if user is a contributor
    user_details = decode_token(conn, token)
    if user_details["is_contributor"] is False:
        raise AccessError("User is not a Contributor")

    ic_list = no_recipes()

    return {
        "ingredient_combination_list": ic_list
    }

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
