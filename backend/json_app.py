from flask import Flask,render_template, request
import json

app = Flask(__name__)

@app.route('/search/categories')
def form1():
    return render_template('categories.html')

@app.route('/search/ingredients')
def form2():
    return render_template('ingredients.html')
 
@app.route('/categories', methods = ['GET'])
def categories():
    # Open json file of ingredients and load data
    f = open('data/ingredient_categories_table.json')
    data = json.load(f)

    # Append ingredient categories into a list
    categories = []
    for dict in data:
        categories.append(dict["name"])

    print(categories) 
    
    # Format return dict
    ret = {"status": 200,
            "body": {"categories": categories}}
        
    return ret

@app.route('/ingredients', methods = ['GET'])
def ingredients():
    # Get user input
    ingredient = request.args['Ingredient']

    # Open json file of ingredients and load data
    f = open('data/ingredients_table.json')
    data = json.load(f)

    # Search ingredient dict for string matches
    suggestions = []
    for dict in data:
        if ingredient in dict["name"]:
            suggestions.append(dict["name"])

    # Format return dict
    ret = {"status": 200,
            "body": {"suggestions": suggestions}}

    return ret

 
app.run(host='localhost', port=5000)