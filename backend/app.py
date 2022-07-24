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
    conn = db_connection()

    req = request.get_json()
    email = req['email']
    password = req['password']
    username = req['username']

    if not email or not password or not username:
        raise InputError
    
    # Check email format
    if not valid_email(email):
        raise InputError("Invalid email")

    if email_already_exists(conn, email):
        raise InputError("Email already in use")

    ruser_id = get_new_user_id(conn)
    print(ruser_id)
    add_new_user(conn, ruser_id, email, password, username)

    token = generate_token(email)
    add_token(conn, token, ruser_id, False)

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
        add_token(conn, token, user_id, is_contributor)

        return {
            "status": 200,
            "body": {"token": token , "is_contributor": is_contributor}
        }

@app.route('/logout', methods = ['POST'])
def logout():
    conn = db_connection()

    req = request.get_json()
    token = request.headers.get('token')

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

    # Get tag categories
    tag_categories = get_tag_categories(conn)

    return {
        "tag_categories": tag_categories
    }

@app.route('/search/tag/tags', methods = ['GET'])
def search_tag_tags():
    conn = db_connection()

    # Get params
    # req = request.get_json()
    tag_category_id = request.args.get('tag_category_id')

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
    token = request.headers.get('token')
    if (token != '-1'):
        user_details = decode_token(conn, token) 
    else :
        user_details = -1


    ingredients_req = req['ingredients_id']

    cur.execute('''
        SELECT r.id, GROUP_CONCAT(ir.ingredient_id)
        FROM    Recipes r
                JOIN ingredientInRecipe ir on ir.recipe_id = r.id
        GROUP BY r.id
    ''')
    info = cur.fetchall()
    cur.close()

    recipes = []
    for i in info:
        recipe_id, ingredients = i
        ingredients_split = ingredients.split(',')
        ingredients_split_int = [int(i) for i in ingredients_split]    
       
        if set(ingredients_split_int) >= set(ingredients_req) or ingredients_req is None:
            recipe_details = get_recipe_details(conn, recipe_id, user_details)
            recipes.append(recipe_details)
    
    return {
        "recipes": recipes
    }

