from flask import Flask, request
from json import dumps
from error import *
from helper import *
from search import *
from dash import *
from auth import *
from recipe import *
from ingredients import *
from skill_videos import *

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
        conn.close()
        raise AccessError("Invalid token")
        
    delete_token(conn, token)

    return {
        "body": {}
    }

@app.route('/categories', methods = ['GET'])
def categories():
    categories = ingredient_categories()
        
    ret = {"status": 200,
            "body": {"categories": categories}}

    return ret
    
@app.route('/ingredients', methods = ['GET'])
def ingredients():
    ingredient = request.args.get('query')

    suggestions = ingredient_information(ingredient)
    
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
        conn.close()
        raise AccessError("Invalid token")

    # Check if user is a contributor
    user_details = decode_token(conn, token)
    if user_details["is_contributor"] is False:
        conn.close()
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
        conn.close()
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
        conn.close()
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

    # Get params
    req = request.get_json()
    token = request.headers.get('token')
    recipe_id = (req['recipe_id'])

    # Error if blank recipe id
    if recipe_id is None: 
        conn.close()
        raise InputError("Recipe ID cannot be empty")

    # Error if recipe does not exist
    if not valid_recipe_id(conn, recipe_id):
        conn.close()
        raise InputError("Recipe ID does not exist")

    # Validate token
    if not validate_token(conn, token):
        conn.close()
        raise AccessError("Invalid token")

    delete_recipe(recipe_id)

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
        conn.close()
        raise AccessError("User not sign in")
    
    # Validate token
    if not validate_token(conn, token):
        conn.close()
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_recipe_id(conn, recipe_id):
        conn.close()
        raise InputError("No such recipe id")

    # Get user id
    user_details = decode_token(conn, token) 
    recipe_save(recipe_id, user_details)
    
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
        conn.close()
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_recipe_id(conn, recipe_id):
        conn.close()
        raise InputError("No such recipe id")
    
    # Get user details 
    user_details = decode_token(conn, token)

    recipe_rate(recipe_id, user_details, rating)

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
        conn.close()
        raise InputError("No such recipe id")
    
    # Get recipe details 
    ret = get_recipe_details(conn, recipe_id, user)
    
    conn.close()

    return ret

@app.route('/recipe_details/update', methods = ['PUT'])
def recipe_details_update():
    # Connect to db
    conn = db_connection()

    # Validate token
    req = request.get_json()
    token = request.headers.get('token')
    if not validate_token(conn, token):
        conn.close()
        raise AccessError("Invalid token")

    # Decode token to get user details
    user_details = decode_token(conn, token)

    # Get recipe id
    recipe_id = req['recipe_id']
    print(recipe_id)
    # print(req['original_id'])
    update_recipe(recipe_id, user_details, req)

    return {}

@app.route('/dash/my_recipes', methods = ['GET'])
def dash_my_recipes():
    # Connect to db
    conn = db_connection()

    # Get user input
    token = request.headers.get('token')

    # Validate token
    if not validate_token(conn, token):
        conn.close()
        raise AccessError("Invalid token")
    
    # Get user_id
    user = decode_token(conn, token)

    recipes = personal_recipes(user)

    ret = {"recipes" : recipes}

    return ret

# Erivan here u go
@app.route('/get/tags', methods = ['GET'])
def get_all_tags():
    conn = db_connection()

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
        conn.close()
        raise AccessError("Invalid token")
    
    # Get user_id
    user = decode_token(conn, token)

    # Validate contributor status
    if not user["is_contributor"]:
        conn.close()
        raise AccessError("Action not permitted.")
    
    # Get Body
    req = request.get_json()
    ingredient_name = req['ingredient_name']
    category_id = req['category_id']

    # Check valid category id
    if valid_category_id(category_id) == -1:
        conn.close()
        raise InputError("Incorrect category id")

    if ingredient_exists(ingredient_name) == -1:
        conn.close()
        raise InputError("Ingredient already exists")

    new_ingredient_id = add_new_ingredient(ingredient_name, category_id)

    return {
        "ingredient_id" : new_ingredient_id
    }

