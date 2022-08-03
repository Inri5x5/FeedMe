from flask import Flask, request
from json import dumps
from error import *
from helper import *
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
    
    if token == 'null':
        print('heree')
        raise AccessError("User not sign in")
    
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
    if has_saved_recipe(conn, recipe_id, user_details) == False:
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

    # Connect to db 
    conn = db_connection()
    
    token = request.headers.get('token')

    # Validate token
    if not validate_token(conn, token):
        user = -1
    else :
        # Get user_id
        user = decode_token(conn, token)

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
    print(recipe_id)
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
    
    # Get user_id
    user = decode_token(conn, token)
    user_id = user["user_id"]

    # Get all Personal Recipes. For contributor this includes their drafts and public recipes. For ruser it is just drafts.
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

    token = request.headers.get('token')
    
    if token == str(-1) or not validate_token(conn, token):
        video_list = get_skill_videos(conn, -1)
    else:
        user = decode_token(conn, token)
        if user["is_contributor"]:
            video_list = get_skill_videos(conn, -1)
        else:
            video_list = get_skill_videos(conn, user["user_id"])

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
        prefix = "https://www.youtube.com/"
        c.execute("SELECT * FROM Contributors WHERE id = ?", [contributor_id])
        creator_details = c.fetchone()
        video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4]})
    
    ret = {"video_list" : video_list}

    return ret

@app.route('/skill_videos/ruser', methods = ['GET'])
def skill_videos_ruser():
    conn = db_connection()
    c = conn.cursor()
    token = request.headers.get('token')
    
    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Get user_id
    user = decode_token(conn, token)
    user_id = user["user_id"]

    # Validate contributor status
    if user["is_contributor"]:
        raise AccessError("Action not permitted.")
    
    c.execute("SELECT skill_video_id FROM SkillVideoSaves WHERE ruser_id = ?", [user_id])

    
    videos = c.fetchall()
    
    if videos is None:
        return{"video_list" : []}

    video_list = []
    for v in videos:
        c.execute("SELECT * FROM SkillVideos WHERE id = ?", [v[0]])
        row = c.fetchone()
        c.execute("SELECT * FROM Contributors WHERE id = ?", [row[1]])
        creator_details = c.fetchone()
        prefix = "https://www.youtube.com/"
        video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4]})

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
    # password = req['password']
    dp = req['profile_pic']
    email = req['email']

    if user["is_contributor"]:
        c.execute("UPDATE contributors SET email = ? WHERE id = ?", [email, user_id])
        c.execute("UPDATE contributors SET username = ? WHERE id = ?", [username, user_id])
        # c.execute("UPDATE contributors SET password = ? WHERE id = ?", [password, user_id])
        c.execute("UPDATE contributors SET profile_picture = ? WHERE id = ?", [dp, user_id])
    else:
        c.execute("UPDATE rusers SET email = ? WHERE id = ?", [email, user_id])
        c.execute("UPDATE rusers SET username = ? WHERE id = ?", [username, user_id])
        # c.execute("UPDATE rusers SET password = ? WHERE id = ?", [password, user_id])
        c.execute("UPDATE rusers SET profile_picture = ? WHERE id = ?", [dp, user_id])
    
    conn.commit()

    return {}

@app.route('/skill_videos/add', methods = ['PUT'])
def skill_videos_add():
    req = request.get_json()
    video_name = req['title']
    full_url = req['url']

    temp_url = full_url.split('watch?v=', 1)
    url = "watch?v=" + temp_url[1]

    token = request.headers.get('token')
    
    # Connect to db 
    conn = db_connection()
    c = conn.cursor()

    user_details = decode_token(conn, token)
    if not user_details["is_contributor"]:
        raise AccessError("Do not have permission to upload skill video.")
    
    c.execute("SELECT * FROM skillVideos ORDER BY id DESC LIMIT 1")
    video_id = c.fetchone()[0]
    video_id = video_id + 1

    c.execute("INSERT INTO SkillVideos VALUES (?, ?, ? ,?)", [video_id, user_details["user_id"], video_name, url])
    conn.commit()
     
    return {}


