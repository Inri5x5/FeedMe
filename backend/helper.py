'''
Helper functions
'''

import json
import jwt
import re
from datetime import datetime

regex = '^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$'

def generate_token(email):
    payload = {"email": email, "datetime": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")}
    return jwt.encode(payload, "", algorithm="HS256")

def validate_token(token):
    # Get tokens json file
    f = open('./data/tokens_table.json', 'r')
    tokens = json.load(f)
    f.close()

    # Validate token
    for t in tokens:
        if t["token"] == token:
            return True
            
    return False

def valid_email(email):
    if not re.search(regex, email):
        return False
    else:
        return True

def get_contributor(email):
    # Get contributors json file
    f = open('./data/contributors_table.json')
    contributors = json.load(f)
    f.close()

    user_id = -1
    for c in contributors:
        # Contributor exists
        if c["email"] == email:
            user_id = c["contributor_id"]

    return user_id

def get_ruser(email):
    # Get users json file
    f = open('./data/rusers_table.json')
    users = json.load(f)
    f.close()

    user_id = -1
    for u in users:
        # User exists
        if u["email"] == email:
            user_id = u["ruser_id"]

    return user_id

def check_password(email, password, is_contributor):
    if (is_contributor):
        f = open('./data/contributors_table.json')
        contributors = json.load(f)
        f.close()

        for c in contributors:
            if c["email"] == email and c["password"] == password:
                return True
    else:
        f = open('./data/rusers_table.json')
        users = json.load(f)
        f.close()

        for u in users:
            if u["email"] == email and u["password"] == password:
                return True

    return False

