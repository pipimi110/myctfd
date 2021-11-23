from flask import Blueprint, redirect, url_for, render_template, session, request, flash
from utils import auth
# from app import app

_login = Blueprint('login', __name__)


@_login.route('/login', methods=['GET', 'POST'])
def login():
    if auth():
        return redirect(url_for('index.index'))
    errors = []
    if request.method == 'POST':
        # print(request.form)
        # if request.form!=None and request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
        # if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
        if request.form['username'] != "admin" or request.form['password'] != "123123":
            errors.append('Invalid username or password')
        else:
            session['user'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('index.index'))
    return render_template('login.html', errors=errors, user=session.get('user'))