@app.route('/skill_videos/delete', methods = ['DELETE'])
def skill_videos_delete():
    # delete from skillVideos, skillVideoSaves, skillVideoInRecipe
    # Connect to db 
    conn = db_connection()
    c = conn.cursor()

    req = request.get_json()
    video_id = req['video_id']
    token = request.headers.get('token')

    user_details = decode_token(conn, token)
    if not user_details["is_contributor"]:
        raise AccessError("Do not have permission to delete skill video.")
    
    if not valid_video_id(conn, video_id):
        raise InputError("video id does not exist.")

    c.execute("SELECT * FROM SkillVideos WHERE contributor_id = ? AND id = ?", [user_details["user_id"], video_id])
    if c.fetchone() is None:
        raise AccessError("You cannot delete another contributor's video.")

    c.execute("DELETE FROM SkillVideos WHERE id = ?", [video_id])

    conn.commit()

    return {}

@app.route('/skill_videos/save', methods = ['POST'])
def save_skill_videos():
    req = request.get_json()
    video_id = req['video_id']
    token = request.headers.get('token')

    # Connect to db 
    conn = db_connection()
    c = conn.cursor()

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_video_id(conn, video_id):
        raise InputError("No such recipe id")

    # Get user id
    user_details = decode_token(conn, token)
    if user_details["is_contributor"]:
        raise AccessError["Contributors cannot save skill videos"]

    user_id = user_details["user_id"]
    if has_saved_video(conn, video_id, user_id):
        c.execute("DELETE FROM skillVideoSaves WHERE skill_video_id = ? AND ruser_id = ?", [video_id, user_id])
    else:
        c.execute("INSERT INTO SkillVideoSaves VALUES (?, ?)", [user_id, video_id])
    
    conn.commit()

    return {}

@app.route('/skill_videos/search', methods = ['GET'])
def skill_videos_search():
    video_list = []

    req = request.get_json()
    search_string = req['search_string'].lower()

    # Connect to db 
    conn = db_connection()
    c = conn.cursor()

    # NOTE: I'm not sure if this query will work - to avoid case sensitivity, I've made all strings upper case
    c.execute("SELECT * FROM skillVideos WHERE LOWER(title) LIKE ?", ['%'+search_string+'%'])
    videos = c.fetchall()
    for v in videos:
        c.execute("SELECT * FROM Contributors WHERE id = ?", [v[1]])
        creator_details = c.fetchone()
        prefix = "https://www.youtube.com/"
        video_list.append({"id" : v[0], "title" : v[2], "url" : prefix + v[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4]})

    ret = {"video_list" : video_list}

    return ret


########################## SPRINT 3 ##########################


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

@app.route('/is_contributor', methods = ['GET'])
def check_is_contributor():
    # Connect to database
    conn = db_connection()

    # Get and validate token
    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")
    
    # Decode token
    user = decode_token(conn, token)

    return {
        "is_contributor": user["is_contributor"]
    }

@app.route('/dash/get_details', methods = ['GET'])
def get_profile_details():
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Get token
    token = request.headers.get('token')

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Get user id
    user = decode_token(conn, token)
    user_id = user["user_id"]
    is_contributor = user["is_contributor"]

    # Get user details from database
    if is_contributor:
        cur.execute('SELECT * FROM Contributors WHERE id = ?', [user_id])
    else:
        cur.execute('SELECT * FROM Rusers WHERE id = ?', [user_id])

    id, email, username, password, profile_picture = cur.fetchone()
    user_details = {
        "user_id": user_id,
        "email": email,
        "username": username,
        "profile_picture": profile_picture
    }

    return {
        "user_details": user_details
    }

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
