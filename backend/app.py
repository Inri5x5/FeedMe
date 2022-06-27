from flask import Flask, jsonify, render_template, request
from error import AccessError, InputError
from helper import get_contributor, get_ruser, check_password, valid_email, generate_token, validate_token
from werkzeug.exceptions import HTTPException
from json import dumps
import json

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

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
 
 
@app.route("/auth/register", methods = ['POST'])
def register():
    req = request.get_json()
    email = req['email']
    password = req['password']
    username = req['username']

    if not email or not password or not username:
        raise InputError

    fp1 = open('./data/rusers_table.json', 'r')
    ruser_data = json.load(fp1)
    for ruser in ruser_data:
        if ruser['email'] == email:
            raise EmailAlreadyInUse

    ruser_id = len(ruser_data)
    print(ruser_id)
    ruser_data.append({"ruser_id": ruser_id, "email": email, "password": password, "username": username, "profile_picture": ''})
    fp1.close()
    fp = open('./data/rusers_table.json', 'w')
    fp.write(json.dumps(ruser_data))
    fp.close()

    token = generate_token(email)
    fp2 = open('data/tokens_table.json', 'r')
    token_data = json.load(fp2)
    token_data.append({"token": token, "user_id": ruser_id, "is_contributor": False})
    fp2.close()
    fp = open('./data/tokens_table.json', 'w')
    json.dump(token_data, fp)
    fp.close()

    status_code = 200
    response = {
        "success": True,
        "body": {
            "token": token    
    }

    return jsonify(response), status_code
    
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
    app.run(host='localhost', port=5000, debug=True)