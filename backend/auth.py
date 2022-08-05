from helper import *
from error import *

def register_helper(email, password, username):
    # Connect to database
    conn = db_connection()

    if not email or not password or not username:
        conn.close()
        raise InputError
    
    if not valid_email(email):
        conn.close()
        raise InputError("Invalid email")

    if email_already_exists(conn, email):
        conn.close()
        raise InputError("Email already in use")

    ruser_id = get_new_user_id(conn)
    add_new_user(conn, ruser_id, email, password, username)

    token = generate_token(ruser_id, False)
    add_token(conn, token, ruser_id, False)

    return token

def login_helper(email, password, is_contributor):
    # Connect to database
    conn = db_connection()

    # Get user id
    if is_contributor:
        user_id = get_contributor(conn, email)
    else:
        user_id = get_ruser(conn, email)
    
    # User does not exist
    if (user_id < 0):
        raise InputError("User is not registered")

    # Check password
    if not check_password(conn, email, password, is_contributor):
        raise InputError("Incorrect password")
    
    # Create token 
    token = generate_token(user_id, is_contributor)

    # Update tokens json file
    add_token(conn, token, user_id, is_contributor)

    return token
