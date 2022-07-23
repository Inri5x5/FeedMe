'''
Helper functions
'''

import json
import jwt
import re
import sqlite3
from datetime import datetime

regex = '^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$'

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("./database/database.sqlite")
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
    except sqlite3.error as e:
        print(e)
    return conn

########################### TOKENS ##########################
def generate_token(email):
    # NOTE: use id instead of email in the token!
    payload = {"email": email, "datetime": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")}
    return jwt.encode(payload, "", algorithm="HS256")

def decode_token(conn, token):
    cur = conn.cursor()

    # Get email
    payload = jwt.decode(token, "", algorithms=["HS256"])
    email = payload["email"]

    # Check if contributor
    cur = conn.cursor()
    cur.execute('SELECT ruser_id, contributor_id FROM Tokens WHERE token = ?', [token])
    info = cur.fetchone()
    cur.close()

    # Find user id
    if info[1] is not None:
        user_id = get_contributor(conn, email)
        is_contributor = True
    else:
        user_id = get_ruser(conn, email)
        is_contributor = False

    return {
        "email": email, 
        "user_id": user_id,
        "is_contributor": is_contributor
    }

def validate_token(conn, token):
    cur = conn.cursor()
    cur.execute('SELECT * FROM Tokens WHERE token = ?', [token])
    info = cur.fetchone()
    cur.close()

    if not info:
        return False
    else:
        return True

def add_token(conn, token, user_id, is_contributor):
    cur = conn.cursor()
    if is_contributor:
        cur.execute('INSERT INTO Tokens VALUES (?, ?, ?)', (token, None, user_id))
    else:
        cur.execute('INSERT INTO Tokens VALUES (?, ?, ?)', (token, user_id, None))
        
    conn.commit()
    cur.close()

    return 0

def delete_token(conn, token):
    cur = conn.cursor()
    cur.execute('DELETE FROM Tokens WHERE token = ?', [token])
    cur.close()

    return 0

########################### AUTH ##########################

def email_already_exists(conn, email):
    cur = conn.cursor()
    cur.execute('SELECT * from Rusers WHERE email = ?', [email])
    info = cur.fetchone()

    cur.close()

    if not info: 
        return False
    else:
        return True

def get_new_user_id(conn):
    cur = conn.cursor()
    cur.execute('SELECT max(id) from Rusers')
    max = cur.fetchone()[0]

    cur.close()
    return max + 1

def add_new_user(conn, ruser_id, email, password, username):
    cur = conn.cursor()
    insert_query = """INSERT INTO rusers (id, email, username, password, profile_picture) VALUES (?, ?, ?, ?, ?)"""
    cur = cur.execute(insert_query, (ruser_id, email, username, password, ""))
    conn.commit()

def valid_email(email):
    if not re.search(regex, email):
        return False
    else:
        return True

def check_password(conn, email, password, is_contributor):
    cur = conn.cursor()
    if (is_contributor):
        cur.execute('SELECT * from Contributors WHERE email = ? AND password = ?', [email, password])
        info = cur.fetchone()
    else:
        cur.execute('SELECT * from Rusers WHERE email = ? AND password = ?', [email, password])
        info = cur.fetchone()

    cur.close()

    if not info: 
        return False
    else:
        return True
    
def get_contributor(conn, email):
    cur = conn.cursor()
    cur.execute('SELECT id FROM Contributors WHERE email = ?', [email])
    info = cur.fetchone()
    cur.close()

    if not info: 
        return -1
    else: 
        return info[0]

def get_ruser(conn, email):
    cur = conn.cursor()
    cur.execute('SELECT id FROM RUsers WHERE email = ?', [email])
    info = cur.fetchone()
    cur.close()

    if not info: 
        return -1
    else: 
        return info[0]

########################### RECIPES ##########################

def get_tag_categories(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM tagCategories')
    info = cur.fetchall()
    cur.close()
    
    tag_categories = []
    for i in info: 
        id, name = i
        tag_categories.append({"name": name, "category_id": id})
    
    return tag_categories

def get_tags(conn, tag_category_id):
    cur = conn.cursor()

    # Get tags of the given tag category
    cur.execute('''SELECT name, id FROM Tags 
    WHERE tag_category_id = ?''', [tag_category_id])
    info = cur.fetchall()
    cur.close()

    tags = []
    for i in info:
        name, id = i
        tags.append(
            {"name": name, "tag_id": id}
        )

    return tags

def get_tags_and_categories(conn):
    cur = conn.cursor()
    cur.execute('''
        SELECT tc.id, tc.name
        FROM tagCategories tc
            JOIN Tags t on t.tag_category_id = tc.id
    ''')
    info = cur.fetchall()
    cur.close()
    
    tag_categories = []
    for i in info: 
        tc_id, tc_name = i
        tags = get_tags(conn, tc_id)
        tag_categories.append(
            {"tag_category_id": tc_id, "tag_category_name": tc_name, "tags": tags}
        )
    
    return tag_categories

def get_recipe_details(conn, recipe_id, user_details):
    # initialise return dict
    ret = {}

    # initialise db connection
    c = conn.cursor()
    # print(type(recipe_id))
    # print(recipe_id)
    # Get General Recipe details
    c.execute("SELECT * FROM recipes WHERE id = ?", [recipe_id])
    recipe = c.fetchone()
    # print(recipe)
    ret.update({'recipe_id' : recipe[0]})
    ret.update({'title' : recipe[1]})
    ret.update({'description' : recipe[2]})
    ret.update({'image' : recipe[3]})
    ret.update({'video' : recipe[4]})
    ret.update({'time_required' : recipe[5]})
    ret.update({'servings' : recipe[6]})

    # Get steps
    qry = '''
        SELECT * 
        FROM steps
        WHERE recipe_id = ?
        ORDER BY step_number ASC
    '''
    c.execute(qry, [recipe_id])
    info = c.fetchall()
    steps = []
    for i in info:
        recipe_id, step_id, description, image = i
        steps.append({
            "step_id": step_id,
            "description": description,
            "image": image
        })
    ret.update({'steps' : steps})

    # Get tags
    tags = []
    c.execute("SELECT * FROM TaginRecipe WHERE recipe_id = ?", [recipe_id])
    tag_ids = c.fetchall()
    for row in tag_ids:
        c.execute("SELECT * FROM Tags WHERE id = ?", [row[1]])
        tag_data = c.fetchone()
        tags.append({'tag_id': tag_data[0], 'name' : tag_data[2]})
    ret.update({'tags' : tags})

    # Get author and public state
    c.execute("SELECT contributor_id FROM PublicRecipes WHERE recipe_id = ?", [recipe_id])
    info = c.fetchone()
    if info is not None:
        author_id = info[0]
        c.execute("SELECT username FROM Contributors WHERE id = ?", [author_id])
        author_name = c.fetchone()[0]
        ret.update({'author' : author_name, 'public_state' : 'public'})
    else:
        c.execute("SELECT ruser_id FROM PersonalRecipes WHERE recipe_id = ?", [recipe_id])
        author_id = c.fetchone()[0]
        c.execute("SELECT username FROM RUsers WHERE id = ?", [author_id])
        author_name = c.fetchone()[0]
        ret.update({'author' : author_name, 'public_state' : 'private'})

    # Get ingredients
    ingredients = []
    c.execute("SELECT * FROM IngredientinRecipe WHERE recipe_id = ?", [recipe_id])
    i = c.fetchall()
    for row in i:
        c.execute("SELECT name FROM ingredients WHERE id = ?", [row[1]])
        ingredients.append({'name' : c.fetchone()[0], 'ingredient_id' : row[1], 'description' : row[2]})
    ret.update({'ingredients' : ingredients})

    # get skill videos
    skill_videos = []
    c.execute("SELECT * FROM SkillVideoinRecipe WHERE recipe_id = ?", [recipe_id])
    videos = c.fetchall()
    for video in videos:
        c.execute("SELECT * FROM SkillVideos WHERE id = ?", [video[1]])
        info = c.fetchone()
        c.execute("SELECT username FROM Contributors WHERE id = ?", [info[1]])
        name = c.fetchone()[0]
        prefix = "https://www.youtube.com/"
        skill_videos.append({"video_id" : info[0], "title": info[2], "url": prefix + info[3], "is_full_recipe_video" : info[4], "creator" : name})
    ret.update({'skill_videos' : skill_videos})
    
    # get ratings
    c.execute("SELECT * FROM RecipeRatings WHERE recipe_id = ?", [recipe_id])
    ratings = c.fetchall()
    counter = 0
    total = 0
    for row in ratings:
        counter = counter + 1
        total = total + row[3]
    if (counter == 0) :
        avg_rating = 0
    else :
        avg_rating = total / counter
    ret.update({'avg_rating' : avg_rating})

    # get saved or not 
    b = has_saved(conn, recipe_id, user_details)
    ret.update({'saved' : b})

    # conn.close()

    return ret

def valid_recipe_id(conn, recipe_id):
    c = conn.cursor()
    c.execute("SELECT * FROM recipes WHERE id = ?", [recipe_id])
    recipe = c.fetchall()
    if recipe == None: 
        return False
    
    return True

def has_saved(conn, recipe_id, user_details):
    if (user_details == -1): return False
    c = conn.cursor()
    if user_details["is_contributor"] == False:
        c.execute("SELECT * FROM recipeSaves WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, user_details["user_id"]])
    else:
        c.execute("SELECT * FROM recipeSaves WHERE recipe_id = ? AND contributor_id = ?", [recipe_id, user_details["user_id"]])
    
    info = c.fetchone()
    if info is None:
        return False
    
    return True

def has_rated(conn, recipe_id, user_details):
    c = conn.cursor()
    if user_details["is_contributor"] == False:
        c.execute("SELECT * FROM RecipeRatings WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, user_details["user_id"]])
    else:
        c.execute("SELECT * FROM RecipeRatings WHERE recipe_id = ? AND contributor_id = ?", [recipe_id, user_details["user_id"]])
    
    if c.fetchone() is None: # INCLUDE
        return False
    
    return True

def insert_recipe_details(conn, user_details, recipe_id, req):
    c = conn.cursor()

    # Update data in "Recipe"
    c.execute("INSERT INTO Recipes(id, title, description, image, video, time_required, servings) VALUES (?, ?, ?, ?, ?, ?, ?)", (recipe_id, req['title'], req['description'], req['image'], req['video'], req['time_required'], req['servings']))
    # Update data in "Ingredient in Recipe"
    ingredients = req['ingredients']
    for i_dict in ingredients:
        c.execute("INSERT INTO IngredientinRecipe(recipe_id, ingredient_id, description) VALUES (?, ?, ?)", (recipe_id, i_dict['ingredient_id'], i_dict['description']))

    # Update data in "Tag in Recipe"
    tags = req['tags']
    for t_dict in tags:
        c.execute("INSERT INTO TaginRecipe VALUES (?, ?)", (recipe_id, t_dict['tag_id']))
    
    # Update "Skill Video in Recipe" **(Pending Confirmation)
    videos = req['skill_videos']
    for v in videos:
        c.execute("INSERT INTO SkillVideoinRecipe VALUES (?, ?)", (recipe_id, v))
    
    # Update data in "Steps" **(Pending confirmation)
    steps = req['steps']
    for s_dict in steps:
        c.execute("INSERT INTO Steps VALUES (?, ?, ?, ?)", (recipe_id, s_dict['step_id'], s_dict['description'], ''))

    # if contributor has public_state = public it should go into "Public Recipes"
    # if contributor has public_state = private it should go into "Personal Recipes"
    if user_details["is_contributor"]:
        if str(req['public_state']) == "public":
            c.execute("INSERT INTO PublicRecipes VALUES (?, ?)", (recipe_id, user_details["user_id"]))
            c.execute("INSERT INTO PersonalRecipes(contributor_id, recipe_id) VALUES (?, ?)", (user_details["user_id"], recipe_id))
        else:
            c.execute("INSERT INTO PersonalRecipes(contributor_id, recipe_id) VALUES (?, ?)", (user_details["user_id"], recipe_id))
        conn.commit()
    # If update request is made my ruser, it should go into personal recipes with new recipe id - ** should there be a author field here?
    else:
        c.execute("INSERT INTO PersonalRecipes(ruser_id, recipe_id) VALUES (?, ?)", (user_details["user_id"], recipe_id))
    
    conn.commit()
    c.close()
    
    return 

def update_recipe_details(conn, user_details, recipe_id, req):
    c = conn.cursor()

    # Update data in "Recipe"
    c.execute("UPDATE Recipes SET title=?, description=?, image=?, video=?, time_required=?, servings=? WHERE id = ?", (req['title'], req['description'], req['image'], req['video'], req['time_required'], req['servings'], recipe_id))

    # Update data in "Ingredient in Recipe"
    ingredients = req['ingredients']
    c.execute("DELETE FROM IngredientinRecipe WHERE recipe_id=?", [recipe_id])
    for i_dict in ingredients:
        c.execute("INSERT INTO IngredientinRecipe(recipe_id, ingredient_id, description) VALUES (?, ?, ?)", (recipe_id, i_dict['ingredient_id'], i_dict['description']))

    # Update data in "Tag in Recipe"
    tags = req['tags']
    c.execute("DELETE FROM TaginRecipe WHERE recipe_id=?", [recipe_id])
    for t_dict in tags:
        c.execute("INSERT INTO TaginRecipe VALUES (?, ?)", (recipe_id, t_dict['tag_id']))
    
    # Update "Skill Video in Recipe" **(Pending Confirmation)
    videos = req['skill_videos']
    c.execute("DELETE FROM SkillVideoinRecipe WHERE recipe_id=?", [recipe_id])
    for v in videos:
<<<<<<< HEAD
        c.execute("INSERT INTO SkillVideoinRecipe VALUES (?, ?)", (recipe_id, v))
=======
        c.execute("INSERT INTO SkillVideoinRecipe VALUES (?, ?)", (recipe_id, v['skill_video_id']))
        # c.execute("UPDATE SkillVideoinRecipe SET video_id=? WHERE recipe_id-?", (v, recipe_id))
>>>>>>> sprint_three_data
    
    # Update data in "Steps" **(Pending confirmation)
    steps = req['steps']
    c.execute("DELETE FROM Steps WHERE recipe_id=?", [recipe_id])
    for s_dict in steps:
        c.execute("INSERT INTO Steps VALUES (?, ?, ?, ?)", (recipe_id, s_dict['step_id'], s_dict['description'], ''))
    
    # Update public or private state
    #public_status = 
    
    conn.commit()
    c.close()
    
    return 

########################### SEARCHES ##########################

def get_new_search_id(conn):
    cur = conn.cursor()
    cur.execute('SELECT MAX(id) FROM Searches')
    max = cur.fetchone()[0]
    cur.close()
    return max + 1

def get_searched_combinations(conn, search_id):
    '''Get the ingredients' ids and names of a 
    particular search id'''

    cur = conn.cursor()
    cur.execute('''
        SELECT iss.ingredient_id, i.name
        FROM IngredientInSearch iss
            JOIN Ingredients i on i.id = iss.ingredient_id
        WHERE search_id = ?''', [search_id])
    
    ingredients = []
    info = cur.fetchall()
    for i in info:
        id, name = i
        ingredients.append({"id": id, "name": name})

    cur.close()

    return ingredients

def check_search_combinations(conn, ingredients_req):
    new_combination = True
    search_id = -1

    cur = conn.cursor()
    cur.execute('''
        SELECT s.id, GROUP_CONCAT(iis.ingredient_id)
        FROM Searches s
            JOIN IngredientInSearch iis on iis.search_id = s.id
        GROUP BY s.id
    ''')
    info = cur.fetchall()
    for i in info:
        s_id, ingredients = i
        ingredients_split = [int(j) for j in ingredients.split(',')]    
        if set(ingredients_split) == set(ingredients_req):
            new_combination = False
            search_id = s_id
            break
    cur.close()

    return new_combination, search_id