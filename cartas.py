from flask import Flask, redirect, render_template, request, flash
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config["MYSQL_DATABASE_HOST"] = 'localhost'
app.config["MySQL_DATABASE_PORT"] = 3306
app.config["MYSQL_DATABASE_USER"] = 'root'
app.config["MYSQL_DATABASE_PASSWORD"] = ''
app.config["MYSQL_DATABASE_DB"] = 'senasoft_2022'

mysql.init_app(app)


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/login', methods=['POST'])
def login():
    return render_template('/login/login.html')


@app.route('/login2', methods=['POST'])
def login2():
    return render_template('login2/login2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='5080')