@app.route('/dash/statistics', methods = ['GET'])
def dash_statistics():
    conn = db_connection()

    # Validate token
    # req = request.get_json()
    token = request.headers.get('token')
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
        SELECT r.id, 
            SUM(CASE WHEN rr.rating = 1 THEN 1 ELSE 0 END) AS one_rating,
            SUM(CASE WHEN rr.rating = 2 THEN 1 ELSE 0 END) AS two_rating,
            SUM(CASE WHEN rr.rating = 3 THEN 1 ELSE 0 END) AS three_rating,
            SUM(CASE WHEN rr.rating = 4 THEN 1 ELSE 0 END) AS four_rating,
            SUM(CASE WHEN rr.rating = 5 THEN 1 ELSE 0 END) AS five_rating
        FROM recipes r
            LEFT JOIN publicRecipes pr ON pr.recipe_id = r.id
            LEFT JOIN recipeRatings rr ON rr.recipe_id = r.id
        WHERE pr.contributor_id = ?
        GROUP BY r.id
    '''
    cur.execute(qry, [contributor_id])
    info = cur.fetchall()
    statistics = [] 

    for i in info:
        # Recipe id and number of ratings
        recipe_id, one_rating, two_rating, three_rating, four_rating, five_rating = i

        # Average rating = sum of ratings/total number of ratings
        num_ratings = one_rating + two_rating + three_rating + four_rating + five_rating
        sum_ratings = (one_rating + two_rating * 2 + three_rating * 3 + four_rating * 4 + five_rating * 5)

        if num_ratings == 0:
            avg_rating = 0
        else:
            avg_rating = sum_ratings/num_ratings

        # Number of recipe saves
        cur.execute('SELECT COUNT(*) FROM recipeSaves WHERE recipe_id = ?', [recipe_id])
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
                "num saves": num_saves,
                "num ratings": num_ratings
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
    # req = request.get_json()
    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Decode token to get user details
    user = decode_token(conn, token)
    cur = conn.cursor()
    if user["is_contributor"]:  # Contributor
        cur.execute('SELECT recipe_id FROM recipeSaves WHERE contributor_id = ?', [user["user_id"]])
    else: # RUser
        cur.execute('SELECT recipe_id FROM recipeSaves WHERE ruser_id = ?', [user["user_id"]])
    info = cur.fetchall()

    recipes = []
    for i in info:
        recipe_details = get_recipe_details(conn, i[0], user)
        recipes.append(recipe_details)
    
    cur.close()
    return {
        "recipes": recipes
    }

@app.route('/dash/rated', methods = ['GET'])
def dash_rated():
    conn = db_connection()

    # Validate token
    # req = request.get_json()
    token = request.headers.get('token')
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Decode token to get user details
    user = decode_token(conn, token)

    cur = conn.cursor()
    if user["is_contributor"]:  # Contributor
        cur.execute('''SELECT recipe_id, rating FROM recipeRatings
            WHERE contributor_id = ?''', [user["user_id"]])
    else: # RUser
        cur.execute('''SELECT recipe_id, rating FROM recipeRatings
            WHERE ruser_id = ?''', [user["user_id"]])
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
            one_star_recipes.append(get_recipe_details(conn, recipe_id, user))
        elif rating == 2:
            two_star_recipes.append(get_recipe_details(conn, recipe_id, user))
        elif rating == 3:
            three_star_recipes.append(get_recipe_details(conn, recipe_id, user))
        elif rating == 4:
            four_star_recipes.append(get_recipe_details(conn, recipe_id, user))
        else: # rating == 5
            five_star_recipes.append(get_recipe_details(conn, recipe_id, user))

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
    print(recipe_id)
    # Connect to db 
    conn = db_connection()
    
    token = request.headers.get('token')

    # Validate token
    if not validate_token(conn, token):
        user = -1
    else :
        # Get user_id
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
        c.execute("SELECT * FROM Contributors WHERE id = ?", [row[1]])
        creator_details = c.fetchone()
        prefix = "https://www.youtube.com/"
        if not row[4]:
            video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[0], "creator_profile_pic" : creator_details[4]})

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
        if not row[4]:
            video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[0], "creator_profile_pic" : creator_details[4]})
    
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
        if not row[4]:
            video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[0], "creator_profile_pic" : creator_details[4]})

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

@app.route('/skill_videos/add', methods = ['PUT'])
def skill_videos_add():
    req = request.get_json()
    video_name = req['title']
    full_url = req['url']

    # NOTE: I dunno if this works ;( - might need to check I;ve appende the right stuff to the url and split it correctly
    temp_url = full_url.split('=', 1)
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

    c.execute("INSERT INTO SkillVideos VALUES (?, ?, ? ,?", [video_id, user_details["user_id"], video_name, url])
    conn.commit()
     
    return {}


@app.route('/skill_videos/delete', methods = ['PUT'])
def skill_videos_delete():
    # delete from skillVideos, skillVideoSaves, skillVideoInRecipe
    # Connect to db 
    conn = db_connection()
    c = conn.cursor()

    req = request.get_json()
    video_id = req["'video_id"]
    token = request.headers.get('token')

    user_details = decode_token(conn, token)
    if not user_details["is_contributor"]:
        raise AccessError("Do not have permission to delete skill video.")
    
    if not valid_video_id(conn, video_id):
        raise InputError("video id does not exist.")

    c.execute("SELECT * FROM SkillVideos WHERE contirbutor_id = ? AND id = ?", [user_details["user_id"], video_id])
    if c.fetchone() is None:
        raise AccessError("You cannot delete another contributor's video.")

    c.execute("DELETE FROM SkillVideos WHERE id = ?", [video_id])
    c.execute("DELETE FROM SkillVideoSaves WHERE video_id = ?", [video_id])
    c.execute("DELETE FROM SkillVideoInRecipe WHERE video_id = ?", [video_id])

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
    if has_saved_video(conn, video_id, user_id) == False:
        c.execute("DELETE FROM skillVideoSaves WHERE video_id = ? AND ruser_id = ?", [video_id, user_id])
    else:
        c.execute("INSERT INTO SkillVideoSaves VALUES (?, ?)", [user_id, video_id])
    
    conn.commit()

    return {}

@app.route('/skill_videos/search', methods = ['GET'])
def skill_videos_search():
    video_list = []

    req = request.get_json()
    search_string = req['search'].upper()

    # Connect to db 
    conn = db_connection()
    c = conn.cursor()

    # NOTE: I'm not sure if this query will work - to avoid case sensitivity, I've made all strings upper case
    c.execute("SELECT * FROM skillVideos WHERE UPPER(title) LIKE ?", ['%'+search_string+'%'])
    videos = c.fetchall()
    for v in videos:
        c.execute("SELECT * FROM Contributors WHERE id = ?", [v[1]])
        creator_details = c.fetchone()
        prefix = "https://www.youtube.com/"
        if not v[4]:
            video_list.append({"id" : v[0], "title" : v[2], "url" : prefix + v[3], "creator": creator_details[0], "creator_profile_pic" : creator_details[4]})

    ret = {"video_list" : video_list}

    return ret


########################## SPRINT 3 ##########################


@app.route('/search/has_searched', methods = ['POST'])
def search_hassearched():
    '''Add a search combination.'''

    # Get params
    req = request.get_json()
    ingredients_req = req['ingredient_id_list']

    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Check if search combination already exists
    n_comb, search_id = check_search_combinations(conn, ingredients_req)

    # New search combination
    if n_comb:
        # Get a new search id
        search_id = get_new_search_id(conn)

        # Update Searches table
        cur.execute('INSERT INTO Searches (id, count) VALUES (?, ?)', [search_id, 1])

        # Insert rows of ingredient ids to IngredientInSearch table
        qry = '''INSERT INTO IngredientInSearch 
            (ingredient_id, search_id) VALUES (?, ?)'''
        for ingredient_id in ingredients_req:
            cur.execute(qry, [ingredient_id, search_id])

    # Existing search combination
    else:
        # Update Searches table (increment count)
        cur.execute('UPDATE Searches SET count = count + 1 WHERE id = ?', [search_id])

    conn.commit()
    cur.close()

    return {}

@app.route('/search/recommendation', methods = ['GET'])
def search_recommendation():
    '''Get ingredient recommendations in homepage search.'''

    # frontend will remove ingredient if it is already in the search bar

    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Get top ingredients in recipes
    cur.execute('''
        SELECT ir.ingredient_id, COUNT(ir.ingredient_id) AS occurence, i.name
        FROM IngredientInRecipe ir
            JOIN Ingredients i on i.id = ir.ingredient_id
        GROUP BY ir.ingredient_id
        ORDER BY occurence DESC
    ''')
    info = cur.fetchall()

    # Add top ingredients to the recommendations
    ingredients = []
    rank = 1
    for i in info:
        id, count, name = i
        i_dict = {"rank": rank, "id": id, "name": name}
        ingredients.append(i_dict)

        rank += 1

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

    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Create a view of ingredients (ingredient_id, name, search_id) that 
    # are in searches but not in recipes
    cur.execute("DROP VIEW IF EXISTS searches_minus_recipes")
    cur.execute('''
        CREATE VIEW searches_minus_recipes AS
        SELECT 
            iss.ingredient_id as ingredient_id, 
            i.name as ingredient_name, 
            iss.search_id as search_id
        FROM IngredientInSearch iss
            LEFT JOIN IngredientInRecipe ir on ir.ingredient_id = iss.ingredient_id
            LEFT JOIN Ingredients i on i.id = iss.ingredient_id
        WHERE ir.ingredient_id is NULL
    ''')
    conn.commit()

    # From the previous view, order the ingredients by the number of times
    # its search id occurs (descending)
    cur.execute('''
        SELECT search_id, COUNT(*)
        FROM searches_minus_recipes
        GROUP BY search_id
        ORDER BY COUNT(*) DESC
    ''')
    info = cur.fetchall()

    # From the search ids, get its ingredient combinations and add to return list
    ic_list = []
    rank = 1
    for i in info:
        search_id, count = i

        # Get number of searches
        cur.execute('SELECT count FROM searches WHERE id = ?', [search_id])
        num_searches = cur.fetchone()
        # rank based on count in searches table

        # Get ingredient list
        ingredient_list = get_searched_combinations(conn, search_id)

        ic_list.append({
            "rank": rank,
            "num_searches": num_searches,
            "ingredient_list": ingredient_list
        })
        
        rank += 1

    cur.close()

    return {
        "ingredient_combination_list": ic_list
    }

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
