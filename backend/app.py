from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
 

@app.route('/search/categories')
def form1():
    return render_template('categories.html')

@app.route('/search/ingredients')
def form2():
    return render_template('ingredients.html')
 
@app.route('/categories', methods = ['GET'])
def categories():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'dummy_data' ORDER BY ORDINAL_POSITION")
        myresult = []
        for i in cursor.fetchall():
            myresult.extend(i)
    
        ret = {"status": 200,
                "body": {"categories": myresult}}
        print(ret)
        
        return f"Categories are: {myresult}"

@app.route('/ingredients', methods = ['GET'])
def ingredients():
    if request.method == 'GET':
        ingredient = request.args['Ingredient']
        print(ingredient)
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM dummy_data")
        myresult = []
        for i in cursor.fetchall():
            myresult.extend(i)

        suggestions = [i for i in myresult if ingredient in i]

        ret = {"status": 200,
                "body": {"suggestions": suggestions}}
        print(ret)
        
        return f"Suggestions are: {suggestions}"

 
app.run(host='localhost', port=5000)

