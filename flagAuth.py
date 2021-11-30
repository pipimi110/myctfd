from flask import Blueprint, redirect, url_for, render_template, session, request, flash
# from flaskLearn.myctfd.models import Challenge
# from app import app
from models import db, User, Solve, Challenge, userName2TeamUidList
from userAuth import auth
import json


_flagAuth = Blueprint('flagAuth', __name__)

# /flag uid=1&cid=1&flag=flag{test}
@_flagAuth.route('/flag', methods=['GET', 'POST'])
def flag_check():
    if not auth():
        return redirect(url_for('index.index'))
    status = {"res": "flag error"}
    if request.method == 'POST':
        uids = userName2TeamUidList(session.get('user'))
    
        cid = request.form['cid']
        flag = request.form['flag']
        submit_auth = (db.session.query(Solve)
                     .filter(Solve.cid == cid)
                     .filter(Solve.uid.in_(uids))
                     )
        count = submit_auth.count()
        # print(count)
        if count != 0:
            status = {"res": "flag already"}
        else:
            flag_auth = (db.session.query(Challenge)
                        .filter(Challenge.cid == cid)
                        .filter(Challenge.flag == flag)
                        )
            count = flag_auth.count()
            # print(count)
            if count != 0:
                uid = db.session.query(User.uid).filter(User.username == session.get('user')).one()[0]
                # print(uid)
                solve = Solve(uid,cid)
                db.session.add(solve)
                db.session.commit()
                status = {"res": "flag success"}
    # return render_template('flagAuth.html', user=session.get('user'))
    print(status)
    return json.dumps(status)
