'''
Helper functions
'''

import json
import jwt


def create_token(email):
    return jwt.encode({"email": email}, "", algorithm="HS256")