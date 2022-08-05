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
    except sqlite3.Error as e:
        print(e)
    return conn

########################### TOKENS ##########################
def generate_token(user_id, is_contributor):
    # NOTE: use id instead of email in the token!
    payload = {
        "user_id": user_id, 
        "is_contributor": is_contributor, 
        "datetime": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    }
    return jwt.encode(payload, "", algorithm="HS256")

def decode_token(conn, token):
    # Get user details
    payload = jwt.decode(token, "", algorithms=["HS256"])
    user_id = payload["user_id"]
    is_contributor = payload["is_contributor"]

    return {
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

    c.execute("SELECT * FROM recipes WHERE id = ?", [recipe_id])
    recipe = c.fetchone()

    ret.update({'recipe_id' : recipe[0]})
    ret.update({'title' : recipe[1]})
    ret.update({'description' : recipe[2]})
    ret.update({'image' : recipe[3]})

    if not recipe[4]:
        ret.update({'video' : None})
    else:
        ret.update({'video' : recipe[4]})
    
    ret.update({'time_required' : recipe[5]})
    ret.update({'servings' : recipe[6]})
    ret.update({'original_id' : recipe[7]})

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
    c.execute("SELECT * FROM PersonalRecipes WHERE recipe_id = ?", [recipe_id])
    info = c.fetchone()
    if info is not None:
        ruser_id = info[0]
        contributor_id = info[1]
    else:
        c.execute("SELECT * FROM PublicRecipes WHERE recipe_id = ?", [recipe_id])
        info = c.fetchone()
        ruser_id = None
        contributor_id = info[1]

    if ruser_id is None: # contributor wrote recipe
        c.execute("SELECT username FROM Contributors WHERE id = ?", [contributor_id])
    else: # ruser wrote recipe
        c.execute("SELECT username FROM Rusers WHERE id = ?", [ruser_id])

    author_name = c.fetchone()[0]

    c.execute("SELECT * FROM PublicRecipes WHERE recipe_id = ?", [recipe_id])
    is_public = c.fetchone()
    if is_public is None:
        public_state = 'private'
    else:
        public_state = 'public'

    ret.update({'author' : author_name, 'public_state' : public_state})

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
        prefix = "https://www.youtube.com/"
        skill_videos.append({"video_id" : info[0], "title": info[2], "url": prefix + info[3]})
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
    b = has_saved_recipe(conn, recipe_id, user_details)
    ret.update({'saved' : b})

    # conn.close()

    return ret

def valid_recipe_id(conn, recipe_id):
    c = conn.cursor()
    c.execute("SELECT * FROM recipes WHERE id = ?", [recipe_id])
    recipe = c.fetchone()
    if recipe == None: 
        return False
    
    return True

def valid_video_id(conn, video_id):
    c = conn.cursor()
    c.execute("SELECT * FROM skillVideos WHERE id = ?", [video_id])
    recipe = c.fetchone()
    if recipe == None: 
        return False
    
    return True

def has_saved_recipe(conn, recipe_id, user_details):
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

def has_saved_video(conn, video_id, user_id):
    c = conn.cursor()
    c.execute("SELECT * FROM skillVideoSaves WHERE skill_video_id = ? AND ruser_id = ?", [video_id, user_id])

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
    if not req['video']:
        video = None
    else:
        video = req['video']
    
    #print(req['original_id'])
    c.execute("INSERT INTO Recipes(id, title, description, image, video, time_required, servings, original_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (recipe_id, req['title'], req['description'], req['image'], video, req['time_required'], req['servings'], req['original_id']))
    
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
        c.execute("INSERT INTO SkillVideoinRecipe VALUES (?, ?)", (recipe_id, v['video_id']))
    
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
    if not req['video']:
        video = None
    else:
        video = req['video']
    
    if req['original_id'] is None:
        original_id = None
    else:
        original_id = req['original_id']
    
    c.execute("UPDATE Recipes SET title=?, description=?, image=?, video=?, time_required=?, servings=?, original_id=? WHERE id = ?", (req['title'], req['description'], req['image'], video, req['time_required'], req['servings'], original_id, recipe_id))

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
    
    # Update "Skill Video in Recipe"
    videos = req['skill_videos']
    c.execute("DELETE FROM SkillVideoinRecipe WHERE recipe_id=?", [recipe_id])
    for v in videos:
        c.execute("INSERT INTO SkillVideoinRecipe VALUES (?, ?)", (recipe_id, v['video_id']))
    
    # Update data in "Steps"
    print("recipe id type")
    print(type(recipe_id))
    print(recipe_id)
    steps = req['steps']
    c.execute("DELETE FROM Steps WHERE recipe_id=?", [recipe_id])
    for s_dict in steps:
        print(s_dict['step_id'])
        print(type(s_dict['step_id']))
        c.execute("INSERT INTO Steps VALUES (?, ?, ?, ?)", (recipe_id, s_dict['step_id'], s_dict['description'], ''))
    
    # Update public or private state
    public_status = req['public_state']

    c.execute("SELECT contributor_id FROM PublicRecipes WHERE recipe_id = ?", [recipe_id])
    info = c.fetchone()
    if info is not None and public_status == "private": # currently a public recipe and becomes private
        # Delete from publicRecipes
        c.execute("DELETE FROM publicRecipes WHERE recipe_id = ?", [recipe_id])
        # Add to PersonalRecipes
        if user_details["is_contributor"]:
            c.execute("INSERT INTO PersonalRecipes(contributor_id, recipe_id) VALUES (?, ?)", (user_details["user_id"], recipe_id))
        else:
            c.execute("INSERT INTO PersonalRecipes(ruser_id, recipe_id) VALUES (?, ?)", (user_details["user_id"], recipe_id))
    elif info is None and public_status == "public": # currently a personal personal recipe and becomes public
        # DO NOT Delete from personalRecipes since a contributor's public recipes is also their personal recipe
        c.execute("INSERT INTO PublicRecipes VALUES (?, ?)", (recipe_id, user_details["user_id"]))
        c.execute("DELETE FROM PersonalRecipes WHERE recipe_id = ? and contributor_id = ?", [recipe_id, user_details["user_id"]])
    
    conn.commit()
    c.close()
    
    return

def get_skill_videos(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT * FROM SkillVideos")
    videos = c.fetchall()
    
    video_list = []
    if user_id == -1:
        for row in videos:
            c.execute("SELECT * FROM Contributors WHERE id = ?", [row[1]])
            creator_details = c.fetchone()
            prefix = "https://www.youtube.com/"
            video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4], "isSaved" : False})
    else:
        for row in videos:
            c.execute("SELECT * FROM Contributors WHERE id = ?", [row[1]])
            creator_details = c.fetchone()
            prefix = "https://www.youtube.com/"
            c.execute("SELECT * FROM SkillVideoSaves WHERE ruser_id = ? AND skill_video_id = ?", [user_id, row[0]])
            has_saved = c.fetchone()
            if has_saved is None:
                video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4], "isSaved" : False})
            else:
                video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4], "isSaved" : True})

    return video_list

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