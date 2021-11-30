from flask import Blueprint, redirect, url_for, render_template, session
from userAuth import auth
from models import db,User
_index = Blueprint('index', __name__)


@_index.route('/index', methods=['GET', 'POST'])
def index():
    if not auth():
        return redirect(url_for('userAuth.login'))
    
    # uid = db.session.query(User.uid).filter(
    #     User.username == session.get('user')
    # ).one()[0]
    # print(uid)

    return render_template("index.html", user=session.get('user'))
