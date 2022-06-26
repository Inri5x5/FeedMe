from flask import Flask,render_template, request
import json

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
 
# @app.route('/categories', methods = ['GET'])
# def categories():
#     # Open json file of ingredients and load data
#     f = open('data/ingredient_categories_table.json')
#     data = json.load(f)

#     # Append ingredient categories into a list
#     categories = []
#     for dict in data:
#         categories.append(dict["name"])

#     print(categories) 

#     # Format return dict
#     ret = {"status": 200,
#             "body": {"categories": categories}}
        
#     return ret

@app.route('/categories', methods = ['GET'])
def categories():
    # Open json file of ingredients and load data
    f = open('data/ingredient_categories_table.json')
    data = json.load(f)

    # Append ingredient categories into a list
    categories = []
    for dict in data:
        categories.append({"name": dict["name"], "c_id": dict["category_id"]})

    print(categories) 

    # Format return dict
    ret = {"status": 200,
            "body": {"categories": categories}}
        
    return ret

# @app.route('/ingredients', methods = ['GET'])
# def ingredients():
#     # Get user input
#     ingredient = request.args['Ingredient']

#     # Open json file of ingredients and load data
#     f = open('data/ingredients_table.json')
#     data = json.load(f)

#     # Search ingredient dict for string matches
#     suggestions = []
#     for dict in data:
#         if ingredient.lower() in dict["name"].lower():
#             suggestions.append(dict["name"])

#     # Format return dict
#     ret = {"status": 200,
#             "body": {"suggestions": suggestions}}

#     return ret

@app.route('/ingredients', methods = ['GET'])
def ingredients():
    # Get user input
    ingredient = request.args.get('query')

    # Open json file of ingredients and load data
    f = open('data/ingredients_table.json')
    data = json.load(f)

    # Search ingredient dict for string matches
    suggestions = []
    for dict in data:
        if ingredient.lower() in dict["name"].lower():
            suggestions.append({"name": dict["name"], "i_id": dict["ingredient_id"]})

    # Format return dict
    ret = {"status": 200,
            "body": {"suggestions": suggestions}}

    return ret

# @app.route('/category/ingredients', methods = ['GET'])
# def category_ingredients():
#     # Get user input (string)
#     category = request.args['Category']

#     # Load category_id to category name mapping and get id
#     i = open('data/ingredient_categories_table.json')
#     category_data = json.load(i)
#     category_id = 0
#     for j in category_data:
#         if category == j["name"]:
#             category_id = j["category_id"]

#     # Load ingredient data and get all ingredient in category
#     f = open('data/ingredients_table.json')
#     ingredient_data = json.load(f)
#     ingredients = []
#     for dict in ingredient_data:
#         if category_id == dict["ingredient_category_id"]:
#             ingredients.append(dict["name"])

#     # Format return dict
#     if len(ingredients) == 0:
#         ret = {"status": 400,
#                 "body": {"error": "Invalid category name"}}
#     else:
#         ret = {"status": 200,
#                 "body": {"ingredients": ingredients}}
    
#     return ret

@app.route('/category/ingredients', methods = ['GET'])
def category_ingredients():
    # Get user input (string)
    category = request.args.get('category')

    # Load category_id to category name mapping and get id
    i = open('data/ingredient_categories_table.json')
    category_data = json.load(i)
    category_id = 0
    for j in category_data:
        if category == j["name"]:
            category_id = j["category_id"]

    # Load ingredient data and get all ingredient in category
    f = open('data/ingredients_table.json')
    ingredient_data = json.load(f)
    ingredients = []
    for dict in ingredient_data:
        if category_id == dict["ingredient_category_id"]:
            ingredients.append({"name": dict["name"], "i_id": dict["ingredient_id"]})

    
    ret = {"status": 200,
            "body": {"ingredients": ingredients}}
    
    return ret

 
app.run(host='localhost', port=5000)