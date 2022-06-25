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
    f = open('ingredients.json')
    data = json.load(f)

    print(data)

    # Append ingredient categories into a list
    categories = []
    for n in data:
        categories.append(n)

    # Format return dict
    ret = {"status": 200,
            "body": {"categories": categories}}
        
    return f"Frontend receives: {ret}"

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
    #for c, i in data.items():
        #for n in i:
            #if ingredient in n:
                #suggestions.append(n)
    
    # Format return dict
    ret = {"status": 200,
            "body": {"suggestions": suggestions}}

    return f"Frontend receives: {ret}"

 
app.run(host='localhost', port=5000)