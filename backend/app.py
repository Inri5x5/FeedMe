from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the form"
     
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()

        cursor.execute('''SELECT 1 FROM MyTable WHERE email = %s''', email)
        info = cursor.fetchone()
        if not info:
            mysql.connection.commit()
            cursor.close()
            return f"Email doesn't exist"

        cursor.execute('''SELECT 1 FROM MyTable WHERE email = %s, password = %s''', 
                        (email, password))
        info = cursor.fetchone()
        if not info:
            mysql.connection.commit()
            cursor.close()
            return f"Wrong password"

        mysql.connection.commit()
        cursor.close()
        return f"User logged in"


app.run(host='localhost', port=5000)