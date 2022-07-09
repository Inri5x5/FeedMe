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