'''
Helper functions
'''

import json
import jwt
from datetime import datetime

def generate_token(email):
    payload = {"email": email, "datetime": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")}
    return jwt.encode(payload, "", algorithm="HS256")

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
    ret = False

    if (is_contributor):
        f = open('./data/contributors_table.json')
        contributors = json.load(f)
        f.close()

        for c in contributors:
            if c["email"] == email and c["password"] == password:
                ret = True
    else:
        f = open('./data/rusers_table.json')
        users = json.load(f)
        f.close()

        for u in users:
            if u["email"] == email and u["password"] == password:
                ret = True

    return ret

