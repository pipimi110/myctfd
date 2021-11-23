from flask import Blueprint, redirect, url_for, render_template, session
from userAuth import auth

_users = Blueprint('users', __name__)


@_users.route('/users', methods=['GET', 'POST'])
def users():
    # if not auth():
    #     return redirect(url_for('userAuth.login'))
    user1 = {"id": 1, "name": "user1", "score": 100, "rank": 1,
             "Website": "www.a.com", "Affiliation": "aaa", "Country": "AAA"}
    user2 = {"id": 2, "name": "user2", "score": 10, "rank": 2}
    user3 = {"id": 3, "name": "user3", "score": 10, "rank": 3}
    users = [user1, user2, user3]
    return render_template("users.html", user=session.get('user'), users=users)
