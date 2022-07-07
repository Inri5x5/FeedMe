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

