from flask import Blueprint, redirect, url_for, render_template, session
from utils import auth

_challenges = Blueprint('challenges', __name__)


@_challenges.route('/challenges', methods=['GET', 'POST'])
def challenges():
    if not auth():
        return redirect(url_for('login.login'))
    return render_template("challenges.html")
