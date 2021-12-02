# from db import get_db
from flask import Flask, render_template, request, url_for, redirect, session
from flask import flash
import uuid
import os
# from utils import auth
from models import app

# app = Flask(__name__)
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


@app.route('/test')
def test():
    # print(get_db())
    return render_template("1test.html")


from index import _index
app.register_blueprint(_index)
from userAuth import _userAuth
app.register_blueprint(_userAuth)
from teamAuth import _teamAuth
app.register_blueprint(_teamAuth)
from flagAuth import _flagAuth
app.register_blueprint(_flagAuth)
from challenges import _challenges
app.register_blueprint(_challenges)
from scoreboard import _scoreboard
app.register_blueprint(_scoreboard)
from teams import _teams
app.register_blueprint(_teams)
from users import _users
app.register_blueprint(_users)
from insertchallenge import _ichallenge
app.register_blueprint(_ichallenge)
from deletechallenge import _dchallenge
app.register_blueprint(_dchallenge)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=10300,debug=True)
