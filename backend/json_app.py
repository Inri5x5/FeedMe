from cmath import atanh
from flask import Flask, render_template, request
from helper import valid_email
from error import AccessError, InputError
from helper import get_contributor, get_ruser, check_password, generate_token, validate_token, get_recipe_details
import json
import sqlite3
import os.path

db_path = os.path.join("./data/", "nepka.db")
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
    recipe_id = request.args['Recipe']

    # throw errors

    
    ret = get_recipe_details(db_path, recipe_id)
    print(ret)
    return f'done'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)