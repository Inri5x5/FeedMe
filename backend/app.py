from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from helper import create_token
import json
import jwt

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'feedme_test'
 
mysql = MySQL(app)


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the form"
     
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']

        cursor = mysql.connection.cursor()

        cursor.execute('''SELECT 1 FROM MyTable WHERE email = %s''', email)
        info = cursor.fetchone()
        if not info:
            cursor.close()
            return {
                "status": 400,
                "body": {"error": "Email is not registered"}
            }

        cursor.execute('''SELECT 1 FROM MyTable WHERE email = %s, password = %s''', 
                        (email, password))
        info = cursor.fetchone()
        if not info:
            cursor.close()
            return {
                "status": 400,
                "body": {"error": "Wrong password"}
            }

        # check if contributor or regular user

        cursor.close()
        
        token = create_token(email)

        return {
            "status": 200,
            "body": {"token": token}
        }

@app.route('/logout', methods = ['GET'])
def logout():

    # delete token

    return {
        "status": 200
    }


if __name__ == '__main__':
    app.run(host='localhost', port=5000)