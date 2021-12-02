from myutils import quickSort
from flask import Blueprint, redirect, url_for, render_template, session
from userAuth import auth
from models import db, Team, tid2TeamUidList, solveCids2ValueSum, uids2SolveCids
_scoreboard = Blueprint('scoreboard', __name__)

@_scoreboard.route('/scoreboard', methods=['GET', 'POST'])
def scoreboard():
    # if not auth():
    #     return redirect(url_for('userAuth.login'))
    team1 = {"tid":1,"teamname":"team1","score":100,"rank":1}
    team2 = {"tid":2,"teamname":"team2","score":10,"rank":2}
    team3 = {"tid":3,"teamname":"team3","score":10,"rank":3}
    teams = [team2, team3, team1, ]
    
    # uids = userName2TeamUidList(session.get("user"))
    # print(uids)
    # solveCids = uids2SolveCids(uids)
    # print(solveCids)
    
    teams = db.session.query(Team).order_by(Team.tid).all()
    for i in teams:
        # print(i.tid)
        uids = tid2TeamUidList(i.tid)
        solveCids = uids2SolveCids(uids)
        sum = solveCids2ValueSum(solveCids)
        i.score = sum
        # print(i["score"])#报错
    teams = (sorted(teams, key=lambda i: i.score, reverse=True))
    rank = 0
    for i in teams:
        rank += 1
        i.rank = rank
    return render_template("scoreboard.html", user=session.get('user'), teams=teams)
