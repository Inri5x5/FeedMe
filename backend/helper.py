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
        conn = sqlite3.connect('feedme.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

########################### TOKENS ##########################
def generate_token(email):
    payload = {"email": email, "datetime": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")}
    return jwt.encode(payload, "", algorithm="HS256")

def decode_token(conn, token):
    # Get email
    payload = jwt.decode(token, "", algorithms=["HS256"])
    email = payload["email"]

    # Check if contributor
    cur = conn.cursor()
    cur.execute('SELECT is_contributor FROM Tokens WHERE token = %s', [token])
    is_contributor = cur.fetchone()
    cur.close()

    # Find user id
    if is_contributor:
        user_id = get_contributor(conn, email)
    else:
        user_id = get_ruser(conn, email)

    return {
        "email": email, 
        "user_id": user_id,
        "is_contributor": is_contributor
    }

def validate_token(conn, token):
    cur = conn.cursor()
    cur.execute('SELECT 1 FROM Tokens WHERE token = %s', [token])
    info = cur.fetchone()
    cur.close()

    if not info:
        return False
    else:
        return True

def add_token(conn, token, user_id, is_contributor):
    cur = conn.cursor()
    cur.execute('INSERT INTO Tokens VALUES (?, ?, ?)', (token, user_id, is_contributor))
    cur.close()

    return 0

def delete_token(conn, token):
    cur = conn.cursor()
    cur.execute('DELETE FROM Tokens WHERE token = %s', [token])
    cur.close()

    return 0

########################### AUTH ##########################

def valid_email(email):
    if not re.search(regex, email):
        return False
    else:
        return True

def check_password(conn, email, password, is_contributor):
    cur = conn.cursor()
    
    if (is_contributor):
        cur.execute('SELECT * from Contributors WHERE email = %s AND password = %s')
        info = cur.fetchone()
    else:
        cur.execute('SELECT * from Rusers WHERE email = %s AND password = %s')
        info = cur.fetchone()

    cur.close()

    if not info: 
        return False
    else:
        return True
    
def get_contributor(conn, email):
    cur = conn.cursor()
    cur.execute('SELECT contributor_id FROM Contributors WHERE email = %s', [email])
    info = cur.fetchone()
    cur.close()

    if not info: 
        return -1
    else: 
        return info

def get_ruser(conn, email):
    cur = conn.cursor()
    cur.execute('SELECT ruser_id FROM RUsers WHERE email = %s', [email])
    info = cur.fetchone()
    cur.close()

    if not info: 
        return -1
    else: 
        return info

########################### RECIPES ##########################

def get_tag_categories(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM Tag_Categories')
    info = cur.fetchall()
    cur.close()
    
    tag_categories = []
    for i in info: 
        tag_category_id, name = i
        tag_categories.append(
            {"name": name, "category_id": tag_category_id}
        )
    
    return tag_categories

def get_tags(conn, tag_category_id):
    cur = conn.cursor()

    if tag_category_id is None:
        cur.execute('SELECT name, tag_id FROM Tags')
    else:
        cur.execute('''
        SELECT name, tag_id 
        FROM Tags 
        WHERE tag_category_id = %s''', [tag_category_id]
        )

    info = cur.fetchall()
    cur.close()

    tags = []
    for i in info:
        tag_id, name = i
        tags.append(
            {"name": name, "tag_id": tag_id}
        )

    return tags

def get_recipe_steps(conn, recipe_id):
    cur = conn.cursor()
    qry = '''
        SELECT * 
        FROM Steps
        WHERE recipe_id = %s
        ORDER BY step_number ASC
    '''
    cur.execute(qry, [recipe_id])
    info = cur.fetchall()
    cur.close()
    
    steps = []
    for i in info:
        recipe_id, step_id, description, image = i
        steps.append({
            "step_id": step_id,
            "description": description
        })

    return steps

def get_recipe_details(conn, recipe_id):
    # initialise return dict
    ret = {}

    # initialise db connection
    c = conn.cursor()

    # Get General Recipe details
    c.execute("SELECT * FROM Recipe WHERE recipe_id = ?", [recipe_id])
    recipe = c.fetchone()
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
        FROM Steps
        WHERE recipe_id = %s
        ORDER BY step_number ASC
    '''
    c.execute(qry, [recipe_id])
    info = c.fetchall()
    steps = []
    for i in info:
        recipe_id, step_id, description, image = i
        steps.append({
            "step_id": step_id,
            "description": description
        })
    ret.update({'steps' : steps})

    # Get tags
    tags = []
    c.execute("SELECT * FROM Tag_in_Recipe WHERE recipe_id = ?", [recipe_id])
    tag_ids = c.fetchall()
    for row in tag_ids:
        c.execute("SELECT * FROM Tags WHERE tag_id = ?", [row[1]])
        tag_data = c.fetchone()
        tags.append({'tag_id': tag_data[0], 'name' : tag_data[2]})
    ret.update({'tags' : tags})

    # Get author and public state
    c.execute("SELECT author_id FROM Public_Recipes WHERE recipe_id = ?", [recipe_id])
    if c.fetchone() != None:
        author_id = c.fetchone()[0]
        c.execute("SELECT username FROM Contributors WHERE contributor_id = ?", [author_id])
        author_name = c.fetchone()[0]
        ret.update({'author' : author_name, 'public_state' : 'public'})
    else:
        c.execute("SELECT ruser_id FROM Personal_Recipes WHERE recipe_id = ?", [recipe_id])
        author_id = c.fetchone()[0]
        c.execute("SELECT username FROM RUSers WHERE ruser_id = ?", [author_id])
        author_name = c.fetchone()[0]
        ret.update({'author' : author_name, 'public_state' : 'private'})

    # Get ingredients
    ingredients = []
    c.execute("SELECT * FROM Ingredient_in_Recipe WHERE recipe_id = ?", [recipe_id])
    i = c.fetchall()
    for row in i:
        c.execute("SELECT name FROM ingredients_table WHERE ingredient_id = ?", [row[1]])
        ingredients.append({'name' : c.fetchone()[0], 'ingredient_id' : row[1], 'amount' : row[2]})
    ret.update({'ingredients' : ingredients})

    # get skill videos
    skill_videos = []
    c.execute("SELECT * FROM Skill_Video_in_Recipe WHERE recipe_id = ?", [recipe_id])
    vids = c.fetchall()
    for row in vids:
        c.execute("SELECT link FROM Skill_Videos WHERE video_id = ?", [row[1]])
        skill_videos.append(c.fetchone()[0])
    ret.update({'skill_videos' : skill_videos})
    
    # get ratings
    c.execute("SELECT * FROM Recipe_Ratings WHERE recipe_id = ?", [recipe_id])
    ratings = c.fetchall()
    counter = 0
    total = 0
    for row in ratings:
        counter = counter + 1
        total = total + row[2]
    avg_rating = total / counter
    ret.update({'avg_rating' : avg_rating})

    # get saved or not 

    conn.close()

    return ret

def valid_recipe_id(conn, recipe_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Recipe WHERE recipe_id = ?", [recipe_id])
    recipe = c.fetchall()
    if recipe == None: 
        return False
    
    return True

def has_saved(conn, recipe_id, user_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Recipe WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, user_id])
    if c.fetchall() == None:
        return False
    
    return True

def has_rated(conn, recipe_id, user_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Recipe_Ratings WHERE recipe_id = ? AND author_id = ?", [recipe_id, user_id])
    if c.fetchall() == None:
        return False
    
    return True

def update_recipe_details(conn, user_details, recipe_id, req):
    c = conn.cursor()

    # Update data in "Recipe"
    c.execute("INSERT INTO Recipe VALUES (?, ?, ?, ?, ?, ?, ?)", (req['recipe_id'], req['title'], req['description'], req['image'], req['video'], req['time_required'], req['servings']))

    # Update data in "Ingredient in Recipe"
    ingredients = req['ingredients']
    for i_dict in ingredients:
        c.execute("INSERT INTO Ingredient_in_Recipe VALUES (?, ?, ?)", (recipe_id, i_dict['ingredient_id'], i_dict['amount']))

    # Update data in "Tag in Recipe"
    tags = req['tags']
    for t_dict in tags:
        c.execute("INSERT INTO Tag_in_Recipe VALUES (?, ?)", (recipe_id, t_dict['tag__id']))
    
    # Update "Skill Video in Recipe" **(Pending Confirmation)
    videos = req['skill_videos']
    for v in videos:
         c.execute("INSERT INTO Skill_Video_in_Recipe VALUES (?, ?)", (recipe_id, v))
    
    # Update data in "Steps" **(Pending confirmation)
    steps = req['steps']
    for s_dict in steps:
        c.execute("INSERT INTO Steps VALUES (?, ?, ?, ?)", (recipe_id, s_dict['step_number'], s_dict['description'], s_dict['image']))

    # if contributor has public_state = public it should go into "Public Recipes"
    # if contributor has public_state = private it should go into "Draft Recipes"
    if user_details["is_contributor"]:
        if str(req['public_state']) == "public":
            c.execute("INSERT INTO Public_Recipes VALUES (?, ?)", (recipe_id, user_details["user_id"]))
        else:
            c.execute("INSERT INTO Draft_Recipes VALUES (?, ?)", (recipe_id, user_details["user_id"]))
    # If update request is made my ruser, it should go into personal recipes with new recipe id - ** should there be a author field here?
    else:
        c.execute("INSERT INTO Personal_Recipes VALUES (?, ?)", (recipe_id, user_details["user_id"]))
    
    return 
