from flask import Blueprint, redirect, url_for, render_template, session
from userAuth import auth

_challenges = Blueprint('challenges', __name__)


@_challenges.route('/challenges', methods=['GET', 'POST'])
def challenges():
    # if not auth():
    #     return redirect(url_for('userAuth.login'))
    challenge1 = {"id": 1, "name": "signin1", "value": 100, "desc": "flag{123}"}
    challenge2 = {"id": 2, "name": "signin2", "value": 100, "desc": "flag{123}"}
    challenge3 = {"id": 3, "name": "signin3", "value": 100, "desc": "flag{123}"}
    challenge4 = {"id": 4, "name": "signin4", "value": 100, "desc": "flag{123}"}
    challenge5 = {"id": 5, "name": "signin5", "value": 100, "desc": "flag{123}"}
    challenge6 = {"id": 6, "name": "signin6", "value": 100, "desc": "flag{123}"}
    challenge7 = {"id": 7, "name": "signin7", "value": 100, "desc": "flag{123}"}
    solves = 1
    tags = ["misc","web"]
    web_challenges = [challenge1, challenge2,
                      challenge5, challenge6, challenge7 ]
    misc_challenges = [challenge3, challenge4]
    category = {"WEB": web_challenges, "MISC": misc_challenges}
    # challengess = [challenge1]
    return render_template("challenges.html", user=session.get('user'), category=category, solves=solves, tags=tags)

