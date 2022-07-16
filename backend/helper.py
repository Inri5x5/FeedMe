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
        conn = sqlite3.connect("database.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

########################### TOKENS ##########################
def generate_token(email):
    payload = {"email": email, "datetime": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")}
    return jwt.encode(payload, "", algorithm="HS256")

def decode_token(conn, token):
    cur = conn.cursor()

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

    # Get tags of the given tag category
    cur.execute('''SELECT name, tag_id FROM Tags 
        WHERE tag_category_id = %s''', [tag_category_id])
    info = cur.fetchall()
    cur.close()

    tags = []
    for i in info:
        name, tag_id = i
        tags.append(
            {"name": name, "tag_id": tag_id}
        )

    return tags

def get_tags_and_categories(conn):
    cur = conn.cursor()
    cur.execute('''
        SELECT tc.id, tc.name, 
        FROM Tag_Categories tc
            JOIN Tags t on t.tag_category_id = tc.tag_category_id
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

def get_recipe_details(conn, recipe_id):
    c = conn.cursor()
    
    # initialise return dict
    ret = {}

    # Get General Recipe details
    c.execute("SELECT * FROM Recipe WHERE recipe_id = ?", [recipe_id])
    recipe = c.fetchone()
    ret.update({'recipe_id' : recipe[0]})
    ret.update({'title' : recipe[1]})
    ret.update({'description' : recipe[2]})
    ret.update({'img' : recipe[3]})
    ret.update({'video' : recipe[4]})
    ret.update({'time_required' : recipe[5]})
    ret.update({'servings' : recipe[6]})

    # Get steps
    c.execute("SELECT * FROM Steps WHERE recipe_id = ?", [recipe_id])
    steps = c.fetchall()
    ret_steps = []
    for row in steps:
        ret_steps.append({'step_number': row[1], 'description' : row[2]})
    ret.update({'steps' : ret_steps})

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
    
    return ret