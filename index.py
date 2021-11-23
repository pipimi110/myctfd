from flask import Blueprint, redirect, url_for, render_template, session
from userAuth import auth

_index = Blueprint('index', __name__)


@_index.route('/index', methods=['GET', 'POST'])
def index():
    if not auth():
        return redirect(url_for('userAuth.login'))
    return render_template("index.html", user=session.get('user'))
