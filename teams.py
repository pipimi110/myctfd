from flask import Blueprint, redirect, url_for, render_template, session, request
from userAuth import auth
from models import Team,db,User

_teams = Blueprint('teams', __name__)
_teams_user=Blueprint('showteam_user', __name__)

@_teams.route('/teams', methods=['GET', 'POST'])
def teams():
    # if not auth():
    #     return redirect(url_for('userAuth.login'))
    # team1 = {"id": 1, "name": "team1", "score": 100, "rank": 1, "Website": "www.a.com", "Affiliation": "aaa", "Country": "AAA"}
    # team2 = {"id": 2, "name": "team2", "score": 10, "rank": 2}
    # team3 = {"id": 3, "name": "team3", "score": 10, "rank": 3}
    # teams = [team1, team2, team3]
    '''if request.args.get("field") != None and request.args.get("q") != None:
        print(request.args.get("q"))
        teams = db.session.query(Team).filter(
            Team.username.like('%'+request.args.get("q")+'%')
        ).all()
    else:
        teams = db.session.query(Team).all()
        print(teams)'''
    teams=db.session.query(Team).all()
    return render_template("teams.html", user=session.get('user'), teams=teams)



@_teams_user.route('/teams/<int:tid>', methods=['GET', 'POST'])
def showteam_user(tid):
    teamsuser=db.session.query(User).filter(User.tid==tid)
    return render_template("showteam_user.html",user=session.get('user'),teamsuser=teamsuser)

