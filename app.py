from flask import Flask, render_template, request, url_for, redirect, session
from flask import flash
import uuid
import os
from utils import auth

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "upload_folder"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or "popko"
app.secret_key = uuid.uuid4().bytes
app.config['USERNAME'] = "admin"
app.config['PASSWORD'] = "123123"



@app.route('/')
def hello_world():  # put application's code here
    # return 'Hello World!'
    # return render_template("basetest.html")
    # return render_template("extendtest.html")
    return redirect("/index")

from index import _index
app.register_blueprint(_index)
from login import _login
app.register_blueprint(_login)
from challenges import _challenges
app.register_blueprint(_challenges)




@app.route('/logout')
def logout():
    if(session.get('user') is not None):
        session.pop('user', None)
    return redirect(url_for('login.login'))


@app.route('/test')
def test():
    return render_template("1test.html")

if __name__ == '__main__':
    app.run(debug=True)
