from cmath import atanh
from flask import Flask, render_template, request
from helper import *
from error import AccessError, InputError
import json
from json import dumps
import sqlite3
import os.path

db_path = os.path.join("./database/", "nepka.db")
regex = '^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$'

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

app = Flask(__name__)

app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.register_error_handler(Exception, defaultHandler)

@app.route('/search/categories')
def form1():
    return render_template('categories.html')

@app.route('/search/ingredients')
def form2():
    return render_template('ingredients.html')

@app.route('/search/category/ingredients')
def form3():
    return render_template('ingredient_category.html')

@app.route('/recipe_details/view')
def form4():
    return render_template('recipe_details.html')

@app.route('/categories', methods = ['GET'])
def categories():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM ingredient_categories")
    data = c.fetchall()
    conn.close()

    categories = []
    for (i, j) in data:
        categories.append({"name": j, "c_id": i})
        
    ret = {"status": 200,
            "body": {"categories": categories}}

    return ret

@app.route('/ingredients', methods = ['GET'])
def ingredients():
    # USE FOR REAL WEBSITE
    # ingredient = request.args.get('query')

    # USE FOR TESTING
    ingredient = request.args['Ingredient']
    print(ingredient)
    
    db_path = os.path.join("./data/", "nepka.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM ingredients_table")
    data = c.fetchall()
    conn.close()

    suggestions = []
    for (i, j, k) in data:
        if ingredient.lower() in k.lower():
            suggestions.append({"name": k, "i_id": i, "c_id": j})
    
    ret = {"status": 200,
            "body": {"suggestions": suggestions}}
    
    return ret

@app.route('/view', methods = ['GET'])
def recipe_details():
    # how to get input in reality?
    recipe_id = request.args.get('query')
    # recipe_id = request.args['Recipe']

    # throw errors === Doesn't really work rn and i don't know why
    if not valid_recipe_id(db_path, recipe_id):
        raise InputError("No such recipe id")
    
    ret = get_recipe_details(db_path, recipe_id)

    return ret

@app.route('/save_and_rate/save', methods = ['POST'])
def save():
    db_path = os.path.join("./data/", "nepka.db")
    conn = sqlite3.connect(db_path)

    req = request.get_json()
    recipe_id = req['recipe_id']
    token = req['token']

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_recipe_id(db_path, recipe_id):
        raise InputError("No such recipe id")
    
    # Get user id
    user_details = decode_token(conn, token)
    id = user_details["user_id"]

    c = conn.cursor()
    c.execute("SELECT * FROM Recipe WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, id])
    if c.fetchall() == None:
        c.execute("INSERT INTO Recipe_Saves VALUES (?, ?)", (recipe_id, id))
    else:
        c.execute("DELETE FROM Recipe_Saves WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, id])
    
    conn.commit()
    conn.close()
    return f'done'

@app.route('/save_and_rate/rate', methods = ['POST'])
def rate():
    db_path = os.path.join("./data/", "nepka.db")
    conn = sqlite3.connect(db_path)

    req = request.get_json()
    recipe_id = req['recipe_id']
    token = req['token']
    rating = req['rating']

    # Validate token
    if not validate_token(conn, token):
        raise AccessError("Invalid token")

    # Validate recipe_id
    if not valid_recipe_id(db_path, recipe_id):
        raise InputError("No such recipe id")

    #validate rating
    if rating > 5 or rating < 0:
        raise InputError("Rating our of range.")
    
    # Get user id
    user_details = decode_token(conn, token)
    id = user_details["user_id"]

    c = conn.cursor()
    c.execute("SELECT * FROM Recipe_Ratings WHERE recipe_id = ? AND author_id = ?", [recipe_id, id])
    if c.fetchall() != None:
        c.execute("DELETE FROM Recipe_Ratings WHERE recipe_id = ? AND author_id = ?", [recipe_id, id])
        c.execute("INSERT INTO Recipe_Ratings VALUES (?, ?, ?)", (recipe_id, id, rating))
    else:
        c.execute("INSERT INTO Recipe_Ratings VALUES (?, ?, ?)", (recipe_id, id, rating))
    
    conn.commit()
    conn.close()

    return

if __name__ == '__main__':
    app.run(host='localhost', port=5000)