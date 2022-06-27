from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from helper import create_token

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
 

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']

        cursor = mysql.connection.cursor()

        # Check if email exists
        cursor.execute('''SELECT 1 FROM users WHERE email = %s''', email)
        info = cursor.fetchone()
        if not info:
            cursor.close()
            return {
                "status": 400,
                "body": {"error": "Email is not registered"}
            }

        # Check password
        cursor.execute('''SELECT 1 FROM users WHERE email = %s, password = %s''', 
                        (email, password))
        info = cursor.fetchone()
        if not info:
            cursor.close()
            return {
                "status": 400,
                "body": {"error": "Wrong password"}
            }

        # Check if contributor or regular user
        email, password, is_contributor = info
        if (is_contributor):
            # do something
            print("Contributor")

        # Create token and input to databse
        token = create_token(email)
        cursor.execute('''INSERT INTO tokens VALUES(%s, %s)''', (email, token))

        cursor.close()

        return {
            "status": 200,
            "body": {"token": token}
        }

@app.route('/logout', methods = ['GET'])
def logout():
    email = request.json['email']
    token = request.json['token']

    cursor = mysql.connection.cursor()

    # Validate token
    cursor.execute('''SELECT 1 FROM tokens WHERE token = %s''', token)
    info = cursor.fetchone()
    emailDB, tokenDB = info
    if (not info or tokenDB != token):
        cursor.close()
        return {
            "status": 400,
            "body": {"error": "Invalid token"}
        }

    # Delete token
    cursor.execute('''DELETE FROM tokens WHERE token = %s''', token)

    cursor.close()

    return {
        "status": 200
    }
    
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


if __name__ == '__main__':
    app.run(host='localhost', port=5000)