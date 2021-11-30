from flask import Blueprint, redirect, url_for, render_template, session
from userAuth import auth
from models import Challenge, db, userName2TeamUidList, Solve, uids2SolveCids

_challenges = Blueprint('challenges', __name__)


@_challenges.route('/challenges', methods=['GET', 'POST'])
def challenges():
    if not auth():
        return redirect(url_for('userAuth.login'))
    # challenge1 = {"id": 1, "name": "signin1", "value": 100, "desc": "flag{123}", "flag": "flag{123}"}
    # challenge2 = {"id": 2, "name": "signin2", "value": 100, "desc": "flag{123}", "flag": "flag{123}"}
    # challenge3 = {"id": 3, "name": "signin3", "value": 100, "desc": "flag{123}", "flag": "flag{123}"}
    # challenge4 = {"id": 4, "name": "signin4", "value": 100, "desc": "flag{123}", "flag": "flag{123}"}
    # challenge5 = {"id": 5, "name": "signin5", "value": 100, "desc": "flag{123}", "flag": "flag{123}"}
    # challenge6 = {"id": 6, "name": "signin6", "value": 100, "desc": "flag{123}", "flag": "flag{123}"}
    # challenge7 = {"id": 7, "name": "signin7", "value": 100,"desc": "flag{123}", "flag": "flag{123}"}
    # solves = 1
    # web_challenges = [challenge1, challenge2,
    #                   challenge5, challenge6, challenge7 ]
    # challengess = [challenge1]

    # print(uids)
    uids = userName2TeamUidList(session.get('user'))
    solveCids = uids2SolveCids(uids)
    print(solveCids)
    tags = ["Web","Misc","Reverse","Pwn","Crypto"]
    category = {}
    for tag in tags:
        category[tag] = db.session.query(Challenge).filter(Challenge.category == tag).all()
        for challenge in category[tag]:
            if challenge.cid in solveCids:
                challenge.solve = 1
            # print(i.cid)
            # print(i.solve)
    return render_template("challenges.html", user=session.get('user'), category=category)