@app.route('/skill_videos', methods = ['GET'])
def skill_videos():

    token = request.headers.get('token')
    video_list = display_skill_videos(token)

    ret = {"video_list" : video_list}

    return ret

@app.route('/skill_videos/contributor', methods = ['GET'])
def skill_videos_contributor():
    conn = db_connection()

    token = request.headers.get('token')
    
    # Validate token
    if not validate_token(conn, token):
        conn.close()
        raise AccessError("Invalid token")
    
    # Get user_id
    user = decode_token(conn, token)
    
    # Validate contributor status
    if not user["is_contributor"]:
        conn.close()
        raise AccessError("Action not permitted.")
    
    # contributor_id = user["user_id"]
    video_list = contributor_skill_videos(user)

    
    ret = {"video_list" : video_list}

    return ret

@app.route('/skill_videos/ruser', methods = ['GET'])
def skill_videos_ruser():
    conn = db_connection()
    c = conn.cursor()
    token = request.headers.get('token')
    
    # Validate token
    if not validate_token(conn, token):
        conn.close()
        raise AccessError("Invalid token")

    # Get user_id
    user = decode_token(conn, token)
    user_id = user["user_id"]

    # Validate contributor status
    if user["is_contributor"]:
        conn.close()
        raise AccessError("Action not permitted.")
    
    video_list = ruser_skill_videos(user)

    ret = {"video_list" : video_list}

    return ret

@app.route('/dash/update_details', methods = ['PUT'])
def dash_update_details():
    conn = db_connection()
    c = conn.cursor()
    
    token = request.headers.get('token')

     # Validate token
    if not validate_token(conn, token):
        conn.close()
        raise AccessError("Invalid token")
    
    user = decode_token(conn, token)
    user_id = user["user_id"]

    req = request.get_json()
    username = req['username']
    dp = req['profile_pic']
    email = req['email']
    
    update_details(user, username, dp, email)
    
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
        conn.close()
        raise AccessError("Do not have permission to upload skill video.")
    
    add_skill_videos(user_details, video_name, url)
     
    return {}


@app.route('/skill_videos/delete', methods = ['DELETE'])
def skill_videos_delete():
    conn = db_connection()

    req = request.get_json()
    video_id = req['video_id']
    token = request.headers.get('token')

    user_details = decode_token(conn, token)
    if not user_details["is_contributor"]:
        conn.close()
        raise AccessError("Do not have permission to delete skill video.")
    
    if not valid_video_id(conn, video_id):
        conn.close()
        raise InputError("video id does not exist.")

    if validate_uploader(user_details, video_id) == -1:
        conn.close()
        raise AccessError("You cannot delete another contributor's video.")

    delete_skill_videos(video_id)

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
        conn.close()
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_video_id(conn, video_id):
        conn.close()
        raise InputError("No such recipe id")

    # Get user id
    user_details = decode_token(conn, token)
    if user_details["is_contributor"]:
        conn.close()
        raise AccessError["Contributors cannot save skill videos"]

    skill_videos_saved(user_details, video_id)

    return {}

@app.route('/skill_videos/search', methods = ['GET'])
def skill_videos_search():
    req = request.get_json()
    search_string = req['search_string'].lower()

    video_list = search_skill_videos(search_string)

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
        conn.close()
        raise AccessError("Invalid token")

    # Check if user is a contributor
    user_details = decode_token(conn, token)
    if user_details["is_contributor"] is False:
        conn.close()
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
        conn.close()
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

    # Get token
    token = request.headers.get('token')

    # Validate token
    if not validate_token(conn, token):
        conn.close()
        raise AccessError("Invalid token")

    # Get user id
    user = decode_token(conn, token)

    user_details = get_user_details(user)

    return {
        "user_details": user_details
    }

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
