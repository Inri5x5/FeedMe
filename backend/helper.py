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

def generate_token(email):
    payload = {"email": email, "datetime": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")}
    return jwt.encode(payload, "", algorithm="HS256")

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

def valid_email(email):
    if not re.search(regex, email):
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

def check_password(conn, email, password, is_contributor):
    cur = conn.cursor()
    
    if (is_contributor):
        cur.execute('SELECT * from Contributors WHERE email = %s AND password = %s')
        info = cur.fetchone()
    else:
        cur.execute('SELECT * from Rusers WHERE email = %s AND password = %s')
        info = cur.fetchone()

    if not info: 
        return False
    else:
        return True

def get_recipe_details(db_path, recipe_id):
    # initialise return dict
    ret = {}

    # initialise db connection
    conn = sqlite3.connect(db_path)
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

    conn.close()
    
    return ret

def valid_recipe_id(db_path, recipe_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM Recipe WHERE recipe_id = ?", [recipe_id])
    recipe = c.fetchall()
    if recipe == None: 
        print("was here")
        return False
    
    return True
