from flask import Blueprint, redirect, url_for, render_template, session
from flask.globals import request
from userAuth import auth
from models import db,User

_users = Blueprint('users', __name__)


@_users.route('/users', methods=['GET', 'POST'])
def users():
    # if not auth():
    #     return redirect(url_for('userAuth.login'))
    # user1 = {"id": 1, "name": "user1", "score": 100, "rank": 1,
    #          "Website": "www.a.com", "Affiliation": "aaa", "Country": "AAA"}
    # user2 = {"id": 2, "name": "user2", "score": 10, "rank": 2}
    # user3 = {"id": 3, "name": "user3", "score": 10, "rank": 3}
    # users = [user1, user2, user3]
    # users = User.query.get(1)
    # users = db.session.query(User.uid, User.username).all()
    if request.args.get("field") != None and request.args.get("q") != None:
        print(request.args.get("q"))
        users = db.session.query(User).filter(
            User.username.like('%'+request.args.get("q")+'%')
            ).all()
    else:
        users = db.session.query(User).all()
    # users = User.query.filter_by(username='qwe').first()
    # print(users)
    # for user in users:
    #     print(user.uid)
    #     print(user.username)
    return render_template("users.html", user=session.get('user'), users=users)
