from flask import Blueprint, redirect, url_for, render_template, session
from userAuth import auth

_teams = Blueprint('teams', __name__)


@_teams.route('/teams', methods=['GET', 'POST'])
def teams():
    # if not auth():
    #     return redirect(url_for('userAuth.login'))
    team1 = {"id": 1, "name": "team1", "score": 100, "rank": 1, "Website": "www.a.com", "Affiliation": "aaa", "Country": "AAA"}
    team2 = {"id": 2, "name": "team2", "score": 10, "rank": 2}
    team3 = {"id": 3, "name": "team3", "score": 10, "rank": 3}
    teams = [team1, team2, team3]
    return render_template("teams.html", user=session.get('user'), teams=teams)
