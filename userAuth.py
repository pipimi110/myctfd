from flask import Blueprint, redirect, url_for, render_template, session, request, flash
# from app import app
from models import User
from models import db

def auth():
    if session.get('user') is None:
        return False
    else:
        return True


_userAuth = Blueprint('userAuth', __name__)


@_userAuth.route('/register', methods=['GET', 'POST'])
def register():
    if auth():
        return redirect(url_for('index.index'))
    errors = []
    if request.method == 'POST':
        name_count = (db.session.query(User.username)
            .filter(User.username == request.form['username'])
            .count())
        email_count = (db.session.query(User.email)
            .filter(User.email == request.form['email'])
            .count())
        if name_count == 0 and email_count == 0:
            user = User(request.form['username'],request.form['email'],request.form['password'])
            db.session.add(user)
            db.session.commit()
            # return render_template('login.html', errors=errors)
            return redirect(url_for('userAuth.login'))
        if name_count == 1:
            errors.append("That user name is already taken")
        if email_count == 1:
            errors.append("That email has already been used")
    return render_template('register.html', errors=errors)

@_userAuth.route('/login', methods=['GET', 'POST'])
def login():
    if auth():
        return redirect(url_for('index.index'))
    errors = []
    if request.method == 'POST':
        # print(request.form)
        # if request.form!=None and request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
        # if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
        # admin = User(username='admin123', password='qweqwe')
        # print(db.session)
        # print(db.session.query(User.username).all())
        # print(db.session.query(User).filter(User.username == "admin123"))
        count = (db.session.query(User.username)
        .filter(User.username ==request.form['username'])
        .filter(User.password == request.form['password'])
        .count())

        if count == 0:
            errors.append('Invalid username or password')
        else:
            session['user'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('index.index'))
    return render_template('login.html', errors=errors, user=session.get('user'))


@_userAuth.route('/logout')
def logout():
    if(session.get('user') is not None):
        session.pop('user', None)
    return redirect(url_for('userAuth.login'))


