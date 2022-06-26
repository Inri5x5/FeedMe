'''
Helper functions
'''

import json
import jwt


def create_token(email):
    return jwt.encode({"email": email}, "", algorithm="HS256")

def get_contributor(email, password):
    # Get contributors json file
    f = open('contributors.json')
    contributors = json.load(f)
    f.close()

    ret = {}
    for c in contributors:
        # Contributor exists
        if c["email"] == email & c["password"] == password:
            ret = {
                "status": 200,
                "body": {}
            }
        # Contributor exists but wrong password
        elif c["email"] == email & c["password"] != password:
            ret = {
                "status": 400,
                "body": {"error": "Wrong password"}
            }

    return ret

def get_ruser(email, password):
    # Get users json file
    f = open('users.json')
    users = json.load(f)
    f.close()

    ret = {}
    for u in users:
        # User exists
        if u["email"] == email & u["password"] == password:
            ret = {
                "status": 200,
                "body": {}
            }
        # User exists but wrong password
        elif u["email"] == email & u["password"] != password:
            ret = {
                "status": 400,
                "body": {"error": "Wrong password"}
            }

    return ret
