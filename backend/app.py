from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from helper import create_token

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'feedme_test'
 
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


if __name__ == '__main__':
    app.run(host='localhost', port=5000)