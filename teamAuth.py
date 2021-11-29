from flask import Blueprint, redirect, url_for, render_template, session, request, flash
# from app import app
from models import Team
from models import db
from userAuth import auth


_teamAuth = Blueprint('teamAuth', __name__)


@_teamAuth.route('/team', methods=['GET', 'POST'])
def team():
    if not auth():
        return redirect(url_for('index.index'))
    # if request.method == 'POST':
    return render_template('teamAuth.html', user=session.get('user'))

@_teamAuth.route('/teams/new', methods=['GET', 'POST'])
def register():
    if not auth():
        return redirect(url_for('index.index'))
    errors = []
    if request.method == 'POST':
        name_count = (db.session.query(Team.teamname)
                      .filter(Team.teamname == request.form['teamname'])
                      .count())
        if name_count == 0:
            team = Team(request.form['teamname'], request.form['password'])
            db.session.add(team)
            db.session.commit()
            # return render_template('login.html', errors=errors)
            return redirect(url_for('teamAuth.login'))
        else:
            errors.append("That team name is already taken")
    return render_template('team_register.html', errors=errors, user=session.get('user'))


@_teamAuth.route('/teams/join', methods=['GET', 'POST'])
def login():
    if not auth():
        return redirect(url_for('index.index'))
    errors = []
    if request.method == 'POST':
        # print(request.form)
        # if request.form!=None and request.form['teamname'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
        # if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
        # admin = User(username='admin123', password='qweqwe')
        # print(db.session)
        # print(db.session.query(User.username).all())
        # print(db.session.query(User).filter(User.username == "admin123"))
        count = (db.session.query(User.username)
                 .filter(User.username == request.form['username'])
                 .filter(User.password == request.form['password'])
                 .count())

        if count == 0:
            errors.append('Invalid username or password')
        else:
            session['user'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('index.index'))
    return render_template('team_login.html', errors=errors, user=session.get('user'))


# @_teamAuth.route('/logout')
# def logout():
#     if(session.get('user') is not None):
#         session.pop('user', None)
#     return redirect(url_for('userAuth.login'))
